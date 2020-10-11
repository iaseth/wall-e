import math
import time



class Nanoseconds():
	def __init__(self, nanoseconds):
		self.seconds = math.floor(nanoseconds / 1e9)
		nanoseconds = nanoseconds % 1e9
		self.ms = math.floor(nanoseconds / 1e6)
		nanoseconds = nanoseconds % 1e6
		self.us = math.floor(nanoseconds / 1e3)
		nanoseconds = nanoseconds % 1e3
		self.ns = math.floor(nanoseconds % 1000)
		pass

	def __str__(self):
		return f"[{self.seconds:3}s|{self.ms:3}ms|{self.us:3}us|{self.ns:3}ns]".replace("|", " ")
		pass


class Event():
	def __init__(self, benchmark, name):
		self.end_time = time.monotonic_ns()
		self.start_time = benchmark.last_time
		self.benchmark = benchmark
		self.name = name
		self.index = len(self.benchmark.events)
		pass

	def print(self):
		ns = Nanoseconds(self.end_time - self.start_time)
		print(f"\t---> {self.index + 1:3}. {self.benchmark} took {ns} for {self.name}.")
		pass


class Benchmark():
	def __init__(self, name):
		self.name = name
		self.reset()

	def reset(self):
		self.init_time = time.monotonic_ns()
		self.last_time = self.init_time
		self.events = []

	def get_nanoseconds(self):
		return (self.last_time - self.init_time)

	def record_event(self, name):
		event = Event(self, name)
		self.last_time = event.end_time
		self.events.append(event)
		pass

	def print_events(self):
		ns = Nanoseconds(self.get_nanoseconds())
		print(f"Benchmark {self} took {ns}.")
		for event in self.events:
			event.print()
		pass

	def __str__(self):
		return f"[{self.name}]"
		pass


