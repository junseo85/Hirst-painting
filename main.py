#import colorgram
# extracting colors from the painting and store(as RGB) in the hirst_color list
# hirst_color = []
# colors = colorgram.extract('image.jpg', 54)
#
# def extract_rgb(color_list):
#     for i in color_list:
#         r = i.rgb[0]
#         g = i.rgb[1]
#         b = i.rgb[2]
#         rgb_color = (r,g,b)
#         hirst_color.append(rgb_color)
#
# extract_rgb(colors)
# print(hirst_color)
import random
from turtle import Turtle, Screen
#copy the contemporary art by Hirst and reproduce using Turtle
color_list = [(141, 174, 201), (22, 30, 46), (34, 106, 151), (207, 159, 112), (227, 211, 100), (141, 28, 61), (173, 49, 83), (211, 71, 99), (12, 163, 193), (193, 137, 169), (63, 168, 114), (136, 91, 74), (32, 60, 111), (115, 180, 110), (223, 79, 48), (191, 184, 43), (172, 209, 178), (7, 94, 111), (238, 205, 4), (78, 31, 64), (50, 144, 111), (221, 174, 192), (229, 171, 162), (143, 208, 230), (186, 184, 212), (108, 38, 36), (116, 121, 154), (84, 27, 26), (9, 103, 104)]
tur = Turtle()
tur.speed("fastest")
tur.hideturtle()
screen = Screen()
# set colormode as 255 in order to put RGB number as index
screen.colormode(255)
random_color = random.choice(color_list)
#print(random_color)
y = 0
for _ in range(10):
    for _ in range(10):
        #print 10 dots in first row
        tur.pendown()
        tur.pencolor(random.choice(color_list))
        tur.dot(20)
        tur.penup()
        tur.forward(50)
    #duplicate the process for 10 more lines-painting 10 dots in 10 rows with random color from original painting.
    tur.goto(0, y)
    tur.left(90)
    tur.forward(50)
    tur.right(90)
    y += 50


# tim = Turtle()
# tim.speed("fastest")
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
# for dot_count in range(1, number_of_dots +1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)



screen.exitonclick()