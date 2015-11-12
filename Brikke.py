from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math

class Brikke(object):
    def __init__(self, x, y, isRed, id):
        self.x = x
        self.y = y
        self.isRed = isRed 
        self.id = id
       # self.translate(x, y, isRed)
        self.drawsphare(x, y, isRed)
 
    def drawsphare(self, x, y, isRed):
        #x=-3.5 er  ventre x=3.5 er  hoyre , y=2,5 er topp  y=-2.5 er bunn
        glPushMatrix();
        red = [1.0,0.,0.,1.]
        white = [1.,1.,1.,1.]
        if isRed==1.0:
            glMaterialfv(GL_FRONT,GL_DIFFUSE,red)
        else:
            glMaterialfv(GL_FRONT,GL_DIFFUSE,white)
        
       
        glTranslatef(x, y, 0);

        
        glutSolidSphere(0.5,40,40)
        glPopMatrix();
    def printut(self):
        print self.id  