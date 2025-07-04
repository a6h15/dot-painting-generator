import turtle as turtle_nodule
import random
# import colorgram
#
# getting out the extracted colors.
# colors = colorgram.extract('image.jpg', 50)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

diddy = turtle_nodule.Turtle()
turtle_nodule.colormode(255)
diddy.speed(0)
diddy.penup()
diddy.hideturtle()

color_list = [(217, 157, 93), (191, 71, 20), (204, 146, 19), (125, 33, 41), (152, 30, 10), (221, 89, 51), (165, 49, 66),
              (208, 78, 96), (88, 27, 35), (229, 123, 145), (130, 159, 132), (71, 115, 86), (93, 24, 11),
              (237, 190, 98), (97, 146, 125), (44, 78, 53), (95, 92, 16), (37, 68, 44), (61, 125, 126), (85, 152, 154),
              (96, 160, 163), (238, 146, 171), (234, 153, 150)]

diddy.setheading(225)
diddy.fd(350)
diddy.setheading(0)
number_dots = 100

for dot_count in range (1, number_dots+1): # +1 for the last dot bug
    diddy.dot(20, random.choice(color_list))
    diddy.fd(50)

    if dot_count % 10 == 0:
        diddy.setheading(90)
        diddy.forward(50)
        diddy.setheading(180)
        diddy.forward(500)
        diddy.setheading(0)

window = turtle_nodule.Screen()
window.exitonclick()