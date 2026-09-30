from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose an option (1 or 2): ")

temperature = float(input("Enter temperature: "))

if choice == "1":
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C = {result:.2f}°F")

elif choice == "2":
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F = {result:.2f}°C")

else:
    print("Invalid choice.")