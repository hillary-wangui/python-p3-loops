#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > -1:
        print(i)
        i -= 1
    print("Happy New Year!")
happy_new_year()


def square_integers(int_list):
    # code goes here!
    squared_list= list()
    for integer in int_list :
        squared_list.append(integer ** 2)
    return(squared_list)
    
print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    # code goes here!
    i = 1
    while i < 101:
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)
        i += 1
    
fizzbuzz()