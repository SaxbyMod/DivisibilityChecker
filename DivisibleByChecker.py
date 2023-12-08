import random
import math

Name = input("Whats your name?: ")
y = 1
x = 1
for _ in iter(int, 1):
	InputtedInt = int(input(Name + " What int would you like to input as the first int?: "))
	InputtedInt2 = int(input(Name + " What int would you like to input as the second int?: "))

	if InputtedInt % InputtedInt2 == 0:
		OutputtedInt = InputtedInt // InputtedInt2
		print(OutputtedInt)
		print(str(InputtedInt) + " Is divisible by " + str(InputtedInt2))
	else:
		OutputtedInt = float(float(InputtedInt) / float(InputtedInt2))
		print(OutputtedInt)
		print(str(InputtedInt) + " Is NOT divisible by " + str(InputtedInt2))
