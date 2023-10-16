from modules.linkedList import LinkedList

if __name__ == "__main__":
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente.
    """
    ll = LinkedList()
    assert(ll.head is None)
    assert(ll.tail is None)
    assert(ll.toList() == [])
    
    ll.append(1)
    assert(ll.head.value == 1)
    assert(ll.tail.value == 1)
    assert(len(ll) == 1)
    assert(ll.toList() == [1])
    
    ll.append(2)
    assert(ll.head.value == 1)
    assert(ll.tail.value == 2)
    assert(len(ll) == 2)
    assert(ll.toList() == [1, 2])
    
    ll.append(3)
    assert(ll.head.value == 1)
    assert(ll.tail.value == 3)
    assert(len(ll) == 3)
    assert(ll.toList() == [1, 2, 3])
    
    ll.insert(0)
    assert(ll.head.value == 0)
    assert(ll.tail.value == 3)
    assert(len(ll) == 4)
    assert(ll.toList() == [0, 1, 2, 3])
    
    ll.insert(-1)
    assert(ll.toList() == [-1, 0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == -1)
    assert(ll.toList() == [0, 1, 2, 3])
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
    assert(len(ll) == 0)

    print("100%")