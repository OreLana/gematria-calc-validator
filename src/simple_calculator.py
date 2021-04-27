
from formula_error import FormulaError

def user_input():
    operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}
    user_operation = ''
    while user_operation != 'quit':
        user_operation = input('>>>')
        if user_operation == 'quit':
            break  
        else:
            try:
                #This line checks and ensures there's space between the operands and the operator
                if not check_elements(user_operation.split()):
                    raise FormulaError(user_operation, 'There must be space between the operands and the operator')

                operator = user_operation.split()[1]
                
                #This checks that the operation entered by the user is within the scope of addition, division, subtraction and multiplication
                if not check_operators: 
                    raise FormulaError(user_operation, 'you can only perform these operations +,-,/,*')

                numbers = (user_operation.split())

                #This line checks that the operands are numbers and not letters
                if numbers[0].isalpha() or numbers[2].isalpha():
                    raise FormulaError(user_operation, 'You can only perform operation on numbers and not letters')

                first_number =float(numbers[0])
                second_number = float(numbers[2])
            
                #This line checks and ensures the user doesn't enter more or less than 3  elements
                if not check_elements(numbers):
                    raise FormulaError(user_operation, 'The number of elements cannot be less than or more than 3')
                print(operations[operator](first_number,second_number))
            except FormulaError as error:
                print(error)
            


def add(a,b):
    return a + b

#This function returns the subtraction of the two numbers passed by the user
def subtract(a,b):
    return a - b

#This function returns the product of the two numbers passed by the user
def multiply(a,b):
    return a * b

#This function returns the division of the two numbers passed by the user
def divide(a,b):
    return a / b

def check_elements(value):
    return len(value) == 3
    
def check_operators(value):
    return value in ['+','-','*','/']


(user_input())