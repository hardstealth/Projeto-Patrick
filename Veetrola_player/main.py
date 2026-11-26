import time
from musica import Musica
from lista_circular import ListaDuplamenteEncadeadaCircular
from fila import Fila
from pilha import Pilha
from tabela_hash import TabelaHash
from arvore_avl import ArvoreAVL
from veetrola_ui import renderizar_tela, animar_troca_disco


class MusicPlayerVeetrola:
    def __init__(self):
        self.playlist = ListaDuplamenteEncadeadaCircular()
        self.fila_proximas = Fila()
        self.historico = Pilha()
        self.tabela_busca = TabelaHash(capacidade=103)
        self.catalogo_avl = ArvoreAVL()
        self.tocando = True
        self.musica_em_execucao = None

    def cadastrar_musica(self, titulo, artista, duracao_seg, arte="♫", na_playlist=True):
        nova = Musica(titulo, artista, duracao_seg, arte)
        self.tabela_busca.inserir(nova)
        self.catalogo_avl.inserir(nova)
        if na_playlist:
            self.playlist.inserir(nova)
            if self.musica_em_execucao is None:
                self.musica_em_execucao = self.playlist.obter_atual()

    def proxima_musica(self):
        antiga = self.musica_em_execucao
        if antiga is not None:
            self.historico.empilhar(antiga)

        # Prioridade 1: Fila "Tocar a seguir" (FIFO)
        if not self.fila_proximas.esta_vazia():
            proxima = self.fila_proximas.desenfileirar()
            self.playlist.definir_atual(proxima)
        else:
            # Prioridade 2: Próxima da Lista Circular
            proxima = self.playlist.avancar()

        self.musica_em_execucao = proxima
        self.tocando = True
        animar_troca_disco(antiga, proxima, self.tocando)

    def musica_anterior(self):
        antiga = self.musica_em_execucao
        # Se houver histórico na pilha, volta para ele; senão volta na lista circular
        if not self.historico.esta_vazia():
            anterior = self.historico.desempilhar()
            self.playlist.definir_atual(anterior)
        else:
            anterior = self.playlist.voltar()

        self.musica_em_execucao = anterior
        self.tocando = True
        animar_troca_disco(antiga, anterior, self.tocando)

    def executar_teste_carga(self, quantidade=5000):
        print(f"\nIniciando teste de carga com {quantidade} músicas...")
        hash_teste = TabelaHash(capacidade=1009)
        avl_teste = ArvoreAVL()

        inicio = time.perf_counter()
        for i in range(quantidade):
            m = Musica(f"Faixa_Teste_{i:05d}", f"Artista_{i % 50}", 180 + (i % 60), "TST")
            hash_teste.inserir(m)
            avl_teste.inserir(m)
        fim = time.perf_counter()

        print("-" * 50)
        print(f"Registros inseridos : {quantidade}")
        print(f"Tempo total         : {fim - inicio:.4f} segundos")
        print(f"Altura da Árvore AVL: {avl_teste.obter_altura(avl_teste.raiz)} (O(log n) garantido)")
        print(f"Colisões na Hash    : {hash_teste.colisoes} (Fator de carga: {hash_teste.fator_de_carga():.2f})")
        print("-" * 50)
        input("Pressione ENTER para voltar à vitrola...")


def carregar_musicas_iniciais(player):
    player.cadastrar_musica("Bohemian Rhapsody", "Queen", 354, "QUN")
    player.cadastrar_musica("Time", "Pink Floyd", 413, "PNK")
    player.cadastrar_musica("Construção", "Chico Buarque", 384, "CHC")
    player.cadastrar_musica("Hotel California", "Eagles", 391, "EGL")
    player.cadastrar_musica("Billie Jean", "Michael Jackson", 294, "MJK")


def main():
    player = MusicPlayerVeetrola()
    carregar_musicas_iniciais(player)

    while True:
        renderizar_tela(
            player.musica_em_execucao,
            player.tocando,
            player.fila_proximas,
            player.historico,
        )
        opcao = input("Escolha uma opção: ").strip().upper()

        if opcao == "P":
            player.tocando = not player.tocando

        elif opcao == "N":
            player.proxima_musica()

        elif opcao == "B":
            player.musica_anterior()

        elif opcao == "F":
            titulo = input("Digite o título exato da música para colocar na fila: ").strip()
            encontrada = player.tabela_busca.buscar(titulo)
            if encontrada:
                player.fila_proximas.enfileirar(encontrada)
                print(f"'{encontrada.titulo}' adicionada à fila!")
            else:
                print("Música não encontrada na Tabela Hash.")
            input("Pressione ENTER para continuar...")

        elif opcao == "S":
            titulo = input("Buscar título na Tabela Hash: ").strip()
            encontrada = player.tabela_busca.buscar(titulo)
            if encontrada:
                print(f"Encontrada em O(1): {encontrada}")
                tocar = input("Deseja tocar agora na vitrola? (s/n): ").strip().lower()
                if tocar == "s":
                    antiga = player.musica_em_execucao
                    if antiga:
                        player.historico.empilhar(antiga)
                    player.playlist.definir_atual(encontrada)
                    player.musica_em_execucao = encontrada
                    player.tocando = True
                    animar_troca_disco(antiga, encontrada, True)
            else:
                print("Música não encontrada.")
                input("Pressione ENTER para continuar...")

        elif opcao == "A":
            print("\n=== CATÁLOGO ORDENADO (PERCURSO IN-ORDER NA AVL) ===")
            player.catalogo_avl.exibir_em_ordem()
            print(f"Altura atual da AVL: {player.catalogo_avl.obter_altura(player.catalogo_avl.raiz)}")
            input("\nPressione ENTER para continuar...")

        elif opcao == "+":
            titulo = input("Título: ").strip()
            artista = input("Artista: ").strip()
            duracao = int(input("Duração (em segundos): ").strip())
            arte = input("Sigla do disco (3 letras): ").strip().upper()
            player.cadastrar_musica(titulo, artista, duracao, arte or "♫")

        elif opcao == "T":
            qtd = input("Quantidade de registros para o teste (padrão 5000): ").strip()
            player.executar_teste_carga(int(qtd) if qtd.isdigit() else 5000)

        elif opcao == "0":
            print("Encerrando vitrola...")
            break


if __name__ == "__main__":
    main()

