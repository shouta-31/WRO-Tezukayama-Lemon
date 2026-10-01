from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
target=0
turn_count=0
back_motor=Motor(Port.C)
front_motor=Motor(Port.D)
eyes=UltrasonicSensor(Port.E)
left_sensor=UltrasonicSensor(Port.A)
right_sensor=UltrasonicSensor(Port.B)
distance=0
timer=StopWatch()
hub.imu.reset_heading(0)
def right():
    turn_count=1
    print("Clock_turn")
    while True:
        print(right_sensor.distance())
        print(left_sensor.distance())
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,(0-Yaw)*2)
        speed=100+eyes.distance()
        back_motor.run(speed)
        print(Yaw)
        if eyes.distance()<500:
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,35)
                speed=(90-Yaw)*11+100
                back_motor.run(speed)
                print(Yaw)
                if Yaw>90:
                    back_motor.stop()
                    front_motor.run_target(1000,0)
                    turn_count=turn_count+1
                    print(turn_count/4,"周成功")
                    break
            hub.imu.reset_heading(0)
        if turn_count==12:
            break
def left():
    turn_count=1
    print("Un_clock_turn")
    while True:
        print(right_sensor.distance())
        print(left_sensor.distance())
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,(0-Yaw)*2)
        speed=100+eyes.distance()
        back_motor.run(speed)
        print(Yaw)
        if eyes.distance()<500:
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,-35)
                speed=(90+Yaw)*11+100
                back_motor.run(speed)
                print(Yaw)
                if Yaw<-90:
                    back_motor.stop()
                    front_motor.run_target(1000,0)
                    turn_count=turn_count+1
                    print(turn_count/4,"周成功")
                    break
            hub.imu.reset_heading(0)
        if turn_count==12:
            break
#===============================================================================
while True:
    hub.display.char(str(0))
    if Button.LEFT in hub.buttons.pressed()  or Button.RIGHT in hub.buttons.pressed():
        hub.display.off()
        break
hub.imu.reset_heading(0)
while True:
    Yaw=hub.imu.heading()
    front_motor.run_target(1000,(0-Yaw)*2)
    speed=100+eyes.distance()
    back_motor.run(speed)
    if eyes.distance()<400:
        back_motor.stop()
        break
print(right_sensor.distance())
print(left_sensor.distance())
if right_sensor.distance()>1000:
    print("right_turn")
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,35)
        speed=(90-Yaw)*11+100
        back_motor.run(speed)
        print(Yaw)
        if Yaw>90:
            back_motor.stop()
            front_motor.run_target(1000,0)
            turn_count=1
            print(turn_count/4,"周成功")
            break
    distance=1
elif left_sensor.distance()>1000:
    print("left_turn")
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,-35)
        speed=(90+Yaw)*11+100
        back_motor.run(speed)
        print(Yaw)
        if Yaw<-90:
            back_motor.stop()
            front_motor.run_target(1000,0)
            turn_count=1
            print(turn_count/4,"周成功")
            break
    distance=2
hub.imu.reset_heading(0)
print(right_sensor.distance())
print(left_sensor.distance())
if distance==1:
    right()
elif distance==2:
    left()
back_motor.stop()
front_motor.run_target(1000,0)
timer.reset()
while True:
    front_motor.run_target(1000,0)
    back_motor.run(1000)
    if timer.time()>1000:
        print(timer.time())
        break
while True:
    Yaw=hub.imu.heading()
    front_motor.run_target(1000,(0-Yaw)*2)
    back_motor.run(eyes.distance()-700)
    print(eyes.distance())
    if eyes.distance()<1300:
        front_motor.run_target(1000,0)
        back_motor.stop()
        break
