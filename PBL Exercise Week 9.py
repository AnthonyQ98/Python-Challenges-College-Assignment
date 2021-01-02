"""
Anthony Quinn X00138635
07/12/2020
Week 9 PBL Lab Exercises
"""

start = input("Enter y to start and any other key to exit: ")

while start == "y":

    genderChild = int(input("Enter child gender (0 for male, 1 for female): "))


    while genderChild < 0 or genderChild > 1:

        genderChild = int(input("Invalid entry. Re-enter gender. 1 for female, 0 for male: "))


    if genderChild == 1:
        motherFeet = int(input("Mother Height Feet: "))
        motherInches = float(input("Mother Height Inches:"))
        fatherFeet = int(input("Father Height Feet: "))
        fatherInches = float(input("Father Height Inches:"))
        TOTAL_MHEIGHT = ((motherFeet * 12)+ motherInches)
        TOTAL_FHEIGHT = ((fatherFeet * 12)+ fatherInches)
        female_child = ((TOTAL_FHEIGHT * 12/13) + TOTAL_MHEIGHT)/2
        print("Your childs future height is estimated to be ", round(female_child // 12, 2), "feet and ", round(female_child%12, 2), "inches.")



    if genderChild == 0:
        motherFeet = int(input("Mother Height Feet: "))
        motherInches = float(input("Mother Height Inches:"))
        fatherFeet = int(input("Father Height Feet: "))
        fatherInches = float(input("Father Height Inches:"))
        TOTAL_MHEIGHT = ((motherFeet * 12)+ motherInches)
        TOTAL_FHEIGHT = ((fatherFeet * 12)+ fatherInches)
        male_child = ((TOTAL_MHEIGHT * 13/12) + TOTAL_FHEIGHT)/2
        print("Your childs future height is estimated to be ", round(male_child // 12, 2), "feet and ", round(male_child%12, 2), "inches.")
    start = input("Press y to run again. Press anything else to exit the program: ")

