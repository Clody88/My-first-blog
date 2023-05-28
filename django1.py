print("hello, djoango girls")
if 2>3:
    print("it works")
if 3 > 2:
    print("ok")
if 5 > 2:
    print("5 is greater than 2")
else:
    print("5 is not greater")

name = "clo"
if name == "clo":
    print("hello clo")
elif name == "bob":
    print("hello bob")
else:
    print("hello ??")

volume = 50
if volume < 20:
    print("it's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <- volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

# FUNCTIONS
def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi(name)

#LOOPS
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

def hi(name):
    print("hi " + name + "!")


for name in girls:
    hi(name)
    print("Next girl")

for i in range (1,6):
    print(i)

