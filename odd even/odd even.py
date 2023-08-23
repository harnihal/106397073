while True:
    x=int(input('What number is on your mind?: '))

    if x%2 == 0:
        print('This number is even')
    else:
        print('This number is odd')

    answer = input("Do you have another number?(y/n): ")
    answer = answer.lower()
    if answer == "y":
        continue
    elif answer == "n":
        print("Thanks for using Odd or Even checker!!")
        break
