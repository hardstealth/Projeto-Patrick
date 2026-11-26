class NoPilha:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.topo is None

    def empilhar(self, musica):
        novo_no = NoPilha(musica)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            return None
        musica_topo = self.topo.musica
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return musica_topo

    def listar_elementos(self, limite=5):
        if self.esta_vazia():
            return "  (Histórico vazio)"
        resultado = ""
        atual = self.topo
        cont = 0
        while atual is not None and cont < limite:
            resultado += f"  - {atual.musica}\n"
            atual = atual.proximo
            cont += 1
        return resultado.rstrip()
