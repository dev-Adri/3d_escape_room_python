from ursina import *
from ursina.shaders import lit_with_shadows_shader
import random

app = Ursina()

window.title = 'My Game'
# window.borderless = True
window.exit_button.visible = True
window.fps_counter.enabled = True  

cube = Entity(model = "cube", scale = (2, 2, 2))

def update():
    cube.rotation_y += time.dt * 100

def input(key):
    if key == "s":
        cube.color = color.rgb(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

app.run()