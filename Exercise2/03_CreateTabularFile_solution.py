import io
import os
import random
import time
from os.path import expanduser


finished = False
filepath = "tabularFile.txt"
print("filepath: " + filepath)
numCols = 10

# write file with n columns (random ints) of specific file size
start = time.time()
with open(filepath, 'w') as file:
	while not finished:
		size = os.path.getsize(filepath)
		if(size >= 10000000):
			finished = True
		else:
			randomNumbers = [];
			for i in range(numCols):
				x = random.randint(1,1000000)
				file.write(str(x))
				if i < 9:
					file.write(", ")
			file.write("\n")
end = time.time()
print("Time to create file took ", (end-start), " seconds")
