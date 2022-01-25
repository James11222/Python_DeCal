from vpython import *

ball_1 = sphere(pos=vector(500,0,500), radius = 100, color=color.red)
x_axis = arrow(pos=vector(0,0,0), axis=1000*vector(1,0,0))
y_axis = arrow(pos=vector(0,0,0), axis=1000*vector(0,1,0))
z_axis = arrow(pos=vector(0,0,0), axis=1000*vector(0,0,1))
velocity = vector(0,20,0)


# while ball_1.pos.x < 1000:
#     rate(60)
#     if ball_1.pos.x > 800:
#         velocity *= -1
#     elif ball_1.pos.x < 100:
#         velocity *= -1
#     ball_1.pos += velocity


#a bouncing ball
while True:
    rate(60)
    if ball_1.pos.y < 0:
        velocity.y *= -1

    ball_1.pos += velocity
    velocity.y -= 1

print("finished")
