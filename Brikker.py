from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math

class brikke(object):
    def __init__(self, x, y, isRed, id):
        self.x = x
        self.y = y
        self.isRed = isRed 
        self.id = id
       # self.drawsphare()
 
    def drawsphare(self):
        #x=-3.5 er  ventre x=3.5 er  hoyre , y=2,5 er topp  y=-2.5 er bunn
        glPushMatrix();
        red = [1.0,0.,0.,1.]
        white = [1.,1.,1.,1.]
        if self.isRed==1.0:
            glMaterialfv(GL_FRONT,GL_DIFFUSE,red)
        else:
            glMaterialfv(GL_FRONT,GL_DIFFUSE,white)
        
       
        glTranslatef(self.x, self.y, 0);

        
        glutSolidSphere(0.5,40,40)
        glPopMatrix();
    def printut(self):

        print self.id  

        #glFlush()
    def flyttH(self):  
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  
        self.x = self.x+1.0
      #  display() 
    def flyttV(self):    
        self.x = self.x-1.0 
      #  display()    
    def flyttOpp(self):    
        self.y = self.y+1.0
      #  display() 
    def flyttNed(self):    
        self.y = self.y-1.0
      #  display() 
        
        #self.drawsphare()
        
   