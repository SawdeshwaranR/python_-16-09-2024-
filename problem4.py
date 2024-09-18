# print the math table of a number for upto mutiples of 20:

input_number = int(input("Enter a number for upto multiples of 20 "))

print(f"Multiplication table for {input_number}:")
for i in range(1, 21):
    #print(f"{input_number} x {i} = {input_number * i}")
    print('%d*%-2d=%-53d'%(input_number,i,input_number*i))
    


