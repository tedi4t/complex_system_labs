import time
import matrix_operations
import utils
from concurrent.futures import ThreadPoolExecutor, Future

class Calculations:
	def __init__(self, input) -> None:
		self.MM = input["MM"]
		self.MT = input["MT"]
		self.MZ = input["MZ"]
		self.B = input["B"]
		self.E = input["E"]

		self.f1Temp1 = [[[0 for j in range(len(self.MM))] for i in range(len(self.MM))]]
		self.f1Temp2 = [[0 for i in range(len(self.E))]]

		self.f2Temp1 = [[0 for i in range(len(self.E))]]
		self.f2Temp2 = [[[0 for j in range(len(self.MM))] for i in range(len(self.MM))]]
		self.f2Temp3 = [[[0 for j in range(len(self.MM))] for i in range(len(self.MM))]]

	def saveToClosure(self, f, resultValue, *args):
		resultValue[0] = f(*args)

	def calculateFunc1(self):
		with ThreadPoolExecutor(max_workers=2) as executor:
			f1 = executor.submit(self.saveToClosure, matrix_operations.addMatrixes, self.f1Temp1, self.MM, self.MZ)
			f2 = executor.submit(self.saveToClosure, matrix_operations.vectorMultiplyMatrix, self.f1Temp2, self.E, self.MM)

			f1.result()
			f2.result()
			executor.shutdown()
		
		return matrix_operations.addVectors(matrix_operations.vectorMultiplyMatrix(self.B, self.f1Temp1[0]), self.f1Temp2[0])

	def calculateFunc2(self):
		with ThreadPoolExecutor(max_workers=3) as executor:
			f1 = executor.submit(self.saveToClosure, matrix_operations.subtractVectors, self.f2Temp1, self.B, self.E)
			f2 = executor.submit(self.saveToClosure, matrix_operations.multiplyMatrixes, self.f2Temp2, self.MM, self.MT)
			f3 = executor.submit(self.saveToClosure, matrix_operations.addMatrixes, self.f2Temp3, self.MT, self.MM)

			f1.result()
			f2.result()
			f3.result()
			executor.shutdown()

		temp1 = matrix_operations.scalarMultiplyMatrix(max(self.f2Temp1[0]), self.f2Temp2[0])
		temp2 = matrix_operations.multiplyMatrixes(self.MZ, self.f2Temp3[0])

		return matrix_operations.subtractMatrixes(temp1, temp2)

	def calculateAndTrackTime(self, outputFile, f, prefix, timeTrackings, i):
		start = time.time()
		result = f()
		end = time.time()

		utils.printMessage(outputFile, prefix, result)
		timeTrackings[i] = end - start