def length(value_to_convert: float=None, type: str='foot'):
    britinch = 2.54  #cm
    foot = 30.48 #cm
    mile = 1.609 #km

    if value_to_convert:
        return eval(type) * value_to_convert
    else:
        return eval(type)

def volume(value_to_convert: float=None, type: str='fluidOunce'):
    fluidOunce = 28.4 #ml
    pint = 0.568 #l
    britgallon = 4.546 #l

    if value_to_convert:
        return eval(type) * value_to_convert
    else:
        return eval(type)


def area(value_to_convert: float=None, type: str='squarefoot'):
    squarefoot = 0.0929 #sq.m.
    rood = 1.011 #sq.m.
    acre = 4046 #sq.m.
    
    if value_to_convert:
        return eval(type) * value_to_convert
    else:
        return eval(type)


def weight(value_to_convert: float=None, type: str='pound') -> float:
    ounce: float = 28.349 #grams
    pound = 0.453 #kg
    stone = 6.350 #kg

    if value_to_convert:
        return eval(type) * value_to_convert
    else:
        return eval(type)

if __name__ == "__main__":
    print(f"{area(type='squarefoot',value_to_convert=8.53)=}")
    #                    ||
    print(f"area(type='squarefoot',value_to_convert=8.53)={area(type='squarefoot',value_to_convert=8.53)}")

    print(f"I am {'Gosho'}")


