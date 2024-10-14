import math
from string import ascii_uppercase

calc_on = True

havePar = {
    "p1": False,
    "p2": False,
    "p3": False,
    "a1": False,
    "a2": False,
    "a3": False,
    "l1": False,
    "l2": False,
    "l3": False
}

canCalc = {

}

parList = {
    "p1": "",
    "p2": "",
    "p3": "",
    "a1": "",
    "a2": "",
    "a3": "",
    "l1": "",
    "l2": "",
    "l3": ""
}


def get_pars():
    print(r"""        p1
        /\
       /a1\
      /    \
  l3 /      \ l1
    /        \
   /          \
  / a3      a2 \
 /______________\
p3      l2      p2""")
    print("Enter parameters:\nif unknown enter 'NA'")
    parList["p1"] = input("Point 1: ")
    parList["p2"] = input("Point 2: ")
    parList["p3"] = input("Point 3: ")
    parList["a1"] = input("Angle 1: ")
    parList["a2"] = input("Angle 2: ")
    parList["a3"] = input("Angle 3: ")
    parList["l1"] = input("Length 1: ")
    parList["l2"] = input("Length 2: ")
    parList["l3"] = input("Length 3: ")
    # getting all the known parameters


def check_pars():
    for i in parList:
        if i == "NA":
            continue
        elif i in ascii_uppercase:
            continue
        else:
            float(i)
    if parList["p1"] or parList["p2"] or parList["p3"] not in ascii_uppercase:
        print("Invalid input")
        exit()


def reset():
    for i in parList:
        i = ""
    for i in havePar:
        i = False
    for i in canCalc:
        i = False
    print("Reset the values")


class Triangle:
    global parList

    def __init__(self):
        self.parList = parList

    def abt(self):
        print("p1: " + self.parList["p1"])
        print("p2: " + self.parList["p2"])
        print("p3: " + self.parList["p3"])
        print("a1: " + str(self.parList["a1"]))
        print("a2: " + str(self.parList["a2"]))
        print("a3: " + str(self.parList["a3"]))
        print("l1: " + str(self.parList["l1"]))
        print("l2: " + str(self.parList["l2"]))
        print("l3: " + str(self.parList["l3"]))
        print("l3: " + str(self.parList["l3"]))


get_pars()
Figure = Triangle()
Figure.abt()
check_pars()
reset()
