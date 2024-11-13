name = input("Enter your name: ")
print("Hello, " + name + "!")

age_input = input("How old are you? ")
if age_input.isdigit():
    age = int(age_input)
    if age > 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
else:
    print("Invalid input. Please enter a number.")
