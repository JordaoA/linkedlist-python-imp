# Linked List em Python

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
