from mpiy import MPI

def distr_filter(data, f):
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()

	data = []

	if rank == 0:
		data = argv[1]

	#Scatter
	data = comm.scatter(data, root=0)
	data = f(data)

	data = comm.gather(data, root=0)

	comm.Barrier()

	if rank == 0:
		print data

def example_function(i)
	return i * 2

distr_filter([1, 2, 3, 4, 5], example_function)