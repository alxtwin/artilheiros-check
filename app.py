# NOME DO JOGADOR
# NUMERO DE PARTIDAS
# NUMERO DE GOLS
from math import *
from multiprocessing.sharedctypes import Value
from numpy import *

artilheiros_historicos = [

    {"nome": "PELÉ",
     "posicao": "ATACANTE",
     "jogos": 818,
     "gols": 753, },

    {"nome": "ROMÁRIO",
     "posicao": "ATACANTE",
     "jogos": 955,
     "gols": 744, },

    {"nome": "CRUYIFF",
     "posicao": "MEIO-CAMPO",
     "jogos": 710,
     "gols": 403, },

    {"nome": "MARADONA",
     "posicao": "MEIO-CAMPO",
     "jogos": 680,
     "gols": 346, },

    {"nome": "RONALDO",
     "posicao": "ATACANTE",
     "jogos": 616,
     "gols": 414, },

    {"nome": "NETO",
     "posicao": "MEIO-CAMPO",
     "jogos": 583,
     "gols": 172, },
]


def media_gols(gols, jogos):
    return gols/jogos


def maravilha(gols):
    if gols > 1000:
        tulio = print("Mais que o Túlio Maravilha, hein?")
        return tulio
    
# def posicoes_disponiveis():
#     for jogador in artilheiros_historicos:
#         print(jogador['posicao'].lower())


def checar_craque(media_de_gols):
    if media_de_gols > 0.6:
        print('Craque!')
        print()
    else:
        print('Pé de rato.')
        print()


def check_artilheiro_historico(nome, posicao):
    for jogador in artilheiros_historicos:
        if jogador['nome'] == nome and jogador['posicao'] == posicao:
            print(f'{nome} é um jogador histórico!')
            print(
                f'Você jogou {jogador["jogos"]} partidas e fez {jogador["gols"]} gols.')
            print(
                f'Uma média de {jogador["gols"] / jogador["jogos"] : .2f} gols por partida!')
            print()
            main()


def maior_media_posicao(media_de_gols, posicao):
    for jogador in artilheiros_historicos:
        if posicao == jogador['posicao']:
            if media_de_gols > jogador['gols'] / jogador['jogos']:
                print(f'{jogador["nome"]}, com uma média de {jogador["gols"] / jogador["jogos"] : .2f} gols por partida.')


def maior_media(media_de_gols):
    for jogador in artilheiros_historicos:
        if media_de_gols > jogador['gols'] / jogador['jogos']:
            print(f'{jogador["nome"]}, com uma média de {jogador["gols"] / jogador["jogos"] : .2f} gols por partida.')


def lista_artilheiros_historicos(sim):
    if sim == 'sim':
        print('Lista de artilheiros históricos:')
        for v in range(len(artilheiros_historicos)):
            nome_artilheiro = artilheiros_historicos[v]['nome']
            gols_artilheiro = artilheiros_historicos[v]['gols']
            partidas_artilheiro = artilheiros_historicos[v]['jogos']
            posicao = artilheiros_historicos[v]['posicao']
            media_gols = artilheiros_historicos[v]['gols'] / \
                artilheiros_historicos[v]['jogos']
            print()
            print(
                f'O {posicao} {nome_artilheiro} jogou {partidas_artilheiro} partidas e fez {gols_artilheiro} gols.')
            print(
                f'{nome_artilheiro} teve uma média de {media_gols : .2f} gols por partida!')
            print()
            
def main():
    while True:
                
        print('Bem-vindo ao sistema de artilheiros!')
        print('Deseja ver a lista de artilheiros históricos? (sim/não): ')
        sim = input()
        if sim == 'sim':
            lista_artilheiros_historicos(sim)
            break
        
        print()
        print('Digite o nome do jogador: ')
        nome = input()
        print('Digite a posição do jogador: ')
        # posicoes_disponiveis()
        posicao_jogador = input()
        check_artilheiro_historico(nome.upper(), posicao_jogador.upper())
        try:
            print(('Digite o numero total de gols: '))
            gols = int(input())
            maravilha(gols)
            print('Digite o numero total de jogos: ')
            jogos = int(input())
        except ValueError:
            print('Digite um número válido!')
            print('Voltando ao início...')
            print()
            continue
        
        print(
            f'Ao todo, o {posicao_jogador.upper()} {nome.upper()} jogou {jogos} e anotou {gols} gols.')
        print()

        media_de_gols = media_gols(gols, jogos)

        print(f'{nome.upper()} teve uma média de:')
        print(f'{media_de_gols : .2f} gols por partida')
        print()

        checar_craque(media_de_gols)
        print(f'Entre os jogadores da posição, {nome} tem uma média melhor que: ')
    
        if maior_media_posicao(media_de_gols, posicao_jogador.upper()) == None:    
            print('Ninguém.')
        else:
            maior_media_posicao(media_de_gols, posicao_jogador.upper())         
        print(f'Entre todos os jogadores, {nome} tem uma média melhor que: ')
        if maior_media(media_de_gols) == None:
            print('Ninguém.')
        else:
            maior_media(media_de_gols)
        print()
        print('Deseja adicionar o jogador à lista de artilheiros históricos? (sim/não)')
        if input() == 'sim':
            print('Jogador adicionado com sucesso!')
            print()
          
        print('Deseja continuar? (sim/não')
        resposta = input()
        if resposta == 'sim':
            print()
            continue
        else:
            print('Até mais!')
            break


if __name__ == "__main__":
    main()
