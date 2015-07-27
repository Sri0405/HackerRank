# Calculate Library Fine

x_1 = raw_input()
y_1 = raw_input()

x = x_1.split(" ")
y = y_1.split(" ")

z = 0
if y[2] > x[2]:
    print z
elif y[2] == x[2] and y[1] > x[1]:
    print z
elif y[2] == x[2] and y[1] == x[1] and y[0] > x[0]:
    print z

elif (int(x[2]) != int(y[2])):
    print 10000

elif (int(x[1]) != int(y[1])):
    print abs(int(x[1]) - int(y[1])) * 500

elif (int(y[0]) != int(x[0])):
    print abs(int(y[0]) - int(x[0])) * 15
