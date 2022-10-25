x=int(input('число: '))
guess=x/2
while abs(x-guess**2)>10**-12:
    guess=(guess+x/guess)/2
print(guess)