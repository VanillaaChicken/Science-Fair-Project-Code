from ursina import *                    # Import the Ursina engine.

# Window Settings
app = Ursina()                          # Initialise your Ursina app.
window.title = 'Ursina Game Test App'   # Window title.
window.borderless = False               
window.fullscreen = False               
window.exit_button.visible = False      
window.fps_counter.enabled = True 
window.forced_aspect_ratio = '1.25'  
size = 1.25

# Cube List
cubes = []                                          # Create the list
cube = Entity(model='cube', color=color.orange, scale=(2,2,2))
cubes.append(cube)                                  # Add the cube to the list

# New Cube when 'c' pressed.
def input(key):
    if key == 'space':
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        cube.color = color.rgb(red, green, blue)   # Note I still can reference any individual object I want

    if key == 'c':
        x = random_generator.random() * 10 - 5     # Value between -5 and 5
        y = random_generator.random() * 10 - 5     # Value between -5 and 5
        z = random_generator.random() * 10 - 5     # Value between -5 and 5
        s = random_generator.random() * 1          # Scale between 0 and 1
        # Create the new cube and add it to the list
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255
        newcube = Entity(parent=cube, model='cube', color=color.rgb(red, green, blue), position=(x, y, z), scale=(s,s,s))
        cubes.append(newcube)
        num = 1
        print('New Cube Added.')


# Cubes
cube = Entity(model='cube', color=color.orange, scale=(2,2,2))
random_generator = random.Random()      # Random # generator.
def update():
    cube.rotation_y += time.dt * 100                 # Rotate every time update is called
    if held_keys['r']:                               # If r is pressed
        red = random_generator.random() * 255
        green = random_generator.random() * 255
        blue = random_generator.random() * 255

        cube.color = color.rgb(red, green, blue)

        for entity in cubes:                             # Go through the cube list
            entity.rotation_y += time.dt * 100           # Rotate all the cubes every time update is called
        if held_keys['q']:                               # If q is pressed
            camera.position += (0, time.dt, 0)           # move up vertically
        if held_keys['a']:                               # If a is pressed
            camera.position -= (0, time.dt, 0)           # move down vertically      
        # ! Note: R has to be help in order to move up and down.
# Runs App 
app.run()                               