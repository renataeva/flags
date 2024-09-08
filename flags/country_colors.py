from tkinter import *

root = Tk()

france = [ "france", "blue", "red", "white"]
swizerland = ["swizerland","red", "white"]
germany = ["germany", "black", "red", "yellow"]

m = 0

countries = [france, germany, swizerland]
countries_names = ['france', 'germany', 'swizerland']
countries_flag = ["Flag_of_France.gif"]


color = input("Color? ")

for i in countries:
    for j in i:
        if j == color:
            print(i[0])

n = input("Which flag would you like to see? ")

for i in countries_names:
    if i == n:
        m = i.index(i)
        img = PhotoImage(file=countries_flag[m])
        panel = Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")

root.mainloop()
