from threading import Thread
import time
import matrix_operations
import utils

class V2Calculations:
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
		thread1 = Thread(target=self.saveToClosure, args=[matrix_operations.addMatrixes, self.f1Temp1, self.MM, self.MZ])
		thread2 = Thread(target=self.saveToClosure, args=[matrix_operations.vectorMultiplyMatrix, self.f1Temp2, self.E, self.MM])

		threads = [thread1, thread2]

		for thread in threads:
		  thread.start()
    
		for thread in threads:
		  thread.join()
		
		return matrix_operations.addVectors(matrix_operations.vectorMultiplyMatrix(self.B, self.f1Temp1[0]), self.f1Temp2[0])

	def calculateFunc2(self):
		thread1 = Thread(target=self.saveToClosure, args=[matrix_operations.subtractVectors, self.f2Temp1, self.B, self.E])
		thread2 = Thread(target=self.saveToClosure, args=[matrix_operations.multiplyMatrixes, self.f2Temp2, self.MM, self.MT])
		thread3 = Thread(target=self.saveToClosure, args=[matrix_operations.addMatrixes, self.f2Temp3, self.MT, self.MM])

		threads = [thread1, thread2, thread3]

		for thread in threads:
		  thread.start()
    
		for thread in threads:
		  thread.join()

		temp1 = matrix_operations.scalarMultiplyMatrix(max(self.f2Temp1[0]), self.f2Temp2[0])
		temp2 = matrix_operations.multiplyMatrixes(self.MZ, self.f2Temp3[0])

		return matrix_operations.subtractMatrixes(temp1, temp2)

	def calculateAndTrackTime(self, outputFile, f, prefix, timeTrackings, i):
		start = time.time()
		result = f()
		end = time.time()

		utils.printMessage(outputFile, prefix, result)
		timeTrackings[i] = end - start