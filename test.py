from physics import *
from graphics import GraphWin, Point, Circle
import time
from copy import deepcopy

r = 5.0

F = gravity_field_homogeneous(9.81, [0,1])
def g_rel(coors):
    return coors.values[1] <= 200.0 - r

g = ground(g_rel, 1)
dt = 0.05


points = [Mass_Point([10+2*r*i, r*(i+1)], [0,0], [0,0], 1)\
           for i in range(int(100/r))]


s = System(points, forces = [F], constrains = [g])
sim = Simulation([s], dt)


circs = [Circle(Point(p.coors.values[0], p.coors.values[1]), r)\
         for p in points]

win = GraphWin('Pokus', 200, 200)

[circ.draw(win) for circ in circs]

for i in range(5000):
    coors = [deepcopy(p.coors) for p in points]
        
    sim.step_next()
    
    us = [(p.coors - coor).values for p, coor in zip(points, coors)]
    
    [circ.move(u[0], u[1]) for circ, u in zip(circs, us)]
    
    time.sleep(0.25*dt)
    
win.getMouse()
win.close()
