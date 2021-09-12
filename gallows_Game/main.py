from tkinter import *
from tkinter import messagebox
import random as r
# ---Const---
FONT = "Arial"
root_height = 900
width_root = 1000
MARGIN = 100
WIDTH_CANVAS = 900
HEIGHT_CANVAS = 800
label_word = []
btn_alpha = []
num = 0
tmp = 0




root = Tk()

def game_ower(tmp,st,num):
    can.destroy()
    for btn in btn_alpha:
        btn.place_forget()
    for label_upper in label_word:
        label_upper.place_forget()
    btn_food.place_forget()
    label_text.place_forget()
    btn_animal.place_forget()
    btn_plant.place_forget()
    btn_appliances.place_forget()
    btn_color.place_forget()
    btn_wardrobe.place_forget()
    label_title.place_forget()
    label_luck.place_forget()
    if num < 5:
        tmp += 1
    main(tmp)

def btn(word):
    shift_x = shift_y = 0
    count = 0
    for i in range(ord('А'), ord("Я")+1):
        btn = Button(root, text=chr(i), width=2, font=(FONT, 16), relief=SOLID)
        btn.place(x=width_root - MARGIN*7 + shift_x, y=MARGIN*6.5 - shift_y, anchor=CENTER)
        btn.bind('<Button-1>', lambda event: chek_alpha(event, word))
        btn_alpha.append(btn)
        shift_x += 50
        count += 1
        if count == 8:
            shift_x = count = 0
            shift_y -= 50

def risunok(num):
    global can
    if num == 1:
        can.create_line(800,700,900, 700,width=5,tags="myRectangle");can.create_line(900,10,900,700,width=5,tags="myRectangle");can.create_line(902,10,450,10,width=5,tags="myRectangle");can.create_line(450,10,450,100,width=5,tags="myRectangle")
    elif num == 2:
        can.create_oval(400,100,500,200,tags="myRectangle");can.create_line(420,120,440,130,tags="myRectangle");can.create_line(440,120,420,130,tags="myRectangle");can.create_line(460,120,480,130,tags="myRectangle");can.create_line(480,120,460,130,tags="myRectangle");can.create_arc(435,180,465,170,extent=180,style=ARC,tags="myRectangle")
    elif num == 3:
        can.create_line(450,200,450,350,tags="myRectangle")
    elif num == 4:    
        can.create_line(450,200,400,300);can.create_line(450,200,500,300,tags="myRectangle")
    elif num == 5:
        can.create_line(450,350,400,450);can.create_line(450,350,500,450,tags="myRectangle") 




def start_position(word,text):
    shift = 0
    global label_text
    label_text = Label(root, text="Категория: "+ text, font=(FONT, 25), width=25)
    label_text.place(x=width_root - MARGIN*10.5+shift, y=MARGIN*1)
    for i in range(len(word)):
        label_upper = Label(root, text = "__", font=(FONT, 16), width=2)
        label_upper.place(x=width_root - MARGIN*6.5+shift, y=MARGIN*5, anchor=CENTER)
        shift += 50
        label_word.append(label_upper)
        btn(word)

def chek_alpha(event, word):
    event.widget["state"] = DISABLED
    global label_word
    alpha = event.widget['text']
    lis = []
    global num
    for i in range(len(word)):
        global tmp
        if word[i] == alpha:
            lis.append(i)
    if len(lis) != 0:
        for i in lis:      
            label_word[i].config(text='{}'.format(word[i]))
        count_alpha = 0
        for i in label_word:
            if(i["text"].isalpha()):
                count_alpha += 1
        if count_alpha == len(word):
            
            messagebox.showinfo("Победа", "Поздравляем с победой")
            game_ower(tmp,"win",num)
    else:
        num += 1
        if num <= 4:
            risunok(num)
        else:
            risunok(num)
            messagebox.showinfo("Проигрышь", "Вы проиграли")
            game_ower(tmp,"lose", num)

