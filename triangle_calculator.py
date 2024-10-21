import math
import string

calc_on = True

have_params = {
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

params = {
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

twitch = [params["l1"], params["l2"], params["l3"]]

biggest_side = twitch[2]


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
    print("Enter parameters:\nIf unknown, press enter")
    params["p1"] = input("Point 1: ")
    params["p2"] = input("Point 2: ")
    params["p3"] = input("Point 3: ")
    params["a1"] = input("Angle 1: ")
    params["a2"] = input("Angle 2: ")
    params["a3"] = input("Angle 3: ")
    params["l1"] = input("Length 1: ")
    params["l2"] = input("Length 2: ")
    params["l3"] = input("Length 3: ")
    # getting all the known parameters


def check_pars():
    global twitch

    for k in params:
        if params[k] == "":
            print(k + " is empty")
            have_params[k] = False
        else:
            have_params[k] = True

    if not have_params["p1"] or not have_params["p2"] or not have_params["p3"]:
        if params["p1"] == "" or params["p2"] == "" or params["p3"] == "":
            print("Please enter all point names")
            exit(2)
    elif params["p1"] not in string.ascii_uppercase or params["p2"] not in string.ascii_uppercase or params["p3"] not in string.ascii_uppercase or len(params["p1"]) > 1 or len(params["p2"]) > 1 or len(params["p3"]) > 1:
        print("Invalid input in point names")
        exit(4)

    if have_params["a1"] and int(params["a1"]):
        int(params["a1"])
    if have_params["a2"] and int(params["a2"]):
        int(params["a2"])
    if have_params["a3"] and int(params["a3"]):
        int(params["a3"])
    if params["a1"].isnumeric() and have_params["a1"]:
        if int(params["a1"]) > 180 or int(params["a1"]) < 0:
            print("Invalid input in angle value 3.1")
            exit(3)
    if params["a2"].isnumeric() and have_params["a2"]:
        if int(params["a2"]) > 180 or int(params["a2"]) < 0:
            print("Invalid input in angle value 3.2")
            exit(3)
    if params["a3"].isnumeric() and have_params["a3"]:
        if int(params["a3"]) > 180 or int(params["a3"]) < 0:
            print("Invalid input in angle value 3.3")
            exit(3)

    if have_params["l1"] and int(params["l1"]):
        int(params["l1"])
    if have_params["l2"] and int(params["l2"]):
        int(params["l2"])
    if have_params["l3"] and int(params["l3"]):
        int(params["l3"])
    if params["l1"] != "":
        if params["l1"].isnumeric() == 0:
            print("Invalid input in length 4.1")
            exit(4)
    if params["l2"] != "":
        if params["l2"].isnumeric() == 0:
            print("Invalid input in length 4.2")
            exit(4)
    if params["l3"] != "":
        if params["l3"].isnumeric() == 0:
            print("Invalid input in length 4.3")
            exit(4)


    twitch = [params["l1"], params["l2"], params["l3"]]

    # sorting the lengths
    n = len(twitch)

    for k in range(n - 1):
        for j in range(n - k - 1):
            if twitch[j] > twitch[j + 1]:
                twitch[j], twitch[j + 1] = twitch[j + 1], twitch[j]
    print(twitch)


def reset():
    global params, have_params

    for i in params:
        params[i] = ""

    for i in have_params:
        have_params[i] = False

    print("Reset the values")


class Triangle:
    global params

    def __init__(self):
        self.param = params

    def abt(self):
        print("p1: " + self.param["p1"] + " " + str(have_params["p1"]))
        print("p2: " + self.param["p2"] + " " + str(have_params["p2"]))
        print("p3: " + self.param["p3"] + " " + str(have_params["p3"]))
        print("a1: " + str(self.param["a1"]) + " " + str(have_params["a1"]))
        print("a2: " + str(self.param["a2"]) + " " + str(have_params["a2"]))
        print("a3: " + str(self.param["a3"]) + " " + str(have_params["a3"]))
        print("l1: " + str(self.param["l1"]) + " " + str(have_params["l1"]))
        print("l2: " + str(self.param["l2"]) + " " + str(have_params["l2"]))
        print("l3: " + str(self.param["l3"]) + " " + str(have_params["l3"]))
        print("l3: " + str(self.param["l3"]) + " " + str(have_params["l3"]))

    def is_triangle(self):
        pass

    def is_rectangle(self):
        if have_params["a1"] == 90 or have_params["a2"] == 90 or have_params["a3"] == 90:
            return True
        else:
            return False


get_pars()
check_pars()
figure = Triangle()
figure.abt()
reset()
figure.abt()
