# wallet_generator2.py

import random
import threading
import multiprocessing as mp
import cachetools
import psutil
import time
import hmac
import hashlib
import curses
from mnemonic import Mnemonic
from bip32utils import BIP32Key
from Crypto.Hash import RIPEMD160
from functools import lru_cache

# Cache LRU para armazenamento temporário
cache = cachetools.LRUCache(maxsize=512)

def ripemd160(data):
    h = RIPEMD160.new()
    h.update(data)
    return h.digest()

# Atualize a classe BIP32Key para usar ripemd160
def identifier(self):
    sha256 = hashlib.sha256(self.PublicKey()).digest()
    return ripemd160(sha256)

BIP32Key.Identifier = identifier

@lru_cache(maxsize=2048)
def completar_com_palavra_inicial(word, word_list, num_words_needed):
    frase = [word]

    while len(frase) < num_words_needed:
        random_word = random.choice(word_list)
        frase.append(random_word)

    return " ".join(frase[:num_words_needed])

def completar_ate_num_palavras(num_palavras, word_list):
    frases_completas = []

    for word in word_list:
        frase_completa = completar_com_palavra_inicial(word, tuple(word_list), num_palavras)
        frases_completas.append(frase_completa)

    return frases_completas

@lru_cache(maxsize=2048)
def criar_wallets(mnemonic):
    wallets = []
    HARDENED_OFFSET = 0x80000000
    
    seed = Mnemonic.to_seed(mnemonic, passphrase="")
    master_key = hmac.new(b'Bitcoin seed', seed, hashlib.sha512).digest()
    bip32_root_key = BIP32Key.fromEntropy(master_key)
    bip32_account_key = bip32_root_key.ChildKey(44 + HARDENED_OFFSET).ChildKey(0 + HARDENED_OFFSET).ChildKey(0 + HARDENED_OFFSET)
    bip32_chain_key = bip32_account_key.ChildKey(0)
    bip32_address_key = bip32_chain_key.ChildKey(0)
        
    wallets.append({
        "mnemonic": mnemonic,
        "address": bip32_address_key.Address(),
        "private_key": bip32_address_key.WalletImportFormat()
    })

    return wallets[0]

def gerar_frases_aleatorias(stdscr, num_palavras, word_list):
    curses.curs_set(0)  # Esconder o cursor
    stdscr.clear()
    stdscr.refresh()
    
    height, width = stdscr.getmaxyx()
    columns = 3
    column_width = width // columns

    # Desenhar divisores verticais
    for i in range(1, columns):
        x = i * column_width
        stdscr.vline(0, x, '|', height)

    stdscr.refresh()

    y_positions = [1] * columns

    # Inicializar cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    generation_count = 0
    start_time = time.time()

    last_time = start_time
    last_generation_count = 0

    while True:
        frases_aleatorias = completar_ate_num_palavras(num_palavras, word_list)
        for idx, frase in enumerate(frases_aleatorias):
            column = idx % columns
            start_x = column * column_width + 1
            start_y = y_positions[column]
            wallet = criar_wallets(frase)
            stdscr.addstr(start_y, start_x, f"Mnem: {wallet['mnemonic']}")
            stdscr.addstr(start_y + 1, start_x, f"Wallet: ", curses.color_pair(1))
            stdscr.addstr(f"{wallet['address']}", curses.color_pair(1))
            stdscr.addstr(start_y + 2, start_x, f"(WIF): ", curses.color_pair(2))
            stdscr.addstr(f"{wallet['private_key']}", curses.color_pair(2))
            stdscr.clrtoeol()
            stdscr.refresh()
            y_positions[column] += 4  # Mover para a próxima linha na mesma coluna
            if y_positions[column] >= height - 4:
                y_positions[column] = 1  # Voltar para o topo da coluna quando chegar ao final da tela
            generation_count += 1

        # Atualizar contador de gerações por segundo
        current_time = time.time()
        elapsed_time = current_time - start_time
        gen_per_second = generation_count / elapsed_time

        if current_time - last_time >= 1:
            gen_per_second_current = generation_count - last_generation_count
            last_generation_count = generation_count
            last_time = current_time

        stdscr.addstr(0, 0, f"Gerações Totais: {generation_count}")
        stdscr.addstr(0, 30, f"Gerações por segundo: {gen_per_second_current:.2f}")
        stdscr.clrtoeol()
        stdscr.refresh()

def monitorar_e_limpar_cache():
    while True:
        time.sleep(60)  # Espera de 1 minuto
        cache.clear()  # Limpa o cache
        print("Cache limpo.")
        
        # Monitoramento da memória RAM
        memoria = psutil.virtual_memory()
        if memoria.percent > 80:
            print("Uso de RAM acima de 80%. Considere fechar alguns processos para liberar memória.")

def iniciar_interface():
    curses.wrapper(main)

if __name__ == "__main__":
    iniciar_interface()
