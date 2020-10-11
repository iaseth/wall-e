import time



class Event():
	def __init__(self, benchmark, name):
		self.end_time = time.monotonic_ns()
		self.start_time = benchmark.last_time
		self.benchmark = benchmark
		self.name = name
		pass

	def print(self):
		microseconds = (self.end_time - self.start_time) / 1e6
		print(f"{self.name} took {microseconds}us.")
		pass


class Benchmark():
	def __init__(self, name):
		self.name = name
		self.init_time = time.monotonic_ns()
		self.last_time = self.init_time
		self.events = []

	def record_event(self, name):
		event = Event(self, name)
		self.last_time = event.end_time
		self.events.append(event)
		pass

	def print_events(self):
		for event in self.events:
			event.print()
		pass


