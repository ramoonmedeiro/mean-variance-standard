# coded by Ramon Medeiro. Please use this content only to knowledge. Try to do this project yourself.
# FREECODECAMP project 1.

import mean_var_std

lista = [0,1,2,3,4,5,6,7,8]

try:
	print(mean_var_std.calculate(lista))
except ValueError:
	print('List must contain nine numbers.')
