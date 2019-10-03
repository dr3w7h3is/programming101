from sys import argv

print("Hens", 25 + 30 / 5)
print(10*(10-25))
print(10%9)
print(5%5)
print(100%5)
print(3 + 2 < 5 -7)
print(3 + 2 <= 5 - 7)
print(3 + 2 != 5)


a = True
print(a)

hi = "Hello world"
sum = 5 + 10
print(str(sum) + str(sum))
print(sum)
print("The sum is", sum, " big")

my_name = "Drew"
my_age = 29
my_height = 72
my_weight = 240
my_eyes = "blue"
my_teeth = "white"
my_hair = "blonde"

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inces tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actucall that's not too heavy.")
print(f"He's got {my_eyes} eyes and my {my_hair} hair.")
print(f"jajaja")

print("WORD-1\nWord-2\n" * 10)

print("How old are you?", end=' ')
age = input()
print("How tall are you", end =' ')
height = input()
print("What color are your eyes", end = ' ')
eyes = input()

print(age + " " + height + " " + eyes)
print(f"So you are {age} years old, {height} tall, and your eye color is {eyes}")

new = input("Enter new name: ")
print(f"Your new name is: {new}")

script, first, second, third = argv

print("The script is called:", script)
print("This is the first:", first)
print("Second:", second)
print("Third:", third)
