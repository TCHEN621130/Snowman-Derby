Web VPython 3.2
#
# game_starter.py
#
# Building an interaction with 3D graphics using Python
#   Documentation: http://www.glowscript.org/docs/VPythonDocs/index.html
#   Examples:      http://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
#
#Team members: William Koh, Terence Chen, Jared Carreno 

scene.bind('keydown', keydown_fun)     # Function for key presses
scene.bind('click', click_fun)         # Function for mouse clicks
scene.background = color.blue    # Light gray (0.8 out of 1.0)
scene.width = 640                      # Make the 3D canvas larger
scene.height = 480


# +++ start of OBJECT_CREATION section
# These functions create "container" objects, called "compounds"
#snowman function here 

def make_blood(x_coordinate, z_coordinate):
    """Create blood puddle at location where snowman was killed"""
    blood = cylinder(pos = vec(x_coordinate, -0.5, z_coordinate), axis=vec(0,1,0), size=vec(.05,1,1), color = color.red)
    return blood
    
def make_snowman(starting_position, starting_vel = vec(0, 0, 0)):
  """
  Snowman class here 
  """

  snowman_body = sphere(size = 1*vec(1, 1, 1),
                        pos = vec(0, 0, 0),
                        color = color.white
                        )
  snowman_body2 = sphere(size = 0.8*vec(1, 1, 1),
                        pos = vec(0, 0.5, 0),
                        color = color.white
                        )
  snowman_body3 = sphere(size = 0.6*vec(1, 1, 1),
                        pos = vec(0, 0.9, 0),
                        color = color.white
                        )
  snowman_eye1 = sphere(size = 0.13*vec(1, 1, 1),
                        pos = vec(0.14, 1, 0.2),
                        color = color.black
                        )
  snowman_eye2 = sphere(size = 0.13*vec(1, 1, 1),
                        pos = vec(0, 1, 0.25),
                        color = color.black
                        )
  snowman_eye3 = sphere(size = 0.13*vec(1, 1, 1),
                        pos = vec(-0.14, 1, 0.2),
                        color = color.black
                        )
  snowman_nose = cone(pos=vec(0,0.9,0.25),
                      axis=vec(1,0,1),
                      radius=0.05,
                      length = 0.4,
                      color = color.orange
                     )
  snowman_hat = cylinder(pos = vec(0, 1.1, 0),
                         axis = vec(.02, .2, -.02),
                         size = 0.65*vec(0.2, 0.7, 0.7),
                         color = color.red
                         )
                        
  handle = cylinder( size=vector(1,.2,.2),                   
                   color=vector(0.72,0.42,0),
                   pos = vector(0,0.8,0)
                   )
  head = box( size=vector(.2,.6,.2), pos=vector(1.1,0.8,0),              
            color=color.white)
  hammer = compound([handle, head])
  hammer.axis = vector(1,1,0)
                         
  snowman_objects = [snowman_body, snowman_body2, snowman_body3, snowman_eye1,
  snowman_eye2, snowman_eye3, snowman_nose, snowman_hat, hammer]
  com_snowman = compound(snowman_objects, pos = starting_position)
  com_snowman.vel = starting_vel    # Set the initial velocity
  return com_snowman




# The ground is represented by a box (vPython's rectangular solid)
# http://www.glowscript.org/docs/VPythonDocs/box.html
#
ground = box(size = vec(20, 1, 20),
             pos = vec(0, -1, 0),
             color = color.white)
            
wallA = box(pos=vector(0,0,-10), axis=vector(1,0,0), size=vector(20,1,.2), color=color.red) # amber
wallB = box(pos=vector(-10,0,0), axis=vector(0,0,1), size=vector(20,1,.2), color=color.green)   # blue
wallC = box(pos=vector(0,0, 10), axis=vector(1,0,0), size=vector(20,1,.2), color=color.red)   # fuschia
wallD = box(pos=vector( 10,0,0), axis=vector(0,0,1), size=vector(20,1,.2), color=color.green)  # green
# Gates
gateA = box(pos = vec(5, -.5, 0),
            size = vec(1, .5, 15),
            color = color.green  # Amber
            )
gateB = box(pos = vec(-5, -.5, 0),
            size = vec(1, .5, 15),
            color = color.red  # Amber
            )
gateC = box(pos = vec(3.5, -.5, -7),
            size = vec(1, .5, 2),
            axis=vector(0,0,1),
            color = color.green  # Amber
            )
gateD = box(pos = vec(-3.5, -.5, -7),
            size = vec(1, .5, 2),
            axis=vector(0,0,1),
            color = color.red  # Amber
            )
gateE = box(pos = vec(3.5, -.5, 7),
            size = vec(1, .5, 2),
            axis=vector(0,0,1),
            color = color.green  # Amber
            )
