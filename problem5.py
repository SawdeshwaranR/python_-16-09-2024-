#Read the from the user and print the lucky digit of the user where the lucky digit is found y finding the sum of digits of the given number and repeaar he algorithm until single digit number is arrived.
"""def find_lucky_digit(number):

    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))
    while number >9:
        number = sum_of_digits(number)
    
    return number
user_input = int(input("Enter a number: "))

lucky_digit = find_lucky_digit(user_input)
print(f"the lucky digit is : {lucky_digit}")"""


 #print second lagrest number in digit 


def second_largest_digit(number):
    digits = set(str(number))
    sorted_digits = sorted([int(digit) for digit in digits], reverse=True)
    if len(sorted_digits) < 2:
        return "Not enough unique digits to determine a second largest digit."
    else:
        return sorted_digits[1]
user_input = int(input("Enter a number: "))
second_largest = second_largest_digit(user_input)
print(f"The second largest digit is: {second_largest}")


