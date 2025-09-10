def is_prime(num):
    if num==1:
        return False
    for i in range(2,num//2+1):
        if (num%i)==0:
            return False
    return True

def print_prime (n1,n2):
    for i in range(n1,n2+1):
        if is_prime(i):
            print(i)

if __name__=="__main__":
    n1,n2 = input("Enter the range of numbers seperated by space :").split()
    print_prime(int(n1),int(n2))