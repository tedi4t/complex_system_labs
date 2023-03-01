import time
import matrix_operations
import utils

class V1Calculations:
	def __init__(self, input) -> None:
		self.MM = input["MM"]
		self.MT = input["MT"]
		self.MZ = input["MZ"]
		self.B = input["B"]
		self.E = input["E"]

	def calculateFunc1(self):
		temp1 = matrix_operations.addMatrixes(self.MM, self.MZ)
		temp2 = matrix_operations.vectorMultiplyMatrix(self.B, temp1)
		temp3 = matrix_operations.vectorMultiplyMatrix(self.E, self.MM)

		return matrix_operations.addVectors(temp2, temp3)

	def calculateFunc2(self):
		temp1 = max(matrix_operations.subtractVectors(self.B, self.E))
		temp2 = matrix_operations.multiplyMatrixes(self.MM, self.MT)
		temp3 = matrix_operations.scalarMultiplyMatrix(temp1, temp2)

		temp4 = matrix_operations.addMatrixes(self.MT, self.MM)
		temp5 = matrix_operations.multiplyMatrixes(self.MZ, temp4)

		return matrix_operations.subtractMatrixes(temp3, temp5)

	def calculateAndTrackTime(self, outputFile, f, prefix, timeTrackings, i):
		start = time.time()
		result = f()
		end = time.time()

		utils.printMessage(outputFile, prefix, result)
		timeTrackings[i] = end - start