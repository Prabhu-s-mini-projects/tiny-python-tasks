import  turtle as controller

# creating a pen.
pen = controller.Turtle()
#pen.shape("circle")
pen.speed("fastest")
#pen.hideturtle()

# creating a board
board =  controller.Screen()
board.listen()

# operations
def move_forward():
    pen.forward(10)

def move_backward():
    pen.backward(10)

def rotate_clockwise():
    pen.right(90)

def rotate_anti_clockwise():
    pen.left(90)

def clear_screen():
    board.clearscreen()
    pen.home()

# Mapping operations with Key
board.onkey(move_forward,'w')
board.onkey(move_backward,'s')
board.onkey(rotate_anti_clockwise,'a')
board.onkey(rotate_clockwise,'d')
board.onkey(clear_screen,'c')


board.exitonclick()
