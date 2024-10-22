import numpy as np
from numpy.linalg import solve
from numpy.random import RandomState
from multiprocessing import Pool, cpu_count


class OptimizedParallelSimulation:
    def __init__(self):
        self.rng = RandomState(42)
        self.n_cores = cpu_count()
        self._warmup()  # Initialize during creation

    def _warmup(self):
        """Warmup run to initialize multiprocessing"""
        n_small = 10
        data = np.random.rand(3, n_small, n_small)
        A = data[0]
        B = data[1]
        C = data[2]

        A_chunks = np.array_split(A, self.n_cores)
        C_chunks = np.array_split(C, self.n_cores)

        with Pool(processes=self.n_cores) as pool:
            args = [(A_chunks[i], B, C_chunks[i]) for i in range(self.n_cores)]
            _ = pool.map(self.process_chunk, args)
        print("Warmup completed")

    @staticmethod
    def process_chunk(args):
        A_chunk, B, C_chunk = args
        result = np.dot(A_chunk, B)
        result *= C_chunk
        return result

    def simulate(self, n):
        data = np.ascontiguousarray(self.rng.rand(3, n, n), dtype=np.float64)

        A = data[0]
        B = data[1]
        C = data[2]

        if n >= 500:
            A_chunks = np.array_split(A, self.n_cores)
            C_chunks = np.array_split(C, self.n_cores)

            with Pool(processes=self.n_cores) as pool:
                args = [(A_chunks[i], B, C_chunks[i]) for i in range(self.n_cores)]
                results = pool.map(self.process_chunk, args)
                result = np.vstack(results)
        else:
            result = np.dot(A, B)
            result *= C

        return solve(result, np.ones(n))
