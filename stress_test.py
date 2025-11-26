#!/usr/bin/env python3
"""
CPU and power stress test for Raspberry Pi.
Usage: python3 stress_test.py [duration_seconds] [num_workers]
Default: 60 seconds, all CPU cores
"""

import multiprocessing
import time
import sys
import math


def cpu_stress_worker(worker_id: int, duration: float) -> None:
    """Perform CPU-intensive calculations."""
    end_time = time.time() + duration
    x = 0.0
    while time.time() < end_time:
        # Mix of floating point operations to stress FPU
        for _ in range(10000):
            x = math.sin(x) * math.cos(x) + math.sqrt(abs(x) + 1)
            x = math.tan(x % 1.0) + math.log(abs(x) + 1)
            x = x ** 1.1 + math.exp(x % 10)
    print(f"Worker {worker_id} finished")


def main():
    duration = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    num_workers = int(sys.argv[2]) if len(sys.argv) > 2 else multiprocessing.cpu_count()

    print(f"Starting stress test: {num_workers} workers for {duration} seconds")
    print("Press Ctrl+C to stop early")

    processes = []
    start_time = time.time()

    try:
        for i in range(num_workers):
            p = multiprocessing.Process(target=cpu_stress_worker, args=(i, duration))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

    except KeyboardInterrupt:
        print("\nStopping...")
        for p in processes:
            p.terminate()
            p.join()

    elapsed = time.time() - start_time
    print(f"Stress test completed in {elapsed:.1f} seconds")


if __name__ == "__main__":
    main()
