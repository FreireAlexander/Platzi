import random

def search(list, target) -> bool:
    print("Searching and sorting")
    for element in list:
        if element == target:
            return True
    return False

def main():
    lista = [1,2,34,5,6]
    first = search(lista, 7)
    print(f"Lista {lista}")
    print(f"Valor de first {first} para 7")
    if first:
        print("true")
    else: 
        print("false")

    second = search(lista, 34)
    print(f"Valor de second {second} para 34")
    if second:
        print("true x2")
    else: 
        print("false x2")


if __name__ == "__main__":
    main()
