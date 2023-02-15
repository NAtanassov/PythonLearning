# import nicky
from nicky import workout_plan_func

def main():
    print("Print in nicky2.py")
    print(f"In nicky2.py, {__name__=}")

    # nicky.workout_plan_func()  # if using "import nicky"
    workout_plan_func()


if __name__ == "__main__":
    main()
