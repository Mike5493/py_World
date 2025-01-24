from noise import pnoise2

def generate_voxel_world(size_x, size_z, height, scale=0.1):
    world = {}
    for x in range(size_x):
        for z in range(size_z):
            # Generate terrain height using Perlin Noise