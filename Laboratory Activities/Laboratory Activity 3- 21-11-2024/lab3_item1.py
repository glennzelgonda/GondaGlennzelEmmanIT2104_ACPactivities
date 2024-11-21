def roman_to_integer(roman_numeral):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_numeral = roman_numeral.upper()

    total= 0
    prev_value= 0

    for char in reversed(roman_numeral):
        if char not in roman_values:
            raise ValueError(f"Invalid Roman Numeral Character.")
        
        current_value = roman_values[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total

if __name__ == "__main__":
    user_input = input("Enter a Roman numeral: ")

    upper_input = user_input.upper()

    try:
        result = roman_to_integer(user_input)
        print(f"The integer value of the Roman numeral {upper_input} is: {result}")
    except ValueError as e:
        print(e)