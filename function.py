def area_circle(r):
    pi = 3.14
    return  pi*r**2


radius = int(input("Enter the value of r"))
print(area_circle(radius))
 



def sum(a,b):
    return a + b

# print(sum(5,6))
print(sum(int(input("enter the value of a")), int(input("enter the value of b"))))



def factorial(n):
    if n < 0 :
        raise("valuee error")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
     
print(factorial(int(input("Enter the value of n"))))  






def reversed_string(a):

    return a[::-1]


a = input("Enter any word :")
print(reversed_string(a))    




def is_prime(n):
    if n <= 1:
        return False
    for i in range(2 , n):
        if n % i == 0:
            return False
        else:
            return True

n = int(input("Enter any value :"))
print(is_prime(n))


 


def is_vowel(a):

    if a in 'a,e,i,o,u,A,E,i,o,u':
        return True
    else:
        return False
    
a = input("Enter the value :")
print(is_vowel(a))





def larg(a):
    return max(a)

a = list(map(int, input("Enter values: ").split()))

print(larg(a))




def fab_recu(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fab_recu(n-1) + fab_recu(n-2)

n = int(input("Enter the number :"))
print(f"The {n}th fabonni number is {fab_recu(n)}")




def is_plandrom(word):

    if word == word[::-1]:
        return True
    else:
        return False
word = input("Enter the word")
print(is_plandrom(word))




def su(num):
    return sum(num)

a = list(map(int , input("Enter the values :").split()))
print(su(a))


def divisor(a,b):
    while b != 0:
        a , b = b, a%b
    return abs(a)

num1 = int(input("Enter The first number : "))
num2 = int(input("Enter The second number : "))
print(f"The GCD of {num1} and {num2} is {divisor(num1,num2)}")





def d_k(data):
    return max(data)

ex = {"a" : 12 , "b"  : 14, "c" : 17}
print(d_k(ex))



def sqr(a):
    return a * a

a = int(input("Enter the value to find square of thr number"))
print(sqr(a))



def anagrams(str1,str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

str1 = input("Enter first word :")
str2 = input("Enter second word :")
print(anagrams(str1,str2))


def remove(a):
    return (set(a))

a = list(map(int,input("Enter the values :").split()))
print(remove(a))


def avg(a):
    return sum(a) / len(a)

a = list(map(int,input("Enter the values :").split()))
print (avg(a))

import random
def pswd(a):

    

    lower = "abcdefgijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    char = "!@#$%^&*()"

    string = lower + upper + number + char
    

    password =random.sample(string,a)


    n = "".join(password)
    return (n)
print(pswd(12))