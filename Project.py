from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math
#from var import ID, brikker
from Brikker import brikke
from Keyboard import Keyboard
from MouseHandler import MouseHandler
from DrawBrett import DrawBrett


class Project():
    name = 'TDT4195 Peter Holiman'
    #// angle of rotation for the camera direction
    
    
    def __init__(self):
        self.brikker = []
        self.Keyboard = Keyboard(self.brikker)
        self.mouse_handler = MouseHandler()
      #  self.drawBrett = DrawBrett()



    def keyPress(self, key, x, y):
        Keyboard.keydown(self.Keyboard, key, x, y)
        self.display()
       # self.drawBrett()
        
#     def initList(self):
#         displayLists = glGenLists(1)
#         glNewList(1, GL_COMPILE_AND_EXECUTE)
#         self.drawBrett()
#         glEndList()
#     
    def DRITIDENNEdrawBrett_(self):
        glClear(GL_COLOR_BUFFER_BIT  | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        red= (1,0,0)
        blue= (0,0,1)
        for x in range(0, 8):
                for y in range(0,5):
                    if (x + y) % 2 == 0:
                        glMaterialfv(GL_FRONT,GL_DIFFUSE,blue)
                    else:
                        glMaterialfv(GL_FRONT,GL_DIFFUSE,red)   
                    glRectf(x-4, y-2, x -3, y -1)

    def drawBrett_(self):

        print 'draw'            
        #glPushMatrix();           
        red=GLfloat_3(1,0,0)
        blue=GLfloat_3(0,0,1)
        for i in range (0,8):
            for j in range (0,5):
                glBegin(GL_POLYGON)
                if (i%2 == 0 and j%2 != 0) or (i%2 != 0 and j%2 == 0):
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,red)
                else:
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,blue) 
                glVertex3f((-4+i)*1, (-4+j)*1, 0)
                glVertex3f((-4+i+1)*1, (-4+j)*1, 0)
                glVertex3f((-4+i+1)*1, (-4+j+1)*1, 0)
                glVertex3f((-4+i)*1, (-4+j+1)*1, 0)
                glEnd()
                
    def drawBrett_side(self):
        
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5, 0.5, 0.5, 0])
        # Brett bottom
        glBegin(GL_POLYGON)
        glNormal3d(0,0,-1)
        glVertex3f(-4*1,-4*1,-1/2)
        glNormal3d(0,0,-1)
        glVertex3f(-4*1,4*1,-1/2)
        glNormal3d(0,0,-1)
        glVertex3f(4*1,4*1,-1/2)
        glNormal3d(0,0,-1)
        glVertex3f(4*1,-4*1,-1/2)
        glEnd()
        
        # Brett sides:
        glBegin(GL_POLYGON)
        glNormal3d(-1,0,0)
        glVertex3f(-4*1,-4*1,-1/2)
        glNormal3d(-1,0,0)
        glVertex3f(-4*1,4*1,-1/2)
        glNormal3d(-1,0,0)
        glVertex3f(-4*1,4*1,0)
        glNormal3d(-1,0,0)
        glVertex3f(-4*1,-4*1,0)
        glEnd()
        
        glBegin(GL_POLYGON)
        glNormal3d(1,0,0)
        glVertex3f(4*1,4*1,-1/2)
        glNormal3d(1,0,0)
        glVertex3f(4*1,-4*1,-1/2)
        glNormal3d(1,0,0)
        glVertex3f(4*1,-4*1,0)
        glNormal3d(1,0,0)
        glVertex3f(4*1,4*1,0)
        glEnd()
        
        glBegin(GL_POLYGON)
        glNormal3d(0,1,0)
        glVertex3f(-4*1,4*1,-1/2)
        glNormal3d(0,1,0)
        glVertex3f(4*1,4*1,-1/2)
        glNormal3d(0,1,0)
        glVertex3f(4*1,4*1,0)
        glNormal3d(0,1,0)
        glVertex3f(-4*1,4*1,0)
        glEnd()
        
        glBegin(GL_POLYGON)
        glNormal3d(0,-1,0)
        glVertex3f(-4*1,-4*1,-1/2)
        glNormal3d(0,-1,0)
        glVertex3f(4*1,-4*1,-1/2)
        glNormal3d(0,-1,0)
        glVertex3f(4*1,-4*1,0)
        glNormal3d(0,-1,0)
        glVertex3f(-4*1,-4*1,0)
        glEnd()    
        #glPopMatrix();           

    def rounding_X(self, x):
        #pass
        i = round(x*2)
        i = i/2;
        if i.is_integer():
            t = abs(i-x)
            if t<0.25:
                return i-0.5
            else:
                return i+0.5
        else:
            return i           
    def rounding_Y(self, x):
        #pass
        i = round(x*2)
        i = i/2;
        if i.is_integer():
            t = abs(i-x)
            if t<0.25:
                return i+0.5
            else:
                return i-0.5
        else:
            return i
                
          
                  
     
            
    def initBrikke(self):
        
        with open('exp.txt') as f:
            lines = f.readlines()
            numbers =[float(e.strip()) for e in lines]
        
        brikke_id = 0
        i = 0;  
        
        while i < len(numbers):
            x= self.rounding_X(((numbers[i]/800)*8.)-3.5)
            y = -self.rounding_Y(((numbers[i+1]/498)*5.)-1)
            
            xw = ((numbers[i]/800)*7.)-3.5
            yw= -(((numbers[i+1]/498)*5.)-3)
            
            isRed = numbers[i+2]
            
            b = brikke(x, y, isRed, brikke_id)
            self.brikker.append(b)
            print(numbers[i], x,numbers[i+1], y, numbers[i+2], isRed)
            i = i+3
            brikke_id = brikke_id+1        
      
    def drawBrikke(self):
        for b in self.brikker:
            b.drawsphare()           
    def mouse_moved (self, x, y):  
        self.mouse_handler.mouse_moved(x,y)

    def mouse_pressed (self, button, state, x, y):
        self.mouse_handler.handle_click(button, state, x, y) 
        
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
       
        glTranslatef(0.0, 0.0, -20.0)
        glRotatef(self.mouse_handler.getRotation()[0],1.0,0.0,0.0)
        glRotatef(self.mouse_handler.getRotation()[1],0.0,0.0,1.0)
       
        #self.drawBrett.drawBrettTop()   
 
        #self.drawBrett.drawBrettButtom()
        self.drawBrett_()
        self.drawBrett_side()
        self.drawBrikke()
       
      
        #glCallList (1)    
        
        glutSwapBuffers()
        glFlush() 
        return
    
    def reshape (self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, width/height, 1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 3, 5, 
                  0, 0, 0, 
                  0, 1, 0)
    
    def main(self):
    
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800,800)
        glutCreateWindow('TDT4195 Peter Holiman')
    
        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        lightZeroPosition = [10.,4.,10.,1.]
        lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)
        
        
        
        
        
        self.initBrikke()
        
       # print self.brikker
        glutDisplayFunc(self.display)
        
        glMatrixMode(GL_PROJECTION)
        gluPerspective(40,1,10,40)
        gluLookAt(0,0,12,
          0,0,0,
          0,1,0)
        glutReshapeFunc (self.reshape)
        glutMotionFunc (self.mouse_moved)
        glutMouseFunc (self.mouse_pressed)
    
        glMatrixMode(GL_MODELVIEW)
    
        glutKeyboardFunc(self.keyPress)
        
        glutMainLoop()
        
        return
    
    #800x486
project = Project()
project.main()