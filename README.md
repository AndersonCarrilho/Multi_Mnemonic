# Gerador de Mnemonics WIF Randomico

Este script em python elaborado em cima de Ubuntu e Arch Linux, utiliza bibliotecas como Multiprocessing, lru_cache, para melhor performance em hardwares mais modestos. Foi testado em cima de uma CPU I7 de 4 Geração com 8 Nucleos e 8 Gigas de RAM.
Sua capacidade em cima deste hardware chegou a 22 mil gerações por segundos, seu sistema de limpeza de cache via psutil, fica em constante analise de utilização de recursos do algoritimo para que não aconteça travamentos de hardware, podendo utilizar o hardware para outras funções.

Ele trabalha com a biblioteca mnemonic do python onde ordena que das 2048 palavras existentes na lingua inglesa, cada uma das 2048 palavras são utilizadas como primeira das sequencias, e o restante de forma aleatoria, assim gerando por ciclo, 2048 gerações por ciclo, onde atingi a capacidade de 22 mil gerações por segundo com o hardware testado.

Este script faz parte de um projeto maior onde venho estudando as formas de segurança de geração de cripto Wallets de onde dou o crédito das idéias ao grande programador @PyMmdrza.
Ou sejá, este script é uma pequena parte de um algoritimo muito maior onde esta sendo elaborado ao longo de 2 anos de pesquisa, e 1 ano de estruturação que já esta em fase final de testes.

Futuramente postarei mais partes do Algoritimo Final, lembrando que todos os algoritimos são feitos para rodar em CPU's, a utilização de GPU's não postarei tão cedo ainda por motivos de segurança, e não confiar no Humano que utilizará do mesmo para fins não aceitaveis pelo meu padrão de boas condutas.
Então se este script básico pode gerar 22 mil informações por segundo, imagina oque ele fez em sua versão mais básica utilizando uma simples Quadro P1000? Práticamente 180 mil gerações por segundo, os testes em cima de 2 GPU's Nvidia 4090 ligadas no mesmo Hardware chegou a 590 mil gerações por segundo sem o sistema de controle de cache, com o controle de cache ele chegou a 1.000.470 gerações por segundo.

A versão que denomiei como versão PRO, tem capacidade de multiplos sistemas de Gerações de Mnemonics possiveis, coisas que surgem na cabeça de programador que só Deus sabe como vem. Ele tem capacidade de geração de mais de 2 Milhões de Informações por segundo, de todos os formatos de Mnemonics, ou seja, de 12, 18, e 24 palavras, com sistema de Colisão de Informações onde pode ser importado listas gigantes de wallets de todos os padrões de endereço, e consulta de saldos em nível avançado, o sistema de consulta de saldo tem capacidade de consulta por cerca de 3 a 4 mil wallets por segundo usando somente API's Grátis.


Aproveitem e usem este script da forma que mais lhe agrada em seus projetos, qualquer dúvida ou sugestão, estarei aqui pra ajudar ou simplismente ouvir.
