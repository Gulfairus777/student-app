# Математикалық функциялар
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def average(numbers):
    return sum(numbers) / len(numbers)

def odd_even_difference(numbers):
    odds = [x for x in numbers if x % 2 != 0]   # тақ сандар
    evens = [x for x in numbers if x % 2 == 0]  # жұп сандар
    return sum(odds) - sum(evens)

if __name__ == "__main__":
  
    print( add(10, 3))
    print( subtract(10, 3))
    print( multiply(7, 2))

    # Массив
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print( numbers)
    print( average(numbers))

    odds = [x for x in numbers if x % 2 != 0]
    evens = [x for x in numbers if x % 2 == 0]
    print( odds)
    print( evens)
    print( sum(odds))
    print( sum(evens))
    print( odd_even_difference(numbers))