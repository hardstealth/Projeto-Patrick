# Fila


class No:       # Guarda o dado e a referência para o próximo nó.
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Fila:         # Fila FIFO
    def __init__(self):
        self.inicio = None      # inicio: primeiro elemento (de onde se remove)
        self.fim = None         # fim: último elemento (onde se insere)
        self._tamanho = 0


    def enfileirar(self, dado):         # Insere no FIM da fila
        novo = No(dado)
        if self.fim is None:          # fila vazia: o novo é o único
            self.inicio = novo
            self.fim = novo
        else:                         # encaixa depois do último e move o 'fim'
            self.fim.proximo = novo
            self.fim = novo
        self._tamanho += 1

    def desenfileirar(self): #Remove e devolve o elemento do início
        if self.inicio is None:
            raise IndexError("Fila vazia: não há nada para desenfileirar")
        no = self.inicio
        self.inicio = no.proximo

# CASO CRÍTICO: se era o último elemento, o 'fim' ficaria apontando para um nó que não está mais na fila, precisa voltar a None.  
        if self.inicio is None:         
            self.fim = None
        no.proximo = None       # "solta" o nó removido
        self._tamanho -= 1
        return no.dado

    def frente(self):       # Consulta (sem remover) o próximo a sair
        if self.inicio is None:
            raise IndexError("Fila vazia")
        return self.inicio.dado


# utilitários


    def vazia(self):
        return self.inicio is None

    def tamanho(self):
        return self._tamanho

    def __len__(self):
        return self._tamanho

    def __iter__(self):         # Permite percorrer a fila sem removê-la: for m in fila.
        atual = self.inicio

        while atual is not None:
            yield atual.dado
            atual = atual.proximo

    def limpar(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def remover(self, dado):        
        # Remove a 1ª ocorrência de dado (comparação por ==).
        # Operação EXTRA (não faz parte do FIFO puro).
        # Usada para cancelar um "tocar a seguir".
        anterior = None
        atual = self.inicio

        while atual is not None:
            if atual.dado == dado:
                if anterior is None:        # era o primeiro
                    self.inicio = atual.proximo
                else:       # "pula" o nó removido
                    anterior.proximo = atual.proximo
                if atual is self.fim:       # era o último
                    self.fim = anterior
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def __str__(self):
        if self.vazia():
            return "[fila vazia]"
        texto = ""
        atual = self.inicio
        while atual is not None:
            if texto:
                texto += "  ->  "
            texto += str(atual.dado)
            atual = atual.proximo
        return texto


# módulo responsável pela fila "Tocar a seguir".
# Este arquivo mostra como a Fila se integra ao resto do sistema.


from estruturas.fila import Fila
import time

class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao      # segundos

    def __str__(self):
        return f"{self.titulo} — {self.artista}"

    def __repr__(self):
        return f"Musica({self.titulo!r})"

    def __eq__(self, outro):        # necessário para Fila.remover() achar a música por igualdade
        return (isinstance(outro, Musica)
                and self.titulo == outro.titulo
                and self.artista == outro.artista)


# Playlist (LISTA ENCADEADA - JOÃO)
# Acrescentar AQUI


# PLAYER

class Player:
    def __init__(self, playlist):
        self.playlist = playlist
        self.a_seguir = Fila()
        self.atual = None

    def tocar_agora(self, musica):
        self.atual = musica
        print(f"▶  Tocando agora: {self.atual}")

    def agendar(self, musica):      # Usuário pediu "tocar a seguir" entra no FIM da fila.
        self.a_seguir.enfileirar(musica)
        print(f"＋ '{musica.titulo}' agendada "
              f"(posição {self.a_seguir.tamanho()} na fila)")

    def proxima(self):      
    # REGRA CENTRAL DO SISTEMA:
    # 1º) se há pedidos em "tocar a seguir", eles têm PRIORIDADE;
    # 2º) senão, segue a ordem natural da playlist.
        if not self.a_seguir.vazia():
            self.atual = self.a_seguir.desenfileirar()
            print(f"▶  (da fila) Tocando agora: {self.atual}")
        else:
            self.atual = self.playlist.proxima()
            print(f"▶  (da playlist) Tocando agora: {self.atual}")
        return self.atual

    def cancelar_agendada(self, titulo):
        alvo = None
        for m in self.a_seguir:
            if m.titulo == titulo:
                alvo = m
                break

        if alvo is None:
            print(f"✖ Não há '{titulo}' na fila.")
            return False

        self.a_seguir.remover(alvo)
        print(f"✖ '{titulo}' removida da fila.")
        return True

    def mostrar_fila(self):
        print(f"Fila 'tocar a seguir' ({self.a_seguir.tamanho()} faixa(s)):")
        print("   ", self.a_seguir)


# TESTE DE CARGA

def teste_de_carga(n=50000):
    print(f"\n=== TESTE DE CARGA — Fila ({n} elementos) ===")
    f = Fila()

    t0 = time.perf_counter()
    for i in range(n):
        f.enfileirar(i)
    t1 = time.perf_counter()

    for i in range(n):
        f.desenfileirar()
    t2 = time.perf_counter()

    print(f"enfileirar   : {t1 - t0:.4f}s  ({(t1-t0)/n*1e6:.2f} µs/operação)")
    print(f"desenfileirar: {t2 - t1:.4f}s  ({(t2-t1)/n*1e6:.2f} µs/operação)")
    print(f"total        : {t2 - t0:.4f}s para {2*n} operações")
    print("Custo cresce LINEAR com n  ->  O(n) no total, O(1) por operação.")
    print("(Se fosse uma list com pop(0), o total seria O(n²).)\n")


# MENU 

def main():
    catalogo = (
        Musica("Bohemian Rhapsody", "Queen", 355),
        Musica("Imagine", "John Lennon", 183),
        Musica("Aquarela", "Toquinho", 240),
        Musica("Construção", "Chico Buarque", 320),
    )

    player = Player(PlaylistSimples(catalogo))

    while True:
        print("""
╔══════════════════════════════════════════╗
║  PLAYER — MÓDULO "TOCAR A SEGUIR" (Fila) ║
╠══════════════════════════════════════════╣
║  1) Agendar música para tocar a seguir   ║
║  2) Próxima faixa (pular)                ║
║  3) Ver fila                             ║
║  4) Cancelar agendamento                 ║
║  5) Teste de carga                       ║
║  0) Sair                                 ║
╚══════════════════════════════════════════╝""")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            for i, m in enumerate(catalogo, start=1):
                print(f"  {i}) {m}")
            escolha = input("Número da música: ").strip()
            try:
                player.agendar(catalogo[int(escolha) - 1])
            except (ValueError, IndexError):
                print("Opção inválida.")

        elif opcao == "2":
            player.proxima()

        elif opcao == "3":
            player.mostrar_fila()

        elif opcao == "4":
            titulo = input("Título a cancelar: ").strip()
            player.cancelar_agendada(titulo)

        elif opcao == "5":
            teste_de_carga()

        elif opcao == "0":
            print("Até mais! 🎧")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
