#accept a number from the user and check if it is a perfect square:
import math
input_number = int(input("Enter a number: "))
root = math.sqrt(input_number)
root_int = math.floor(root)
if root_int * root_int == input_number:
    print(f"{input_number} is a perfect square.")
else:
    print(f"{input_number} is not a perfect square.")
