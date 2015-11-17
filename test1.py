from OpenGL.GL import shaders
from OpenGL.arrays import vbo
from OpenGL.GL import *
from OpenGL.raw.GL.ARB.vertex_array_object import glGenVertexArrays, \
                                                  glBindVertexArray

import pygame

import numpy as np

def run():
    pygame.init()
    screen = pygame.display.set_mode((800,600), pygame.OPENGL)

    #Create the Vertex Array Object
    vertexArrayObject = GLuint(0)
    glGenVertexArrays(1, vertexArrayObject)
    glBindVertexArray(vertexArrayObject)

    #Create the VBO
    vertices = np.array([[0,1,0],[-1,-1,0],[1,-1,0]], dtype='f')
    vertexPositions = vbo.VBO(vertices)

    #Create the index buffer object
    indices = np.array([0,1,2], dtype='uint16')
    indexPositions = vbo.VBO(indices, target=GL_ELEMENT_ARRAY_BUFFER)

    indexPositions.bind()
    vertexPositions.bind()

    glEnableVertexAttribArray(0) # from 'location = 0' in shader
    glVertexAttribPointer(0, 3, GL_FLOAT, False, 0, None)

    glBindVertexArray(0)
    vertexPositions.unbind()
    indexPositions.unbind()

    #Now create the shaders
    VERTEX_SHADER = shaders.compileShader("""
    #version 330
    layout(location = 0) in vec4 position;
    void main()
    {
        gl_Position = position;
    }
    """, GL_VERTEX_SHADER)

    FRAGMENT_SHADER = shaders.compileShader("""
    #version 330
    out vec4 outputColor;
    void main()
    {
        outputColor = vec4(0.0f, 1.0f, 0.0f, 1.0f);
    }
    """, GL_FRAGMENT_SHADER)

    shader = shaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)

    #The draw loop
    while True:
        glUseProgram(shader)
        glBindVertexArray(vertexArrayObject)

        #glDrawArrays(GL_TRIANGLES, 0, 3) #This line works
        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, 0) #This line does not

        glBindVertexArray(0)
        glUseProgram(0)

        # Show the screen
        pygame.display.flip()

run()