import converters.AmericanMesurementSystem as american
import converters.BritishMesurementSystem as british


#Us-Brit-Converter
def main():
    try:
        decksize = float( input("What is the total square meters value of the desired deck you want to build?\n") )
    except ValueError:
        print("Motherfucka, you gave me a string. Bye! killing myself!")
        exit(1)
    # except Exception as err:
    #     print(f"We got an '{err}' error.")
    else: 
        print("Nice. You gave me a number. I can continue working...")

    # Make sure user gives us wghat we want, not a string - start



    # Make sure user gives us wghat we want, not a string - end

    # print(type(american.area(None,'yard')))
    # print(type(decksize))

    # usresult = decksize * americanSystem.yard
    usresult = decksize * american.area(None,'yard')

    # britresult = decksize * britSystem.squarefoot  
    # britresult = decksize * british.area(None, "yard")
    britresult = decksize * british.area(type="squarefoot")


    print(f"According to United States mesurement system your deck will be {usresult} yards\n According to the Great Britain mesurement system your deck will be {britresult} yards")


if __name__ == "__main__":
    main()
    