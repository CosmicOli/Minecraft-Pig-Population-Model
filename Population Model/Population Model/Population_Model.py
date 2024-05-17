from math import floor
from queue import Queue


def SimulateGenerations(currentAdultPopulation : int, generations : int) -> int:    
    currentKids = Queue(maxsize = 4);
    currentGeneration = 0;
    while currentGeneration < generations:
        currentGeneration += 1;

        # The new kids are born, the amount being half the current adult population.
        # These new kids are added to the currentKids queue, which starts them 'growing up'.
        newKids = floor(currentAdultPopulation / 2);
        currentKids.put(newKids);
    
        # Once the pigs have gotten started, kid pigs become adults every 5 minutes, or every generation.
        # This only isn't true at the beginning, where there are no preexisting kids waiting to be born.
        # Hence, there should always only be a maximum of 4 'batches' of kids (20 min / 5 min = 4), and whenever that is the case it means the kids at the bottom of the queue should have grown up.
        if (currentKids.qsize() == 4):
            currentAdultPopulation += currentKids.get()

    return currentAdultPopulation;

def UI():
    # The starting adult population assumes no kids are currently being born.
    print("What is the starting adult population?")
    startingAdultPopulation = int(input());
    
    # The simulation time in minutes is turned into generations.
    # These generations are 5 minute intervals in length, given it takes 5 minutes for every birth cycle to occur.
    print("How many minutes do you want to simulate?")
    simulatedTime = input();
    generations = int(simulatedTime) / 5;

    endingAdultPopulation = SimulateGenerations(startingAdultPopulation, generations)
    print("After " + str(simulatedTime) + " minutes there will be " + str(endingAdultPopulation) + " pigs.")

UI()
input()