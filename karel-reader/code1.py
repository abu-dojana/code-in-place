# topic: till new function(3), world size: 8x8
# Program: Turn right and turn left and use function
# --------------------------------------------------

#task: pick up beeper from (4,1) and put it in (7,3) and return to (1,1). Create the scenario and solve.
#creating scenerio:
#1. put beeper in (4,1)
#2. return to (1,1)
#Solve:
#1. move to (4,1)
#2. turn left
#3. move to (4,3)
#4. turn right
#5. move to (7,3)
#6. put the beeper
#7. turn around
#8. move to (1,1)

from karel.stanfordkarel import *

def main():
   
   create_scenerio()
   solve()

def create_scenerio():
   #put beeper to (4,1)
   move()
   move()
   move()
   put_beeper()
   
   turn_around()
   
   move()
   move()
   move()
   
   turn_around()
   
def solve():
   #move to (4,1)
   move()
   move()
   move()
   
   #pick_beepr
   pick_beeper()
   
   #turn left
   turn_left()
   
   #move to (4,3)
   move()
   move()
   
   #turn right
   turn_right()
   
   #move to (7,3)
   move()
   move()
   move()
   
   #put beeper
   put_beeper()
   
   #turn around
   turn_around()
   
   #move to (1,1)
   move()
   move()
   move()
   move()
   move()
   move()
   turn_left()
   move()
   move()
   turn_left()
   
   
def turn_right():
   turn_left()
   turn_left()
   turn_left()
   
def turn_around():
   turn_left()
   turn_left()
   
