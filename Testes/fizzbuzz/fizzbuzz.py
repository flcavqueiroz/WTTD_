'''
Regras FizzBuzz
1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio número.
'''
from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)

'''def multiple_of(base, num):
    #return num % base == 0


def multiple_of_5(num):
    return multiple_of(5, num)


def multiple_of_3(num):
    return multiple_of(3, num) 
'''

def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_5 (pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'
    
    return say


''' 
def assert_true(result, expected):
    from sys import _getframe
    msg = 'Fail: Line {} got {} expecting {}'
   
    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        print(msg.format(line_no, result, expected))

if __name__ =='__main__':
    assert_true(robot(1), '1'), 'Falha no teste'
    assert_true(robot(2), '2'), 'Falha no teste'
    assert_true(robot(4), '4'), 'Falha no teste'

    assert_true(robot(3), 'fizz'), 'Retorno não é fizz'
    try:
        assert robot(3) == 'fizz', 'Retono não é fizz'
    except AssertionError:
        print('Falha na linha 43')
    assert_true(robot(6), 'fizz'), 'Retono não é fizz'
    assert_true(robot(9), 'fizz'), 'Retorno não é fizz'

    assert_true(robot(5), 'buzz'), 'Retorno não é buzz'
    assert_true(robot(10),'buzz'), 'Retorno não é buzz'
    assert_true(robot(20), 'buzz'), 'Retorno não é buzz'

    assert_true(robot(15), 'fizzbuzz'), 'Retorno não é fizzbuzz'
'''
'''armando = 
boris = 
clovis =''' 
