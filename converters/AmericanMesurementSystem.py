

def length(value_to_convert: float=None, type: str='furlong') -> float:
    chains = 2011.68  #cm
    furlong = 20116.8  #cm
    yard = 91.44  #cm

    if value_to_convert:
        return eval(type) * value_to_convert
    else:
        return eval(type)  #How this works; evaluates a string to an object in the current scope


def volume(value_to_convert: float=None, type: str='cubyard') -> float:
    cubfoot = 28.3168 #l
    cubyard = 764.55 #l

    if value_to_convert:  # value_to_convert != None
    # None/0 -> False
    # Not-None -> True
        return eval(type) * value_to_convert
    else:
        return eval(type)


def area(value_to_convert: float=None, type: str='yard') -> float:
    yard = 0.836 #sq.m.
    acre = 4046.85 #sq.m.

    if value_to_convert:
        return eval(type) * value_to_convert
    else:
        return eval(type) 


def weight(value_to_convert: float=None, type: str='ounce'):
    ounce = 28.349 #grams
    pound = 0.453 #kg

    if value_to_convert:
        return eval(type) * value_to_convert
    else:
        return eval(type)


if __name__ == "__main__":
    print(f"{weight(2.55,'pound')=}")
