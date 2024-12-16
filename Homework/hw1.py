#Part 1:
number1 = int(input("Please input the first number: "))
number2 = int(input("Please input the second number: "))

print("Addition:", number1 + number2)
print("ASubstraction:", number1 - number2)
print("Multiplication:", number1 * number2)
print("Division:", number1 / number2)

#Part 2:
temp = int(input("Please enter a temperature in Celsius: "))
print("Temperature in Fahrenheit:", temp * 9/5 +32)

#Part 3:
user_input = input("Enter a number: ")

integer_vers = int(user_input)
float_vers = float(user_input)
string_vers = str(user_input)

print(f"Integer: {integer_vers} {type(integer_vers)}")
print(f"Float: {float_vers} {type(float_vers)}")
print(f"String: '{string_vers}' {type(string_vers)}")