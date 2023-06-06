from tkinter import *
import Leaderboard
from winsound import *
loading = False

def main_window(root):
    bg = PhotoImage(file="car_start_alpha.png")
    label = Label(root,image=bg)
    label.image = bg

    label.place(x=0, y=0)
    print()

    # bg = PhotoImage(file = "car-beta.png")
    # label1 = Label(root, image = bg)
    # label1.place(x = 0, y = 0)

    def play_func():

        print()



    def leaderboard_func():

        file = open("TopScores.txt", "r")
        try:
            root = Tk()
            root.attributes("-topmost",True)
            root.geometry("900x900")
            root.title("Leaderboard")
            root.configure(bg="#002952")
            # Creating table headings
            header = Label(root, text="LEADERBOARD", bg="#002952", fg="white", font=('algerian', 40))
            header.grid(row="3", column="2", pady="40")
            rank = Label(root, text="RANK", bg="#002952", fg="white", font=('algerian', 30))
            rank.grid(row="4", column="1", padx="70", pady="30")
            player = Label(root, text="PLAYER", bg="#002952", fg="white", font=('algerian', 30))
            player.grid(row="4", column="2", padx="70", pady="30")
            score = Label(root, text="SCORE", bg="#002952", fg="white", font=('algerian', 30))
            score.grid(row="4", column="3", padx="70", pady="30")

            for j in range(5):
                i = file.readline()
                position_list = i.split(",")
                Leaderboard.table(position_list[0], position_list[1], position_list[2], root)

        except:
            pass
        file.close()



    def settings_func():

        settings = Button(left_panel, width = 38, height = 2, text = "Settings",command=lambda x = root: settings_window(x)).place(x = 2, y = 240)





    left_panel = Frame(root, width=300, height=500, bg="#FEF24E")
    left_panel.place(x=0, y=0)

    leaderboard = Button(left_panel, width=38, height=2, text="Leaderboard", command=leaderboard_func)
    leaderboard.place(x=2, y=180)
    settings_func()


def settings_window(root):

    left_panel = Frame(root, width=300, height=500, bg="#FEF24E")
    left_panel.place(x=0, y=0)


    def load_func():
        load = Button(left_panel, width=38, height=2, text="Load",command=lambda x = 1: load1(x) ).place(x=2, y=60)
        print()
    def difficulty_func():
        global opt
        difficulty = Button(left_panel, width=38, height=2, text="Difficulty").place(x=2, y=120)
        opt = IntVar()
        opt.set(2)

        easy = Radiobutton(left_panel, width=7, height=2, text="Easy", variable=opt, value=1,
                           command=getval,bg="#FEF24E").place(x=30, y=180)
        medium = Radiobutton(left_panel, width=7, height=2, text="Medium", variable=opt, value=2,
                             command=getval,bg="#FEF24E").place(x=100, y=180)
        hard = Radiobutton(left_panel, width=7, height=2, text="Hard", variable=opt, value=3,
                           command=getval,bg="#FEF24E").place(x=170, y=180)


    def customization_func():
        customization = Button(left_panel, width=38, height=2, text="Customization",command=lambda x=root: customization_window(x)).place(x=2, y=240)

    def collapse_func():
        left_panel.destroy()


    load_func()
    difficulty_func()
    customization_func()
    Button(left_panel, text="Back", command=collapse_func).place(x=5, y=10)


def load1(x=0):
    global loading
    if x == 1:
        loading = True
    if loading is True:
        return True
def change():
    global loading
    loading = False

def getval():
    global opt
    try:
        velocity = opt.get()
    except:
        velocity = 2
    return True,velocity


def customization_window(root):
    def collapse_func():
        customization_panel.destroy()

    def get_keys():
        b = right_var.get()
        c = left_var.get()
        change_controls(b,c)
        right_var.set("")
        left_var.set("")
    customization_panel = Frame(root, width=300, height=500, bg="beige")
    customization_panel.place(x=0, y=0)
    right_var = StringVar(root)
    left_var = StringVar(root)
    controls_label = Label(customization_panel, width=38, height=2, text="Controls").place(x=2, y=50)
    right_label = Label(customization_panel, width=20, height=2, text="Move Right").place(x=2, y=120)
    right_entry = Entry(customization_panel, width=4, textvariable=right_var).place(x=160, y=128)

    left_label = Label(customization_panel, width=20, height=2, text="Move Left").place(x=2, y=180)
    left_entry = Entry(customization_panel, width=4, textvariable=left_var).place(x=160, y=188)

    skins_label = Label(customization_panel, width=38, height=2, text="Car Skins").place(x=2, y=250)

    orange = Button(customization_panel, width=3, height=1, bg="orange", command=lambda x="orange": get_vals(x)).place(
        x=110, y=320)
    yellow = Button(customization_panel, width=3, height=1, bg="yellow", command=lambda: get_vals("yellow")).place(x=50,
                                                                                                                   y=350)
    green = Button(customization_panel, width=3, height=1, bg="green", command=lambda: get_vals("green")).place(x=80,
                                                                                                                y=350)
    blue = Button(customization_panel, width=3, height=1, bg="blue", command=lambda: get_vals("blue")).place(x=110,
                                                                                                             y=350)
    violet = Button(customization_panel, width=3, height=1, bg="violet", command=lambda: get_vals("violet")).place(x=50,
                                                                                                                   y=380)
    save_changes = Button(customization_panel, width=10, height=1, text="Save Changes", command=get_keys).place(x=110,y=440)
    Button(customization_panel,text="Back",command=collapse_func).place(x=2,y=10)
change_skin = False
change_color = ""
change_control = False
control_right = ""
control_left = ""
def get_vals(a=""):
    global change_skin,change_color
    if a != "":
        print("This ran")
        change_skin = True
        change_color = a
    if change_skin is False:
        return False,a
    else:

        return True,change_color

def change_controls(b="d",c="a"):
    global change_control,control_right,control_left
    print(b,c)
    if b != "d" or c != "a":
        print("This ran here",b,c)
        change_control = True
        control_right = b
        control_left = c
    if change_control is False:
        return False,b,c
    else:
        return True,control_right,control_left













