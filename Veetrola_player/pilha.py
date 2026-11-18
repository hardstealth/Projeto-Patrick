
class Pilha:
    def __init__(self):
        """Inicializa uma pilha vazia."""
        self.itens = []

    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0

    def empilhar(self, item):
        """Adiciona um item no topo da pilha (push)."""
        self.itens.append(item)# faz com append para não apagar o que ja existe

    def desempilhar(self):
        """Remove e retorna o item do topo da pilha (pop)."""
        if self.esta_vazia():
            raise IndexError("Não é possível desempilhar: a pilha está vazia!")#Tratamento de erro; no caso o raise é uma palavra reserva do python que para o código e sinaliza o erro, e o index error é quando tenta acessar um indice que não existe(no caso o indice da pilha)
        return self.itens.pop()

    def topo(self):
        """Retorna o item do topo sem removê-lo (peek)."""
        if self.esta_vazia():
            raise IndexError("Não é possível ver o topo: a pilha está vazia!")
        return self.itens[-1]

    def tamanho(self):
        """Retorna o número de itens na pilha."""
        return len(self.itens)

    def __str__(self):
        """Representação visual da pilha (topo à esquerda)."""
        if self.esta_vazia():
            return "Pilha vazia"
        return "Topo -> " + " | ".join(str(x) for x in reversed(self.itens))


# ------------------- Exemplo de uso -------------------
if __name__ == "__main__":
    pilha = Pilha()

    print("Empilhando: 10, 20, 30")
    pilha.empilhar(10)
    pilha.empilhar(20)
    pilha.empilhar(30)

    print(f"Estado da pilha: {pilha}")
    print(f"Topo: {pilha.topo()}")
    print(f"Tamanho: {pilha.tamanho()}")

    print(f"\nDesempilhando: {pilha.desempilhar()}")
    print(f"Estado da pilha: {pilha}")
    print(f"Novo topo: {pilha.topo()}")

    print(f"\nDesempilhando: {pilha.desempilhar()}")
    print(f"Desempilhando: {pilha.desempilhar()}")
    print(f"Pilha está vazia? {pilha.esta_vazia()}")

    # Testando erro ao desempilhar vazia
    try:
        pilha.desempilhar()
    except IndexError as e:
        print(f"\nErro capturado: {e}")
