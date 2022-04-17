from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0.06, exposure=2)
scene.set_floor(height=-1, color=(0.86,0.75,0.55))
scene.set_directional_light((-2, 3, -1), 0.1, (1, 1, 1))

@ti.func
def make_pyradmid(center, n, h):
    ci, ck = center
    for i, j, k in ti.ndrange((ci-n+1, ci+n), (0, h), (ck-n+1, ck+n)):
        x = ivec3(i, j, k)
        is_border = int(i >= ci-n+1+j and k >= ck-n+1+j and i <= ci+n-1-j and k <= ck+n-1-j and
         (ti.max(i-ci, k-ck) == n-1-j or ti.min(i-ci, k-ck) == j+1-n))
        scene.set_voxel(x, is_border, vec3(0.7568, 0.6039, 0.4941))

@ti.kernel
def initialize_voxels():
    make_pyradmid((0, 0), 30, 30)
    make_pyradmid((-32, 45), 8, 8)
    make_pyradmid((-16, 40), 6, 6)
    make_pyradmid((3, 40), 8, 8)
    make_pyradmid((20, 50), 9, 9)

initialize_voxels()

scene.finish()
