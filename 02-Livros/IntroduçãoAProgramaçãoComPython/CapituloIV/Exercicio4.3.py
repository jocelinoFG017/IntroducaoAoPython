"""
Escreva um programa que leia três números e que imprima o maior e o menor
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())


if (n1>n2) and (n1>n3): # n1 > n2 and n3
    if (n2>n3): #n1>n2>n3
        print("maior:",n1)
        print("menor:",n3)
    if (n3>n2): # n1>n3>n2
        print("maior:", n1)
        print("menor:", n2)
if (n2>n1) and (n2 > n3):# n2> n1 and n3
    if (n1>n3): #n2>n1>n3
        print("maior:",n2)
        print("menor:",n3)
    if (n3>n1): # n2>n3>n1
        print("maior:", n2)
        print("menor:", n1)
if (n3>n1) and (n3 > n2): # n3 > n1 and n2
    if (n1>n2): #n3>n1>n2
        print("maior:",n3)
        print("menor:",n2)
    if (n2>n1): # n3>n2>n1
        print("maior:", n3)
        print("menor:", n1)