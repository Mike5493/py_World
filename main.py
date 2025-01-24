import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def init_window(width, height, title):
    if not glfw.init():
        raise Exception("GLFW can't initialize...")
    
    window = glfw.create_window(width, height, title, None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window can't be created...")
    
    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    return window

# Initialize the window
window = init_window(800, 600, "Voxel World")

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # TODO: Rendering logic

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()