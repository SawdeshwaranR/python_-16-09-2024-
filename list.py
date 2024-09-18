"""biggerZoo = ['bear', 'lion', 'panda', 'zebra', ['chimpanzees', 'gorillas', 'orangutans', 'gibbons']]
print(biggerZoo)

print(biggerZoo[1])

print(biggerZoo[3])

print(biggerZoo[4])

print(biggerZoo[4][0])

print(biggerZoo[4][0][1])
print(biggerZoo.count('lion'))"""
"""import sys 
numbers=[]
for i in range(1,len(sys.argv)):
    numbers.append(int(sys.argv[i]))
    print(numbers)

    even_numbers=[element for element in numbers if element %2==0]
    print(even_numbers)


    import sys 
    string =sys.argv
    print(string)"""
    
    #num1=0o27
    #rint('%d %o %x %x'%(num1,num1,num1,num1)
    # )
    """
    list=["hello","helo","heelo","hi"]
list2=["hello123","hello233","hello456","12344re"]
list3=["sawdesh","waran","123sawdesh"]
list.extend(list2)
print(list)
list.append(list3)
print(list.append(list3))

list.extend(list3)
print(list.extend(list3))"""


my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5]) # print the elements from index 2 to index 4

# elements beginning to 2nd
print(my_list[:-7]) # leave the last 7 elements of the list

# elements 6th to end
print(my_list[5:]) # print all the elements starting from index 5

# elements beginning to end
print(my_list[:]) # Print all elements of the list
print(my_list[::2])