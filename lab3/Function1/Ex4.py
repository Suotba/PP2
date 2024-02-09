def is_prime():
    a = input("List of numbers: ")
    num_list = list(map(int, a.split()))
    
    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    prime_numbers = [num for num in num_list if check_prime(num)]
    print("Prime numbers:", prime_numbers)

is_prime()
