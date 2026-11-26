# fila.py

class No:       #Guarda o dado e a referência para o próximo nó.
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Fila:         #Fila FIFO: enfileira no fim, desenfileira no início. O(1) por operação.
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def enfileirar(self, dado):
        novo = No(dado)
        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self._tamanho += 1

    def desenfileirar(self):
        if self.inicio is None:
            raise IndexError("Fila vazia: não há nada para desenfileirar")
        no = self.inicio
        self.inicio = no.proximo
        if self.inicio is None:
            self.fim = None
        no.proximo = None
        self._tamanho -= 1
        return no.dado

    def frente(self):
        if self.inicio is None:
            raise IndexError("Fila vazia")
        return self.inicio.dado

    def vazia(self):
        return self.inicio is None

    def tamanho(self):
        return self._tamanho

    def __len__(self):
        return self._tamanho

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual.dado
            atual = atual.proximo

    def limpar(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def remover(self, dado):        #Remove a 1ª ocorrência de dado (comparação por ==). O(n).
        anterior = None
        atual = self.inicio
        while atual is not None:
            if atual.dado == dado:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual is self.fim:
                    self.fim = anterior
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def listar_elementos(self):         #Compatível com renderizar_tela() em veetrola_ui.py.
        if self.vazia():
            return "  (Fila vazia)"
        resultado = ""
        atual = self.inicio
        while atual is not None:
            resultado += f"  - {atual.dado}\n"
            atual = atual.proximo
        return resultado.rstrip()

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
