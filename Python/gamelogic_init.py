import bge
import bpy
import random

def duplicateObject(scene, name, copyobj):
    # Create new mesh
    mesh = bpy.data.meshes.new(name)
    # Create new object associated with the mesh
    ob_new = bpy.data.objects.new(name, mesh)
    # Copy data block from the old object into the new object
    ob_new.data = copyobj.data.copy()
    ob_new.scale = copyobj.scale
    ob_new.location.x=random.randrange(0,4)-2
    ob_new.location.y=random.randrange(0,8)-4
    ob_new.location.z=0.5
    # Link new object to the given scene and select it
    scene.addObject(name, ob_new)
    ob_new.select = True 
    return ob_new

def resetGame():
    bge.logic.globalDict['highscore']=0
    scene = bge.logic.getCurrentScene()
    hc=scene.objects["HighscoreContent"]
    hc.text = str(bge.logic.globalDict['highscore'])
    bge.logic.saveGlobalDict()
    

def initProgram():
    bge.logic.loadGlobalDict()
    bge.logic.globalDict['points']=0
    if not 'highscore' in bge.logic.globalDict:
        bge.logic.globalDict['highscore']=0
    scene = bge.logic.getCurrentScene()
    hc=scene.objects["HighscoreContent"]
    hc.text = str(bge.logic.globalDict['highscore'])
    
def endProgram():
    bge.logic.saveGlobalDict()
    
def initGame():
    bge.logic.globalDict['points']=0
    bge.logic.addScene("OverlayScene",True)

def endLostGame():
    print("Points = "+str(bge.logic.globalDict['points']))
    print("Highscore = "+str(bge.logic.globalDict['highscore']))
    scene = bge.logic.getCurrentScene()
    scene.replace("StartScene")
    os = bge.logic.getSceneList()[1]
    os.end()

def endWonGame():
    print("Points = "+str(bge.logic.globalDict['points']))
    print("Highscore = "+str(bge.logic.globalDict['highscore']))
    if bge.logic.globalDict['points'] > bge.logic.globalDict['highscore']:
        bge.logic.globalDict['highscore'] = bge.logic.globalDict['points']
        bge.logic.saveGlobalDict()
    scene = bge.logic.getCurrentScene()
    scene.replace("StartScene")
    os = bge.logic.getSceneList()[1]
    os.end()
        
def addPoints():
     bge.logic.globalDict['points']+=20
     os = bge.logic.getSceneList()[1]
     os.objects["PointContent"].text = str(bge.logic.globalDict['points'])
     
initProgram()