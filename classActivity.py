def is_narc(n): #colon is missing from function declaration
    """Check if a number is narc."""
    num_str = str(n) # = should be used for assignment, == is used for checking equality
    num_digits = len(num_str) # = should be used for assignment, == is used for checking equality
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str) # ** is used for taking power not ***
    
    return sum_of_powers == n

def print_narcis_numbers(start, end): # comma missing between parameters and colon is missing from function declaration
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): # colon is missing from loop
        if is_narc(num): #colon is missing from if statement and is_narc is the name of function defined previously
            print(num)

print_narcis_numbers(1000, 5000) # function name should be print_narcis_numbers instead of print_narc_numbers
