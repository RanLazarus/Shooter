from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import triplanar_shader
from ursina.shaders import basic_lighting_shader
from ursina.shaders import unlit_shader

modea = 1

square = 4
app = Ursina()
firing = 0
mapp = 1
globaltimer = 0
localtimer = 0

crosshair = Entity(
    model='cube',
    origin_y=0,
    parent=camera.ui,
    scale_x=0.1,
    scale_y=0.1,
    scale_z=0.1,
    texture=load_texture('crosshair.png'),
)


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


savetime = 0

skytext = load_texture('skyboxes.png')
skytext2 = load_texture('sunsets.png')
skytext3 = load_texture('midnights.png')


def update():
    global firing, punch_sound, globaltimer, localtimer, savetime, modea
    if held_keys['p']:
        exit()

    # water.on_trigger_enter = Func(math, player.y += 1)

    globaltimer += 1
    localtimer += 1

    if held_keys['o']:
        player.y += 10

    if held_keys['i']:
        player.x, player.y, player.z = player.x, player.y, player.z


# player settings
player = FirstPersonController()
player.collider = 'sphere'


player.speed = 15

if mapp == 1:
    pivot = Entity(shape='sphere')
    world1 = DirectionalLight(parent=pivot, x=10, y=50, z=200, shadows=True, color=color.rgb(150, 150, 150), direction=(1, 100, 100), shader=triplanar_shader)
    world2 = AmbientLight(color=color.rgb(125, 125, 125), shader=triplanar_shader)
    sun = SpotLight(x=10, y=50, z=200, color=color.rgb(256, 256, 256), parent=scene, scale=100, shader=triplanar_shader)
    antisun = PointLight(x=10, y=50, z=200, color=color.rgb(-106, -106, -106), parent=scene, scale=100, shader=triplanar_shader)

    # floor
    grass = Entity(model='cube', x=0, y=-2, z=0, texture=load_texture('grasses.png'), scale_x=150, scale_y=0.01,
                   scale_z=140, collider='box')
    grass2 = Entity(model='cube', x=-10, y=-5, z=-10, texture=load_texture('grasses.png'), scale_x=20, scale_y=0.01,
                   scale_z=20, collider='box')
    #Road
    Road = Entity(model='cube', x=-0, y=-2, z=-0, texture=load_texture('stones.png'), scale_x=20, scale_y=0.11,
                   scale_z=120, collider='box')
    Side_Walk = Entity(model='cube', x=-0, y=-2, z=-0, texture=load_texture('stone.png'), scale_x=25, scale_y=0.10,
                   scale_z=120, collider='box')
    #Road_End
    Road_Wall_1 = Entity(model='cube', x=-0, y=0, z=-60, texture=load_texture('stone.png'), scale_x=25, scale_y=15,
                   scale_z=10, collider='box')
    Road_Wall_2 = Entity(model='cube', x=-0, y=0, z=60, texture=load_texture('stone.png'), scale_x=25, scale_y=15,
                   scale_z=10, collider='box')
    #World Walls
    #To be made after backyards



    #House 1
    H1_Floor = Entity(model='cube', x=-40, y=-2, z=-35, texture=load_texture('stone.png'), scale_x=30, scale_y=0.30,
                   scale_z=40, collider='box')
    #House 2
    H2_Floor = Entity(model='cube', x=40, y=-2, z=-35, texture=load_texture('stone.png'), scale_x=30, scale_y=0.30,
                   scale_z=40, collider='box')
    #House 3
    H3_Floor = Entity(model='cube', x=-40, y=-2, z=35, texture=load_texture('stone.png'), scale_x=30, scale_y=0.30,
                   scale_z=40, collider='box')
    #House 4
    H4_Floor = Entity(model='cube', x=40, y=-2, z=35, texture=load_texture('stone.png'), scale_x=30, scale_y=0.30,
                   scale_z=40, collider='box')

    # plat1
    plat1 = Entity(model='cube', texture=load_texture('crates.png'), scale_x=2, scale_y=2,
                   scale_z=2, collider='box', y = -1, x = -3, z = -3)
    plat1shadow = Entity(model='cube', texture=None, color=color.rgba(0, 0, 0, 50), scale_x=2, scale_z=2, scale_y=0.002,
                         x=-3, y=-1.9, z=-1)
    player.y = grass.y

Sky()
app.run()