import math
import random
from tkinter import *
import time


MAX_X_SPEED = 2
MAX_Y_SPEED = 2

#DISEASE CONSTANTS
NUMBER_INFECTED = 1
DISEASE_RANGE = 20
INFECTION_PERIOD = 1000

#WORLD CONSTANTS
WORLD_HEIGHT = 800
WORLD_WIDTH = 800
NUM_PEOPLE = 50
PERSON_SIZE = 5


class Person:
    x, y, speedX, speedY, timeInfected = 0, 0, 0, 0, 0
    infected, immune = False, False

    def __init__(self):
        self.x = random.randint(PERSON_SIZE, WORLD_WIDTH - PERSON_SIZE)
        self.y = random.randint(PERSON_SIZE, WORLD_HEIGHT - PERSON_SIZE)
        self.speedX = random.randint(-MAX_X_SPEED, MAX_X_SPEED)
        self.speedY = random.randint(-MAX_Y_SPEED, MAX_Y_SPEED)

    def distance(self, Person):
        return math.sqrt(math.pow((Person.y - self.y), 2) + math.pow((Person.x - self.x), 2))





print("Enter file name: ", end='')
fileN = input()
f = open(fileN, "a")
f.write("Time\t# Infected:\t# Immune:\t# Suceptible:\n")
f.close()


#START CLOCK
tI = time.time()

tk = Tk()
canvas = Canvas(tk, width=WORLD_WIDTH, height=WORLD_HEIGHT)
tk.title("")
canvas.pack()

people = []
canvasP = []

for i in range(NUM_PEOPLE-NUMBER_INFECTED):
    people.append(Person())
    canvasP.append(canvas.create_oval(people[i].x-PERSON_SIZE,people[i].y-PERSON_SIZE,people[i].x+PERSON_SIZE,people[i].y+PERSON_SIZE, fill = 'black', outline = 'white', width=5))
for i in range(NUM_PEOPLE-NUMBER_INFECTED, NUM_PEOPLE):
    inf = Person()
    inf.infected = True
    people.append(inf)
    canvasP.append(canvas.create_oval(people[i].x-PERSON_SIZE,people[i].y-PERSON_SIZE,people[i].x+PERSON_SIZE,people[i].y+PERSON_SIZE, fill = 'white', outline = 'red', width=5))


pos = []
for i in range(len(canvasP)):
    pos.append(canvas.coords(canvasP[i]))








while True:
    for i in range(len(people)):
        canvas.move(canvasP[i], people[i].speedX, people[i].speedY)
        pos[i] = canvas.coords(canvasP[i])

        people[i].x += people[i].speedX
        people[i].y += people[i].speedY
        if (pos[i][3] >= WORLD_HEIGHT or pos[i][1] <= 0):
            people[i].speedY = -people[i].speedY
        if (pos[i][2] >= WORLD_WIDTH or pos[i][0] <= 0):
            people[i].speedX = -people[i].speedX




        if(people[i].infected and not people[i].immune):
            for j in range(len(people)):
                if (j != i):
                    if (people[i].distance(people[j]) <= DISEASE_RANGE and not people[j].infected and not people[j].immune):
                        people[j].infected = True
                        canvas.itemconfigure(canvasP[j], fill='white', outline='red')
            people[i].timeInfected += 1
            if(people[i].timeInfected >= INFECTION_PERIOD):
                people[i].immune = True
                people[i].infected = False
                canvas.itemconfigure(canvasP[i], fill='red', outline='white')



    numInfected = 0
    numImmune = 0
    suceptible = 0
    for i in range(len(people)):
        if(people[i].infected):
            numInfected += 1
        if (people[i].immune):
            numImmune += 1
        if (not people[i].immune and not people[i].infected):
            suceptible += 1




    tk.update()
    time.sleep(0.01)
    print("Time: " + str(time.time() - tI) + "\t# Infected: " + str(numInfected) + "\t# Immune: " + str(numImmune) + "\t# Suceptible: " + str(suceptible))
    f = open(fileN, "a")
    f.write(str(time.time() - tI) + "\t" + str(numInfected) + "\t" + str(numImmune) + "\t" + str(suceptible) + "\n")
    f.close()