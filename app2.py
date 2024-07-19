# other_program.py

import curses
from mnemonic import Mnemonic
import wallet_generator as wg1
import wallet_generator2 as wg2
import multiprocessing as mp
import time

def gerar_com_primeiro(stdscr, num_palavras, word_list, lock, queue):
    start_time = time.time()
    generation_count = 0
    with lock:
        wg1.gerar_frases_aleatorias(stdscr, num_palavras, word_list)
        generation_count += 1
    elapsed_time = time.time() - start_time
    queue.put(("wg1", generation_count, elapsed_time))

def gerar_com_segundo(stdscr, num_palavras, word_list, lock, queue):
    start_time = time.time()
    generation_count = 0
    with lock:
        wg2.gerar_frases_aleatorias(stdscr, num_palavras, word_list)
        generation_count += 1
    elapsed_time = time.time() - start_time
    queue.put(("wg2", generation_count, elapsed_time))

def gerar_frases_aleatorias_com_ambas(stdscr, num_palavras, word_list):
    lock = mp.Lock()
    queue = mp.Queue()

    process1 = mp.Process(target=gerar_com_primeiro, args=(stdscr, num_palavras, word_list, lock, queue))
    process2 = mp.Process(target=gerar_com_segundo, args=(stdscr, num_palavras, word_list, lock, queue))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    result1 = queue.get()
    result2 = queue.get()

    return result1, result2

def main(stdscr):
    mnemo = Mnemonic("english")
    word_list = mnemo.wordlist

    num_palavras = 12  # Exemplo: escolha 12 palavras

    result1, result2 = gerar_frases_aleatorias_com_ambas(stdscr, num_palavras, word_list)

    # Exibir resultados na tela
    stdscr.clear()
    stdscr.addstr(0, 0, f"Wallet Generator 1: {result1[1]} gerações em {result1[2]:.2f} segundos")
    stdscr.addstr(1, 0, f"Gerações por segundo: {result1[1] / result1[2]:.2f}")
    stdscr.addstr(2, 0, f"Wallet Generator 2: {result2[1]} gerações em {result2[2]:.2f} segundos")
    stdscr.addstr(3, 0, f"Gerações por segundo: {result2[1] / result2[2]:.2f}")
    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(main)
