import turtle as t
import random
timy=t.Turtle()
screen=t.Screen()
t.colormode(255)
def colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)

#timy.penup()



def forward_move():
    #while True:
    timy.forward(100)
    
def backward_move():
    #while True:
    timy.backward(100)
def anticlockwise_move():
    timy.left(10)
    
def clockwise_move():
    timy.right(10)
    
def clear():
    timy.clear()
    timy.penup()
    timy.home()
    timy.pendown()


screen.listen()
screen.onkey(key="w",fun=forward_move)
screen.onkey(key="s",fun=backward_move)
screen.onkey(key="a",fun=anticlockwise_move)
screen.onkey(key="d",fun=clockwise_move)
screen.onkey(key="c",fun=clear)


screen.exitonclick()

