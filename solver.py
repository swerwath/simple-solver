from collections import deque

class Solver:
	WIN = 1
	LOSS = -1
	OTHER = 0
	known_states = {}
	@staticmethod
	def solve():
		root = GameTree(ExampleGame.initial_position)
		queue = deque([root])
		while len(queue) > 0:
			node = queue.popleft()
			moves = ExampleGame.gen_moves(node.data)
			next_states = []
			for m in moves:
				next = GameTree(ExampleGame.do_move(node.data, m))
				next.parent = node
				next_states.append(next)
			node.children = next_states
			if (ExampleGame.primitive(node.data) != Solver.OTHER or node.data in Solver.known_states):
				Solver.record(node)
			else:
				for c in node.children:
					queue.append(c)
		if (ExampleGame.initial_position in Solver.known_states):
			if Solver.known_states[ExampleGame.initial_position] == Solver.WIN:
				print("Winning position")
			else:
				print("Losing position")
		else:
			print("Unable to solve game")

	@staticmethod
	def record(node):
		if (ExampleGame.primitive(node.data) != Solver.OTHER):
			Solver.known_states[node.data] = ExampleGame.primitive(node.data)
		elif not(node.data in Solver.known_states):
			all_children_win = True
			for c in node.children:
				if c.data in Solver.known_states:
					if Solver.known_states[c.data] == Solver.LOSS:
						all_children_win = False
						Solver.known_states[node.data] = Solver.WIN
				else:
					all_children_win = False
			if all_children_win:
				Solver.known_states[node.data] = Solver.LOSS
		if node.data != ExampleGame.initial_position:
			Solver.record(node.parent)


class GameTree:
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.children = []

# We'll use the 4 game as our example
class ExampleGame:
	initial_position = 4
	def primitive(pos):
		return Solver.LOSS if pos == 0 else Solver.OTHER
	def gen_moves(pos):
		if pos == 1:
			return [-1]
		elif pos > 1 and pos <= 4:
			return [-1, -2]
		else:
			return []
	def do_move(pos, move):
		return pos + move

Solver.solve()
