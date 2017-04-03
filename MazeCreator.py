# Maze
from PIL import Image
from random import randint

class Maze(list):


    def __init__(self, hw):
        if hw < 4:
            print("Doolhof moet groter zijn dan 4x4")
            return
        MazePicture = Image.new("RGB", (hw, hw), (255, 255, 255))
        self.node = [0, 0]
        self.nodes = dict()
        self.nodes = {}

        #Leeg doolhof
        for x in range(hw+1):
            for y in range(hw+1):
                self.nodes[x, y] = False
                self.nodes[y, x] = False

        #Omheining genereren
        for x in range(hw):
            self.nodes[0, x] = True
            self.nodes[x, 0] = True
            self.nodes[hw, x] = True
            self.nodes[x, hw] = True

        # Willekeurige route
        x = 0
        y = 0
        while y <= hw - 2:
            Route = randint(0, 3)
            print(Route)
            if Route == 0:
                x += 2
            elif Route == 1:
                y += 1
            elif Route == 2:
                x -= 1
            elif Route == 3:
                y += 1
            if x < 0:
                x = 0
            if y < 0:
                y = 0
            if x >= hw:
                x = hw - 1
            if y >= hw:
                y = hw -1
            print (x, y )
            MazePicture.putpixel((x, y), (255, 0, 0))
        print("hi")

        for x in range(hw):
            for y in range(hw):
                toets = randint(0, 9)
                if toets % 2 == 0:
                    MazePicture.putpixel((x, y), (0, 0, 0))


        # Plaatje maken
        for x in range(hw):
            for y in range(hw):
                if self.nodes[x, y] == True:
                    MazePicture.putpixel((x, y), (0, 0, 0))
                if self.nodes[y, x] == True:
                    MazePicture.putpixel((x, y), (0, 0, 0))
        # Plaatje zien
        MazePicture.show()


Maze(1000)
