class Musica: #seria o no em uma lista normal -> elemento individual da lista
    def __init__(self, musica):
        self.musica = musica #OBS -> PRECISA DO SELF PORQUE POO em python é estranho (esta se referindo ao objeto da vez)
        self.proximo = None   # Ponteiro para a proxima musica
        self.anterior = None  # Ponteiro para a musica anterior


class ListaDuplamenteEncadeadaCircular: # estrutura da lista
    def __init__(self):
        self.cabeca = None  # Primeira musica da lista (início)

    def esta_vazia(self):
        return self.cabeca is None #verifica se a lista está vazia ou não.  Pq se não tem cabeça a lista obrigatoriamente conhnece seu primeiro elemento, caso não conheça ou a lista não existe ou ela está vazia

    def inserir_no_fim(self, musica):
        nova_musica = Musica (musica) #cria um novo objeto da classe musica

        # Caso 1: A lista está vazia
        if self.esta_vazia(): #Usa a função esta_vazia para verificar se a lista está vazia
            self.cabeca = nova_musica #cria a lista usando a primeira musica adicinada
            nova_musica.proximo = nova_musica   # Aponta para si mesmo porque é circular e só tem ela na lista
            nova_musica.anterior = nova_musica  # Aponta para si mesmo porque é circular e só tem ela na lista
            return

        # Caso 2: A lista já tem elementos
        # Como é circular, o "anterior" da cabeça é sempre o último nó (cauda)
        ultimo = self.cabeca.anterior

        # Quando uma nova musica é adicionada
        nova_musica.proximo = self.cabeca #a nova musica vai ficar no final, ela tem que apontar para o inicio como o proximo
        nova_musica.anterior = ultimo # como a nova musica vai ficar no final, o antecessor dela é o antigo ultimo
        ultimo.proximo = nova_musica #atualiza o antigo ultimo para apontar para a nova musica.
        self.cabeca.anterior = nova_musica #Manda a origem da lista apontar para a nova musica (apontar o anterior no caso)

    def exibir_frente(self):
        """Percorre a lista do início ao fim."""
        if self.esta_vazia():# verifica se a lista ta vazia (é um tratamento de excessão praticamente)
            print("Lista vazia.")
            return

        atual = self.cabeca #aponta para o nó que estamos olhando (começa da cabeça porque quer exibir pela frente (se a lista não fosse duplamente encadeada seria obrigado a começar por aqui porque o primeiro elemento conhece o prox))
        elementos = [] # cria uma lista vazia para armazenar os elementos da lista circular
        while True:
            elementos.append(str(atual.musica))#guarda a musica atual como uma string e coloca ela na lista com o append sem apagar o que ja esta la
            atual = atual.proximo #aponta para a proxima musica/no da musica
            if atual == self.cabeca:  # Condição de parada: deu a volta completa na lista
                break
        print(" <-> ".join(elementos) + " (volta ao início)") #O método .join() pega todos os itens da lista elementos (ex: ["Música A", "Música B", "Música C"]) e cola todos em uma única string, colocando " <-> " entre eles

    def exibir_tras(self):
        """Percorre a lista de trás para frente."""
        if self.esta_vazia():
            print("Lista vazia.")
            return

        ultimo = self.cabeca.anterior #começa pelo ultimo porque a lista é ao contrario
        atual = ultimo
        elementos = []
        while True:
            elementos.append(str(atual.musica))
            atual = atual.anterior # aponta para a musica anterior (percorre a lista ao contrario)
            if atual == ultimo:  # Condição de parada: voltou ao último
                break
        print(" <-> ".join(elementos) + " (volta ao fim)")


# --- Exemplo de uso ---
lista = ListaDuplamenteEncadeadaCircular()
lista.inserir_no_fim(10)
lista.inserir_no_fim(20)
lista.inserir_no_fim(30)

lista.exibir_frente()  # Saída: 10 <-> 20 <-> 30 (volta ao início)
lista.exibir_tras()    # Saída: 30 <-> 20 <-> 10 (volta ao fim)
