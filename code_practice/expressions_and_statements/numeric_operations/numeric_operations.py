# The initial value of width is set to 24
width = 24
# The initial value of height is set to 78
height = 78
# The initial value of pi is set to 3.1415
pi = 3.1415
# The initial value of radius is set to 2
radius = 2
# The initial value of area_square is set to width raised to the second power
area_square = width ** 2
# The initial value of area_rectangle is set to width times height
area_rectangle = width * height
# The initial value of area_triangle is set to width time height over 2
area_triangle = width * height / 2
# The initial value of area_circle is set to pi times radius raised to the second power
area_circle = pi * radius ** 2
# The initial value of circumference is set to 2 times pi times radius
circumference = 2 * pi * radius

# The initial value of v is set to 1
v = 1
# The initial value of w is set to 1
w = 1
# The initial value of x is set to 1
x = 1
# The initial value of y is set to 1
y = 1
# The initial value of z is set to 2
z = 2

# Shorthand for v = v + 2
v += 2
# Shorthand for w = w - 2
w -= 2
# Shorthand for x = w * 2
x *= 2
# Shorthand for y = y / 2
y /= 2
# Shorthand for z = z % 1
z %= 1

# Outputs area_square which is the result of a side in this case width raised to the second power
print(area_square)
# Outputs area_rectangle which is the result of width times height
print(area_rectangle)
# Outputs area_rectangle which is the result of width times height over 2
print(area_triangle)
# Outputs area_circle which is the result of pi times radius raised to the second power
print(area_circle)
# Outputs circumference which is the result of 2 times pi times radius
print(circumference)
# Outputs current value of v which is what the initial value was plus 2
print(v)
# Outputs current value of w which is what the initial value was minus 2
print(w)
# Outputs current value of x which is what the initial value was times 2
print(x)
# Outputs current value of y which is what the initial value was divided by 2
print(y)
# Outputs current value of z which is what the initial value was mod 1
print(z)
