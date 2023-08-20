#Function for equation result
def equation_result(first_number, second_number, choice_operator):

    match choice_operator:
        case '-':
            return first_number - second_number
        case '+':
            return first_number + second_number
        case '*':
            return first_number * second_number
        case '/':
           return first_number / second_number 


#Number input
print("Welcome To Basic Calculator Program\n")

while True:
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")

    if not first_number.isdigit() and not second_number.isdigit():
        print("\nInvalid input, please try again!\n")
    else:
        first_number, second_number = int(first_number), int(second_number)
        break


#Operator Input
while True:
    choice_operator = input("\nChoose an operator (-, +, *, / ): ")

    if choice_operator != ('-' or '+' or '/' or '*'):
        print("Invalid input, please try again!\n")
    else:
        print("Result: ", equation_result(first_number, second_number, choice_operator))
        break