gateF = box(pos = vec(-3.5, -.5, 7),
            size = vec(1, .5, 2),
            axis=vector(0,0,1),
            color = color.red  # Amber
            )

# Create a ball that we will be able to control
#
ball = sphere(size = 1.0*vec(1, 1, 1),  # Ball is an object of class sphere
              color = color.green,
              pos = vec(0,0,5)
              )
ball.vel = vec(0, 0, 0)                 # This is its initial velocity


snowman1 = make_snowman(starting_position = vec(0, 0, -5))
snowman2 = make_snowman(starting_position = vec(2, 0, -5))
snowman3 = make_snowman(starting_position = vec(-2, 0, -5))

snowman4 = make_snowman(starting_position = vec(-9, 0, -9))
snowman5 = make_snowman(starting_position = vec(-9, 0, 9))
snowman6 = make_snowman(starting_position = vec(9, 0, -9))
snowman7 = make_snowman(starting_position = vec(9, 0, 9))
# +++ end of OBJECT_CREATION section


# +++ start of ANIMATION section

# Other constants
#
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vec(0, -2, -2)  # Ask for a bird's-eye view of the scene...

# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt


while True:

    rate(RATE)                              # Maximum number of times per second
                                            # ..that the while loop runs

    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step

#    alien1.pos = alien1.pos + alien1.vel*dt # Update the first alien's position
    ball.pos = ball.pos + ball.vel*dt       # Update the ball's position
    ball.vel = ball.vel * 0.995             # Friction
    snowman1.pos = snowman1.pos + snowman1.vel*dt
    snowman2.pos = snowman2.pos + snowman2.vel*dt
    snowman3.pos = snowman3.pos + snowman3.vel*dt

    snowman4.rotate(angle=180,
           axis= vec(0,1,0),
           origin=vec(-9, 0, -9))
    snowman5.rotate(angle=180,
           axis= vec(0,1,0),
           origin=vec(-9, 0, 9))
    snowman6.rotate(angle=180,
           axis= vec(0,1,0),
           origin=vec(9, 0, -9))
    snowman7.rotate(angle=180,
           axis= vec(0,1,0),
           origin=vec(9, 0, 9))
    # +++ End of PHYSICS UPDATES -- be sure new objects are updated appropriately!


    # +++ Start of COLLISIONS -- check for collisions & do the "right" thing
    gate_collide(ball)
  
    snowman_collide(snowman1)
    snowman_collide(snowman2)
    snowman_collide(snowman3)

    # If the ball collides with the first alien, give the alien
    # a vertical velocity
    if mag(ball.pos - snowman1.pos) < 1.0:
        make_blood(snowman1.pos.x, snowman1.pos.z)
        snowman1.pos = vec(0, -5, 0)
        snowman1.vel = vec(0, 0, 0)
    
        
    if mag(ball.pos - snowman2.pos) < 1.0:
        make_blood(snowman2.pos.x, snowman2.pos.z)
        snowman2.pos = vec(0, -5, 0)
        snowman2.vel = vec(0, 0, 0)
        
    
    if mag(ball.pos - snowman3.pos) < 1.0:
        make_blood(snowman3.pos.x, snowman3.pos.z)
        snowman3.pos = vec(0, -5, 0)
        snowman3.vel = vec(0, 0, 0)
        
    
    # If a snowman goes outside the gate, restart the game
    if snowman1.pos.z > 8.0:
        lose_game()
    
    if snowman2.pos.z > 8.0:
        lose_game()
    
    if snowman3.pos.z > 8.0:
       lose_game()
      
    # If ALL THREE SNOWMEN ARE DEAD RESTART

    if snowman1.pos == vec(0, -5, 0) and snowman2.pos == vec(0,-5,0) and snowman3.pos == vec(0,-5,0):
        win_game()
        
    # +++ End of COLLISIONS



# +++ Start of EVENT-HANDLING section--separate functions for
#                                keypresses and mouse clicks...

def keydown_fun(event):
    """This function is called each time a key is pressed."""
    key = event.key
    ri = randint(0, 10)

    amount = 0.42               # "Strength" of the keypress's velocity changes
    if key == 'up' or key in 'wWiI':
        ball.vel = ball.vel + vec(0, 0, -amount)
    elif key == 'left' or key in 'aAjJ':
        ball.vel = ball.vel + vec(-amount, 0, 0)
    elif key == 'down' or key in 'sSkK':
        ball.vel = ball.vel + vec(0, 0, amount)
    elif key == 'right' or key in "dDlL":
        ball.vel = ball.vel + vec(amount, 0, 0)
    elif key in ' rR':
        ball.vel = vec(0, 0, 0) # Reset! via R or the spacebar, " "
        ball.pos = vec(0, 0, 5)
    elif key in 'gG':   # grutor mode! stop the snowmans
        snowman1.vel = vec(0, 0, 0)
        snowman2.vel = vec(0, 0, 0)
        snowman3.vel = vec(0, 0, 0)
        

