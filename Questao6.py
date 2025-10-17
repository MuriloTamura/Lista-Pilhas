# Seja P uma pilha de inteiros não negativos ocupando um array A com N posições, de modo que:
#   a) Números empilhados em P ocupam posições crescentes de A a partir de A[1]
#   b) A[0] contém o índice em A do número empilhado por último (topo da pilha)
#   c) A pilha pode crescer enquanto houver posições em A.
# Implemente as funções de acesso às pilhas: push, pop, peek, len, isEmpty, isFull, empty( esvazia a pilha).


def push(a, i):
    if isFull(a):
        return 0
    a[0] += 1
    a[a[0]] = i

def pop(a):
    if isEmpty(a):
        return 0
    i = a[a[0]]
    a[0] = None
    a[0] -= 1
    return i

def peek(A):
    if isEmpty(A):
        return 0
    return A[A[0]]

def len(A):
    return A[0]

def isEmpty(A):
    return A[0] == 0

def isFull(A):
    return A[0] == len(A) - 1

def empty(A):
    while not isEmpty(A):
        pop(A)