#build in methid 
#exception handling error in python:
#catch block in occur in program  for try adn catch:
#error index in pogram to show the user how the error are 
import sys


def split_states_capitals():
    states=[]
    captials=list()
    for i in range(1,len(sys.argv)):
        argument=sys.argv[i]
        index_of_space= argument.find(' ')
        states.append(argument[:index_of_space])
        capitals.append(argument[index_of_space+1:])
    print('%-15s %s'%('STATES','CAPITALS'))
    print('-'*27)
    i=0
    while states:
        
