def add(a, b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
print('************************************************')
print('1\t Addition')
print('2\t Subtraction')
print('3\t Multiplication')
print('4\t Division')
print('5\tExit')

print('**************************************************')
ch=int(input('Enter Your Choice 1-5'))
if ch==5:
    exit()
else:
    a=int(input('Enter First Number'))
    b=int(input('Enter Second Number'))
    if ch==1:
        print('First Number=',a)
        print('Second Number=',b)
        print('Result=',add(a,b))
    elif ch==2:
        print('First Number=',a)
        print('Second Number=',b)
        print('Result=',sub(a,b))
    elif ch==3:
        print('First Number=',a)
        print('Second Number=',b)
        print('Result=',mul(a,b))
    elif ch==4:
        print('First Number=',a)
        print('Second Number=',b)
        print('Result=',div(a,b))
    else:
        print('Invalid Choice')
