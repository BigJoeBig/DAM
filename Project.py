from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math

name = 'TDT4195 Peter Holiman'
#// angle of rotation for the camera direction


brikker = [] 
BrikkeID = 0 
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
    def flyttV(self):    
        self.x = self.x-1.0    
    def flyttOpp(self):    
        self.y = self.y+1.0
    def flyttNed(self):    
        self.y = self.y-1.0
        
        #self.drawsphare()
        
        


    
    

def main():

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
    
    initBrikke()
    
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40,1,10,40)
    gluLookAt(0,0,12,
      0,0,0,
      0,1,0)
    

    glMatrixMode(GL_MODELVIEW)
    glutKeyboardFunc(processSpecialKeys)

    glPushMatrix()
    glutMainLoop()
    
    return

def initList():
    displayLists = glGenLists(1)
    glNewList(1, GL_COMPILE_AND_EXECUTE)
    drawBoard()
    glEndList()

def drawBoard():
#     color = [1.0,0.,0.,1.]
#     glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
#     glRectf(0,0,1,1)
#     red=GLfloat_3(1,0,0)
#     blue=GLfloat_3(0,0,1)
#     for x in range(0, 8):
#             for y in range(0,5):
#                 if (x + y) % 2 == 0:
#                     glMaterialfv(GL_FRONT,GL_DIFFUSE,blue)
#                 else:
#                     glMaterialfv(GL_FRONT,GL_DIFFUSE,red)   
#                 glRectf(x-4, y-2, x -3, y -1)
#     
    print 'draw'            
    #glPushMatrix();           
    red=GLfloat_3(1,0,0)
    blue=GLfloat_3(0,0,1)
    for i in range (0,8):
        for j in range (0,8):
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
                
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5, 0.5, 0.5, 0])
    # board bottom
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
    
    # board sides:
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
                
# def drawsphare(x, y, isRed):
#     glPushMatrix();
#     #x=-3.5 er  ventre x=3.5 er  hoyre , y=2,5 er topp  y=-2.5 er bunn
#     glTranslatef(x, y, 0);
#     red = [1.0,0.,0.,1.]
#     white = [1.,1.,1.,1.]
#     if isRed==1.0:
#         glMaterialfv(GL_FRONT,GL_DIFFUSE,red)
#     else:
#         glMaterialfv(GL_FRONT,GL_DIFFUSE,white)
# 
#     
#     
#     glutSolidSphere(0.5,40,40)
#     glPopMatrix();
#     color = [1.0,0.,0.,1.]
#     glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
#     glutSolidSphere(0.5,20,20)
#     glLoadIdentity()
#     glPushMatrix();
#     glTranslatef(0,10,-5);
#     #DrawObjectOne
#     glPopMatrix();
# #/DrawObjectTwo
#    # glTranslatef(0,10,-5);
#  
def rounding_X(x):
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
def rounding_Y(x):
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
            
     
              
def processSpecialKeys(key, xx, yy):
    print key
    print xx
    
    b = brikker[0] 
    if key == 'w' : 
             
        b.flyttOpp()
        
    elif key == 's' : 
             
        b.flyttNed()
        
    elif key == 'a' : 
             
        b.flyttV()
        
    elif key == 'd' : 
             
        b.flyttH()
        
     
        
    elif key == '1' :        
        BrikkeID = 0
        
    elif key == '2' :        
        BrikkeID = 1
        #b.printut()
    display()    
        
        
def initBrikke():
    
    with open('exp.txt') as f:
        lines = f.readlines()
        numbers =[float(e.strip()) for e in lines]
    
    brikke_id = 0;
    i = 0;  
    
    while i < len(numbers):
        x = rounding_X(((numbers[i]/800)*7.)-3.5)
        y = -rounding_Y(((numbers[i+1]/498)*5.)-3)
        isRed = numbers[i+2]
        
        b = brikke(x, y, isRed, brikke_id)
        brikker.append(b)
        print(numbers[i], x,numbers[i+1], y, numbers[i+2], isRed)
        i = i+3
        brikke_id = brikke_id+1        
  
def drawBrikke():
    for b in brikker:
        b.drawsphare()           
 
def reshape (width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, width/height, 1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 3, 5, 0, 0, 0, 0, 1, 0)    
    
    
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #glPushMatrix()
    drawBoard()
#     initList()
#     
#     
#     glCallList (1)
#    initBrikke()
    #glCallList(1)
    drawBrikke()
    
   # glPopMatrix()
    glutSwapBuffers()
    glFlush() 
    return
#800x486
main()