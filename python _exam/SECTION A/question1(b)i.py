def areaOfTriangle():

    base = int(input('Enter the base of the triangle: '))
    height = int(input('Enter the height of the triangle: '))

    area = (1/2) * base * height

    print(f"The area of a triangle of base {base} and height {height} is {area:.2f}")
#calling the function
areaOfTriangle()

