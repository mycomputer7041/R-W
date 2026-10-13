import datetime
import filemodule
import math
import random
import time
import uuid


def showtime():
    """Print current time."""
    now = datetime.datetime.now()
    print(now)


def datediff():
    """Calculate difference between two dates."""
    print("Enter first date YYYY-MM-DD")
    dateone = input()
    print("Enter second date YYYY-MM-DD")
    datetwo = input()
    done = datetime.datetime.strptime(dateone, "%Y-%m-%d")
    dtwo = datetime.datetime.strptime(datetwo, "%Y-%m-%d")
    diff = dtwo - done
    print("Days difference is")
    print(diff.days)


def customformat():
    """Format current date."""
    now = datetime.datetime.now()
    result = now.strftime("%d %B %Y")
    print(result)


def runstopwatch():
    """Run a simple stopwatch."""
    print("Press enter to start")
    input()
    start = time.time()
    print("Press enter to stop")
    input()
    end = time.time()
    diff = end - start
    print("Seconds passed")
    print(diff)


def runcountdown():
    """Run a countdown timer."""
    print("Enter seconds")
    secs = int(input())
    while secs > 0:
        print(secs)
        time.sleep(1)
        secs = secs - 1
    print("Done")


def calcfactorial():
    """Calculate factorial."""
    print("Enter number")
    number = int(input())
    result = math.factorial(number)
    print(result)


def calctrig():
    """Calculate sine value."""
    print("Enter angle")
    angle = float(input())
    result = math.sin(angle)
    print(result)


def calcinterest():
    """Calculate compound interest."""
    print("Enter principal")
    prin = float(input())
    print("Enter rate")
    rate = float(input())
    print("Enter years")
    year = float(input())
    amount = prin * (math.pow((1 + rate / 100), year))
    print(amount)


def calcarea():
    """Calculate circle area."""
    print("Enter radius")
    radius = float(input())
    area = math.pi * radius * radius
    print(area)


def randnum():
    """Generate random number."""
    result = random.randint(1, 100)
    print(result)


def randlist():
    """Sample items from list."""
    things = ["cricket", "minecraft", "burger", "watch", "laptop"]
    result = random.sample(things, 2)
    print(result)


def randpass():
    """Generate random password."""
    print("Enter length")
    size = int(input())
    letters = "qwertyuiop1234567890asdfghjkl"
    word = ""
    for index in range(size):
        word = word + random.choice(letters)
    print(word)


def randotp():
    """Generate random OTP."""
    result = random.randint(1000, 9999)
    print(result)


def genuuid():
    """Generate unique identifier."""
    unique = uuid.uuid4()
    print(unique)


def exploremod():
    """Explore module attributes."""
    print("Enter module name like math or random")
    name = input()
    if name == "math":
        print(dir(math))
    elif name == "random":
        print(dir(random))
    elif name == "time":
        print(dir(time))


def printdocs():
    """Print all docstrings."""
    print(showtime.__doc__)
    print(datediff.__doc__)
    print(customformat.__doc__)
    print(runstopwatch.__doc__)
    print(runcountdown.__doc__)
    print(calcfactorial.__doc__)
    print(calctrig.__doc__)
    print(calcinterest.__doc__)
    print(calcarea.__doc__)
    print(randnum.__doc__)
    print(randlist.__doc__)
    print(randpass.__doc__)
    print(randotp.__doc__)
    print(genuuid.__doc__)
    print(exploremod.__doc__)
    print(filemodule.makefile.__doc__)
    print(filemodule.writefile.__doc__)
    print(filemodule.readfile.__doc__)
    print(printdocs.__doc__)
    print(main.__doc__)


def main():
    """Run the main menu."""
    loop = True
    while loop:
        print("\nMenu")
        print("1 Datetime")
        print("2 Math")
        print("3 Random")
        print("4 UUID")
        print("5 File")
        print("6 Explore")
        print("7 Exit")
        print("Enter choice")
        choice = input()

        if choice == "1":
            print("1 Time")
            print("2 Diff")
            print("3 Format")
            print("4 Stopwatch")
            print("5 Countdown")
            print("Enter option")
            option = input()
            if option == "1":
                showtime()
            elif option == "2":
                datediff()
            elif option == "3":
                customformat()
            elif option == "4":
                runstopwatch()
            elif option == "5":
                runcountdown()

        elif choice == "2":
            print("1 Factorial")
            print("2 Interest")
            print("3 Area")
            print("4 Trig")
            print("Enter option")
            option = input()
            if option == "1":
                calcfactorial()
            elif option == "2":
                calcinterest()
            elif option == "3":
                calcarea()
            elif option == "4":
                calctrig()

        elif choice == "3":
            print("1 Number")
            print("2 Password")
            print("3 OTP")
            print("4 List")
            print("Enter option")
            option = input()
            if option == "1":
                randnum()
            elif option == "2":
                randpass()
            elif option == "3":
                randotp()
            elif option == "4":
                randlist()

        elif choice == "4":
            genuuid()

        elif choice == "5":
            print("1 Make")
            print("2 Write")
            print("3 Read")
            print("Enter option")
            option = input()
            if option == "1":
                filemodule.makefile()
            elif option == "2":
                filemodule.writefile()
            elif option == "3":
                filemodule.readfile()

        elif choice == "6":
            exploremod()

        elif choice == "7":
            print("Goodbye")
            printdocs()
            loop = False

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()