#snake game!

#tips and tricks to understand what coding is and how python is OOP

#basically you ask the computer to do something in a way it understands

from tkinter import * #basically just the graphics and it is set like a chess board
import random

#constants--------------------------------------
game_width=800#these are the best for my computer screen
game_height=550
speed=100#larger number is slower
space_size=25#the size of the cubes in the graphic
body_parts=3#starting size


#could make a rainbow using random.random(r,g,b)
snake_color="blue"
food_color="red"
background_color="chartreuse1"#lol just lime green. 
#wanted it to look like googles version

#-------------------------------------------------

#this is our first object!
class Snake:


    def __init__(self):#constructing our object with self being the object
        self.body_size=body_parts
        self.coordinates=[]#graphic is still relative to x y coordinates
        self.squares=[]#again, using tkinter easy to think like chess

        for i in range(0,body_parts):#a for loop goes through the specificed data (in this case body parts)
            self.coordinates.append([0,0])#append items one by one to an existing list

            
        for x,y in self.coordinates:#this is setting where the snake is and  its color
            square=canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color,tag="snake")#tag just makes it more muttable
            self.squares.append(square)




class Food:
    
    def __init__(self):#randomly placing food items

        x=random.randint(0,(game_width/space_size-1))*space_size
        y=random.randint(0,(game_height/space_size-1))*space_size

        self.coordinates=[x,y]

        canvas.create_oval(x,y,x+space_size,y+space_size,fill=food_color,tag="food")#wanted it to look like an apple
        


def next_turn(snake,food):


    x,y=snake.coordinates[0]

    if direction=="up":#constantly subtracting the y coordinate. 0,0 is at the top left corner
        y -= space_size
    elif direction=="down":
        y += space_size#constantly adding to the y coordinate
    elif direction=="left":
        x -= space_size
    elif direction=="right":
        x+= space_size

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color)

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:#basically if we eat an apple, we add to the score
        global score
        score+=1
        label.config(text="SCORE: {}".format(score))

        canvas.delete("food")

        food=Food()
    else:#this just makes it so we do not add a square if we do not eat apples

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):#collisions is a seperate function that i will explain later
        game_over()
    else:
        window.after(speed,next_turn,snake,food)



    
def change_direction(new_direction):
    global direction

    
    if new_direction == "left":
        if direction != "right":
            direction = new_direction   #only if the new direction does not turn the snake inwards will the computer follow the directions
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

    
def check_collisions(snake):
    x,y=snake.coordinates[0]
    if x <0 or x >= game_width:#if returns true we died
        return True
    elif y <0 or y>= game_height:
        return True
    for body_part in snake.coordinates[1:]:#snake cant hit its tail
        if x == body_part[0] and y == body_part[1]:

            return True
    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER", fill="red", tag="gameover",)
#--------------------------------------------------------------

    
window=Tk()
window.title("Snake Game")


score=0
direction='down'
label=Label(window, text="SCORE {}".format(score),font=('consolas',40))
label.pack()#specific to tkinter. organizes the blocks and puts them where specified in the screen

canvas=Canvas(window,bg=background_color, height=game_height, width=game_width)
canvas.pack()

window.update()#updating the window with the below information so screen and window are "synchronized"
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_height/2))
y=int((screen_height-50)-(screen_width/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")#replaces expressions with data like x and y
#we just set those up above

#the following are events physically imputed into the computer
#which are then turned into objects to that they can be read with my code
window.bind('<Left>',lambda event: change_direction('left'))#anonymous functions
window.bind('<Right>',lambda event: change_direction('right'))#event to object so the code can read it
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))

snake=Snake()
food=Food()

next_turn(snake,food)
window.mainloop()
