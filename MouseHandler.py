from OpenGL.GLUT import *

class MouseHandler:

    def __init__(self):
        self.mouse = [0.0, 0.0]
        self.rotation = [-60.0, -30.0] # x and z rotation
        self.button = None

    def handle_click(self, button, state, x, y):
        self.button = button
        if (button == GLUT_LEFT_BUTTON) and (state == GLUT_DOWN):
            self.mouse[0] = x
            self.mouse[1] = y
        if(button == GLUT_RIGHT_BUTTON) and (state == GLUT_DOWN):
            self.selectPiece(x,y)

    def mouse_moved(self, x, y):
        if self.button != GLUT_LEFT_BUTTON:
          return
        self.rotation[0] += (y - self.mouse[1]) / 85
        self.rotation[1] += (x - self.mouse[0]) / 85
        glutPostRedisplay()

    def getRotation(self):
        return self.rotation

    def getMouse(self):
        return self.mouse


    def sharpenCoordinates(self, x, y):
        print x, y
        return x, y

    def selectPiece(self, x, y):
        self.sharpenCoordinates(x,y)


