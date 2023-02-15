import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Get your ass up, its time for a workout!')

t = input('Enter the amount of time that will be countdown in seconds: ')

countdown(int(t))