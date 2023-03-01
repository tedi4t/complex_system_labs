from threading import Thread
import matplotlib.pyplot as plt
import v1_calculations
import v2_calculations
import utils
from constantas import min_matrix_size, max_matrix_size, output_file_path

size = max_matrix_size - min_matrix_size
f1TimeTrackings = [0 for i in range(size)]
f2TimeTrackings = [0 for i in range(size)]

utils.createInput()
input = utils.getInput()

Calculations = v1_calculations.V1Calculations

for i in range(size):
	calculations = Calculations(input[i])

	thread1 = Thread(target=calculations.calculateAndTrackTime, args=[output_file_path, calculations.calculateFunc1, f"Function 1 Iteration {i}", f1TimeTrackings, i])
	thread2 = Thread(target=calculations.calculateAndTrackTime, args=[output_file_path, calculations.calculateFunc2, f"Function 2 Iteration {i}", f2TimeTrackings, i])

	thread1.start()
	thread2.start()
	
	thread1.join()
	thread2.join()

fig, ax = plt.subplots()
xAxisTitles = [i for i in range(min_matrix_size, max_matrix_size)]

ax.plot(xAxisTitles, f1TimeTrackings)
ax.plot(xAxisTitles, f2TimeTrackings)

plt.show()

