
from pywall.benchmark import Benchmark

benchmark = Benchmark("example")

max_x = 1000
max_y = 1000
max_z = 100

number = 1
for x in range(0, max_x):
	for y in range(0, max_y):
		for z in range(0, max_z):
			number += 1
			pass

benchmark.record_event("done loop")
#benchmark.print_events()

ns = benchmark.get_nanoseconds()
ops = max_x * max_y * max_z
ops_per_sec = ops * 1e9 / ns
print(f"We are doing: {ops_per_sec} ops/sec.")

