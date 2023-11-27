def only_two_positive_numbers(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1

    if b > 0:
        positive_count += 1

    if c > 0:
        positive_count += 1

    result = positive_count == 2
    print(f"Numbers: {a}, {b}, {c} | Condition: {result}")
    return result

print(only_two_positive_numbers(-4, 6, 8)) 
print(only_two_positive_numbers(4, -6, 9))  
print(only_two_positive_numbers(-4, 6, 0))  
print(only_two_positive_numbers(4, 6, 10)) 