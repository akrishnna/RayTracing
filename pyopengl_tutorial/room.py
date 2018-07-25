import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

room_vertices = (
	(-1,-3,-1),
	( 1,-3,-1),
	(-1,-3, 3),
	( 1,-3, 3),
	)

room_edges = (
	(0,1),
	(0,2),
	(1,3),
	(2,3)
	)

room_surfaces = (
	(0,1,2,3)
	)

room_color = (
	(1,0,0)
	)

def room()
	glBegin(GL_QUADS)
	for surface in room_surfaces:
		x = 0
		for vertex in surface:
			x += 1
			glColor3fv(room_color[x])
			glVertex3fv(room_vertices[vertex])
	glEnd