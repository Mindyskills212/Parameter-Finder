print("Welcome to Mindy Skills parameter finder.")
parameter = input("Find the parameter of 1.Square 2.Rectangle : ")
length = int(input("Length of the one side of the shape : "))
width = int(input("Width of the one side of the shape : "))

if parameter == "1" and length == width :
    length_s = length * 2
    width_s = width * 2
    print(length_s + width_s)
    
elif parameter == "2" and length != width :
    length_r = length * 2
    width_r = width * 2
    print(length_r + width_r)
    
else :
    print("You typed wrong. ERROR !!!")