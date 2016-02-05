# We'll use the 4 game as our example
class ExampleGame:
	initial_position = 4
	def primitive(pos):
		return solver.LOSE if pos == 0 else solver.OTHER
	def gen_moves(pos):
		return [-1] if pos == 1 else [-1, -2]
	def do_moves(pos, move):
		return pos + move