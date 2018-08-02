import webbrowser
from tkinter import *
import os

#-------Initilazing tkinter window, setting geo, title and favicon image-------#
root = Tk()
root.geometry('400x350')
root.title('League of Legends counters')
root.iconbitmap('icon.ico')
root.resizable(False, False)



#--------Def a function that directs to user input with the HTTP website-------#
def champion_search():
    webbrowser.open('https://www.lolcounter.com/champions/'+Text1.get("1.0",END))

def exitbtn():
    quit()


def credits_button_pressed():
    root2 = Tk()

    Labelnew = Label(root2,text="This software uses http://www.lolcounter.com as a reference. \n The software is created by Daniel Gorgis. \n i do not take any credits for any information hosted in lolcounter, i just refer to them. Pictures taken from \n http://www.iconarchive.com/show/league-of-legends-gold-border-icons-by-fazie69.html")
    Labelnew.pack()

    ExitButton = Button(root2, text='Exit',command=exitbtn)
    ExitButton.pack()




#-----------GUI interface------------------------------------------------------#
Label1 = Label(root, text='Who counters the champion?', background = 'red')
Label1.pack()

Text1 = Text(root,height=1,width=15,background='grey')
Text1.pack()

Btn = Button(root,text='Search',command=champion_search,fg='green')
Btn.pack()

CreditsButton = Button(root, text="Credits", command=credits_button_pressed)
CreditsButton.pack()

photo = PhotoImage(file="lux.png")
photolabel = Label(root, image=photo,)
photolabel.pack()

#-------------Running Leauge og legends counter--------------------------------#

root.mainloop()