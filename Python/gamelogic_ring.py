import bge
import random

scene = bge.logic.getCurrentScene()
controller = bge.logic.getCurrentController()
owner=controller.owner

numring = random.randrange(4,15)
print("Scene: "+scene.name)
activeList = scene.objects
for active in activeList:
    print("Objekt aktiv "+active.name)
ebene=scene.objects["Ebene"]
inactiveList = scene.objectsInactive
for inactive in inactiveList:
    print("Objekt inaktiv "+inactive.name)
print("Anzahl "+str(numring))
for num in range(1,numring):
    print("Duplicate Ring")
    owner.position[0]=random.random()*6-3
    owner.position[1]=random.random()*8-4
    owner.position[2]=0.5
    obj = scene.addObject("Ring", owner,0)
    obj.localScale.x=0.25
    obj.localScale.y=0.25
    obj.localScale.z=0.25
    obj.setParent(ebene)
