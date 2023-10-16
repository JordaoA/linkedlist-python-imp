class OutOfBoundsException(Exception):
    pass

class LinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo.
    """

    def __init__(self, value, next=None):
        """
        value = valor do nó atual.
        next = apontador para próximo nó.
        """
        self._value = value
        self._next = next

    @property
    def value(self):
        """
        Retorna o valor do nó atual.
        """
        return self._value

    @property
    def next(self):
        """
        Retorna o apontador para o próximo nó.
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Define o apontador para o próximo nó.
        """
        self._next = node

    def hasNext(self):
        """
        Retorna True se existir um próximo nó, False caso contrário.
        """
        return self._next is not None


class LinkedList(object):
    """
    Construtor de lista ligada. A lista sempre começa vazia.
    """
    def __init__(self):
        self._head = None # Apontador para o nó cabeça (primeiro)
        self._tail = None # Apontador para o nó filho (ultimo)
        self._len = 0 # Contador indicativo do tamanho da lista ligada

    def __len__(self):
        return self._len

    @property
    def head(self):
        """
        Esta propriedade deve retornar o valor do primeiro nó da lista ligada.
        """
        return self._head

    @property
    def tail(self):
        """
        Esta propriedade deve retornar o valor do último nó da lista ligada.
        """
        return self._tail

    def append(self, value):
        """
        Esta função deve inserir um novo nó no FINAL da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - append(0) - [1, 2, 3, 0]
        """
        new_node = LinkedListNode(value)
        if self._len == 0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._len += 1

    def insert(self, value):
        """
        Esta função deve inserir um novo nó no INICIO da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - insert(0) - [0, 1, 2, 3]
        """
        new_node = LinkedListNode(value)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._len += 1

    def removeFirst(self):
        """
        Esta função deve remover o primeiro elemento da lista e retornar o seu valor.
        Apos a execução, a lista ligada deve ter um elemento a menos.
        """
        removedNode = None
        if self._head:
            removedNode = self._head
            self._head = self._head.next
            self._len -= 1
        
        return removedNode.value

    def getValueAt(self, index):
        """
        Esta função deve retornar o valor de um nó na posição definida por INDEX.
        Se o index for maior do que o tamanho da lista, retornar OutOfBoundsException.
        """
        if 0 <= index < self._len:
            current = self._head
            for _ in range(index):
                current = current.next
            return current.value
        else:
            raise IndexError("Index out of range")

    def toList(self):
        """
        Esta função retornar uma representação em forma de vetor ([1, 2, 3....])
        da lista ligada.
        """
        result = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result