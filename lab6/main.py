# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from math import factorial

def en_function(n, x):
    return sum(map(lambda i: (n ** i) / factorial(i), range(1, x + 1))) + 1
result =0

def recursive_function(n):
    global result

    if n == 1:
        result += 1
        return

    result +=  (-1) ** (n + 1) / n
    recursive_function(n - 1)

print(result)
recursive_function(2)
print(result)