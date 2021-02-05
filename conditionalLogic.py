# Python conditional logic
# if, elif (else if), and else

age = int(input('How old are you? '))

if age < 1 or age > 100:
    # This content will run
    print('Incorrect age. Please choose one that\'s honest!')
    # White space matters; everything indented will run under this condition
elif age >= 0 and age < 20:
    print('You are still young! Congrats.')
elif age < 42:
    print('You are not yet middle aged.')
else: # All other ages (above 42)
    print('Ya, you old...')

if age < 19 and age > 5:
    print('You are still in grade school, ya?')