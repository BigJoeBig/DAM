from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from var import *

class DrawBrett:
    
    def __init__(self):
        pass

    def drawBrettTop(self):
        red=GLfloat_3(1,0,0)
        blue=GLfloat_3(0,0,1)
        for i in range (0,6):
            for j in range (0,6):
                glBegin(GL_POLYGON)
                if (i%2 == 0 and j%2 != 0) or (i%2 != 0 and j%2 == 0):
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,red)
                else:
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,blue) 
                glVertex3f((-4+i)*blockSize, (-4+j)*blockSize, 0)
                glVertex3f((-4+i+1)*blockSize, (-4+j)*blockSize, 0)
                glVertex3f((-4+i+1)*blockSize, (-4+j+1)*blockSize, 0)
                glVertex3f((-4+i)*blockSize, (-4+j+1)*blockSize, 0)
                glEnd()

    def drawBrettButtom(self):
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5, 0.5, 0.5, 0])

        # board bottom
        glBegin(GL_POLYGON)
        glVertex3f(-4*blockSize,-4*blockSize,-blockSize/2)
        glVertex3f(-4*blockSize,4*blockSize,-blockSize/2)
        glVertex3f(4*blockSize,4*blockSize,-blockSize/2)
        glVertex3f(4*blockSize,-4*blockSize,-blockSize/2)
        glEnd()

        # board sides:
        glBegin(GL_POLYGON)
        glVertex3f(-4*blockSize,-4*blockSize,-blockSize/2)
        glVertex3f(-4*blockSize,4*blockSize,-blockSize/2)
        glVertex3f(-4*blockSize,4*blockSize,0)
        glVertex3f(-4*blockSize,-4*blockSize,0)
        glEnd()

        glBegin(GL_POLYGON)
        glVertex3f(4*blockSize,4*blockSize,-blockSize/2)
        glVertex3f(4*blockSize,-4*blockSize,-blockSize/2)
        glVertex3f(4*blockSize,-4*blockSize,0)
        glVertex3f(4*blockSize,4*blockSize,0)
        glEnd()

        glBegin(GL_POLYGON)
        glVertex3f(-4*blockSize,4*blockSize,-blockSize/2)
        glVertex3f(4*blockSize,4*blockSize,-blockSize/2)
        glVertex3f(4*blockSize,4*blockSize,0)
        glVertex3f(-4*blockSize,4*blockSize,0)
        glEnd()

        glBegin(GL_POLYGON)
        glVertex3f(-4*blockSize,-4*blockSize,-blockSize/2)
        glVertex3f(4*blockSize,-4*blockSize,-blockSize/2)
        glVertex3f(4*blockSize,-4*blockSize,0)
        glVertex3f(-4*blockSize,-4*blockSize,0)
        glEnd()    