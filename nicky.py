
def workout_plan_func():
    workout_plan = {
        "chest":["Bench Press", "Dumbel Flies","Dips"],
        "legs" :["Squat", "Leg extensions", "Leg press"],
        "hands":["Biceps Curl", "Triceps Pull Down", "BicepsTriceps Barbell"],
        "back" :["Pull ups", "Dead lift", "Barbell lat pull down"],
        "abdominals"  :["Mount Climbers", "Crunches", "Leg raises"]
    }

    while(True):
        input_str: str = input("Give a body workout \n")
        # input_int: int 

        # if   (input_digit==1):     # can this be used ? if (weekdays[day_index]==1)
        #     print(workout_plan["chest"])
        # elif (input_digit==2):
        #     print(workout_plan["abdominals"])
        # elif (input_digit==3):
        #     print(workout_plan["legs"])
        # elif (input_digit==4):
        #     print(workout_plan["abdominals"])
        # elif (input_digit==5):
        #     print(workout_plan["back"])
        # elif (input_digit==6):
        #     print(workout_plan["hands"])
        # elif (input_digit==7):
        #     print("Chill Dude its your day off")
        # elif (input_digit==0):
        #     print("Enjoy your workout!")
        #     break
        # else:
        #     print("There isn't such a day in the week dude, try again")
        

        print(workout_plan.get(input_str, "No such body part in our database... :("))

        print("")


def my_name(name: str, age: int):
    print(f"My name is: {name}")
    print(f"I am {age} yrs old.")


def main():
    print("Outside of function! In nicky.py")

    print(f"in nicky.py, {__name__=}")

    my_name("Nikola Atanasov", 25)
    my_name("Orlin Dimitrov", 30)
    my_name("Kichka Bodurova", 999)

    workout_plan_func()


if __name__ == "__main__":
    main()
