```python
#緑は左、赤は右
#payload[2]は赤のpixel数,payload[5]は緑のpixel数
#payload[0]は赤のx座標,payload[1]は赤のy座標
#payload[3]は緑のx座標,payload[4]は緑のy座標
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pupremote_hub import PUPRemoteHub
from pybricks.pupdevices import Motor,ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from micropython import const#定数
hub = PrimeHub()
p=PUPRemoteHub(Port.F)
p.add_channel('blob','hhhhhh')
distance=0
back_motor=Motor(Port.C)
front_motor=Motor(Port.D)
eyes=UltrasonicSensor(Port.E)
left_sensor=UltrasonicSensor(Port.A)
right_sensor=UltrasonicSensor(Port.B)
timer=StopWatch()
voltage = hub.battery.voltage()/1000  # ボルト(V)で取得.7.4ｖで充電
current = hub.battery.current()/1000  # アンペア(A)で取得
print("バッテリー電圧:", voltage, "V")
print("バッテリー電流:", current, "A")
hub.imu.reset_heading(0)
payload=p.call('blob')
turn_count=0
red_or_green=0
one_set_count=0
right_distance=0
left_distance=0
def start_right():
    red_or_green=0
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,35)
        back_motor.run(1000)
        if Yaw>40:
            back_motor.stop()
            break
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,-35)
        back_motor.run(-1000)
        if Yaw>60:
            back_motor.stop()
            break
    payload=p.call('blob')
    print(payload)
    if payload[2]>payload[5] and payload[2]>600:
        red_or_green=1
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            back_motor.run((90-Yaw)*15+100)
            if Yaw>90:
                back_motor.stop()
                break
        while True:
            front_motor.run_target(1000,0)
            back_motor.run(eyes.distance())
            if eyes.distance()<350:
                break
    else:
        red_or_green=2
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            back_motor.run((70-Yaw)*15+100)
            if Yaw>70:
                back_motor.stop()
                break
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,-35)
        back_motor.run(Yaw*15+100)
        if Yaw<0:
            back_motor.stop()
            hub.imu.reset_heading(0)
            break            
def start_left():
    red_or_green=0
    while True:#yaw<-20まで前進
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,-35)
        back_motor.run(1000)
        if Yaw<-40:
            back_motor.stop()
            break
    while True:#yaw<-45まで後進
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,35)
        back_motor.run(-1000)
        if Yaw<-60:
            back_motor.stop()
            break
    payload=p.call('blob')
    print(payload)
    if payload[5]>payload[2] and payload[5]>500:#緑検知
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run((Yaw+90)*25+100)
            if Yaw<-90:
                back_motor.stop()
                break
        while True:
            front_motor.run_target(1000,0)
            back_motor.run(eyes.distance())
            if eyes.distance()<350:
                break
        red_or_green=1
    else:#その他
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run((Yaw+70)*25+100)
            if Yaw<-70:
                back_motor.stop()
                break
    while True:#yaw>0まで前進
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,35)
        back_motor.run(Yaw*-15+100)
        if Yaw>0:
            back_motor.stop()
            hub.imu.reset_heading(0)
            break
    while True:#前20㎝まで前進
        Yaw=hub.imu.heading()
        degrees=(Yaw-0)*2
        front_motor.run_target(1000,degrees)
        speed=eyes.distance()+200
        back_motor.run(speed)
        if eyes.distance()<200:
            back_motor.stop()
            break
    while True:#yaw>90まで後進
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,35)
        back_motor.run((Yaw-90)*15-100)
        if Yaw>90:
            back_motor.stop()
            break
def right_turn():
    print("turn")
    while True:#直進
        payload=p.call('blob')
        hub.light.on(Color.BLUE)
        Yaw=hub.imu.heading()
        direction=(0-Yaw)*0.8
        if direction>=30:
            direction=30
        if direction<=-30:
            direction=-30
        front_motor.run_target(1000,direction)         
        back_motor.run(1000) 
        print(payload)  
        if payload[2]>10 or payload[5]>10 or eyes.distance()<750:
            break
    print("前の距離:",eyes.distance())
    print("左の距離:",left_sensor.distance())
    payload=p.call('blob')
    print(payload)
    if payload[5]>10 or red_or_green==2:#緑
        print("green")
        while True:
            hub.light.on(Color.BLUE)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*2
            front_motor.run_target(1000,direction)
            payload=p.call('blob')
            back_motor.run(1000)
            if eyes.distance()<500 and payload[5]<10:
                hub.light.off()
                print(eyes.distance())
                break
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            back_motor.run((110-Yaw)*35+100)
            if Yaw>110:
                hub.imu.reset_heading(20)
                break
    elif left_sensor.distance()>400:#左40㎝より大きい
        print("no")
        while True:#前25㎝まで前進
            hub.light.on(Color.BLUE)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*2
            front_motor.run_target(1000,direction)
            payload=p.call('blob')
            back_motor.run(1000)
            if eyes.distance()<250:
                hub.light.off()
                left_distance=left_sensor.distance()
                print(eyes.distance())
                back_motor.stop()
                break
        while True:#緑検知またはyaw>95まで後進
            payload=p.call('blob')
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            if payload[5]>500:
                Yaw=105
            back_motor.run((Yaw-100)*15-100)
            if Yaw>100:
                print("緑ｐ：",payload[5])
                break
        payload=p.call('blob')
        if payload[5]>400:#緑
            print("green")
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,-35)
                back_motor.run((Yaw-15)*25+100)
                if Yaw<15:
                    break
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,35)
                back_motor.run((110-Yaw)*25+100)
                if Yaw>110:
                    hub.imu.reset_heading(20)
                    break
        else:#その他
            print("no")
            hub.imu.reset_heading(10)
            front_motor.run_target(1000,0)
            timer.reset()
            time=(1300-left_distance)*2.3
            while True:
                front_motor.run_target(1000,0)
                back_motor.run(1000)
                if timer.time()>time:
                    print(timer.time())
                    break 
            back_motor.stop()   
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,-35)
                back_motor.run((20+Yaw)*35+100)   
                if Yaw<-20:
                    hub.imu.reset_heading(-20)
                    break
    else:
        print("no")
        while True:#前80㎝まで前進
            hub.light.on(Color.BLUE)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*2
            front_motor.run_target(1000,direction)
            payload=p.call('blob')
            back_motor.run(1000)
            if eyes.distance()<600:
                hub.light.off()
                left_distance=left_sensor.distance()
                print(eyes.distance())
                break
        while True:#前85㎝まで後進
            front_motor.run_target(1000,0)
            back_motor.run(-1000)
            if eyes.distance()>650:
                back_motor.stop()
                break
        while True:#緑検知またはyaw>95まで後進
            Yaw=hub.imu.heading()
            payload=p.call('blob')
            front_motor.run_target(1000,35)
            print(payload)
            if payload[5]>500:
                Yaw=110
            back_motor.run((100-Yaw)*15+100)
            if Yaw>100:
                print("緑ｐ：",payload[5])
                break
        payload=p.call('blob')
        if payload[5]>400:#緑
            print("green")
            back_motor.stop()
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,-35)
                back_motor.run((Yaw-20)*25+100)
                if Yaw<20:
                    break
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,35)
                back_motor.run((105-Yaw)*25+100)
                if Yaw>105:
                    hub.imu.reset_heading(15)
                    break
        else:#その他
            hub.imu.reset_heading(10)
            front_motor.run_target(1000,0)
            timer.reset()
            time=(700-left_distance)*2
            while True:
                front_motor.run_target(1000,0)
                back_motor.run(1000)
                if timer.time()>time:
                    print(timer.time())
                    break
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,-35)
                back_motor.run((20+Yaw)*25+100)   
                if Yaw<-20:
                    hub.imu.reset_heading(-20)
                    break
def left_turn():
    print("turn")
    while True:#直進
        payload=p.call('blob')
        hub.light.on(Color.BLUE)
        Yaw=hub.imu.heading()
        direction=(0-Yaw)*0.8
        if direction>=30:
            direction=30
        if direction<=-30:
            direction=-30
        front_motor.run_target(1000,direction)         
        back_motor.run(1000) 
        print(payload)  
        if payload[2]>10 or payload[5]>10 or eyes.distance()<850:
            break
    print("前の距離:",eyes.distance())
    print("左の距離:",left_sensor.distance())
    payload=p.call('blob')
    print(payload)
    if payload[2]>10 or red_or_green==1:#赤
        print("red")
        while True:
            hub.light.on(Color.BLUE)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*2
            front_motor.run_target(1000,direction)
            speed=100+eyes.distance()
            payload=p.call('blob')
            back_motor.run(1000)
            if eyes.distance()<500 and payload[5]<10:
                hub.light.off()
                print(eyes.distance())
                break
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run((100+Yaw)*25+100)
            if Yaw<-100:
                hub.imu.reset_heading(-10)
                break
    elif right_sensor.distance()>400:
        print("no")
        while True:#前25㎝まで前進
            hub.light.on(Color.BLUE)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*2
            front_motor.run_target(1000,direction)
            payload=p.call('blob')
            back_motor.run(1000)
            if eyes.distance()<250:
                hub.light.off()
                right_distance=right_sensor.distance()
                print(eyes.distance())
                back_motor.stop()
                break
        while True:#赤検知またはyaw<-95まで後進
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            if payload[2]>500:
                Yaw=-100
            back_motor.run((95+Yaw)*-25-100)
            if Yaw<-95:
                print("赤ｐ：",payload[2])
                break
        payload=p.call('blob')
        if payload[2]>500:#赤
            print("red")
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,35)
                back_motor.run((Yaw+15)*-25+100)
                if Yaw>-15:
                    break
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,-35)
                back_motor.run((100+Yaw)*25+100)
                if Yaw<-100:
                    hub.imu.reset_heading(-10)
                    break
        else:
            print("no")
            hub.imu.heading(-5)
            front_motor.run_target(1000,0)
            timer.reset()
            time=(1200-right_distance)*2.3
            while True:
                front_motor.run_target(1000,0)
                back_motor.run(1000)
                if timer.time()>time:
                    print(timer.time())
                    break
            while True:
                Yaw=hub.imu.heading()
                front_motor.run(1000,-35)
                back_motor.run((10-Yaw)*35+100)   
                if Yaw>10:
                    break
    else:
        print("no")
        while True:#前80㎝まで前進
            hub.light.on(Color.BLUE)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*2
            front_motor.run_target(1000,direction)
            payload=p.call('blob')
            back_motor.run(1000)
            if eyes.distance()<800:
                hub.light.off()
                right_distance=right_sensor.distance()
                print(eyes.distance())
                break
        while True:#前85㎝まで後進
            front_motor.run_target(1000,0)
            back_motor.run(-1000)
            if eyes.distance()>850:
                back_motor.stop()
                break
        while True:#赤検知またはyaw<-95まで後進
            Yaw=hub.imu.heading()
            payload=p.call('blob')
            front_motor.run_target(1000,-35)
            print(payload)
            if payload[2]>500:
                Yaw=-110
            back_motor.run((Yaw+95)*15+100)
            if Yaw<-95:
                print("赤ｐ：",payload[2])
                break
        payload=p.call('blob')
        if payload[2]>500:#赤
            print("red")
            back_motor.stop()
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,35)
                back_motor.run((15+Yaw)*-25+100)
                if Yaw>-15:
                    break
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,-35)
                back_motor.run((100+Yaw)*25+100)
                if Yaw<-100:
                    hub.imu.reset_heading(-10)
                    break
        else:
            print("no")
            hub.imu.heading(-5)
            front_motor.run_target(1000,0)
            timer.reset()
            time=(800-right_distance)*2.3
            while True:
                front_motor.run_target(1000,0)
                back_motor.run(1000)
                if timer.time()>time:
                    print(timer.time())
                    break
            while True:
                Yaw=hub.imu.heading()
                front_motor.run(1000,35)
                back_motor.run((10-Yaw)*35+100)   
                if Yaw>10:
                    break
def one_set():
    red_or_green=0#赤なら１緑なら２にする。＊中央補正を行うため
    one_set_count=0
    front_motor.run_target(1000,0)
    payload=p.call('blob')
    print(payload)
    if payload[2]<500 and payload[5]<500 and eyes.distance()>850:
        while True:
            payload=p.call('blob')
            hub.light.on(Color.BLUE)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*1.5
            if direction>=30:
                direction=30
            if direction<=-30:
                direction=-30
            front_motor.run_target(1000,direction)         
            back_motor.run(1000)
            print("not_found")  
            print(payload)  
            if payload[2]>400 or payload[5]>400 or eyes.distance()<850:
                payload=p.call('blob')  
                print(payload)  
                print(eyes.distance())
                break
    if payload[2]>payload[5] and payload[2]>300:
        while True:
            payload=p.call('blob')
            hub.light.on(Color.RED)
            direction=(payload[0]-160)*0.15#P制御
            if direction>=30:
                direction=30
            if direction<=-30:
                direction=-30
            front_motor.run_target(1000,direction)
            back_motor.run(1000) 
            if payload[2]>20000 or payload[2]<0:
                front_motor.run_target(1000,0)
                back_motor.run(-200)
            if payload[2]>=3000:#赤
                timer.reset()
                front_motor.run_target(1000,35)
                while True:
                    hub.light.on(Color.RED)
                    front_motor.run_target(1000,35)
                    back_motor.run(1000) 
                    if timer.time()>600:#赤
                        front_motor.run_target(1000,-35)
                        break
                while True:
                    payload=p.call('blob')
                    Yaw=hub.imu.heading()
                    front_motor.run_target(1000,-35)
                    back_motor.run((Yaw-20)*15+100)
                    if payload[2]>200:
                        red_or_green=1
                    elif payload[5]>200:
                        red_or_green=2
                    if Yaw<10:
                        break
                break
    elif payload[2]<payload[5] and payload[5]>300:
        while True:
            payload=p.call('blob')
            hub.light.on(Color.GREEN)
            direction=(payload[3]-160)*0.15#P制御
            if direction>=30:
                direction=30
            if direction<=-30:
                direction=-30
            front_motor.run_target(1000,direction)
            back_motor.run(1000) 
            if payload[5]>20000 or payload[5]<0:
                    front_motor.run_target(1000,0)
                    back_motor.run(-200)
            if payload[5]>=3000:#緑
                timer.reset()
                front_motor.run_target(1000,-35)
                while True:
                    hub.light.on(Color.GREEN)
                    front_motor.run_target(1000,-35)
                    back_motor.run(1000) 
                    if timer.time()>500:#緑
                        front_motor.run_target(1000,35)
                        break
                while True:
                    Yaw=hub.imu.heading()
                    payload=p.call('blob')
                    front_motor.run_target(1000,35)
                    back_motor.run((Yaw+20)*-15+100)
                    if payload[2]>200:
                        red_or_green=1
                    elif payload[5]>200:
                        red_or_green=2
                    if Yaw>-10:
                        break
                break
    payload=p.call('blob')
    print(payload)
def last_right():
    distance=0
    one_set_count=0
    payload=p.call('blob')
    if payload[2]>payload[5] and 90<payload[0] and payload[0]<230 and payload[2]>300:
        while True:
            payload=p.call('blob')
            print(payload)
            hub.light.on(Color.RED)
            direction=(payload[0]-160)*0.15#P制御
            if direction>=30:
                direction=30
            if direction<=-30:
                direction=-30
            front_motor.run_target(1000,direction)
            back_motor.run(900) 
            if payload[2]>20000 or payload[2]<5:
                    front_motor.run_target(1000,0)
                    back_motor.run(-200)
            if payload[2]>=4000:#赤
                timer.reset()
                front_motor.run_target(1000,35)
                while True:
                    hub.light.on(Color.RED)
                    front_motor.run_target(1000,35)
                    back_motor.run(1000) 
                    if timer.time()>600:#赤
                        break
                while True:
                    hub.light.off()
                    Yaw=hub.imu.heading()
                    front_motor.run_target(1000,-35)
                    back_motor.run((Yaw+0)*25+100)
                    if Yaw<0:
                        hub.imu.reset_heading(0)
                        print(Yaw)
                        break
                break
    elif payload[2]<payload[5] and 90<payload[3] and payload[3]<230 and payload[5]>300:
        while True:
            payload=p.call('blob')
            print(payload)
            hub.light.on(Color.GREEN)
            direction=(payload[3]-160)*0.15#P制御
            if direction>=30:
                direction=30
            if direction<=-30:
                direction=-30
            front_motor.run_target(1000,direction)
            back_motor.run(900) 
            if payload[5]>20000 or payload[5]<0:
                    back_motor.stop()
                    front_motor.run_target(1000,0)
                    back_motor.run(-200)
            if payload[5]>=4000:#緑
                timer.reset()
                front_motor.run_target(1000,-35)
                while True:
                    hub.light.on(Color.GREEN)
                    front_motor.run_target(1000,-35)
                    back_motor.run(1000) 
                    if timer.time()>600:#赤
                        break
                while True:
                    hub.light.off()
                    Yaw=hub.imu.heading()
                    front_motor.run_target(1000,35)
                    back_motor.run((Yaw-0)*-25+100)
                    if Yaw>0:
                        hub.imu.reset_heading(0)
                        print(Yaw)
                        break
                break
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,(0-Yaw)*2)
        back_motor.run(1000)
        if eyes.distance()<350:
            back_motor.stop()
            distance=left_sensor.distance()
            break
    while True:
        front_motor.run_target(1000,0)
        back_motor.run(-1000)
        if eyes.distance()>350:
            break
    while True:
        Yaw=hub.imu.heading()
        payload=p.call('blob')
        front_motor.run_target(1000,-35)
        if payload[5]>500:
            Yaw=75
        back_motor.run((80-Yaw)*-25-100)
        if Yaw>70:
            back_motor.stop()
            break
    payload=p.call('blob')
    print(payload)
    if payload[5]>500:
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run((Yaw-10)*25+100)
            if Yaw<10:
                break
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            back_motor.run((90-Yaw)*25+100)
            if Yaw>90:
                hub.imu.reset_heading(0)
                break
        front_motor.run_target(1000,0)
        timer.reset()
        time=(1150-distance)*2.3
        print(time)
        while True:
            front_motor.run_target(1000,0)
            back_motor.run(1000)
            if timer.time()>time:
                print(timer.time())
                back_motor.stop()
                break
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run((90-Yaw)*-25-100)
            if Yaw>90:
                break
    else:
        front_motor.run_target(1000,0)
        timer.reset()
        time=(1550-distance)*2.3
        print(time)
        while True:
            front_motor.run_target(1000,0)
            back_motor.run(1000)
            if timer.time()>time:
                print(timer.time())
                back_motor.stop()
                break
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run((90-Yaw)*-25-100)
            if Yaw>90:
                hub.imu.reset_heading(0)
                break
        front_motor.run_target(1000,0)
        timer.reset()
        while True:
            front_motor.run_target(1000,0)
            back_motor.run(-1000)
            if timer.time()>800 or (eyes.distance()>700 and eyes.distance()!=2000):
                print("時間：",timer.time())
                print("距離：",eyes.distance())
                back_motor.stop()
                break
def last_left():
    distance=0
    one_set_count=0
    payload=p.call('blob')
    if payload[2]>payload[5] and 90<payload[0] and payload[0]<230 and payload[2]>300:
        while True:
            payload=p.call('blob')
            print(payload)
            hub.light.on(Color.RED)
            direction=(payload[0]-160)*0.15#P制御
            if direction>=30:
                direction=30
            if direction<=-30:
                direction=-30
            front_motor.run_target(1000,direction)
            back_motor.run(900) 
            if payload[2]>20000 or payload[2]<5:
                    front_motor.run_target(1000,0)
                    back_motor.run(-200)
            if payload[2]>=4000:#赤
                timer.reset()
                front_motor.run_target(1000,35)
                while True:
                    hub.light.on(Color.RED)
                    front_motor.run_target(1000,35)
                    back_motor.run(1000) 
                    if timer.time()>600:#赤
                        break
                while True:
                    hub.light.off()
                    Yaw=hub.imu.heading()
                    front_motor.run_target(1000,-35)
                    back_motor.run((Yaw+0)*25+100)
                    if Yaw<0:
                        hub.imu.reset_heading(0)
                        print(Yaw)
                        break
                break
    elif payload[2]<payload[5] and 90<payload[3] and payload[3]<230 and payload[5]>300:
        while True:
            payload=p.call('blob')
            print(payload)
            hub.light.on(Color.GREEN)
            direction=(payload[3]-160)*0.15#P制御
            if direction>=30:
                direction=30
            if direction<=-30:
                direction=-30
            front_motor.run_target(1000,direction)
            back_motor.run(900) 
            if payload[5]>20000 or payload[5]<0:
                    back_motor.stop()
                    front_motor.run_target(1000,0)
                    back_motor.run(-200)
            if payload[5]>=4000:#緑
                timer.reset()
                front_motor.run_target(1000,-35)
                while True:
                    hub.light.on(Color.GREEN)
                    front_motor.run_target(1000,-35)
                    back_motor.run(1000) 
                    if timer.time()>600:#赤
                        break
                while True:
                    hub.light.off()
                    Yaw=hub.imu.heading()
                    front_motor.run_target(1000,35)
                    back_motor.run((Yaw-0)*-25+100)
                    if Yaw>0:
                        hub.imu.reset_heading(0)
                        print(Yaw)
                        break
                break
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,(0-Yaw)*2)
        back_motor.run(1000)
        if eyes.distance()<400:
            back_motor.stop()
            distance=right_sensor.distance()
            break
    while True:
        front_motor.run_target(1000,0)
        back_motor.run(-1000)
        if eyes.distance()>300:
            back_motor.stop()
            break
    while True:
        Yaw=hub.imu.heading()
        payload=p.call('blob')
        front_motor.run_target(1000,35)
        if payload[2]>500:
            Yaw=-75
        back_motor.run((80+Yaw)*-25-100)
        if Yaw<-70:
            back_motor.stop()
            break
    payload=p.call('blob')
    print(payload)
    if payload[2]>500:
        hub.light.on(Color.RED)
        print("RED")
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            back_motor.run((5+Yaw)*-35+100)
            if Yaw>-10:
                break
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run((90+Yaw)*25+100)
            if Yaw<-90:
                hub.imu.reset_heading(0)
                break
        front_motor.run_target(1000,0)
        timer.reset()
        time=(1600-distance)*2.3
        print(time)
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,(0-Yaw)*2)
            back_motor.run(1000)
            if timer.time()>time:
                print(timer.time())
                back_motor.stop()
                break
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            back_motor.run((90+Yaw)*-25-100)
            if Yaw<-90:
                break
    else:
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run((90+Yaw)*25+100)
            if Yaw<-90:
                hub.imu.reset_heading(0)
                break
                front_motor.run_target(1000,0)
        timer.reset()
        time=(2250-distance)*2.3
        print(time)
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,(0-Yaw)*2)
            back_motor.run(1000)
            if timer.time()>time:
                print(timer.time())
                back_motor.stop()
                break
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            back_motor.run((90+Yaw)*-25-100)
            if Yaw<-90:
                break
        front_motor.run_target(1000,0)
        timer.reset()
        while True:
            front_motor.run_target(1000,0)
            back_motor.run(-1000)
            if timer.time()>800 or (eyes.distance()>700 and eyes.distance()!=2000):
                print("時間：",timer.time())
                print("距離：",eyes.distance())
                back_motor.stop()
                break
    payload=p.call('blob')
def parking():
    hub.imu.reset_heading(0)
    front_motor.run_target(1000,-35)
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,-35)
        speed=(Yaw+35)*20+200
        back_motor.run(speed)
        if Yaw<-35:
            back_motor.stop()
            break
    front_motor.run_target(1000,35)
    back_motor.run_angle(1000,-600)
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,-35)
        back_motor.run(300)
        if Yaw<-90:
            back_motor.stop()
            front_motor.run_target(1000,0)
            break
