import random
from multiprocessing import Lock
import json

from constantas import rand_number_multiplier, min_matrix_size, max_matrix_size, input_file_path

lock = Lock()

def genRandMatrix(size):
	return [[random.random() * rand_number_multiplier for e in range(size)] for e in range(size)]

def genRandVector(size):
	return [random.random() * rand_number_multiplier for e in range(size)]

def createInput():
	matrix_size_list = range(min_matrix_size, max_matrix_size)

	result = []

	for i in range(len(matrix_size_list)):
		size = matrix_size_list[i]
		obj = { 
			"MM": genRandMatrix(size),
			"MT": genRandMatrix(size), 
			"MZ": genRandMatrix(size), 
			"B": genRandVector(size), 
			"E": genRandVector(size),
		}

		result.append(obj)

		with open(input_file_path, "w") as outfile:
			resultStr = json.dumps(result)
			outfile.write(resultStr)

def getInput():
	with open(input_file_path, "r") as outfile:
		result = json.load(outfile)

	return result

def printMessage(path, prefix, value):
	lock.acquire()

	with open(path, "a") as outfile:
		result = json.dumps(value)
		outfile.write(f"{prefix}: {result}\n")
		outfile.close()

	print(f"{prefix}: {result}\n\n")
	lock.release()

