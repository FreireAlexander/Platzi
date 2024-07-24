'''
    Busqueda Binaria, es una busqueda recursiva
    - Divide y conquista
    - El problema se divide en 2 en cada iteración.

    ** Para optimizar el espacion debemos utilizar mas memoria,
    estos dos conceptos son inversamente proporcionales
'''

import random
import sys
sys.setrecursionlimit(30000)

def search(list, target) -> bool:
    size = (len(list) - 1)
    
    if 0 > size:
        return False
    
    middle = size // 2

    print(f"Searching {target} in range {list[0]} to {list[size]} and middle value of {list[middle]} on position {middle}")
    print(f"List -> \n {list} \n")

    

    if list[middle] == target:
        return True
    elif list[middle] < target:
        return search(list[middle + 1:], target)
    else:
        return search(list[:middle], target)

    return False

def main():
    size = int(input("Input size: "))
    lista = sorted([random.randint(0,100) for i in range(size)])
    print(f"list -> \n {lista} \n")
    target = int(input("Enter target: "))
    if search(lista, target):
        print(f"{target} is in the list")
    else:
        print("Not found 404")


if __name__ == "__main__":
    main()
