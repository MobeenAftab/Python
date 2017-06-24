
import re

print("Calculator")
print("Type your equations below or \'q\' to exit\n")

previous = 0
run = True

def calculator():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter equations: ")
    else:
        equation = input(str(previous))

    if equation == "q":
        print("Goodbye !")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print("Result: ", previous)

while run:
    calculator()
