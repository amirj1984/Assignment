# this code calculates the body mass index by asking mass and height of the reader. But firstly, reader should indicate the preferred unit type.

unit_type = input("would you like to use metric units to calculate your body mass index?(Yes/No) ")
unit_type_correction = unit_type.title()
if unit_type_correction == "Yes":
    height = input("enter your height in m: ")
    height_float = float(height)
    mass = input("enter your mass in kg: ")
    mass_float = float(mass)
    bmi = mass_float/height_float ** 2

    if bmi < 18.5:
        print("you are underweight")
    elif bmi < 25:
        print("you are normal")
    elif bmi < 30:
        print("you are overweight")
    else:
        print("you are obese")

if unit_type_correction == "No":
    height = input("enter your height in inches: ")
    height_float = float(height)
    mass = input("enter your mass in pounds: ")
    mass_float = float(mass)
    bmi = (mass_float / height_float ** 2) * 703

    if bmi < 18.5:
        print("you are underweight")
    elif bmi < 25:
        print("you are normal")
    elif bmi < 30:
        print("you are overweight")
    else:
        print("you are obese")

