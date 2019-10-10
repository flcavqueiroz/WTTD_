def happy(number):
    next_ = sum(int(char) ** 2 for char in str(number))
    return number in (1, 7) if number < 10 else happy(next_)

    '''box = []
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum_of_squares(n)

    return n == 1'''

    '''if number == 130:
        n = number
        n = sum_of_squares(n)
        n = sum_of_squares(n)
        return n == 1
        number = sum_of_squares(number)
        digits = [int(char) for char in string]
        total = sum(digits)
        number = total'''
       

    '''if number in(1, 10, 100):
        string = str(number)
        digits = [int(char) for char in string]
        total = sum(digits)'''
        

    
     
   

    

assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))

print('Todos os testes passaram')