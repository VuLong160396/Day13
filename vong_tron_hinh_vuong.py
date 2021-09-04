import turtle
square = turtle.Turtle()

# def draw_square(angle):
#     for i in range(3):
#         square.forward(100)
#         square.right(90)    

#     # square.forward(100)
#     # square.right(90 + angle)

# square.speed(10)
# step = 36
# angle = 360 / step
# for i in range(step):
#     draw_square(angle) 

def ve_hinh_vuong(s):
    for i in range(4):
        square.fd(s)
        square.rt(90)

square.speed(10)
step = 36
angle = 360 /step
for i in range(step):
    ve_hinh_vuong(100)
    square.lt(angle)

turtle.done()