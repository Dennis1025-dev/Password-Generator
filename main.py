import random
import string

def password(length,num=False,strength=False):
    lower=string.ascii_lowercase   #for lowercase letters
    upper=string.ascii_uppercase   #for uppercase letters
    letters=upper+lower            #for combination of both uppercase and lowercase letters
    digits=string.digits           #for numbers
    symbols=string.punctuation     #for symbols such as . and,
    pwd=''                         #to hold the password

    if strength=='weak':     #for weak passwords it should cointain ony small case letters
        if num:
            length-=2
            for i in range(2):
                pwd+=random.choice(digits)
        for i in range(length):
            pwd+=random.choice(lower)
    elif strength=='strong':
        if num:
            length=int(length/2)
            for i in range(length):
                pwd+=random.choice(digits)
        for i in range(length):
            pwd+=random.choice(letters)
    elif strength=='very':
        ran=random.randint(2,4)
        if num:
            length-=ran
            for i in range(ran):
                pwd+=random.choice(dig)
        length-=ran
        for i in range(ran):
            pwd+=random.choice(symbols)
        for i in range(length):
            pwd+=random.choice(letters)
    pwd=list(pwd)
    random.shuffle(pwd)
    return ''.join(pwd)


user_strength=input("""What type of password would you like
1.Weak -> reply by weak
2.Strong -> reply by strong
3.Very -> strong reply by very
:""")

user_has_number=int(input("""Would you like to include numbers
repky with the number
1.Yes
2.No
:"""))
if user_has_number ==1:
    user_has_number=True
else:
    user_has_number=False

user_characters=int(input("How many characters would you like to have:"))

print(password(user_characters,num=user_has_number,strength=user_strength))




            



