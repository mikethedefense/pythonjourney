name = 'Zack'
second_half = ('N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
if any(name.startswith(letter) for letter in second_half):
    print(name,'belongs in the second half of the alphabet')
else:
    print(name,'does not belong in the second half of the alphabet')
