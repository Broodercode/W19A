import addition
import division
import multiplication
import subtraction

print('Which operation would you like to do?')
print('1: Addition')
print('2: Subtraction')
print('3: Multiplication')
print('4: Division')

raw_x = input()
x = int(raw_x)

def calc(num):
    if(num < 1 or num > 4):
        print('invalid selection, please try again')
        print('Which operation would you like to do?')
        print('1: Addition')
        print('2: Subtraction')
        print('3: Multiplication')
        print('4: Division')

        raw_x = input()
        x = int(raw_x)
        calc(x)
    elif(num == 1):
        print('Please enter 2 numbers')
        print('First number')
        raw_y = input()
        print('Second number')
        raw_z = input()
        y = int(raw_y)
        z = int(raw_z)
        return addition.addition(y,z)
    elif(num == 2):
        print('Please enter 2 numbers')
        print('First number')
        raw_y = input()
        print('Second number')
        raw_z = input()
        y = int(raw_y)
        z = int(raw_z)
        return subtraction.subraction(y, z)
    elif(num == 3):
        print('Please enter 2 numbers')
        print('First number')
        raw_y = input()
        print('Second number')
        raw_z = input()
        y = int(raw_y)
        z = int(raw_z)
        return multiplication.multiplication(y, z)
    elif(num == 4):
        print('Please enter 2 numbers')
        print('First number')
        raw_y = input()
        print('Second number')
        raw_z = input()
        y = int(raw_y)
        z = int(raw_z)
        return division.division(y, z)
calc(x)