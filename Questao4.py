#Elabore uma função recursiva que remova todos os elementos de uma pilha.

def removeDaPilha(s):
    if s is None:
        return 0
    
    return removeDaPilha(s.pop())

