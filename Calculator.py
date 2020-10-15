import math

def calculate(operation, a, b):
    a = int(a)
    b = int(b)

    if operation == '+':
        return a + b
    elif operation == '/':
        return a / b
    elif operation == 'x':
        return a * b
    elif operation == '-':
        return a - b
    else:
        return "Operator is incorrect you FOOL"


def readFileToList (filepath):
    with open (filepath, "r") as in_file:
        text_list = in_file.read().splitlines()

    return text_list


# def gotoAction(instrNum):
#     # record the 


# Step 2
# list_of_calcs = readFileToList("C:\\Users\\obaya\\DEV\\Corndel-Dev-Ops\\Workshop\\Workshop1\\CalculatorInput.txt")

# for calc in list_of_calcs:
#     split_cal = calc.split()
#     print (calculate(split_cal[1], split_cal[2],split_cal[3]))



# Step 3
# Navigate the document - there are 10k lines in this list
list_of_goto = readFileToList("C:\\Users\\obaya\\DEV\\Corndel-Dev-Ops\\Workshop\\Workshop1\\GotoInput.txt")

visitedInstr = []

currentInstr = list_of_goto[0]
currentInstrNum = currentInstr.split()[1] # change to be less hardcoded for specific input
# goto 9667
# goto calc / 9946 80

while not currentInstr in visitedInstr:
    next_instr = list_of_goto[int(currentInstrNum) -1] # -1 as index starts at 0, put file starts at 1
    next_instr_split = next_instr.split() 
    if len(next_instr_split) == 5:
        nextInstrNum = math.floor (calculate(next_instr_split[2],next_instr_split[3],next_instr_split[4]))       # calculate(*split_instr[1:])
        visitedInstr.append(currentInstr)
        currentInstrNum = nextInstrNum
        currentInstr = next_instr

    elif len(next_instr_split) == 2:
        nextInstrNum = next_instr_split[1] 
        visitedInstr.append(currentInstr)
        currentInstr = next_instr
        currentInstrNum = nextInstrNum
    else:
        print("Corrupted Instructions mate")

print(visitedInstr[-1])

