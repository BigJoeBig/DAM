from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 800, 600                               # window size

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    
    # ToDo draw rectangle
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    x,y,width,height = glGetDoublev(GL_VIEWPORT)
    gluPerspective(
        45, # field of view in degrees
        width/float(height or 1), # aspect ratio
        .25, # near clipping plane
        200, # far clipping plane
    )
    
    drawCheckerBoard()
    
    glutSwapBuffers()                                  # important for double buffering
    

def drawCheckerBoard(M=8, N=5, red=GLfloat_3(1,0,0), blue=GLfloat_3(0,0,1) ):
    """Draw an 2N*2N checkerboard with given colours"""
    glDisable(GL_LIGHTING)
    try:
        for x in range(0, N):
            for y in range(0,M):
                if (x + y) % 2 == 0:
                    glColor3fv(red)
                else:
                    glColor3fv(blue)    
                glRectf(x, y, x + 1, y + 1)
    finally:
        glEnable(GL_LIGHTING)
# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("TDT4195")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything