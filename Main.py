from tkinter import *
from tkinter.constants import *
from random import randint as rand
from winsound import *
import Menu
import webbrowser


def make_lane(x1,y1,x2,y2):
    diff = (y2-y1)-10
    id = canvas.create_rectangle(x1, y1, x2 ,y2, fill="white")
    list_1.append(id)
    global toplevel_item
    toplevel_item = id
    starty = y2 + 35
    endy = starty + diff
    y2 = endy
    id = canvas.create_rectangle(x1 , starty, x2 , endy, fill="white")
    list_1.append(id)
def move_lanes(speed):
    for count in range(len(list_1)):
        canvas.move(list_1[count],0,speed)
    for count in range(len(list_2)):
        canvas.move(list_2[count],0,speed)


def delete_lane():
    id = list_1[0]
    coords_list = canvas.coords(id)
    if coords_list[1] > 750:
        canvas.delete(id)
        list_1.pop(0)
        id = list_1[0]
        list_1.pop(0)
        canvas.delete(id)
def arrow_moveleft(event):
    global pause1
    global x1, y1
    global running, move_right, move_left
    coords_list = canvas.coords(image)
    x_value = coords_list[0]
    if x_value != 605.0:
        if running is True:
            running = collision(-120)
        if running is False:
            canvas.move(image, -80, 0)

        else:
            canvas.move(image,-120,0)
def arrow_moveright(event):
    global pause1
    global x1, y1
    global running, move_right, move_left
    coords_list = canvas.coords(image)
    x_value = coords_list[0]
    if x_value != 845.0:
        if running is True:
            running = collision(120)
        if running is False:
            canvas.move(image, 80, 0)
        else:
            canvas.move(image, 120, 0)
def move(event):
    global pause1
    global x1, y1
    global running,move_right,move_left
    coords_list = canvas.coords(image)
    x_value = coords_list[0]
    if event.char == "p":
        pause1 = True
    if event.char == "b":
        boss_code()
    if event.char == move_left and x_value != 605.0:
        if running is True:
            running = collision(-120)
        if running is False:
            canvas.move(image, -80, 0)

        else:
            canvas.move(image,-120,0)
    elif event.char == move_right and x_value != 845.0:
        if running is True:
            running = collision(120)
        if running is False:
            canvas.move(image, 80, 0)
        else:
            canvas.move(image, 120, 0)
cheat = False
def check_cheatcode():
    global cheat
    if name2 == "cheat":
        cheat = True


def create_obstacles():
    global first_run
    if first_run is True:
        num_cars = 2
        first_run = False
    else:
        num_cars = rand(1, 2)

    if num_cars ==1:
        lane1 = rand(1,3)
        image1 = PhotoImage(file="car3.png")
        label = Label(image = image1)
        label.image = image1
        if lane1 == 1:
            id = canvas.create_image(605, 15, image=image1)
            root.id = id
            list_2.append(id)
        elif lane1 == 2:
            id = canvas.create_image(725, 15, image=image1)
            root.id = id
            list_2.append(id)
        else:
            id = canvas.create_image(845, 15, image=image1)
            root.id = id
            list_2.append(id)
    else:
        lane1 = rand(1, 3)
        chosen = False
        lane2 = rand(1, 3)
        while chosen is False:
            if lane2 == lane1:
                lane2 = rand(1, 3)
            else:
                chosen = True
        image1 = PhotoImage(file="car3.png")
        label = Label(image=image1)
        label.image = image1
        if lane1 == 1:
            id = canvas.create_image(605, 15, image=image1)
            list_2.append(id)
        elif lane1 == 2:
            id = canvas.create_image(725, 15, image=image1)
            list_2.append(id)
        else:
            id = canvas.create_image(845, 15, image=image1)
            list_2.append(id)
        image2 = PhotoImage(file="car9.png")
        label2 = Label(image=image2)
        label2.image = image2
        if lane2 == 1:
            id = canvas.create_image(605, 15, image=image2)
            list_2.append(id)
        elif lane2 == 2:
            id = canvas.create_image(725, 15, image=image2)
            list_2.append(id)
        elif lane2 ==3:
            id = canvas.create_image(845, 15, image=image2)
            list_2.append(id)

def delete_obstacles():
    id = list_2[0]
    coords_list = canvas.coords(id)
    id1 = list_2[1]
    coords_list1 = canvas.coords(id1)
    if coords_list[1] > 850 and coords_list1[1] > 850:
        canvas.delete(id)
        list_2.pop(0)
        id = list_2[0]
        list_2.pop(0)
        canvas.delete(id)
    elif coords_list[1] > 850:
        canvas.delete(id)
        list_2.pop(0)


def collision(move=0):
    global cheat,restart1
    coords_list = canvas.coords(image)
    length = len(list_2)
    list_clone = list_2[:]
    for count in range(length):
        id = list_clone[count]
        coords_list2 = canvas.coords(id)
        if abs((coords_list[1] - coords_list2[1]) - 85) < 10 and abs((coords_list[0] - coords_list2[0])) < 10:

            if cheat is False and restart1 is False:
                return False

        if abs((coords_list[1] - coords_list2[1])) < 80 and abs((coords_list[0] - coords_list2[0]) + move) < 80:

            if cheat is False and restart1 is False:
                return False



    return True
restart1 = True
def save():
    global score,velocity,list_2,obstacle_density
    file = open("SaveGames.txt","w")
    file.write(str(score)+"\n")
    file.write(str(velocity)+"\n")
    file.write(str(obstacle_density)+"\n")
    for x in list_2:
        coords_save = canvas.coords(x)
        file.write(str(coords_save[0])+' '+str(coords_save[1])+" \n")


def load():
    global score,velocity,list_2,obstacle_density,count
    count = 0
    file = open("Savegames.txt","r")
    score = float(file.readline())
    velocity = float(file.readline())
    obstacle_density = float(file.readline())
    for line in file:
        coords_load = line.split(" ")
        coords_x = float(coords_load[0])
        coords_y = float(coords_load[1])
        image1 = PhotoImage(file="car3.png")
        label = Label(image=image1)
        label.image = image1
        image2 = PhotoImage(file="car9.png")
        label2 = Label(image=image2)
        label2.image = image2
        which_image = rand(1,2)
        if which_image == 1 and coords_x != 725.0:
            id = canvas.create_image(coords_x, coords_y, image=image1)
            root.id = id
            list_2.append(id)
        elif which_image == 2 and coords_x != 725.0:
            id = canvas.create_image(coords_x, coords_y, image=image2)
            root.id = id
            list_2.append(id)



def top_score():
    global score,name2
    file1 = open("TopScores.txt","r")
    list_lines = file1.readlines()
    score = "%.1f" % score
    for line in range(5):
        s = list_lines[line].split(",")

        if float(score) > float(s[2]):
            s[2] = score+" \n "
            s[1] = name2
            list_lines[line] = ",".join(s)

            break
    file1 = open("TopScores.txt","w")
    file1.writelines(list_lines)
    file1.close()

name2 = ""

def name():
    global name1,root2
    root2 = Tk()
    root2.attributes("-topmost",True)
    root2.title("Name")
    name1 = StringVar(root2)
    Label(root2,text="Please enter your name:",anchor=CENTER).pack()
    entry = Entry(root2,textvariable=name1)
    entry.pack()
    Button(root2,text="Submit",command= lambda x=root2: name_submit(x)).pack()
def name_submit(root):
    global name2,name1

    name2 = name1.get()
    root.destroy()
def unpause(event):
    global pause1,display,root1
    pause1 = False
    root1.destroy()
    display = False
def resume():
    global pause1, display, root1

    pause1 = False
    root1.destroy()
    root.lift()
    root.focus_force()
    display = False
def score2():
    global score1,score
    score = score + 0.01
    label.config(text="Score: "+ "%.1f" % score)
exited = False
def exit():
    global root1,running,sound,exited,root2

    root1.destroy()
    root.destroy()
    root2.destroy()
    running = False
    sound = False
    exited = True
def menu():
    global root1,pause1
    root1 = Toplevel()
    root1.attributes("-topmost", True)
    root1.geometry("900x500")
    root1.title("Start Menu")
    root1.configure(bg="black")
    Menu.main_window(root1)
    play = Button(root1, width=38, height=2, text="Play/Resume", command=resume)
    play.place(x=2, y=60)
    restart = Button(root1, width=38, height=2, text="Restart",command= restart_func)
    restart.place(x=2, y=120)
    if running is True:
        restart.config(state=DISABLED)
    exit1 = Button(root1, width=38, height=2, text="Exit", command=exit)
    exit1.place(x=2, y=300)
    root1.update()

def restart_func():
    global restart1,root1

    restart1 = True
    root1.destroy()
chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
def boss_code():
    webbrowser.get(chrome).open("www.gmail.com")
    exit()

def background_music():
    PlaySound('bg_music.wav', SND_ALIAS | SND_ASYNC)
    root.after(1000 * 247, background_music)
def set_dificulty(difficulty):
    global velocity
    if difficulty == 1:
        velocity = 1.5
    if difficulty == 2:
        velocity = 2.5
    if difficulty == 3:
        velocity = 3.0
def button_click():
    PlaySound('button_click3.wav', SND_ALIAS | SND_ASYNC)
root = Tk()
first_run = True
root.title("Traffic Mayhem")
canvas = Canvas(root, width=1800, height=900, bg="black")
canvas.pack(expand=YES, fill=BOTH)
background = PhotoImage(file='Road1.png')
canvas.create_image(750, 200, image=background, anchor="center")
score1 = IntVar()
label = Label(canvas, bg="black", fg="white")
label.place(x=5, y=10)
save_button = Button(canvas, command=save, text="Save", height=1, width=4)
save_button.place(x=10, y=40)
menu_button = Button(canvas, command=menu, text="Menu", height=1, width=4)
menu_button.place(x=10, y=80)
org_x1 = 655
org_y1 = -35
org_x2 = 660
org_y2 = 40
first_go = True
move_right = "d"
move_left = "a"
while restart1 is True:
    orange_img = PhotoImage(file="orange car.png")
    violet_img = PhotoImage(file="purple car.png")
    green_img = PhotoImage(file="car_supreme.png")
    blue_img = PhotoImage(file="car3.png")
    yellow_img = PhotoImage(file="yellow car.png")
    img = PhotoImage(file="car9.png")
    image = canvas.create_image(725, 475, image=img)
    canvas.coords(image, 725, 475)
    first_run = True
    restart1 = False
    global list_1
    global list_2
    running = True

    if first_go is True:
        pause1 = True
    else:
        pause1 = False
    sound = True
    score = 0
    display = False
    diff = 75
    list_1 = []
    list_2 = []

    count = 0
    velocity = 1.5
    obstacle_density = 800
    lane_diff = 130
    first = True
    make_lane(org_x1, org_y1, org_x2, org_y2)
    make_lane(org_x1 + lane_diff, org_y1, org_x2 + lane_diff, org_y2)
    bg_sound = True

    while running is True:
        color = Menu.get_vals()
        if color[0] is True:
            Menu.change_skin = False
            if color[1] == "white":
                white_img = PhotoImage(file="Skins/white.png")
            elif color[1] == "red":
                red_img = PhotoImage(file="Skins/red.png")
            elif color[1] == "orange":
                print("This ran")
                canvas.itemconfig(image,image=orange_img)
            elif color[1] == "yellow":
                canvas.itemconfig(image, image=yellow_img)
            elif color[1] == "green":
                canvas.itemconfig(image,image=green_img)
            elif color[1] == "blue":
                canvas.itemconfig(image, image=blue_img)
            elif color[1] == "violet":
                canvas.itemconfig(image,image=violet_img)
            elif color[1] == "black":
                black_img = PhotoImage(file="Skins/black.png")
        control = Menu.change_controls()
        if control[0] is True:
            print("This is controlled",control[1],control[2])
            move_right = control[1]
            move_left = control[2]
            Menu.change_control = False
        if bg_sound is True:
            background_music()
            bg_sound = False
        if Menu.load1() is True:
            load()
            Menu.change()
        check_cheatcode()
        dif = Menu.getval()
        if dif[0] is True:
            set_dificulty(dif[1])
        while pause1 is False and running is True:
            if Menu.load1() is True:
                load()
                Menu.change()
            move_lanes(velocity)
            coords_list = canvas.coords(toplevel_item)
            if coords_list[1] > 70:
                make_lane(org_x1, org_y1, org_x2, org_y2)
                make_lane(org_x1 + lane_diff, org_y1, org_x2 + lane_diff, org_y2)
            if count > obstacle_density:
                create_obstacles()
                delete_obstacles()
                count = 0
            if count > obstacle_density - 100:
                velocity = velocity + 0.0001
                if obstacle_density > 330 or (velocity > 2.5 and obstacle_density > 200) or (
                        velocity > 3.0 and obstacle_density > 150):
                    obstacle_density = obstacle_density - 10
            running = collision()
            delete_lane()
            root.bind("<Key>", move)
            root.bind("<Left>",arrow_moveleft)
            root.bind("<Right>",arrow_moveright)
            root.bind("<Return>", unpause)
            count += 1
            score2()
            root.update()
        while pause1 is True and running is True:
            if Menu.load1() is True:
                load()
                Menu.change()
            if display is False and first is True and first_go is True:
                menu()
                name()
                display = True
                first = False
            elif display is False :
                menu()
                display = True

            root.update()
    top_score()
    if sound is True:
        PlaySound('crashsound.wav', SND_FILENAME)
    display = False
    if exited is False:
        for i in list_2:
            canvas.delete(i)
        for j in list_1:
            canvas.delete(j)
        while restart1 is False:
            if display is False:
                menu()
                display = True
            root.update()
            first_go = False


root.mainloop()



