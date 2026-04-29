# My First Python

print("Hello world")

num1, num2, num3 = 1, 2, 3
print(num1, num2, num3)
#learning how to write strings by using message as the output
message = ("Get me a bottle of water")
print(message)

message = 34
print(message)
# integers number
count = 0
print(count)
#count = count + 2
count += 2
print(count)

print(type(count))
#writing strings
person_name = 'Alice'

alice_food = ("The food belongs to Alice."
              "It's Alice food."
              "please let no one touch that food")
print(alice_food)
# How to write poem
poem = """
violet are blue
love is dangerous
programming is awesome
programmers are boring
coding drives the lazy away
"""
print(poem)
#Learning the boolen
age= 35
is_adult = age >= 18
print(is_adult)

#Truthly and Falsy Value
print(bool(0))
#writing 2 differnt syntax in 1 data
print(int(45.56))
print(float(45))

try:
    num = int("Alim")
    Print(num)
except ValueError:
    print("invalid number conversion")


    print("Hello", "Saidu", "and", "Foday",sep="-")




#  Python Input Function
name=input("What is your name please?")
print("Hello my dear",name)

#Python Input Function
name = input("What is your name please?")
print(f"Hello my dear:{name}!")

age = int(input("How old are you?"))
print(f"your age is:{age}!")
 except  ValueError:
print("please enter a valid number for age!")