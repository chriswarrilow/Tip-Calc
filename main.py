print('Welcome to the tip calculator')
totalCost = float(input('What was to cost of the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12 or 15 '))
split= int(input('How many total people split the bill? '))


percentTotal = tip / 100 * totalCost + totalCost
tipSplit = round(percentTotal / split, 2)
#total = round(tipSplit, 4)


print(f'Each person should pay: ${tipSplit}')
