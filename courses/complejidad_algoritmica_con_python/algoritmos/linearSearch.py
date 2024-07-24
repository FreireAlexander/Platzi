'''
    Busqueda lineal:
        - No tiene necesidad de ordenar la lista
        - Busqueda uno a uno en la lista
'''
import random

def search(list, target) -> bool:
    print(f"Searching target: {target} ->")
    for element in list:
        if element == target:
            print(f"Target found at {list.index(element)}\n", end="")
            return True
    print("Target not found \n", end="")
    return False

def main():
    size = int(input("Input size: "))
    lista = [random.randint(0,100) for i in range(size)]
    print(f"list -> \n {lista} \n")
    target = int(input("Enter target: "))
    if search(lista, target):
        print(f"{target} is in the list")
    else:
        print("Not found 404")


if __name__ == "__main__":
    main()
