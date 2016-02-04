from mpi4py import MPI

def distr_filter(d, f):
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()

	data = []

	if rank == 0:
		data = d

	#Scatter
	data = comm.scatter(data, root=0)
	data = f(data)

	data = comm.gather(data, root=0)

	comm.Barrier()

	if rank == 0:
		print(data)

def example_function(i):
	return i * 2

distr_filter([1, 2, 3, 4, 5], example_function)