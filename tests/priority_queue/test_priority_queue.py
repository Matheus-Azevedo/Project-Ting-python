from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    q = PriorityQueue()

    assert len(q) == 0

    q.enqueue({"nome": "arquivo1.txt", "qtd_linhas": 3})
    assert len(q) == 1

    q.enqueue({"nome": "arquivo2.txt", "qtd_linhas": 5})
    assert len(q) == 2

    q.enqueue({"nome": "arquivo3.txt", "qtd_linhas": 2})
    assert len(q) == 3

    q.enqueue({"nome": "arquivo4.txt", "qtd_linhas": 4})
    assert len(q) == 4

    q.enqueue({"nome": "arquivo5.txt", "qtd_linhas": 1})
    assert len(q) == 5

    assert q.dequeue() == {"nome": "arquivo3.txt", "qtd_linhas": 2}
    assert q.dequeue() == {"nome": "arquivo5.txt", "qtd_linhas": 1}
    assert q.dequeue() == {"nome": "arquivo1.txt", "qtd_linhas": 3}

    assert q.dequeue() == {"nome": "arquivo2.txt", "qtd_linhas": 5}
    assert q.dequeue() == {"nome": "arquivo4.txt", "qtd_linhas": 4}

    try:
        q.dequeue()
    except IndexError:
        pass
    else:
        raise AssertionError("Expected IndexError")

    assert q.search(0) == {"nome": "arquivo2.txt", "qtd_linhas": 5}
    assert q.search(1) == {"nome": "arquivo4.txt", "qtd_linhas": 4}
    assert q.search(2) == {"nome": "arquivo1.txt", "qtd_linhas": 3}
