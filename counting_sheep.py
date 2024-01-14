def count_sheeps (array):
    global amount_sheep
    for element in array:
        if True in array:
            amount_sheep  = array.count(True)
        elif 'Null' or 'null' in array:
            amount_sheep = 0
        elif 'undefined' or 'Undefined' in array:
            amount_sheep = 0
        else:
            amount_sheep = 0 
    return amount_sheep
print(count_sheeps([True,True,False,True,True,False,True,True,False]))
print(count_sheeps([True,True,False,True,False,False,'undefined','Undefined',True,False,False,False,False,False]))
print(count_sheeps([False,False,False,False,False,False,False]))
print(count_sheeps(['null','null','undefined','undefined','Undefined']))
            