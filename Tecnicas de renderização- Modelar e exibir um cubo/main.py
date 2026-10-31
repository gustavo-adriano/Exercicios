import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def conjunto_vertices():
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )
    return vertices

def conjunto_arestas():
    arestas = (
        (0,1),(0,3),(0,4),
        (2,1),(2,3),(2,7),
        (6,3),(6,4),(6,7),
        (5,1),(5,4),(5,7)
    )
    return arestas

def modelar_cubo():
    glBegin(GL_LINES)
    vertices = conjunto_vertices()
    arestas = conjunto_arestas()
    for aresta in arestas:
        for vertice in aresta:
            glVertex3fv(vertices[vertice])
    glEnd()

def rotacao_do_cubo():
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def principal(frotacionar):
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-7)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if(frotacionar):
            rotacao_do_cubo()
        modelar_cubo()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    habilitar_rotacao = True
    principal(habilitar_rotacao)