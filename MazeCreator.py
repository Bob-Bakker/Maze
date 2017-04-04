# Maze
from PIL import Image
from random import randint
from random import choice

class Maze(list):


    def __init__(self, hw):

        if hw < 4:
            print("Doolhof moet groter zijn dan 4x4")
            return
        mazepicture = Image.new("RGB", (hw, hw), (255, 255, 255))
        self.nodes = dict()


        # Empty canvas
        for x in range(hw+1):
            for y in range(hw+1):
                self.nodes[x, y] = False
                self.nodes[y, x] = False

        # Make walls
        for x in range(hw):
            self.nodes[0, x] = True
            self.nodes[x, 0] = True
            self.nodes[hw, x] = True
            self.nodes[x, hw] = True




        # Random startpoint on first row
        startpos = ([randint(1, hw-1), 0])
        x = startpos[0]
        y = startpos[1]
        self.nodes[x, y] = False
        currentx = x
        currenty = y

        # Set stack to starting position
        stack = ([x, y])
        visited = ([])

        def createmaze(currentx, currenty, stack, visited):
            print(currentx, currenty)
            # Check neighbors
            right = False
            left = False
            top = False
            bottom = False

            # Add current position to stack and visited
            stack.append([currentx, currenty])
            visited.append([currentx, currenty])
            # x + 1 (right)
            if currentx < hw and self.nodes[currentx + 1, currenty] == False:
                right = True

            # x - 1 (left)
            if currentx > 0 and self.nodes[currentx - 1, currenty] == False:
                left = True

            #currenty + 1 (bottom)
            if currenty < hw and self.nodes[currentx, currenty + 1] == False:
                bottom = True

            #currenty - 1(top)
            if currenty > 0 and self.nodes[currentx, currenty - 1] == False:
                top = True

            Moves = []
            if right:
                Moves.append(["Right", currentx + 1, currenty])
            if left:
                Moves.append(["Left", currentx - 1, currenty])
            if bottom:
                Moves.append(["Bottom", currentx, currenty + 1])
            if top:
                Moves.append(["Top", currentx, currenty - 1])





            # calculate random 'true' move, first remove visited from choices
            print("Visited:", visited)
            for itm in Moves:
                coords = ([itm[1], itm[2]])

                if coords in visited:
                    print "gotcha"
                    Moves.remove(itm)

            if len(Moves) < 1:
                if currentx == x and currenty == y:
                    print "all done"
                    return
                else:
                    print "POP!"
                    visited.append([currentx, currenty])
                    stack.pop()
                    return
                    createmaze(currentx, currenty, stack, visited)

            NextMove = choice(Moves)
            print(Moves)


            # make walls at other moves
            if NextMove[0] == "Right":
                if currentx > 0 and self.nodes[currentx - 1, currenty] == False:  # left
                    self.nodes[currentx - 1, currenty] = True
                    mazepicture.putpixel((currentx - 1, currenty), (0, 0, 0))
                if currenty < hw and self.nodes[currentx, currenty + 1] == False:  # top
                    self.nodes[currentx, currenty + 1] = True
                    mazepicture.putpixel((currentx, currenty + 1), (0, 0, 0))
                if currenty > 0 and self.nodes[currentx, currenty - 1] == False:  # bottom
                    self.nodes[currentx, currenty - 1 ] = True
                    
                    mazepicture.putpixel((currentx, currenty - 1), (0, 0, 0))

            if NextMove[0] == "Left":
                if currentx < hw and self.nodes[currentx + 1, currenty] == False:  # right
                    self.nodes[currentx + 1, currenty] = True
                    mazepicture.putpixel((currentx - 1, currenty), (0, 0, 0))
                if currenty < hw and self.nodes[currentx, currenty + 1] == False:  # top
                    self.nodes[currentx, currenty + 1] = True
                    mazepicture.putpixel((currentx - 1, currenty), (0, 0, 0))
                if currenty > 0 and self.nodes[currentx, currenty - 1] == False:  # bottom
                    self.nodes[currentx, currenty - 1] = True
                    mazepicture.putpixel((currentx - 1, currenty), (0, 0, 0))

            if NextMove[0] == "Top":
                if currentx < hw and self.nodes[currentx + 1, currenty] == False:  # right
                    mazepicture.putpixel((currentx + 1, currenty), (0, 0, 0))
                    self.nodes[currentx + 1, currenty] = True
                if currentx > 0 and self.nodes[currentx - 1, currenty] == False:  # left
                    mazepicture.putpixel((currentx - 1, currenty), (0, 0, 0))
                    self.nodes[currentx - 1, currenty] = True
                if currentx > 0 and self.nodes[currentx, currenty - 1] == False:  # bottom
                    mazepicture.putpixel((currentx, currenty -1), (0, 0, 0))
                    self.nodes[currentx, currenty - 1] = True


            if NextMove[0] == "Bottom":
                if currentx < hw and self.nodes[currentx + 1, currenty] == False:  # right
                    mazepicture.putpixel((currentx + 1, currenty), (0, 0, 0))
                    self.nodes[currentx + 1, currenty] = True
                if currentx > 0 and self.nodes[currentx - 1, currenty] == False:  # left
                    mazepicture.putpixel((currentx - 1, currenty), (0, 0, 0))
                    self.nodes[currentx - 1, currenty] = True
                if currentx < hw and self.nodes[currentx, currenty + 1] == False:  # top
                    mazepicture.putpixel((currentx - 1, currenty), (0, 0, 0))
                    self.nodes[currentx, currenty + 1] = True


            # Update location
            currentx = NextMove[1]
            currenty = NextMove[2]
            visited.append([currentx, currenty])

            #start again
            createmaze(currentx, currenty, stack, visited)


        createmaze(currentx, currenty, stack, visited)

# Plaatje maken

        mazepicture.show()
        mazepicture.save("C:/Users/FLUX/Desktop/maze/maze.bmp")


Maze(10)
