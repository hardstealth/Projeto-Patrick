class NoHash:
    def __init__(self, chave, musica):
        self.chave = chave
        self.musica = musica
        self.proximo = None


class TabelaHash:
    def __init__(self, capacidade=101):
        self.capacidade = capacidade
        # Único uso de list: vetor de tamanho fixo para buckets (regra 3.1)
        self.buckets = [None] * self.capacidade
        self.total_elementos = 0
        self.colisoes = 0

    def _funcao_hash(self, chave):
        """Hash polinomial simples (base 31) sobre a chave em minúsculo."""
        chave_norm = chave.lower().strip()
        h = 0
        for caractere in chave_norm:
            h = (h * 31 + ord(caractere)) % self.capacidade
        return h

    def inserir(self, musica):
        chave = musica.titulo.lower().strip()
        indice = self._funcao_hash(chave)
        atual = self.buckets[indice]

        # Se já existe, atualiza o registro
        while atual is not None:
            if atual.chave == chave:
                atual.musica = musica
                return
            atual = atual.proximo

        # Se o bucket já tinha algo, registra colisão (encadeamento separado)
        if self.buckets[indice] is not None:
            self.colisoes += 1

        novo_no = NoHash(chave, musica)
        novo_no.proximo = self.buckets[indice]
        self.buckets[indice] = novo_no
        self.total_elementos += 1

    def buscar(self, titulo):
        chave = titulo.lower().strip()
        indice = self._funcao_hash(chave)
        atual = self.buckets[indice]
        while atual is not None:
            if atual.chave == chave:
                return atual.musica
            atual = atual.proximo
        return None

    def remover(self, titulo):
        chave = titulo.lower().strip()
        indice = self._funcao_hash(chave)
        atual = self.buckets[indice]
        anterior = None

        while atual is not None:
            if atual.chave == chave:
                if anterior is None:
                    self.buckets[indice] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.total_elementos -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def fator_de_carga(self):
        return self.total_elementos / self.capacidade
