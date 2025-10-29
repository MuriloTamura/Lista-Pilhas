"""
Considere duas pilhas de inteiros não negativos P1 e P2 ocupando um único array A com N posições, 
de modo que: Números empilhados em P1 ocupam posições crescentes a partir de A[0]
Números empilhados em P2 ocupam posições decrescentes de A partir de A[N-1] t1 contém o índice em A do número 
empilhado por último em P1 t2 contém o índice em A do número empilhado por último em P2 As pilhas podem crescer 
enquanto houver posições livres Implemente as funções de acesso às pilhas: push, pop, peek, len, isEmpty, isFull, empty
"""
def inicializa_pilhas(A):
    """Inicializa as duas pilhas no mesmo array."""
    global t1, t2
    t1 = -1               # topo da pilha 1
    t2 = len(A)           # topo da pilha 2 (uma posição além do fim)


def isEmpty1():
    """Verifica se a pilha 1 está vazia."""
    return t1 == -1


def isEmpty2():
    """Verifica se a pilha 2 está vazia."""
    return t2 == len(A)


def isFull():
    """Retorna True se o array estiver cheio."""
    return t1 + 1 == t2


def push1(A, x):
    """Empilha um valor na pilha 1."""
    global t1, t2
    if isFull():
        print("Erro: pilhas cheias!")
        return
    t1 += 1
    A[t1] = x


def push2(A, x):
    """Empilha um valor na pilha 2."""
    global t1, t2
    if isFull():
        print("Erro: pilhas cheias!")
        return
    t2 -= 1
    A[t2] = x


def pop1(A):
    """Desempilha da pilha 1."""
    global t1
    if isEmpty1():
        print("Erro: pilha 1 vazia!")
        return None
    x = A[t1]
    A[t1] = None
    t1 -= 1
    return x


def pop2(A):
    """Desempilha da pilha 2."""
    global t2
    if isEmpty2():
        print("Erro: pilha 2 vazia!")
        return None
    x = A[t2]
    A[t2] = None
    t2 += 1
    return x


def peek1(A):
    """Consulta o topo da pilha 1 sem remover."""
    if isEmpty1():
        print("Pilha 1 vazia!")
        return None
    return A[t1]


def peek2(A):
    """Consulta o topo da pilha 2 sem remover."""
    if isEmpty2():
        print("Pilha 2 vazia!")
        return None
    return A[t2]


def len1():
    """Retorna o tamanho da pilha 1."""
    return t1 + 1


def len2():
    """Retorna o tamanho da pilha 2."""
    return len(A) - t2


def empty1(A):
    """Esvazia a pilha 1."""
    global t1
    while not isEmpty1():
        pop1(A)


def empty2(A):
    """Esvazia a pilha 2."""
    global t2
    while not isEmpty2():
        pop2(A)
