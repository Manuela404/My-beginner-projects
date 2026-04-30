import random

def nameGenerator():
    first_name=["SnackAttack","CoffeeAddict101","LazyLegend","AlwaysHungry","PositiveVibesOnly","johnson","DailyLOL","TheFunSide","LaughFactory","MoodBooster,"]
    last_name=["Tom","Ribeiro","Jinx","Jonson","Smith","Johnson","Anderson","Clark","Garcia","Martinez"]
    lengthFirst=len(first_name)
    lengthLast=len(last_name)
    randomFirst=random.randint(0,lengthFirst-1)
    randomLast=random.randint(0,lengthLast-1)
    print(f"Your name is {first_name[randomFirst]} {last_name[randomLast]}")

def main():
    while True:
        print("Welcome to random name generator")
        nameGenerator()
        tryAgain = input("Do you want to generate a new name? (n/y)")
        if tryAgain.lower()=="n":
            print("See you again soldier!!")
            break
main()