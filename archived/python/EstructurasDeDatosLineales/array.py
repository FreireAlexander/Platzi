#!/usr/bin/python

class Array:
    """
    Array Classs
    """
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index: int):
        return self.items[index]

    def __setitem__(self, index: int, new_item):
        self.items[index] = new_item


def main():
    """
        Colecciones: Grupo de cero o más valores
    """
    fruits = [
            "Apple", "Pineapple", "Banana",
            "Watermelon", "Kiwi", "Strawberry"  
              ]
    
    print(fruits)

if __name__ == "__main__":
    main() # type: ignore