import asyncio
import time


async def fetch_data(name: str, delay: float) -> str:
    asyncio.sleep(delay)  # Simulates non-blocking I/O wait 
    #this print time 5 seconds because it is non-blocking and the other task is running concurrently

    #time.sleep(delay)  # Simulates blocking I/O wait
    # this print time 7 seconds because it is blocking and the other task is waiting for this task to finish
    return f"{name} done"


async def main():
    start = time.perf_counter()
    # Runs both coroutines concurrently instead of waiting 2s + 2s = 4s
    results = await asyncio.gather(
        fetch_data("Task A", 2),
        fetch_data("Task B", 5),
    )
    print(results, f"in {time.perf_counter() - start:.2f}s")


asyncio.run(main())