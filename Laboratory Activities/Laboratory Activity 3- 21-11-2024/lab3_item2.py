def is_perfect_number(number):
    if number <= 0:
        return False
    
    sum_of_divisors= 0
    for i in range (1, number // 2 + 1):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == number

if __name__ == "__main__":
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
        if number <= 0:
            raise ValueError("Please enter a valid integer.")
        
        if is_perfect_number(number):
            print(f"{number} is a perfect number")
        else:
            print(f"{number} is not a perfect number.")

    except ValueError:
         print ("Please enter a valid integer.")
