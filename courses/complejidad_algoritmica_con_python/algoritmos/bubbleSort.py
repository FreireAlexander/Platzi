'''
    Bubble Sort:
        -> Complejidad del algoritmo: O(n**2)
        - al recorrer toda la lista la primera vez nos garantiza que 
            el mayor valor se encuentre al final de la lista
'''
import random

def sort(array, flag=True) -> list:
    size = len(array) - 1
    steps = 0
    for i in range(size):
        print(f"Recorrido [{i}]")
        print(f"Sorting status -> {array}")
        isSorted = True
        
        for j in range(size - i):
            print(f"Recorrido [{i}] step {j}")
            if array[j] > array[j+1]:
                isSorted = False
                print(f"Actual greatest value: {array[j]}")
                print(f"Sorting {array[j], array[j+1]}")
                array[j], array[j+1] = array[j+1], array[j]
                print(f"Sorting for {array[j], array[j+1]}")

        steps+=1
        if isSorted and flag:
            return array, steps

        print("\n")

        

    print(f"Greatest value: {array[size]}")

    return array, steps

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

    print(f"Sorted List \n {sort(lista)}")
    print(f"Sorted List \n {sort(lista, False)}")

if __name__ == "__main__":
    main()
