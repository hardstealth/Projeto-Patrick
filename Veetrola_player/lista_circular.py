class No:  # seria o no em uma lista normal -> elemento individual da lista
    def __init__(self, dado):
        self.dado = dado  # OBS -> PRECISA DO SELF PORQUE POO em python é estranho (esta se referindo ao objeto da vez)
        self.proximo = None   # Ponteiro para o proximo no
        self.anterior = None  # Ponteiro para o no anterior


class ListaDuplamenteEncadeadaCircular:  # estrutura da lista
    def __init__(self):
        self.cabeca = None  # Primeiro no da lista (início)
        self.atual = None   # Ponteiro que acompanha a música tocando agora na vitrola

    def esta_vazia(self):
        return self.cabeca is None  # verifica se a lista está vazia ou não

    def inserir_no_fim(self, dado):
        novo_no = No(dado)  # cria um novo objeto da classe No

        # Caso 1: A lista está vazia
        if self.esta_vazia():  # Usa a função esta_vazia para verificar se a lista está vazia
            self.cabeca = novo_no  # cria a lista usando o primeiro no adicionado
            self.atual = novo_no   # a primeira música inserida já fica pronta na agulha
            novo_no.proximo = novo_no   # Aponta para si mesmo porque é circular e só tem ele na lista
            novo_no.anterior = novo_no  # Aponta para si mesmo porque é circular e só tem ele na lista
            return

        # Caso 2: A lista já tem elementos
        # Como é circular, o "anterior" da cabeça é sempre o último nó (cauda)
        ultimo = self.cabeca.anterior

        # Quando um novo no é adicionado
        novo_no.proximo = self.cabeca  # o novo no vai ficar no final, ele tem que apontar para o inicio como o proximo
        novo_no.anterior = ultimo      # como o novo no vai ficar no final, o antecessor dele é o antigo ultimo
        ultimo.proximo = novo_no       # atualiza o antigo ultimo para apontar para o novo no
        self.cabeca.anterior = novo_no # Manda a origem da lista apontar para o novo no

    # --- Métodos de integração com o MusicPlayerVitrola ---

    def inserir(self, musica):
        """Mantém compatibilidade com a chamada player.playlist.inserir()."""
        self.inserir_no_fim(musica)

    def avancar(self):
        """Move o ponteiro 'atual' para o próximo nó em O(1)."""
        if self.esta_vazia():
            return None
        self.atual = self.atual.proximo
        return self.atual.dado

    def voltar(self):
        """Move o ponteiro 'atual' para o nó anterior em O(1)."""
        if self.esta_vazia():
            return None
        self.atual = self.atual.anterior
        return self.atual.dado

    def obter_atual(self):
        """Retorna o objeto Musica que está no nó 'atual'."""
        return self.atual.dado if self.atual is not None else None

    def definir_atual(self, musica):
        """Percorre o ciclo a partir da cabeça até encontrar a música e atualiza 'atual'."""
        if self.esta_vazia():
            return False

        temp = self.cabeca
        while True:
            if temp.dado.titulo.lower() == musica.titulo.lower():
                self.atual = temp
                return True
            temp = temp.proximo
            if temp == self.cabeca:  # Deu a volta completa sem encontrar
                break
        return False

    # --- Métodos de exibição (sem usar list.append para cumprir a regra 3.1) ---

    def exibir_frente(self):
        """Percorre a lista do início ao fim."""
        if self.esta_vazia():
            print("Lista vazia.")
            return

        atual = self.cabeca
        saida = ""
        while True:
            saida += str(atual.dado)
            atual = atual.proximo
            if atual == self.cabeca:  # Condição de parada: deu a volta completa na lista
                break
            saida += " <-> "
        print(saida + " (volta ao início)")

    def exibir_tras(self):
        """Percorre a lista de trás para frente."""
        if self.esta_vazia():
            print("Lista vazia.")
            return

        ultimo = self.cabeca.anterior  # começa pelo ultimo porque a lista é ao contrario
        atual = ultimo
        saida = ""
        while True:
            saida += str(atual.dado)
            atual = atual.anterior  # aponta para o no anterior
            if atual == ultimo:  # Condição de parada: voltou ao último
                break
            saida += " <-> "
        print(saida + " (volta ao fim)")


# Só executa os testes se rodar este arquivo diretamente (não roda no import do main.py)
if __name__ == "__main__":
    lista = ListaDuplamenteEncadeadaCircular()
    lista.inserir_no_fim(10)
    lista.inserir_no_fim(20)
    lista.inserir_no_fim(30)

    lista.exibir_frente()  # Saída: 10 <-> 20 <-> 30 (volta ao início)
    lista.exibir_tras()    # Saída: 30 <-> 20 <-> 10 (volta ao fim)
