from tkinter import *  # we import the tkinter module
import random  # we import the random module


class Ball:  # we create a ball class
    def __init__(self, canvas, paddle, color):

        self.paddle = paddle
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # We create an oval that will bounce around
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1,1, 2, 3]  # this is the random start position of the ball
        random.shuffle(starts)  # this shuffles the start
        self.x = starts[0]  # this chooses what the position is going to be
        self.y = -3  # this sets the y coordinate to -3
        self.canvas_height = self.canvas.winfo_height()  # this gets the info of the height of our screen
        self.canvas_width = self.canvas.winfo_width()  # this gets the width info of the screen
        self.hit_bottom = False  # this set the hit_bottom state ment to false

    def hit_paddle(self, pos):  # this method check to see if the ball hit the paddle or not
        paddle_pos = self.canvas .coords(self.paddle.id)  # we get the paddles position
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False 
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # moves the ball by self x and self y
        pos = self.canvas.coords(self.id)  # updates the coordinate of the ball
        if pos[1] <= 0:
            self.y = 3  # if it hits the top it comes down
        if pos[3] >= self.canvas_height:
            
            self.hit_bottom = True # if the ball hits the bottom of the canvas turn to true
        if self.hit_paddle(pos) == True:
            self.y = -3# if the ball hits the paddle it goes up
        if pos[0] <= 0: #  left side of the screen it goes right
            self.x = 3
        if pos[2] >= self.canvas_width:  # if the ball goes to the right side it goes left
            self.x = -3


class Paddle:  # a new class named paddle
    def __init__(self, canvas, color):  # this initializes the paddle object
        self.canvas = canvas  # it gives the parameter of the variable
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)  # we make a new rectangle that is our paddle
        self.canvas.move(self.id, 200, 300)  # this moves the paddle to the spot
        self.x = 0  # the set x to 0
        self.canvas_width = self.canvas.winfo_width()  # this gets the info of the width
        self.canvas.bind_all('<Key>', self.turn)  # it binds all the keys to do turn


    def draw(self):  # we make a new define function
        self.canvas.move(self.id, self.x, 0)    # this moves the paddle by the self.x unit
        pos = self.canvas.coords(self.id)  # it gets the paddle position
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:  # the paddle hits the right side of our screen it stops moving
             self.x = 0

    def turn(self, evt):  # this method define the keys that we use left and right
        if evt.keysym == 'Left':  # if the arrow is pressed go x -2 steps

            self.x = -2
        elif evt.keysym == 'Right':  # if right is pressed go to x 2 steps
            self.x = 2


tk = Tk()  # we say tk = Tk
tk.title('Game')  # we say the game title is game
tk.resizable(0, 0)  # we make it so the project can not be reduced
tk.wm_attributes("-topmost", 5) # we say top most so our project will open an all the open tabs
canvas = Canvas(tk, width=500, height=400,bd=0,highlightthickness=0,  bg='black')  # we give the width and height and color and all that stuff to canvas we can also use root for this

canvas.pack()  # we pack all the width and height
tk.update()  # we update the screen
paddle = Paddle(canvas, 'white')  # this defines that color of the paddle
ball = Ball(canvas, paddle, 'white')  # and this defines the color of the ball



def update():  # this method keeps the project alive and running
    if ball.hit_bottom == False:  # it says if the ball has not hit the bottom then run this
        ball.draw()  # this draws the ball
        paddle.draw()  # this draws the paddle
    tk.after(10, update)  # this says after 10 milliseconds update the project ,so we can have a movement that is smooth


update()
tk.mainloop()
