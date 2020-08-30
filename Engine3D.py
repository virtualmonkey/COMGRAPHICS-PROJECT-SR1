from gl import Render, color, V2, V3
from obj import Obj, Texture
from shaders import *
from numpy import random

r = Render(1900,1200)

for x in range (2,1900-2):
    for y in range (2, 1200-2):
        
        size=random.randint(1,1200)
        if size==1:
            r.glVertex_coord(x,y)
        elif size==2:
            r.glVertex_coord(x,y)
            r.glVertex_coord(x+1,y)
            r.glVertex_coord(x,y+1)
            r.glVertex_coord(x+1,y+1)
            
posModel = V3(0, 0, -5)

r.lookAt(posModel, V3(0,0,0))

r.active_texture = Texture('./models/earthday.bmp')
r.active_shader = unlit
r.loadModel('./models/earth.obj', V3(-4,-2.5,-6), V3(0.002,0.002,0.002), V3(0,0,45))


r.active_texture = Texture('./models/spaceship.bmp')
r.active_shader = phong
r.loadModel('./models/spaceship.obj', V3(2,1.4,-5.5), V3(0.003,0.003,0.003), V3(0,0,-30))

r.active_texture = Texture('./models/space-shuttle.bmp')
r.active_shader = toon
r.loadModel('./models/space-shuttle.obj', V3(-1.5,-0.7,-5), V3(0.002,0.002,0.002), V3(-10,200,-30))


r.active_texture = Texture('./models/mars.bmp')
r.active_shader = predominantColor
r.loadModel('./models/earth.obj', V3(0,0,-6), V3(0.002,0.002,0.002), V3(0,0,45))

r.active_texture = Texture('./models/jupyter.bmp')
r.active_shader = coolShader
r.loadModel('./models/earth.obj', V3(4,2.5,-6), V3(0.002,0.002,0.002), V3(0,0,45))


r.glFinish('output.bmp')

