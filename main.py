from MathOP.add import addvalue
from MathOP.sub import subvalue
from MathOP.mul import mulvalue
from MathOP.div import divvalue

if __name__ == '__main__':
    val1 = int(input("Enter The First Number: "))
    val2 = int(input("Enter The Second Number: "))
    op = input('Which operation you want to perform (add, sub, mul, div): ')
    
    if op.lower() == 'add':
        A = addvalue(val1, val2)
        print(f'ADDITION : {A}')
    
    elif op.lower() == 'sub':
        S = subvalue(val1, val2)
        print(f'SUBTRACTION : {S}')
    
    elif op.lower() == 'mul':
        M = mulvalue(val1, val2)
        print(f'MULTIPLICATION : {M}')
    
    elif op.lower() == 'div':
        D = divvalue(val1, val2)
        print(f'DIVISION : {D}')
        
    else:
        print("Please enter a valid operation: add, sub, mul, or div")
