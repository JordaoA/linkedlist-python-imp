from modules.linkedList import LinkedList

def default_test():
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente.
    """
    ll = LinkedList()

    # Verifique se a cabeça (head) e a cauda (tail) da lista estão vazias
    assert(ll.head is None)
    assert(ll.tail is None)

    # Verifique se a lista está vazia usando toList()
    assert(ll.toList() == [])

    # Adiciona um elemento à lista e verifique se a cabeça, a cauda e o comprimento estão corretos
    ll.append(1)
    assert(ll.head.value == 1)
    assert(ll.tail.value == 1)
    assert(len(ll) == 1)

    # Verifica se a lista contém o elemento adicionado usando toList()
    assert(ll.toList() == [1])

    # Adiciona mais elementos à lista e verifique a cabeça, a cauda e o comprimento
    ll.append(2)
    assert(ll.head.value == 1)
    assert(ll.tail.value == 2)
    assert(len(ll) == 2)

    # Verifica se a lista contém os elementos adicionados usando toList()
    assert(ll.toList() == [1, 2])

    # Adiciona outro elemento à lista e verifique a cabeça, a cauda e o comprimento
    ll.append(3)
    assert(ll.head.value == 1)
    assert(ll.tail.value == 3)
    assert(len(ll) == 3)

    # Verifica se a lista contém os elementos adicionados usando toList()
    assert(ll.toList() == [1, 2, 3])

    # Insira um elemento no início da lista e verifique a cabeça, a cauda e o comprimento
    ll.insert(0)
    assert(ll.head.value == 0)
    assert(ll.tail.value == 3)
    assert(len(ll) == 4)

    # Verifica se a lista contém os elementos após a inserção no início
    assert(ll.toList() == [0, 1, 2, 3])

    ll.insert(-1)

    # Verifique se a lista contém o elemento inserido no início
    assert(ll.toList() == [-1, 0, 1, 2, 3])

    # Remova o primeiro elemento da lista e verifique o valor retornado
    v = ll.removeFirst()
    assert(v == -1)

    # Verifica se a lista está correta após a remoção do primeiro elemento
    assert(ll.toList() == [0, 1, 2, 3])

    # Continua removendo elementos e verificando o valor retornado
    v = ll.removeFirst()
    assert(v == 0)
    assert(ll.toList() == [1, 2, 3])

    v = ll.removeFirst()
    assert(v == 1)
    assert(ll.toList() == [2, 3])

    v = ll.removeFirst()
    assert(v == 2)
    assert(ll.toList() == [3])

    v = ll.removeFirst()
    assert(v == 3)
    assert(ll.toList() == [])

    # Verifica se o comprimento da lista está correto após todas as remoções
    assert(len(ll) == 0)

    return "Casos de Testes: 1, passaram com sucesso!"

def aditional_test():
    ll = LinkedList()

    # Adicionando alguns elementos à lista
    ll.append(10)
    ll.append(20)
    ll.append(30)

    assert len(ll) == 3
    assert ll.head.value == 10
    assert ll.tail.value == 30
    assert ll.toList() == [10, 20, 30]

    try:
        value = ll.getValueAt(5)
        assert False, "Falha ao verificar o acesso a um elemento fora dos limites."
    except IndexError as e:
        assert str(e) == "Index out of range"

    removed_value = ll.removeFirst()
    assert removed_value == 10
    assert ll.toList() == [20, 30]
    
    return "Casos de Testes: 2, passaram com sucesso!"