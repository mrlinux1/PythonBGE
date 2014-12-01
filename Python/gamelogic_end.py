import bge

import gamelogic_init

controller = bge.logic.getCurrentController()

endLeftSensor = controller.sensors["MouseLeftEnd"]

endOverSensor = controller.sensors["MouseOverEnd"]

if endLeftSensor.positive and endOverSensor.positive:
    bge.logic.endGame()
