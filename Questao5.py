#Implemente uma função que inverta a ordem dos elementos de um vetor usando uma pilha.

def inverteVertor(v):
    s = Stack()

    for i in range(len(v)):
        s.push(v[i])
    for j in range(len(v)):
        v[j] = s.pop()