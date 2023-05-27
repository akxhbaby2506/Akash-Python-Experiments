"""
You are given two jugs, a 4-gallon one and a 3-gallon one, a pump which has unlimited 
water which you can use to fill the jug, and the ground on which water may be poured. Neither
jug has any measuring markings on it. How can you get exactly 2 gallons of water in the 4-gallon jug?
"""

from collections import defaultdict

jug1 = 4
jug2 = 3
aim = 2

visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2):
    
    if visited[(amt1,amt2)] == False:
        print(amt1, amt2)
        
        visited[(amt1, amt2)] = True
        
        return (waterJugSolver(0,amt2) or 
                waterJugSolver(amt1,0) or
                waterJugSolver(jug1,amt2) or
                waterJugSolver(amt1,jug2) or
                waterJugSolver(amt1+min(amt2,(jug1-amt1)),amt2-min(amt2,(jug1-amt1))) or 
                waterJugSolver(amt1-min(amt1,(jug2-amt2)),amt2+min(amt1,(jug2-amt2))))
    else:
        return False
    
print("Steps: ")

waterJugSolver(0,0)
