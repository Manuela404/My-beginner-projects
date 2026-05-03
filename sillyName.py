import random

def nameGenerator():
    first_name=["SnackAttack","CoffeeAddict101","LazyLegend","AlwaysHungry","PositiveVibesOnly","johnson","DailyLOL","TheFunSide","LaughFactory","MoodBooster,"]
    last_name=["Tom","Ribeiro","Jinx","Jonson","Smith","Johnson","Anderson","Clark","Garcia","Martinez"]
    randomFirst=random.choice(first_name)
    randomLast=random.choice(last_name)
    print(f"Your name is {randomFirst} {randomLast}")

def main():
    while True:
        print("Welcome to random name generator")
        nameGenerator()
        tryAgain = input("Do you want to generate a new name? (n/y)")
        if tryAgain.lower()=="n":
            print("See you again soldier!!")
            break
if __name__ == '__main__':
    main()