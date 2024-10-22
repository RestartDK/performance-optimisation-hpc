import numpy as np
from final_optimised_physical_simulation import OptimizedParallelSimulation
from original_physical_simulation import OriginalSimulation
from memory_profiler import profile
from cProfile import Profile
from pstats import Stats, SortKey
import time


class PerformanceProfiler:
    def __init__(self):
        self.original = OriginalSimulation()
        self.optimized = OptimizedParallelSimulation()

    @profile
    def profile_original(self, n):
        profiler = Profile()
        profiler.enable()
        result = self.original.simulate(n)
        profiler.disable()
        return profiler, result

    @profile
    def profile_optimized(self, n):
        profiler = Profile()
        profiler.enable()
        result = self.optimized.simulate(n)
        profiler.disable()
        return profiler, result

    def run_profiles(self, sizes=[100, 500, 1000, 2000]):
        results = []

        for n in sizes:
            print(f"\nProfiling for size {n}x{n}")
            print("=" * 40)

            # Time and profile original
            start = time.time()
            orig_profiler, result_orig = self.profile_original(n)
            orig_time = time.time() - start

            # Time and profile optimized
            start = time.time()
            opt_profiler, result_opt = self.profile_optimized(n)
            opt_time = time.time() - start

            # Verify results match
            np.testing.assert_allclose(result_orig, result_opt, rtol=1e-5)

            # Store results
            results.append(
                {
                    "size": n,
                    "original_time": orig_time,
                    "optimized_time": opt_time,
                    "speedup": orig_time / opt_time,
                    "original_profile": orig_profiler,
                    "optimized_profile": opt_profiler,
                }
            )

            # Print profiles
            print("\nOriginal Implementation Profile:")
            Stats(orig_profiler).sort_stats(SortKey.TIME).print_stats(10)

            print("\nOptimized Implementation Profile:")
            Stats(opt_profiler).sort_stats(SortKey.TIME).print_stats(10)

            print("\nTime Comparison:")
            print(f"Original:  {orig_time:.3f} seconds")
            print(f"Optimized: {opt_time:.3f} seconds")
            print(f"Speedup:   {orig_time/opt_time:.2f}x")

        return results


if __name__ == "__main__":
    profiler = PerformanceProfiler()
    results = profiler.run_profiles()
