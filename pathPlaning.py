import pygame
from RRTbase import RRTGraph
from RRTbase import RRTMap

dimensions = (600,1000)
start = (10, 10)
goal = (810,510)

obsdim = 25
obsnum = 300

iteration = 0
pygame.init()
map= RRTMap(start,goal,dimensions,obsdim,obsnum)
graph = RRTGraph(start,goal,dimensions,obsdim,obsnum)

obstacles = graph.makeobs()
map.drawMap(obstacles)

while(not graph.path_to_goal()):
    if iteration % 20  ==0:
        x, y, parent = graph.bias(goal)
        pygame.draw.circle(map.map, map.grey, (x[-1], y[-1]), map.nodeRad+2 , 0)
        pygame.draw.line(map.map, map.Red, (x[-1], y[-1]), (x[parent[-1]], y[parent[-1]]),
                       map.edgeThickness)
    else:
       x,y, parent = graph.expand()
       pygame.draw.circle(map.map, map.grey, (x[-1], y[-1]), map.nodeRad+2 , 0)
       pygame.draw.line(map.map, map.Red, (x[-1], y[-1]), (x[parent[-1]], y[parent[-1]]),
                         map.edgeThickness)  ####!!check
       
    if iteration % 5 ==0:
        pygame.display.update()
    iteration += 1
#map.drawPath(graph.getPathCoords())
map.dpath(graph.getPathCoords())
pygame.display.update()
pygame.event.clear()
#pygame.event.wait(0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
