"""Day 10 - Taking User Input in python
In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable

Syntax:
variable=input()
But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

Example:
variable=int(input())
variable=float(input())
We can also display a text using input function. This will make input() function take user input and display a message as well

Example:
a=input("Enter the name: ")
print(a)
Output:
Enter the name: Harry
Harry"""


a=input("Enter the name: ")
print("my name is ",a)



a=input("Enter the value of a: ")
b=input("Enter the value of b: ")
print("The value of a is ",a,"and b is ",b)
print(int(a)+int(b))
      
