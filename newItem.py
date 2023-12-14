import re
from multiprocessing import Pool as ThreadPool
import threading
import time
import asyncio

def work(line):
    ij = 0
    for i in range(1000000):
        ij += 1
    return ij 


async def readFile(string):
    global lenLines
    global compteted
    global i 
    i = 0
    lines = []

    lenLines = 0
    compteted = 0

    pool = ThreadPool(16)

    fs  = open(string)
    for line in fs:
        lenLines += 1
        lines.append("")
        # lines[-1].ProcessTheJunk()

    outputErr = pool.map_async(work, lines)
    print(outputErr)
    sum = 0
    while not outputErr.ready():
        print(outputErr._number_left)
        time.sleep(1)
    for line in outputErr.get():
        print(line)
        sum += line
    print(sum)
    return (outputErr)

if __name__ == "__main__":

    asyncio.run(readFile("./AOC23/day12Input.txt"))