def click_fun(event):
    """This function is called each time the mouse is clicked."""
    start()
    
def start():
    """Begins the game and moves the snowmans"""
    snowman1.vel = 4*vec.random() 
    snowman1.vel.y = 0.0  
    snowman2.vel = 6*vec.random() 
    snowman2.vel.y = 0.0 
    snowman3.vel = 10*vec.random() 
    snowman3.vel.y = 0.0 

# gate collision
def gate_collide(ball):
    """Handles collision between ball and the gates"""
    
    # if the ball hits gateA
    if ball.pos.x > gateA.pos.x: # hit - check for z
        ball.pos.x = gateA.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the z velocity

    # if the ball hits gateB
    if ball.pos.x < gateB.pos.x: # hit - check for x
        ball.pos.x = gateB.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the x velocity
#        
    # if the ball hits gateC
    if ball.pos.z < gateC.pos.z: # hit - check for z
        ball.pos.z = gateC.pos.z  # bring back into bounds
        ball.vel.z *= -1.0        # reverse the z velocity
#
#    # if the ball hits gateD
    if ball.pos.x < gateD.pos.x: # hit - check for x
        ball.pos.x = gateD.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the x velocity
#    
    # gate e
    if ball.pos.z > gateE.pos.z: # hit - check for x
        ball.pos.z = gateE.pos.z  # bring back into bounds
        ball.vel.z *= -1.0        # reverse the x velocity
#
    # gate f
    if ball.pos.x < gateF.pos.x: # hit - check for x
        ball.pos.x = gateF.pos.x  # bring back into bounds
        ball.vel.x *= -1.0        # reverse the x velocity


# Snowman Collision
def snowman_collide(snowman):
    """Handles collision between snowman and the gates"""
    # if the ball hits gateA
    if snowman.pos.x > gateA.pos.x: # hit - check for z
        snowman.pos.x = gateA.pos.x  # bring back into bounds
        snowman.vel.x *= -1.0        # reverse the z velocity

    # if the ball hits gateB
    if snowman.pos.x < gateB.pos.x: # hit - check for x
        snowman.pos.x = gateB.pos.x  # bring back into bounds
        snowman.vel.x *= -1.0        # reverse the x velocity
#        
    # if the ball hits gateC
    if snowman.pos.z < gateC.pos.z: # hit - check for z
        snowman.pos.z = gateC.pos.z  # bring back into bounds
        snowman.vel.z *= -1.0        # reverse the z velocity
#
#    # if the ball hits gateD
    if snowman.pos.x < gateD.pos.x: # hit - check for x
        snowman.pos.x = gateD.pos.x  # bring back into bounds
        snowman.vel.x *= -1.0        # reverse the x velocity


# +++ End of EVENT-HANDLING section


def lose_game():
    """Resets the game if a snowman makes it past the gate"""
    print("You lose!")
    ball.vel = vec(0, 0, 0) # Reset! via R or the spacebar, " "
    ball.pos = vec(0, 0, 5)
    
    snowman1.vel = vec(0,0,0)
    snowman1.pos = vec(0, 0, -5)
    
    snowman2.vel = vec(0,0,0)
    snowman2.pos = vec(2, 0, -5)
    
    snowman3.vel = vec(0,0,0)
    snowman3.pos = vec(-2, 0, -5)
 

def win_game():
    """Resets the game if player kills all three snowmans"""
    print("You Win! Thanks for Playing!")
    ball.vel = vec(0, 0, 0) # Reset! via R or the spacebar, " "
    ball.pos = vec(0, 0, 5)

    snowman1.vel = vec(0,0,0)
    snowman1.pos = vec(0, 0, -5)
    
    snowman2.vel = vec(0,0,0)
    snowman2.pos = vec(2, 0, -5)
    
    snowman3.vel = vec(0,0,0)
    snowman3.pos = vec(-2, 0, -5)
 



def choice(L):
    """Implements Python's choice using the random() function."""
    LEN = len(L)                        # Get the length
    randomindex = int(LEN*random())     # Get a random index
    return L[randomindex]               # Return that element

def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low               # Swap if out of order!
    LEN = int(hi) - int(low) + 1.       # Get the span and add 1
    randvalue = LEN*random() + int(low) # Get a random value
    return int(randvalue)               # Return the integer part of it

def randcolor():
    """Returns a vector of (r, g, b) random from 0.0 to 1.0."""
    r = random()           # This is different than Python's random.uniform
    g = random()           # ..it automatically uses 0.0 to 1.0
    b = random()
    return vec(r, g, b)                 # A color is a three-element vector