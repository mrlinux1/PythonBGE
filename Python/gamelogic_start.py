import bge

import gamelogic_init

controller = bge.logic.getCurrentController()

startLeftSensor = controller.sensors["MouseLeftStart"]

startOverSensor = controller.sensors["MouseOverStart"]

if startLeftSensor.positive and startOverSensor.positive:
    scene = bge.logic.getCurrentScene()
    scene.replace("GameScene")
    gamelogic_init.initGame()
