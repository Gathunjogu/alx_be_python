# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_valid_temperature():
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            return temp
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def get_valid_unit():
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if unit in ['C', 'F']:
            return unit
        print("Invalid unit. Please enter C or F.")

def main():
    temp = get_valid_temperature()
    unit = get_valid_unit()

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {converted_temp:.2f}°F")
    else:
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is equal to {converted_temp:.2f}°C")

if __name__ == "__main__":
    main()
