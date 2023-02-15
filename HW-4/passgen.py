import random

password_symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
password_amount = int(input('Insert the amount of passwords \
 you want to generate: '))
password_length = int(input('Insert the length of the password you desire(number of symbols): '))

test_str = """
    dasasd
    dasdas
    asd
"""

test_str2 = 

print('\nYou can find your generated passwords below:')

for pwd in range(password_amount):
    passwords = ''
    for c in range(password_length):
        passwords += random.choice(password_symbols)
    print(passwords)

