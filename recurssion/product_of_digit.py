def sum_of_digits(n: int)-> int:
    if n==0:
        return 1
    else:
        return n%10* sum_of_digits(n//10)
print(sum_of_digits(505))