from house import House


def test_init():
    pass

def test_repr():
    pass

def test_item():
    pass

def test_score():
    c = House()
    c.put(1, 1, 1)
    c.put(1, 2, 2)
    c.put(1, 3, 3)
    c.put(1, 5, 5)
    #заполнить три башни + две заполнить не до конца, посчитать сколько очков даст и проверить.
def test_score_1():
    c = House()
    assert c.score_1() == 0
    c.put(1, 1, 1)
    assert c.score_1() == 0
    c.put(1, 2, 2)
    c.put(1, 3, 3)
    c.put(1, 5, 5)
    assert c.score_1() == 6
    a = House()
    assert a.score_1() == 0
    a.put(1, 1, 2)
    assert a.score_1() == 0
    a.put(1, 2, 2)
    a.put(1, 3, 2)
    a.put(1, 5, 2)
    assert a.score_1() == 4
    assert type(a.score_1()) == int

def test_score_2():
    c = House()
    c.put()

def test_score_3():
    pass

def test_score_4():
    c = House()
    c.put(3, 5, 4)
    assert c.score_4() == 0
    c.put(4, 5, 1)
    assert c.score_4() == 1
    print(c)

def test_score_5():
    c = House()
    c.put(1, 1, 5)
    assert c.score_5() == 1
    c.put(2, 2, 5)
    assert c.score_5() == 3
    c.put(5, 3, 5)
    assert c.score_5() == 6
    c.put(3, 4, 5)
    assert c.score_5() == 10
    c.put(4, 5, 5)
    assert c.score_5() == 15
    c.put(3, 6, 5)
    assert c.score_5() == 21
    c.put(1, 2, 5)
    assert c.score_5() == 23
    c.put(1, 3, 5)
    assert c.score_5() == 26
    c.put(1, 5, 5)
    assert c.score_5() == 31
    c.put(2, 1, 5)
    assert c.score_5() == 32
    c.put(2, 3, 5)
    assert c.score_5() == 35
    c.put(2, 4, 5)
    assert c.score_5() == 39
    c.put(2, 5, 5)
    assert c.score_5() == 44
    print(c)
def test_score_6():
    pass

def test_put():
    pass

def test_save():
    pass

def test_load():
    pass