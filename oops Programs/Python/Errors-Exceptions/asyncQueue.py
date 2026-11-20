"""
Producer-Consumer pattern with asyncio.Queue
--------------------------------------------
- A PRODUCER puts work items into a shared queue.
- One or more CONSUMERS take items out of the queue and process them.
- asyncio.Queue is safe to share between coroutines (tasks), so no locks are needed.

How asyncio works (in short):
- Everything runs on ONE thread, inside an "event loop".
- `async def` makes a coroutine: a function that can pause itself.
- `await` is the pause point: the coroutine hands control back to the event loop,
  so the loop can run another coroutine while this one waits.
- So tasks take turns at every `await`. They don't run in parallel the way threads do.
"""

import asyncio
import time


# PRODUCER: puts numbers 1..100 into the queue.
async def producer(queue):
  for i in range(1, 101):
    # put() adds an item to the queue.
    # It only has to wait if the queue has a maxsize and is full.
    # This queue has no maxsize, so put() never actually waits here.
    await queue.put(i)

  # NOTE: the consumers stop when they receive None (the "sentinel" value),
  # but the producer never puts None into the queue. So after item 100
  # both consumers wait on queue.get() forever and the program never exits.
  # Fix: put one None per consumer here, e.g.
  #   for _ in range(2):
  #     await queue.put(None)


# CONSUMER: takes items out of the queue one at a time and processes them.
async def consumer(queue):
  while True:
    # get() removes and returns the next item.
    # If the queue is empty, this coroutine pauses here and the event loop
    # runs other tasks until an item arrives.
    item = await queue.get()

    # None is the stop signal (sentinel): mark it done and leave the loop.
    if item is None:
      queue.task_done()
      break

    print(item)

    # NOTE: time.sleep() BLOCKS the whole event loop. There is only one thread,
    # so while one consumer sleeps, the other consumer (and every other task) is frozen.
    # The two consumers end up working one after the other, not concurrently.
    # Use the async version instead, which pauses only this coroutine:
    #   await asyncio.sleep(10)
    time.sleep(10)

    # task_done() tells the queue that one item has been fully processed.
    # queue.join() (not used here) waits until task_done() has been called
    # for every item that was put in.
    queue.task_done()


async def main():
  # One shared queue for the producer and all consumers.
  queue = asyncio.Queue()

  # Run the producer to completion first: all 100 items are queued
  # before any consumer starts.
  # To produce and consume at the same time, run the producer inside gather() too.
  await producer(queue)

  # gather() runs both consumers as concurrent tasks on the same event loop
  # and waits until all of them finish.
  # Both read from the same queue, so each item goes to exactly one consumer.
  await asyncio.gather(
    consumer(queue),
    consumer(queue)
  )


# asyncio.run() creates the event loop, runs main() until it finishes,
# then closes the loop. This is the entry point for async code.
asyncio.run(main())
