import time
import math

def calculate_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000)  
    result = math.sqrt(number)
    return result

number = int(input("Your number: "))
delay_ms = int(input("After: "))


result = calculate_square_root(number, delay_ms)


print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
