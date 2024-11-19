numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for number in numbers:
    squares.append(number * number)
print("Antes de la refactorización:", squares)


squares_refactored = [number * number for number in numbers]
print("Después de la refactorización:", squares_refactored)