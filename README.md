# Linked-List em Python

Este é um código em Python que implementa uma lista ligada simples, incluindo classes para nós individuais e a própria lista ligada. Abaixo, vou explicar a estrutura e funcionalidade do código.

## Classes

### OutOfBoundsException:

Uma exceção personalizada que é levantada quando uma operação tenta acessar um índice fora dos limites da lista.

### LinkedListNode:

Esta classe representa um nó individual na lista ligada. Cada nó contém um valor e uma referência para o próximo nó (ou pode ser nulo no caso do último nó).

- `__init__(self, value, next=None)`: O construtor da classe que inicializa um nó com um valor dado e uma referência opcional para o próximo nó.
- `value`: Uma propriedade que retorna o valor armazenado no nó.
- `next`: Uma propriedade que retorna o próximo nó ou define o próximo nó.
- `hasNext(self)`: Um método que verifica se existe um próximo nó.

### LinkedList:

Esta classe representa a lista ligada em si e contém métodos para manipular a lista.

- `__init__(self)`: O construtor da classe inicializa uma lista ligada vazia.
- `__len__(self)`: Retorna o número de elementos na lista.
- `head`: Uma propriedade que retorna o primeiro nó da lista.
- `tail`: Uma propriedade que retorna o último nó da lista.
- `append(self, value)`: Adiciona um novo nó com o valor fornecido no final da lista.
- `insert(self, value)`: Insere um novo nó com o valor fornecido no início da lista.
- `removeFirst(self)`: Remove o primeiro nó da lista e retorna seu valor.
- `getValueAt(self, index)`: Retorna o valor do nó na posição especificada pelo índice.
- `toList(self)`: Converte a lista ligada em uma lista Python convencional e a retorna.

O código fornece uma estrutura básica para criar e manipular listas ligadas em Python. Você pode usar essas classes para criar e gerenciar listas ligadas em seus programas. Certifique-se de lidar com exceções, como `OutOfBoundsException`, ao acessar elementos fora dos limites da lista.

## Guia de Uso da Linked-List

Este guia descreve como utilizar o código da lista ligada em Python e executar os testes para verificar seu funcionamento. O código inclui o arquivo `main.py` que executa os testes definidos no arquivo `tests.py`.

### Clonando o Repositório

Antes de usar a lista ligada, você precisa clonar o repositório que contém o código. Siga as etapas abaixo:

1. Abra seu terminal ou prompt de comando.
2. Navegue até o diretório onde deseja clonar o repositório.
3. Execute o seguinte comando para clonar o repositório:

```bash
git clone https://github.com/JordaoA/linkedlist-python-imp.git
```

### Executando os Testes

A lista ligada vem com um conjunto de testes para verificar sua funcionalidade. Para executar os testes, siga estas etapas:

1. Navegue até o diretório do repositório clonado:

```bash
cd linkedlist-python-imp
```

2. Execute o arquivo `main.py`:

```bash
python3 src/main.py
```

Isso executará os testes definidos no arquivo `tests.py` e exibirá os resultados no terminal.

### Resultados dos Testes

- O primeiro teste verifica as operações básicas da lista ligada, como adicionar, inserir e remover elementos, bem como verificar o estado da lista em diferentes etapas. Se todos os testes passarem, a mensagem "Casos de Testes: 1, passaram com sucesso!" será exibida.

- O segundo teste adiciona elementos à lista, verifica o acesso a elementos fora dos limites, remove elementos e verifica o estado da lista. Se todos os testes passarem, a mensagem "Casos de Testes: 2, passaram com sucesso!" será exibida.

Se ambos os conjuntos de testes passarem, isso indica que a lista ligada está funcionando conforme o esperado.

## Personalização e Uso

Você pode personalizar e usar a lista ligada em seus próprios projetos. O código inclui uma estrutura básica para listas ligadas, e os testes ajudam a garantir seu correto funcionamento. Para utilizar a lista ligada em seus programas, importe as classes do arquivo `modules.linkedList` e utilize as funções e métodos conforme necessário.

Lembre-se de que, se você desejar, pode adicionar mais testes ou adaptar os testes existentes para atender às suas necessidades específicas. Certifique-se de que todos os testes passem antes de usar a lista ligada em um projeto real.
