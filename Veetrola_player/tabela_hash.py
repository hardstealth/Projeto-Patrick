class NoHash:
    def __init__(self, musica, proximo=None):
        self.musica = musica
        self.proximo = proximo


class TabelaHash:
    def __init__(self, capacidade=103):
        self.capacidade = capacidade
        self.buckets = [None] * self.capacidade
        self.quantidade = 0
        self.colisoes = 0

    def _normalizar(self, titulo):
        return titulo.strip().lower()

    def _hash(self, titulo):
        chave = self._normalizar(titulo)
        valor = 0
        for ch in chave:
            valor = (valor * 31 + ord(ch)) % self.capacidade
        return valor

    def fator_de_carga(self):
        return self.quantidade / self.capacidade

    def inserir(self, musica):
        indice = self._hash(musica.titulo)
        chave = self._normalizar(musica.titulo)
        atual = self.buckets[indice]

        if atual is not None:
            self.colisoes += 1

        while atual is not None:
            if self._normalizar(atual.musica.titulo) == chave:
                atual.musica = musica
                return
            atual = atual.proximo

        self.buckets[indice] = NoHash(musica, self.buckets[indice])
        self.quantidade += 1

    def buscar(self, titulo):
        indice = self._hash(titulo)
        chave = self._normalizar(titulo)
        atual = self.buckets[indice]

        while atual is not None:
            if self._normalizar(atual.musica.titulo) == chave:
                return atual.musica
            atual = atual.proximo

        return None
