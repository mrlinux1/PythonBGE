import bge
import gamelogic_init

controller = bge.logic.getCurrentController()

goalSensor = controller.sensors["GoalCollision"]

if goalSensor.positive:
    print("Gewonnen")
    gamelogic_init.endWonGame()
    
ball = controller.owner

plateSensor = controller.sensors["PlaneNear"]

if plateSensor.positive:
    plane = bge.logic.getCurrentScene().objects["Ebene"]
    if ball.getDistanceTo(plane) > 6.0:
        print("Verloren")
        print("Abstand = "+str(ball.getDistanceTo(plane)))
        gamelogic_init.endLostGame()
        
ringSensor = controller.sensors["RingCollision"]
if ringSensor.positive:
    for ring in ringSensor.hitObjectList:
        ring.endObject()
        gamelogic_init.addPoints()
        
