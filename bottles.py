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

def bottle_song():
	for i in range(99, -1, -1):
		if i > 9:
			print (f"{i} bottles of beer on the wall, {i} bottles of beer. Take one down and pass it around, {i} bottles of beer on the wall.")
		elif i <= 9 and i > 0:
			print (f"{i} bottle of beer on the wall, {i} bottle of beer. Take one down and pass it around, {i} bottle of beer on the wall.")
		elif i == 0: 
			print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall!")

bottle_song()

####kldjsfalkfdajalskdfjdfls