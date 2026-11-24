class NoAVL:
    def __init__(self, musica):
        self.musica = musica
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def obter_altura(self, no):
        return no.altura if no is not None else 0

    def _fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def _atualizar_altura(self, no):
        alt_esq = self.obter_altura(no.esquerda)
        alt_dir = self.obter_altura(no.direita)
        no.altura = 1 + (alt_esq if alt_esq > alt_dir else alt_dir)

    def _rotacao_direita(self, y):
        x = y.esquerda
        t2 = x.direita

        x.direita = y
        y.esquerda = t2

        self._atualizar_altura(y)
        self._atualizar_altura(x)
        return x

    def _rotacao_esquerda(self, x):
        y = x.direita
        t2 = y.esquerda

        y.esquerda = x
        x.direita = t2

        self._atualizar_altura(x)
        self._atualizar_altura(y)
        return y

    def inserir(self, musica):
        self.raiz = self._inserir_recursivo(self.raiz, musica)

    def _inserir_recursivo(self, no, musica):
        if no is None:
            return NoAVL(musica)

        chave_nova = musica.titulo.lower()
        chave_atual = no.musica.titulo.lower()

        if chave_nova < chave_atual:
            no.esquerda = self._inserir_recursivo(no.esquerda, musica)
        elif chave_nova > chave_atual:
            no.direita = self._inserir_recursivo(no.direita, musica)
        else:
            no.musica = musica
            return no

        self._atualizar_altura(no)
        fb = self._fator_balanceamento(no)

        # Caso Esquerda-Esquerda
        if fb > 1 and chave_nova < no.esquerda.musica.titulo.lower():
            return self._rotacao_direita(no)

        # Caso Direita-Direita
        if fb < -1 and chave_nova > no.direita.musica.titulo.lower():
            return self._rotacao_esquerda(no)

        # Caso Esquerda-Direita
        if fb > 1 and chave_nova > no.esquerda.musica.titulo.lower():
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)

        # Caso Direita-Esquerda
        if fb < -1 and chave_nova < no.direita.musica.titulo.lower():
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    def buscar(self, titulo):
        return self._buscar_recursivo(self.raiz, titulo.lower())

    def _buscar_recursivo(self, no, chave):
        if no is None:
            return None
        chave_atual = no.musica.titulo.lower()
        if chave == chave_atual:
            return no.musica
        elif chave < chave_atual:
            return self._buscar_recursivo(no.esquerda, chave)
        else:
            return self._buscar_recursivo(no.direita, chave)

    def remover(self, titulo):
        self.raiz = self._remover_recursivo(self.raiz, titulo.lower())

    def _no_menor_valor(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def _remover_recursivo(self, no, chave):
        if no is None:
            return None

        chave_atual = no.musica.titulo.lower()

        if chave < chave_atual:
            no.esquerda = self._remover_recursivo(no.esquerda, chave)
        elif chave > chave_atual:
            no.direita = self._remover_recursivo(no.direita, chave)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            sucessor = self._no_menor_valor(no.direita)
            no.musica = sucessor.musica
            no.direita = self._remover_recursivo(no.direita, sucessor.musica.titulo.lower())

        self._atualizar_altura(no)
        fb = self._fator_balanceamento(no)

        # Rebalanceamento após remoção
        if fb > 1 and self._fator_balanceamento(no.esquerda) >= 0:
            return self._rotacao_direita(no)

        if fb > 1 and self._fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)

        if fb < -1 and self._fator_balanceamento(no.direita) <= 0:
            return self._rotacao_esquerda(no)

        if fb < -1 and self._fator_balanceamento(no.direita) > 0:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    def exibir_em_ordem(self):
        self._in_order(self.raiz)

    def _in_order(self, no):
        if no is not None:
            self._in_order(no.esquerda)
            print(f"  • {no.musica}")
            self._in_order(no.direita)
