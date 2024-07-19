# other_program.py

import curses
from mnemonic import Mnemonic
import wallet_generator as wg1
import wallet_generator2 as wg2

def gerar_frases_aleatorias_com_ambas(stdscr, num_palavras, word_list):
    wg1.gerar_frases_aleatorias(stdscr, num_palavras, word_list)
    wg2.gerar_frases_aleatorias(stdscr, num_palavras, word_list)

def main(stdscr):
    mnemo = Mnemonic("english")
    word_list = mnemo.wordlist

    num_palavras = 12  # Exemplo: escolha 12 palavras

    gerar_frases_aleatorias_com_ambas(stdscr, num_palavras, word_list)

if __name__ == "__main__":
    curses.wrapper(main)
