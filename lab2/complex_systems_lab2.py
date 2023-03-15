import matplotlib.pyplot as plt
import calculations
import utils
import random
from constantas import min_matrix_size, max_matrix_size, output_file_path
from concurrent.futures import ThreadPoolExecutor, Future

size = max_matrix_size - min_matrix_size
f1TimeTrackings = [0 for i in range(size)]
f2TimeTrackings = [0 for i in range(size)]

utils.createInput()
input = utils.getInput()

for i in range(size):
	calculationsClass = calculations.Calculations(input[i])

	with ThreadPoolExecutor(max_workers=2) as executor:
		f1 = executor.submit(calculationsClass.calculateAndTrackTime, output_file_path, calculationsClass.calculateFunc1, f"Function 1 Iteration {i}", f1TimeTrackings, i)
		f2 = executor.submit(calculationsClass.calculateAndTrackTime, output_file_path, calculationsClass.calculateFunc2, f"Function 2 Iteration {i}", f2TimeTrackings, i)

		f1.result()
		f2.result()
		executor.shutdown()

fig, ax = plt.subplots()
xAxisTitles = [i for i in range(min_matrix_size, max_matrix_size)]

ax.plot(xAxisTitles, f1TimeTrackings)
ax.plot(xAxisTitles, f2TimeTrackings)

plt.show()

