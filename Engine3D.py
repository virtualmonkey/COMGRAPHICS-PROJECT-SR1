from gl import Render, color, V2, V3
from obj import Obj, Texture
from shaders import *
from numpy import random

r = Render(2500,1800)

for x in range (15,2500-2):
    for y in range (15, 1800-2):
        size=random.randint(1,1080)
        if size==2 and x%2 != 0 and y%2 != 0:
            for i in range (1,15):
                r.glVertex_coord(x,y)
                r.glVertex_coord(x+i,y)
                r.glVertex_coord(x,y+i)
                r.glVertex_coord(x-i,y)
                r.glVertex_coord(x,y-i)
            
posModel = V3(0, 0, -5)

r.lookAt(posModel, V3(0,0,0))


r.active_texture = Texture('./models/earthday.bmp')
r.active_shader = mutedColors
r.loadModel('./models/earth.obj', V3(-4,-2.5,-7), V3(0.003,0.003,0.003), V3(0,0,45))


r.active_texture = Texture('./models/spaceship.bmp')
r.active_shader = phong
r.loadModel('./models/spaceship.obj', V3(2,1.4,-6), V3(0.003,0.003,0.003), V3(0,0,-30))

r.active_texture = Texture('./models/rocket.bmp')
r.active_shader = toon
r.loadModel('./models/rocket.obj', V3(-1.5,-0.7,-4), V3(0.003,0.003,0.003), V3(-10,200,-30))


r.active_texture = Texture('./models/mars.bmp')
r.active_shader = predominantColor
r.loadModel('./models/earth.obj', V3(0,0,-10), V3(0.003,0.003,0.003), V3(0,0,45))

r.active_texture = Texture('./models/jupyter.bmp')
r.active_shader = coolShader
r.loadModel('./models/earth.obj', V3(4,2.5,-7), V3(0.003,0.003,0.003), V3(0,0,45))


r.glFinish('output.bmp')

