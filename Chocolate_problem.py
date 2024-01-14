#given n x m size of chocolate, then the chocolate must be broken into 1 x 1 square
#if 2 x 1 chocolate bars, then to break into 1 x 1 square, u need to broke it 1 x 
#if 3 x 1 chocolate bars, then to break into 1 x 1, u need to broke 2 x (twice)
def chocolate_bars(length,width):
    area = length * width
    if area > 0:
        breaks = area - 1
        return(breaks)
    else:
        return 0
print(chocolate_bars(3,1))
print(chocolate_bars(2,3))
print(chocolate_bars(3,0))
