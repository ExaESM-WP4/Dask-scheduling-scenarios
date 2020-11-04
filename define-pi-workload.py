import numpy, dask.array

def calculate_pi(size_in_bytes, number_of_chunks):
    
    """Calculate pi using a Monte Carlo method."""
    
    array_shape = (int(size_in_bytes / 8 / 2), 2) # tuple
    chunk_size = (int(array_shape[0] / number_of_chunks), 2) # tuple
    
    # 2D random positions array using dask.array
    xy = dask.array.random.uniform(
        low=0.0, high=1.0, size=array_shape,
        # specify the chunk size, i.e. Dask graph task number
        chunks=chunk_size )
  
    xy_inside_circle = (xy ** 2).sum(axis=1) < 1 # boolean

    pi = 4 * xy_inside_circle.sum() / xy_inside_circle.size
    
    # start Dask calculation
    pi = pi.compute()

    print(f"\nfrom {xy.nbytes / 1e9} GB randomly chosen positions")
    print(f"   pi estimate: {pi}")
    print(f"   pi error: {abs(pi - numpy.pi)}\n")
    
    return pi
