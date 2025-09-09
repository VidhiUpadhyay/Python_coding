def sum_of_n_natural_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
    return total

if __name__=="__main__":
    n = int(input("Enter a number n to find sum of n natural numbers:"))
    print(sum_of_n_natural_numbers(n))
