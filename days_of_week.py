this1 = "Az sum pich"
this1same = ['A', 'z', ' ', 's', 'u', 'm', ' ', 'p', 'i', 'c', 'h']

# --- if statements ---
# if( predicate ):
#   body
# else:
#   else body

# if( predicate ):
#   body
# elif(another predicate):
#   body
# else:
#   else body

print("Doing the check...")
if (this1 == ''.join(this1same)):  # Check if they are equal
    print(f"'{this1}' is equal to '{this1same}' (joined)")  # fstring = formatted string

# Речник = Именован списък от елементи = Dictionary
# String = Масив от character елементи
weekdays_dict = {
    "Monday": ["Abs"],
    "Tuesday": ["Arms"],
    "Wednesday": ["Cardio with the woman"],
    "Thursday": ["Back"],
    "Friday": ["Shoulders"],  # String -> weekdays_dict["Friday"] -> string(shoulders)
    "Saturday": ["Legs", "Abs"],  # Type Array -> weekdays_dict["Saturday"] -> array([legs])
    "Sunday": ["Techno!"]
}


# List of days of the week 
# Масив = Списък от елементи = Array 
# Arrays have a set order! - defined by the item index
weekdays1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weekdays1.append("Sunday")

weekdays = list()
for day in weekdays1:
    weekdays.append(day)
    print(f"Adding element {day} to weekdays. {weekdays=}")

if(weekdays1 == weekdays):
    print("Both new arrays are equal!")

print(f"weekdays={weekdays}")
# this above and this below are equal/provide same result
print(f"{weekdays=}")


# empty array/list
list() == []
#list() - this is used for an EMPTY array!
# [] - this way you can declare an array which is already filled  
# while could be used without any brackets after the word itself


# --- Loops / Цикли ---

# For loop
for day in weekdays:
    print(f"Today is {day}")
   
print(f"There are {len(weekdays)} days in the weekdays list.")

# While loop
day_index = 0
while(day_index < len(weekdays)):
    day = f"{day_index+1}"

    if(day==1):
        day += "st"
    elif(day==2):
        day += "nd"
    elif(day==3):
        day += "rd"
    else:
        day += "th"

    print(f"Day of week: {weekdays[day_index]} is {day} day of week.")

    # Increment day value
    day_index += 1  # day += 1 is same as: day = day + 1 ; day++ is not working in Python
