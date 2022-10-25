x=int(input('число: '))
guess=x/2
while x-guess**2>10**-12:
    y=x/guess
    guess=y/2
print(guess)