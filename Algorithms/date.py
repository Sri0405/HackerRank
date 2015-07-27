# Convert Date from 12 hr to 24 hr format
x = raw_input()
data = x.split(":")
y = 0
if (int(data[0]) <= 12) and (int(data[0]) >= 1):
    y = int(data[0]) + 12

z = data[2][:2]
if y == 24:
    y = 00
print str(y) + ":" + (data[1]) + ":" + str(z)
