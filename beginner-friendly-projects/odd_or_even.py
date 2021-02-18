print("Welcome User")
num = int(input("What number are you thinking of? "))
def even_or_odd_function():
    if(num % 2 == 0):
        return "That's an even number"
    return "That's an odd number"
        
print(even_or_odd_function())