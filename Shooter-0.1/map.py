
from ursina import *
import os
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import triplanar_shader
from ursina.shaders import basic_lighting_shader
from ursina.shaders import unlit_shader

class Map:
    def __init__(self):
        for y in range(1, 4, 2):
            # floor
            grass = Entity(model='cube', x=0, y=-2, z=0, texture=load_texture('grasses.png'), scale_x=150, scale_y=0.01,
                           scale_z=140, collider='box')
            grass2 = Entity(model='cube', x=-10, y=-5, z=-10, texture=load_texture('grasses.png'), scale_x=20,
                            scale_y=0.01,scale_z=20, collider='box')
            # Road
            Road = Entity(model='cube', x=-0, y=-2, z=-0, texture=load_texture('stone.jpg'), scale_x=20, scale_y=0.11,
                          scale_z=120, collider='box')
            Side_Walk = Entity(model='cube', x=-0, y=-2, z=-0, texture=load_texture('stones.jpg'), scale_x=25,
                               scale_y=0.10,scale_z=120, collider='box')
            # Road_End
            Road_Wall_1 = Entity(model='cube', x=-0, y=0, z=-60, texture=load_texture('stone.jpg'), scale_x=25,
                                 scale_y=15,scale_z=10, collider='box')
            Road_Wall_2 = Entity(model='cube', x=-0, y=0, z=60, texture=load_texture('stone.jpg'), scale_x=25,
                                 scale_y=15,scale_z=10, collider='box')
            # World Walls
            # To be made after backyards

            # House 1
            H1_Floor = Entity(model='cube', x=-40, y=-2, z=-35, texture=load_texture('stone.jpg'), scale_x=30,
                              scale_y=0.30,cale_z=40, collider='box')
            # House 2
            H2_Floor = Entity(model='cube', x=40, y=-2, z=-35, texture=load_texture('stone.jpg'), scale_x=30,
                              scale_y=0.30,scale_z=40, collider='box')
            # House 3
            H3_Floor = Entity(model='cube', x=-40, y=-2, z=35, texture=load_texture('stone.jpg'), scale_x=30,
                              scale_y=0.30,scale_z=40, collider='box')
            # House 4
            H4_Floor = Entity(model='cube', x=40, y=-2, z=35, texture=load_texture('stone.jpg'), scale_x=30,
                              scale_y=0.30,cale_z=40, collider='box')

            # plat1
            plat1 = Entity(model='cube', texture=load_texture('crates.png'), scale_x=2, scale_y=2,
                           scale_z=2, collider='box', y=-1, x=-3, z=-3)
            plat1shadow = Entity(model='cube', texture=None, color=color.rgba(0, 0, 0, 50), scale_x=2, scale_z=2,
                                 scale_y=0.002,x=-3, y=-1.9, z=-1)
            Spawn_Point_1 = Entity(model='cube', x=5, y=-2, z=5, texture=load_texture('stone.jpg'), scale_x=3,
                              scale_y=0.30,scale_z=3, collider='box')
            Spawn_Point_2 = Entity(model='cube', x=-5, y=-2, z=-5, texture=load_texture('stone.jpg'), scale_x=3,
                              scale_y=0.30,scale_z=3, collider='box')
            Spawn_Point_3 = Entity(model='cube', x=-5, y=-2, z=5, texture=load_texture('stone.jpg'), scale_x=3,
                              scale_y=0.30,scale_z=3, collider='box')
            Spawn_Point_4 = Entity(model='cube', x=5, y=-2, z=-5, texture=load_texture('stone.jpg'), scale_x=3,
                              scale_y=0.30,scale_z=3, collider='box')
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=load_texture('skyboxes.png'),
            scale=15000,
            double_sided=True,
            shading=True,
            shader=basic_lighting_shader
        )
