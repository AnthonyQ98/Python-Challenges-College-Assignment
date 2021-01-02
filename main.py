"""
Anthony Quinn X00138635
07/12/2020
Week 9 Lab Exercises Question 1
"""

"""
# EXERCISE 1
import math

option = 0

while option != 4: #4 should be exit menu
    print("*****************************************\n"
          "*Calculation of Volume for Solid Objects*\n"
          "*****************************************\n"
          "1. Cube\n2. Cylinder\n3. Sphere\n4. Exit\n" 
          "*****************************************")

    option = int(input("Enter option: "))

    if option == 1: # CUBE
        print("Option 1")
        cube_length = float(input("Enter the length of the cube: "))
        CUBE_VOLUME = cube_length ** 3
        print("Volume of cube is: ", round(CUBE_VOLUME, 2))

    elif option == 2: # CYLINDER
        print("Option 2")
        cylinder_height = float(input("Enter the height of the cylinder: "))
        radius = float(input("Enter the radius of the cylinder: "))
        while radius <= 0:
            print("Enter a valid radius... must be greater than zero!")
            radius = float(input("Enter the radius of the cylinder: "))
        CYLINDER_VOLUME = math.pi * radius ** 2 * cylinder_height
        print("Volume of the cylinder is: ", round(CYLINDER_VOLUME, 2))

    elif option == 3:  # SPHERE
        print("Option 3")
        radius = float(input("Enter the radius of the sphere: "))
        while radius <= 0:
            print("Enter a valid radius... must be greater than zero!")
            radius = float(input("Enter the radius of the cylinder: "))
        SPHERE_VOLUME = (4/3) * math.pi * radius ** 3
        print("Volume of the sphere is: ", round(SPHERE_VOLUME, 2))

    elif option == 4:  # EXIT
        print("Processing of Volumes completed!")

    else:
        print("Option", option, "\nInvalid menu option chosen.... try again!")
"""

"""
# EXERCISE 2
sentence = input("Enter a sentence: ")
url_sentence = ""

for index in range(len(sentence)):

    if sentence[index] != " ":
        url_sentence = url_sentence + sentence[index]
    else:
        url_sentence = url_sentence + "%20"

print(sentence)
print(url_sentence)
"""

"""
# EXERCISE 3 - INCOMPLETE

chars = 0

sentence = input("Enter sentence: ")
sentence = sentence.lower()
character = input("Enter a single character: ")

while len(character) != 1:
    character = input("Invalid. Enter a single character: ")

print(sentence.count(character))
"""






