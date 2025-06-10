def convert_temperature():
    print("Temperature Converter")
    value = input("Enter temperature (just the number): ")
    unit = input("Is it in Celsius (C) or Fahrenheit (F)? ").upper()

    if unit == "C":
        f = (float(value) * 9 / 5) + 32
        print(value + "°C is " + str(round(f, 2)) + "°F")
    elif unit == "F":
        c = (float(value) - 32) * 5 / 9
        print(value + "°F is " + str(round(c, 2)) + "°C")
    else:
        print("Please enter either C or F as the unit.")

convert_temperature()
