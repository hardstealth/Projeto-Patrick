# Veetrola Player — Player de Música em Modo Texto (Vitrola ASCII)

Projeto prático final da disciplina de **Estrutura de Dados** (Universidade Federal de Alagoas — Campus Arapiraca), ministrada pelo Prof. Patrick Brito.

O sistema simula um reprodutor de músicas com interface visual de vitrola no terminal (comandos no topo e animação em ASCII na troca de discos), implementando manualmente todas as estruturas de dados sem o uso de `dict`, `set`, `collections` ou métodos dinâmicos de `list`.

## Integrantes do Grupo
* Gyl Yury da Silva Lima
* Raul Correia dos Santos
* João Pedro dos Santos
* Antunes Lenini Farias de Oliveira

## Tema Escolhido
**Tema 5.1 — Player de Música (Playlist)** com interface de vitrola em modo texto.

---

## Como Executar o Programa

1. Certifique-se de ter o **Python 3** instalado.
2. Clone este repositório ou baixe os arquivos para uma mesma pasta:
   ```bash
   git clone [https://github.com/hardstealth/Projeto-Patrick.git](https://github.com/hardstealth/Projeto-Patrick.git)
   cd Veetrola_player
   ```
3. Execute o arquivo principal no terminal:
   ```bash
   python main.py
   ```
   *(No Linux/macOS, utilize `python3 main.py` se necessário.)*

---

## Estruturas de Dados Utilizadas e Justificativas

Todas as estruturas foram implementadas manualmente com classes e nós próprios (`musica.py`, `lista_circular.py`, `fila.py`, `pilha.py`, `tabela_hash.py` e `arvore_avl.py`):

1. **Lista Duplamente Encadeada Circular (`lista_circular.py`)**
   * **Papel no sistema:** Gerencia a playlist principal em reprodução.
   * **Justificativa:** Permite avançar (`proximo`) e retroceder (`anterior`) entre as faixas em tempo constante `O(1)` a partir do nó `atual` (agulha da vitrola), além de proporcionar repetição contínua da playlist sem necessidade de reiniciar índices.

2. **Fila — FIFO (`fila.py`)**
   * **Papel no sistema:** Implementa a fila de prioridade *"Tocar a seguir"*.
   * **Justificativa:** Garante a política *First-In, First-Out* com ponteiros `inicio` e `fim`, assegurando que as músicas enfileiradas pelo usuário toquem exatamente na ordem em que foram adicionadas, com inserção e remoção em `O(1)`.

3. **Pilha — LIFO (`pilha.py`)**
   * **Papel no sistema:** Armazena o histórico de faixas já reproduzidas.
   * **Justificativa:** A política *Last-In, First-Out* permite empilhar a música que acabou de tocar no `topo` em `O(1)` e recuperá-la imediatamente quando o usuário aciona o comando de voltar.

4. **Tabela Hash (`tabela_hash.py`)**
   * **Papel no sistema:** Busca rápida de músicas da biblioteca pelo título.
   * **Justificativa:** Utiliza função de dispersão polinomial (base 31) sobre os caracteres do título normalizado e tratamento de colisões por **encadeamento separado** (nós `NoHash` encadeados em cada bucket de um vetor de tamanho fixo), alcançando tempo médio `O(1)` na localização de faixas.

5. **Árvore AVL (`arvore_avl.py`)**
   * **Papel no sistema:** Mantém o catálogo de músicas ordenado alfabeticamente pelo título.
   * **Justificativa:** Por ser uma árvore binária de busca autobalanceada (via rotações simples e duplas à esquerda/direita sempre que o fator de balanceamento sai do intervalo `[-1, 1]`), impede a degeneração para `O(n)` e garante inserção, busca e remoção em `O(log n)`, além de listar todo o catálogo ordenado por meio do percurso *in-order*.

---

## Tabela de Complexidade Assintótica

| Estrutura | Operação | Melhor Caso | Caso Médio | Pior Caso |
| :--- | :--- | :---: | :---: | :---: |
| **Lista Duplamente Circular** | Inserção no fim (`inserir_no_fim`) | `O(1)` | `O(1)` | `O(1)` |
| **Lista Duplamente Circular** | Avançar / Voltar (`avancar` / `voltar`) | `O(1)` | `O(1)` | `O(1)` |
| **Lista Duplamente Circular** | Buscar faixa (`definir_atual`) | `O(1)` | `O(n)` | `O(n)` |
| **Fila (FIFO)** | Enfileirar (`enfileirar`) | `O(1)` | `O(1)` | `O(1)` |
| **Fila (FIFO)** | Desenfileirar (`desenfileirar`) | `O(1)` | `O(1)` | `O(1)` |
| **Pilha (LIFO)** | Empilhar (`empilhar`) | `O(1)` | `O(1)` | `O(1)` |
| **Pilha (LIFO)** | Desempilhar (`desempilhar`) | `O(1)` | `O(1)` | `O(1)` |
| **Tabela Hash** | Inserção (`inserir`) | `O(1)` | `O(1)` | `O(n)` |
| **Tabela Hash** | Busca (`buscar`) | `O(1)` | `O(1)` | `O(n)` |
| **Tabela Hash** | Remoção (`remover`) | `O(1)` | `O(1)` | `O(n)` |
| **Árvore AVL** | Inserção (`inserir`) | `O(log n)` | `O(log n)` | `O(log n)` |
| **Árvore AVL** | Busca (`buscar`) | `O(1)` | `O(log n)` | `O(log n)` |
| **Árvore AVL** | Remoção (`remover`) | `O(log n)` | `O(log n)` | `O(log n)` |
| **Árvore AVL** | Listagem ordenada (`exibir_em_ordem`) | `O(n)` | `O(n)` | `O(n)` |

---

## Teste de Carga e Análise de Desempenho

O sistema possui a opção **`[T] Carga`** no menu principal, que insere automaticamente **5.000 músicas** sequenciais (`Faixa_Teste_00000` até `Faixa_Teste_04999`) na **Árvore AVL** e na **Tabela Hash** (com capacidade de `1009` buckets).

* **Resultados obtidos:**
  * **Registros inseridos:** `5.000`
  * **Altura final da Árvore AVL:** `13`
  * **Tempo total de inserção:** `~0,04 s`
  * **Fator de carga da Tabela Hash (α):** `4,96` (`5000 / 1009`)
* **Análise:** Mesmo recebendo 5.000 chaves em ordem estritamente crescente — cenário que degeneraria uma Árvore Binária de Busca (BST) comum para altura `5.000` (`O(n)`) —, as rotações de rebalanceamento da Árvore AVL mantiveram a altura em apenas **13 níveis** (`log2(5000) ≈ 12,28`), comprovando o custo logarítmico `O(log n)` na prática. Na Tabela Hash, o encadeamento separado absorveu as colisões mantendo listas curtas nos buckets (~5 nós por bucket em média).

---

## Divisão de Tarefas

| Integrante | Responsabilidade |
| :--- | :--- |
| Gyl Yury da Silva Lima | Implementação da Árvore AVL (`arvore_avl.py`), modelo `musica.py`, interface da vitrola (`veetrola_ui.py`) e documentação |
| Raul Correia dos Santos | Implementação da Fila (`fila.py`) e integração da aplicação principal (`main.py`) |
| João Pedro dos Santos | Implementação da Lista Duplamente Encadeada Circular (`lista_circular.py`), da Pilha (`pilha.py`) e documentação |
| Antunes Lenini Farias de Oliveira | Implementação da Tabela Hash (`tabela_hash.py`) e validação do teste de carga |
