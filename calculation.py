def LCM(num1, num2):
    '''Наименьшее общее кратное'''
    if num1 < num2: num1, num2 = num2, num1
    return num1 * num2 // GCD(num1, num2)

def GCD(num1, num2):
    '''Наибольший общий делитель'''
    if num1 < num2: num1, num2 = num2, num1
    while not num1 <= 0 or num2 <= 0:
        if num1 > num2: num1 %= num2
        else: num2 %= num1
    return num1 + num2

def fact(num):
    '''Факториал'''
    res = 1
    if num > 0:
        for i in range(1, num+1): res *= i
    elif num < 0:
        for i in range(num, 0): res *= i
    else: return 0
    return res

def isPrime(num):
    '''Простое ли'''
    res = True
    if num <= 0: return False
    for i in range(2, num):
        if num % i == 0: pass
        else:
            res = False
            break
    return res

def reduce(num1, num2):
    '''Сокращение дроби'''
    gcd = GCD(num1, num2)
    return num1 / gcd, num2 / gcd

def isPerfect(num):
    '''Совершенное ли'''
    res = 0
    for i in range(1, num):
        if num % i == 0: res += i
    if res == num: return True
    else: return False
    
        
