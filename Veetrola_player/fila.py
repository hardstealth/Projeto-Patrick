class NoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, musica):
        novo_no = NoFila(musica)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        self.tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        musica_removida = self.inicio.musica
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return musica_removida

    def listar_elementos(self):
        """Retorna uma string formatada sem usar list.append."""
        if self.esta_vazia():
            return "  (Fila vazia)"
        resultado = ""
        atual = self.inicio
        pos = 1
        while atual is not None:
            resultado += f"  {pos}. {atual.musica}\n"
            atual = atual.proximo
            pos += 1
        return resultado.rstrip()
