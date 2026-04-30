import json
import ast

filename = "saved_expense.txt"

def saveFile(inputExp,filename):
    with open(filename,"w") as f:
        f.write(inputExp)
def loadFile(filename):
    with open(filename,"r") as f:
        return f.read()
    
try:
    Saved = loadFile(filename)
    expList = ast.literal_eval(Saved)
    print("Saved current expenses")
except :
    expList = []

def addExp():
    addedExp = {}
    choices=['food','Entertainment','Rent']
    while True :
        amount = input("Please input the amount for the expense: ")
        if int(amount) > 0:
            addedExp['amounts']= amount
            while True:
                category = input('Please choose your expense category:\n1.Food\n2.Entertainment\n3.Rent\n')
                if int(category) > 0 and int(category) <= 3:
                    addedExp['category'] = choices[int(category)-1]
                    break
                print('Please choose a valid number')
            description = input("Provide a short description of your expense: ")
            addedExp['description']= description
            print(f"Your expense is {addedExp['category']} : {addedExp['amounts']}\n notes: {addedExp['description']}")
            expList.append(addedExp)
            saveFile(str(expList),filename)
            break

def trackExp():
    try:
        save_file = loadFile(filename)
        global expList 
        expList = ast.literal_eval(save_file)
        for items in expList:
            print(f"{items['category']}:\namount :{items['amounts']}\n{items['description']}\n")
    except:
        print("could not find any saved file")
    

def main(): 
    while True:
        choices = input("1.Add expense\n2.Track expense\n")
        if int(choices) == 1:
            addExp()
        elif int(choices) == 2:
            trackExp()
main()