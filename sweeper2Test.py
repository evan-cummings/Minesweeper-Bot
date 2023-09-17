import pyautogui
import time

def checkGreens(pos):
    bottomRight=(pos[0]+90,pos[1]+80)
    right=(pos[0]+90,pos[1]-10)
    topRight=(pos[0]+90,pos[1]-100)
    bottomLeft=(pos[0]-90,pos[1]+80)
    left=(pos[0]-90,pos[1]-10)
    topLeft=(pos[0]-90,pos[1]-100)
    top=(pos[0],pos[1]-100)
    bottom=(pos[0],pos[1]+80)
    #red: 242 54 7
    listOfSquares=[bottomRight,right,topRight,bottomLeft,left,topLeft,top,bottom]
    squaresWithGreen=[]

    countGreens=0
    countFlags=0
    
    for item in listOfSquares:
        pixelX=int(item[0])
        pixelY=int(item[1])
        if(pyautogui.pixelMatchesColor(pixelX, pixelY, (162, 209, 73)) or pyautogui.pixelMatchesColor(pixelX, pixelY, (170, 215, 81))):
            countGreens+=1
            squaresWithGreen.append(item)
        elif(pyautogui.pixelMatchesColor(pixelX, pixelY, (242, 54, 7))):
            countFlags+=1
    return (countGreens, squaresWithGreen, countFlags)

def rightClick(posList):
    for pos in posList:
        pyautogui.rightClick(pos)

def leftClick(posList):
    for pos in posList:
        pyautogui.click(pos)


#allImages=list(pyautogui.locateAllOnScreen('test.png',confidence=0.4))
#print(allImages)
onePositions = []
twoPositions=[]
threePositions=[]

threshhold = 8
tempIndex=-1

alreadyDone=[]


while(pyautogui.locateOnScreen('playAgain.png',confidence=0.8)==None):
    onePositions = []
    twoPositions=[]
    threePositions=[]
    #,region=(1422, 474, 990, 139)
    for p in pyautogui.locateAllOnScreen('one.png',confidence=0.99):
        pos=pyautogui.center(p)
        if((pos in alreadyDone)==False):
            onePositions.append(pos)
    for p in pyautogui.locateAllOnScreen('two.png',confidence=0.99):
        pos=pyautogui.center(p)
        if((pos in alreadyDone)==False):
            twoPositions.append(pos)
    for p in pyautogui.locateAllOnScreen('three.png',confidence=0.99):
        pos=pyautogui.center(p)
        if((pos in alreadyDone)==False):
            threePositions.append(pos)
  
    for pos in onePositions:
        #pyautogui.click(pos)
        #bottomRight=(pos[0]+90,pos[1]+90)
        #green1=(162,209,73)
        #green2=(170,215,81)
        greenCount=checkGreens(pos)[0]
        greenList=checkGreens(pos)[1]
        flagCount=checkGreens(pos)[2]
        #pyautogui.moveTo(pos)
        if(greenCount==1 and flagCount==0):
            rightClick(greenList)
        if(flagCount==1 and greenCount!=0):
            onePositions.remove(pos)
            alreadyDone.append(pos)
            leftClick(greenList)
        if(flagCount==1 and greenCount==0):
            onePositions.remove(pos)
            alreadyDone.append(pos)
        
    for pos in twoPositions:
        greenCount=checkGreens(pos)[0]
        greenList=checkGreens(pos)[1]
        flagCount=checkGreens(pos)[2]
        #pyautogui.moveTo(pos)
        if(greenCount==2 and flagCount==0):
            rightClick(greenList)
        if(flagCount==1 and greenCount==1):
            rightClick(greenList)
            greenList=checkGreens(pos)[1]
        if(flagCount==2 and greenCount!=0):
            twoPositions.remove(pos)
            alreadyDone.append(pos)
            leftClick(greenList)
        if(flagCount==2 and greenCount==0):
            twoPositions.remove(pos)
            alreadyDone.append(pos)
            
    for pos in threePositions:
        greenCount=checkGreens(pos)[0]
        greenList=checkGreens(pos)[1]
        flagCount=checkGreens(pos)[2]
        #pyautogui.moveTo(pos)
        if(greenCount==3 and flagCount==0):
            rightClick(greenList)
        elif(greenCount==2 and flagCount==1):
            rightClick(greenList)
            greenList=checkGreens(pos)[1]
        elif(greenCount==1 and flagCount==2):
            rightClick(greenList)
            greenList=checkGreens(pos)[1]
        if(flagCount==3 and greenCount!=0):
            threePositions.remove(pos)
            alreadyDone.append(pos)
            leftClick(greenList)
        if(flagCount==3 and greenCount==0):
            threePositions.remove(pos)
            alreadyDone.append(pos)




    
    
