def even_numbers(a, b):
    for number in range(a+1,b+1):
        if number % 2 == 0:
            print(number)

# Example usage:
even_numbers(1, 10)
