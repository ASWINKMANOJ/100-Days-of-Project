# import colorgram as cg
#
# colors = cg.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     r_g_b = (r, g, b)
#     rgb_colors.append(r_g_b)
#
# print(rgb_colors)
import random
import turtle as tk
tk.colormode(255)
color_palette = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]
tk.speed("fastest")
tk.penup()
tk.hideturtle()
tk.setheading(225)
tk.forward(300)
tk.setheading(0)
number_of_dots = 101

for _ in range(1, number_of_dots):
    tk.dot(20, random.choice(color_palette))
    tk.forward(50)
    if _%10 == 0:
        tk.setheading(90)
        tk.forward(50)
        tk.setheading(180)
        tk.forward(500)
        tk.setheading(0)



screen = tk.Screen()
screen.exitonclick()