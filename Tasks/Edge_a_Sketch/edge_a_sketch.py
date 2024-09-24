""" Script that contains an edge a sketch program """
# Dependencies
import  turtle as controller

def main()-> None:
    """ Contains the main loop of program"""

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
        """Move the pen 10 steps forward"""
        pen.forward(10)

    def move_backward():
        """Move the pen 10 steps backward"""
        pen.backward(10)

    def rotate_clockwise():
        """turn the pen to right"""
        pen.right(90)

    def rotate_anti_clockwise():
        """turn the pen to left"""
        pen.left(90)

    def clear_screen():
        """clear the play screen"""
        board.clearscreen()
        pen.home()

    # Mapping operations with Key
    board.onkey(move_forward,'w')
    board.onkey(move_backward,'s')
    board.onkey(rotate_anti_clockwise,'a')
    board.onkey(rotate_clockwise,'d')
    board.onkey(clear_screen,'c')


    board.exitonclick()

if __name__ == '__main__':
    main()
