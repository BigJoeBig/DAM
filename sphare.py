from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math
from Brikke import Brikke

name = 'TDT4195 Peter Holiman'
#// angle of rotation for the camera direction
angle=0.0
#// actual vector representing the camera's direction
lx=0.0
lz=-1.0
#// XZ position of the camera
x=0.0
z=5.0

brikker = [] 

class brikke(object):
    def __init__(self, x, y, isRed, id):
        self.x = x
        self.y = y
        self.isRed = isRed 
        self.id = id
        self.drawsphare(x, y, isRed)
        
    def drawsphare(self, x, y, isRed):
        glPushMatrix();
        #x=-3.5 er  ventre x=3.5 er  hoyre , y=2,5 er topp  y=-2.5 er bunn
        glTranslatef(x, y, 0);
        red = [1.0,0.,0.,1.]
        white = [1.,1.,1.,1.]
        if isRed==1.0:
            glMaterialfv(GL_FRONT,GL_DIFFUSE,red)
        else:
            glMaterialfv(GL_FRONT,GL_DIFFUSE,white)
        glutSolidSphere(0.5,40,40)
        glPopMatrix();
        
    def flytt(self, x, y, isRed):
        print('mordi')
        glPushMatrix();
        self.drawsphare(x, y, isRed)
            
    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800,800)
    glutCreateWindow(name)

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
    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40,1,10,40)
    glMatrixMode(GL_MODELVIEW)
    
    glutKeyboardFunc(processSpecialKeys)
   # glutSpecialFunc(processSpecialKeys);

    glPushMatrix()
    glutMainLoop()
    return
def drawBoard():
#     color = [1.0,0.,0.,1.]
#     glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
#     glRectf(0,0,1,1)
    red=GLfloat_3(1,0,0)
    blue=GLfloat_3(0,0,1)
    for x in range(0, 8):
            for y in range(0,5):
                if (x + y) % 2 == 0:
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,blue)
                else:
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,red)   
                glRectf(x-4, y-2, x -3, y -1)
                
                
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

    fraction = 0.1;
    print key

    if key == 's' :
        brikker[4].flytt(0.0, 0.0, 0.0) #hvorfor faen funker ikke denne.    ..
        
        
        
  
           
    
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    
    gluLookAt(0,0,12,
          0,0,0,
          0,1,0)
    
    drawBoard()
    
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
            
    glPopMatrix()
    glutSwapBuffers()
    return
#800x486
if __name__ == '__main__': main()
