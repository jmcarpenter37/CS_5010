import math
y = 81.7576
t = 1.645
k = math.sqrt(34.9753*(1 + 1/272 + (4.5-34.428461)**2/353.1315))

print(y+t*k)
print(y-t*k)