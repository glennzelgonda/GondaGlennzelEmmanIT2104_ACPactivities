from capybara import Capybara

capybaras = [
    Capybara ("Biscoff", "M", 5),
    Capybara ("Ashta", "M", 4),
    Capybara ("Cali", "F", 3),
    Capybara ("Wuna", "M", 5)
]

test_case_number = int(input("Enter the test case number: ")) -1

if 0 <= test_case_number < len(capybaras):
    selected_capybara = capybaras[test_case_number]
    print(f"Test Case {test_case_number +1}: Name: {selected_capybara.name}, Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")
else:
    print("Invalid test case number. Please enter a number between 1-4")
