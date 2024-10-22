# tests.py
import numpy as np
from final_optimised_physical_simulation import OptimizedParallelSimulation
from original_physical_simulation import OriginalSimulation
from profiling import PerformanceProfiler


def test_correctness(sizes=[100, 500, 1000]):
    original = OriginalSimulation()
    optimized = OptimizedParallelSimulation()

    for n in sizes:
        print(f"\nTesting size {n}x{n}")
        # Test both implementations
        result_orig = original.simulate(n)
        result_opt = optimized.simulate(n)

        # Verify results match
        np.testing.assert_allclose(
            result_orig,
            result_opt,
            rtol=1e-5,
            err_msg=f"Results don't match for size {n}",
        )
        print(f"✓ Results match for size {n}")


def test_performance(sizes=[100, 200, 300, 400]):
    profiler = PerformanceProfiler()
    results = profiler.run_profiles(sizes)

    print("\nPerformance Summary:")
    print("=" * 50)
    for r in results:
        print(f"\nSize {r['size']}x{r['size']}:")
        print(f"Original time:  {r['original_time']:.3f}s")
        print(f"Optimized time: {r['optimized_time']:.3f}s")
        print(f"Speedup:        {r['speedup']:.2f}x")


if __name__ == "__main__":
    print("Running correctness tests...")
    test_correctness()

    print("\nRunning performance tests...")
    test_performance()
