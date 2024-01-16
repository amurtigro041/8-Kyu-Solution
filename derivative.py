def derive (num1,num2):
    coefficient = num2 * num1
    exponent = num2 - 1
    derivate = [str(coefficient),'x','^',str(exponent)]
    return ''.join(derivate)
print(derive(5,9))
print(derive(7,8))

