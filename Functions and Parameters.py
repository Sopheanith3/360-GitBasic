import math

def test(s,a, b):
    a = a + 1
    c = b + a * 2
    print(s, a, b, c)

def main():
    num1 = 5
    num2 = 7 
    num3 = 3
    str1 = 'ate'

    test('apple', 2, 6)

    test('banana', num3, num1)

    test('cherry', num1, num3)
    
    test('d' + str1, num2 - num3, num3)
    
    test('elderberry', math.sqrt(16), num3)
    
    test('fig', math.sqrt(16) + 1, num3 - 1)

    print(str1, num1, num2, num3)

main()