def spisok(file,text):
    btn_food.place_forget()
    btn_animal.place_forget()
    btn_plant.place_forget()
    btn_appliances.place_forget()
    btn_color.place_forget()
    btn_wardrobe.place_forget()
    label_title.place_forget()
    label_luck.place_forget()
    op = open(file)
    count = 0

    for i in op:
        count += 1
    
    num_word = r.randint(1, count)
    word = ''
    count = 0

    op = open(file, encoding="utf-8")

    for i in op:
        count += 1

        if count == num_word:
            word = i[:len(i)-1:]
    word = word.upper()
    start_position(word,text)

def category(tmp,*args):
    # ---Удаление предыдущего меню---
    label_Hello.place_forget()
    btn_newgame.place_forget()
    btn_exit.place_forget()
    global label_title
    global label_luck
    label_title = Label(root, text="Категории", font=(FONT, "30", "bold"))
    label_luck = Label(root, text="Угадано слов: " + str(tmp), font=(FONT, 20))

    # ---Категории---
    global btn_food; global btn_animal; global btn_plant; global btn_appliances; global btn_color; global btn_wardrobe
    btn_food = Button(root, text="Еда", font=(FONT, 20), width=20, fg="#801313",command=lambda: spisok("food.txt",btn_food["text"]))
    btn_animal = Button(root, text="Животные", font=(FONT, 20), width=20, fg="#c99b1a",command=lambda: spisok("animal.txt",btn_animal["text"]))
    btn_plant = Button(root, text="Растения", font=(FONT, 20), width=20, fg="#307d11",command=lambda: spisok("plant.txt",btn_plant["text"]))
    btn_appliances = Button(root, text="Техника", font=(FONT, 20), width=20, fg="#1563a3",command=lambda: spisok("appliances.txt", btn_appliances["text"]))
    btn_color = Button(root, text="Цвета", font=(FONT, 20), width=20, fg="#ad4c18",command=lambda: spisok("colors.txt",btn_color["text"]))
    btn_wardrobe = Button(root, text="Гардероб", font=(FONT, 20), width=20, fg="#581380",command=lambda: spisok("wardrobe.txt",btn_wardrobe["text"])) 
    # delet.append(btn_food)
    # delet.append(btn_animal)
    # delet.append(btn_plant)
    # delet.append(btn_appliances)
    # delet.append(btn_color)
    # delet.append(btn_wardrobe)
    # print(delet)
    # ---Вывод категорий на экран---
    label_title.place(x=width_root - MARGIN*7, y=MARGIN,)
    label_luck.place(x=width_root - MARGIN*7, y=MARGIN*1.5,)

    
    btn_food.place(x=width_root - MARGIN*7, y=MARGIN*2,)
    btn_animal.place(x=width_root - MARGIN*7, y=MARGIN*3,)
    btn_plant.place(x=width_root - MARGIN*7, y=MARGIN*4,)
    btn_appliances.place(x=width_root - MARGIN*7, y=MARGIN*5,)
    btn_color.place(x=width_root - MARGIN*7, y=MARGIN*6,)
    btn_wardrobe.place(x=width_root - MARGIN*7, y=MARGIN*7,)



# ---Кнопки главного меню---
def main(tmp):
    global num
    num = 0
    global can
    can = Canvas(root, width=WIDTH_CANVAS, height=HEIGHT_CANVAS)
    can.pack()
    global label_Hello
    global label_word
    label_word = []
    global btn_newgame
    global btn_exit
    #root.after(100, "update")
    label_Hello = Label(root, text="Добро пожаловать", font=(FONT, "30", "bold"), height=5)
    btn_newgame = Button(root, text="Новыя игра", font=(FONT, 20), width=18,command=lambda:category(tmp))
    btn_exit = Button(root, text="Выход", font=(FONT, 20), width=18, command=lambda: root.destroy())

    # ---Вывод содержимого главного окна---
    label_Hello.place(x=width_root - MARGIN*7, y=MARGIN,)
    btn_newgame.place(x=width_root - MARGIN*6.6, y=MARGIN*4,)
    btn_exit.place(x=width_root - MARGIN*6.6, y=MARGIN*5,)


main(tmp)
# btn()
# word = spisok()
# start_position(word)
root.resizable(width=False, height=False)
root.geometry("1000x900")
root.mainloop()

