from mpi4py import MPI

def distr_filter(d, f):
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	#Scatter
	data = comm.scatter(d, root=0)
	if f(data):
		comm.send(True, dest=0, tag=1)
	else:
		comm.send(False, dest=0, tag=0)

	comm.Barrier()

	if rank == 0:
		filtered_data = []
		for i in range(0, size):
			filt = comm.recv(source=i)
			if filt:
				filtered_data.append(d[i])
		print(filtered_data)

def example_function(i):
	return i % 2 == 1

# Execution begins here
example_data = [1, 2, 3, 4, 5]
distr_filter(example_data, example_function)