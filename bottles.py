"""
- take note of how bottles changes to bottle when single digits
- use for loop first, then try to make simpler/prettier
"""
"""""
- need to start at 99
- print each iteration with one less
- use for i in range(start, stop, step)
- use string interpolation : f"{ i } bottles of beer on the wall, { i } bottles of beer. Take one down and pass it around, { i } bottles of beer on the wall."

"""""


# add 'bottles for count to star at - also change the start point of the range() method
def bottle_song(bottles):
	#print(bottles)
	if bottles < 0:
		print("We have no bottles of beer on the wall! Let's go to the store and buy some more!")
	else:
		for i in range(bottles, -1, -1):
			if i > 9:
				print (f"{i} bottles of beer on the wall, {i} bottles of beer. Take one down and pass it around, {i} bottles of beer on the wall.")
			elif i <= 9 and i > 0:
				print (f"{i} bottle of beer on the wall, {i} bottle of beer. Take one down and pass it around, {i} bottle of beer on the wall.")
			elif i == 0: 
				print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall!")

# negative number issue - at first isn't running the first line of code
# -> initially put if check of bottles < 0 inside of the for loop -> so for loop wasn't running because -5 was lower than the stop step of (-1)
bottle_song(-5)
bottle_song(21)
bottle_song(121)