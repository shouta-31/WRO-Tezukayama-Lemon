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
payload=p.call('blob')
distance=0
turn_count=0
one_set_count=0
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
            if Yaw<70:
                Yaw=30
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
            if Yaw<50:
                Yaw=10
            back_motor.run((70-Yaw)*15+100)
            if Yaw>70:
                back_motor.stop()
                break
    while True:
        Yaw=hub.imu.heading()
        front_motor.run_target(1000,-35)
        if Yaw>20:
            Yaw=60
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
def right_turn():
    print("turn")
    global obstacle
    global color
    global red_or_green
    while True:#直進
        if red_or_green==0:
            hub.light.on(Color.BLUE)
        payload=p.call('blob')
        Yaw=hub.imu.heading()
        direction=(0-Yaw)*0.8
        if direction>=30:
            direction=30
        if direction<=-30:
            direction=-30
        front_motor.run_target(1000,direction)         
        back_motor.run(1000)  
        if payload[2]>10 or payload[5]>10 or eyes.distance()<700:
            back_motor.stop()
            break
    print("前の距離:",eyes.distance())
    print("左の距離:",left_sensor.distance())
    print("turn_count",turn_count)
    payload=p.call('blob')
    print(payload)
    near_object=0
    if payload[5]>10 or red_or_green==2:#緑
        print("green")
        eyes_distance=0
        while True:#直進
            hub.light.on(Color.GREEN)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*0.5
            front_motor.run_target(1000,direction)
            payload=p.call('blob')
            back_motor.run(1000)
            eyes_distance=400
            if turn_count==3 or turn_count==7 or turn_count==11:
                eyes_distance=650
            if eyes.distance()<eyes_distance and payload[5]<10:
                hub.light.off()
                print(eyes.distance())
                break
        while True:#旋回
            Yaw=hub.imu.heading()
            payload=p.call('blob')
            front_motor.run_target(1000,35)
            if Yaw<100 and turn_count!=11:
                Yaw=70
            if turn_count==11 and Yaw>70:
                Yaw=140
            if payload[2]>100:
                speed=(160-payload[0])*15+100
            elif payload[5]>100:
                speed=(160-payload[3])*15+100
            else:
                speed=(130-Yaw)*15+100
            back_motor.run(speed)
            if (Yaw>130 and payload[2]<100 and payload[5]<100) or payload[0]>150 or payload[3]>150:
                print(p.call('blob'))
                back_motor.stop()
                Yaw=hub.imu.heading()
                print(Yaw)
                if turn_count!=11:
                    hub.imu.reset_heading(Yaw-90)
                break
        if payload[0]<150 and payload[3]<150 and turn_count!=11:#オブジェクトが先にない
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,-35)
                back_motor.run(Yaw*25+100)
                if Yaw<0:
                    break
        if turn_count==11:
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,35)
                back_motor.run((90-Yaw)*5+100)
                if Yaw>90:
                    break
            hub.imu.reset_heading(0)
            color=2
        front_motor.run_target(1000,0)
    elif left_sensor.distance()>500 and left_sensor.distance!=2000:#左40㎝より大きい
        print("no")
        red=0
        while True:#前25㎝まで前進
            hub.light.on(Color.BLUE)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*0.5
            front_motor.run_target(1000,direction)
            payload=p.call('blob')
            back_motor.run(1000)
            if eyes.distance()<300:
                hub.light.off()
                left_distance=left_sensor.distance()
                print(eyes.distance())
                back_motor.stop()
                break
        while True:#緑検知またはyaw>95まで後進
            payload=p.call('blob')
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            if payload[5]>1000:
                Yaw=100
                back_motor.stop()
            if payload[2]>500:
                red=1
            if Yaw<80:
                Yaw=40
            back_motor.run((Yaw-90)*15-100)
            if Yaw>90:
                back_motor.stop()
                print("緑ｐ：",payload[5])
                break
        Yaw=hub.imu.heading()
        hub.imu.reset_heading(Yaw-90)
        print("Yaw:",hub.imu.heading())
        payload=p.call('blob')
        if turn_count==11:
            if payload[5]>500:
                if payload[5]>3000:
                    while True:
                        payload=p.call('blob')
                        hub.light.on(Color.GREEN)
                        front_motor.run_target(1000,0)
                        back_motor.run(-1000)
                        if payload[5]<2000:
                            back_motor.stop()
                            break
                while True:#緑回避
                    payload=p.call('blob')
                    hub.light.on(Color.GREEN)
                    direction=(payload[3]-160)*0.15#P制御
                    front_motor.run_target(1000,direction)
                    back_motor.run(1000) 
                    if payload[5]>20000 or payload[5]<0:
                            front_motor.run_target(1000,0)
                            back_motor.run(-200)
                    if payload[5]>=3000:#緑に近づいた
                        timer.reset()
                        front_motor.run_target(1000,-35)
                        while True:#左
                            hub.light.off()
                            front_motor.run_target(1000,-35)
                            back_motor.run(1000) 
                            if timer.time()>500:
                                front_motor.run_target(1000,35)
                                break
                        while True:#yaw>-10まで右に曲がる。途中読み取り
                            Yaw=hub.imu.heading()
                            front_motor.run_target(1000,35)
                            if Yaw<-30:
                                Yaw=-70
                            back_motor.run(Yaw*-15+100)
                            if Yaw>0:
                                break
                        break
                color=2
            else:#その他
                front_motor.run_target(1000,0)
                time=(1200-left_distance)*2.3
                if red==1:
                    hub.light.on(Color.RED)
                timer.reset()
                while True:
                    Yaw=hub.imu.heading()
                    front_motor.run_target(1000,(0-Yaw)*0.8)
                    back_motor.run(1000)
                    if timer.time()>time:
                        print(timer.time())
                        break
                while True:
                    Yaw=hub.imu.heading()
                    payload=p.call('blob')
                    front_motor.run_target(1000,-35)
                    back_motor.run((Yaw+0)*25+100)
                    if Yaw<0:
                        break
                color=1
            front_motor.run_target(1000,0)
        elif red!=1 and payload[5]>400:#緑
            if payload[5]>3000:
                near_object=1
                while True:
                    payload=p.call('blob')
                    hub.light.on(Color.GREEN)
                    front_motor.run_target(1000,0)
                    back_motor.run(-1000)
                    if payload[5]<2000:
                        back_motor.stop()
                        break
            while True:#緑回避
                payload=p.call('blob')
                hub.light.on(Color.GREEN)
                direction=(payload[3]-160)*0.15#P制御
                front_motor.run_target(1000,direction)
                back_motor.run(1000) 
                if payload[5]>20000 or payload[5]<0:
                        front_motor.run_target(1000,0)
                        back_motor.run(-200)
                if payload[5]>=3000:#緑に近づいた
                    timer.reset()
                    front_motor.run_target(1000,-35)
                    while True:#左
                        hub.light.off()
                        front_motor.run_target(1000,-35)
                        back_motor.run(1000) 
                        if timer.time()>500:
                            front_motor.run_target(1000,35)
                            break
                    while True:#右yaw>40
                        Yaw=hub.imu.heading()   
                        payload=p.call('blob')
                        front_motor.run_target(1000,35)
                        if near_object!=1 and Yaw>0:
                            Yaw=50
                        if payload[2]>500 or payload[5]>500:
                            Yaw=50
                            back_motor.stop()
                        back_motor.run((40-Yaw)*25+100)
                        if Yaw>40:
                            break
                    if payload[2]<300 and payload[5]<300:
                        obstacle=1
                        while True:
                            Yaw=hub.imu.heading()   
                            payload=p.call('blob')
                            front_motor.run_target(1000,-35)
                            back_motor.run(Yaw*25+100)
                            if Yaw<0:
                                break
                    front_motor.run_target(1000,0)
                    break
        else:#その他
            front_motor.run_target(1000,0)
            time=(1200-left_distance)*2.3
            if red==1:
                hub.light.on(Color.RED)
            timer.reset()
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,(0-Yaw)*0.8)
                back_motor.run(1000)
                if timer.time()>time:
                    print(timer.time())
                    break
            while True:
                Yaw=hub.imu.heading()
                payload=p.call('blob')
                front_motor.run_target(1000,-35)
                if payload[2]>500 or payload[5]>500:
                    Yaw=-60
                back_motor.run((Yaw+40)*25+100)
                if Yaw<-40:
                    break
            if payload[2]<500 and payload[5]<500:
                obstacle=1
                while True:
                    Yaw=hub.imu.heading()
                    payload=p.call('blob')
                    front_motor.run_target(1000,35)
                    back_motor.run(Yaw*-25+100)
                    if Yaw>0:
                        break
            front_motor.run_target(1000,0)
            if turn_count==11:
                color=1
    else:
        red=0
        print("no")
        while True:#前80㎝まで前進
            hub.light.on(Color.BLUE)
            Yaw=hub.imu.heading()
            direction=(0-Yaw)*0.5
            front_motor.run_target(1000,direction)
            payload=p.call('blob')
            back_motor.run(1000)
            if eyes.distance()<700:
                hub.light.off()
                left_distance=left_sensor.distance()
                print(eyes.distance())
                break
        while True:#前85㎝まで後進
            back_motor.run(-1000)
            front_motor.run_target(1000,0)
            if eyes.distance()>750:
                back_motor.stop()
                break
        while True:#緑検知またはyaw>95まで後進
            Yaw=hub.imu.heading()
            payload=p.call('blob')
            front_motor.run_target(1000,35)
            if payload[5]>1000:
                Yaw=100
            if payload[2]>500:
                red=1
            if Yaw<80:
                Yaw=40
            back_motor.run((90-Yaw)*15+100)
            if Yaw>90:
                print("緑ｐ：",payload[5])
                back_motor.stop()
                break
        Yaw=hub.imu.heading()
        hub.imu.reset_heading(Yaw-90)
        print("Yaw:",hub.imu.heading())
        payload=p.call('blob')
        if turn_count==11:
            if payload[5]>500:
                if payload[5]>3000:
                    while True:
                        payload=p.call('blob')
                        hub.light.on(Color.GREEN)
                        front_motor.run_target(1000,0)
                        back_motor.run(-1000)
                        if payload[5]<2000:
                            back_motor.stop()
                            break
                while True:#緑回避
                    payload=p.call('blob')
                    hub.light.on(Color.GREEN)
                    direction=(payload[3]-160)*0.15#P制御
                    front_motor.run_target(1000,direction)
                    back_motor.run(1000) 
                    if payload[5]>20000 or payload[5]<0:
                            front_motor.run_target(1000,0)
                            back_motor.run(-200)
                    if payload[5]>=3000:#緑に近づいた
                        timer.reset()
                        front_motor.run_target(1000,-35)
                        while True:#左
                            hub.light.off()
                            front_motor.run_target(1000,-35)
                            back_motor.run(1000) 
                            if timer.time()>500:
                                front_motor.run_target(1000,35)
                                break
                        while True:#yaw>-10まで右に曲がる。途中読み取り
                            Yaw=hub.imu.heading()
                            front_motor.run_target(1000,35)
                            if Yaw<-30:
                                Yaw=-70
                            back_motor.run(Yaw*-15+100)
                            if Yaw>0:
                                break
                        break
                color=2
            else:#その他
                front_motor.run_target(1000,0)
                time=(1200-left_distance)*2.3
                if red==1:
                    hub.light.on(Color.RED)
                timer.reset()
                while True:
                    Yaw=hub.imu.heading()
                    front_motor.run_target(1000,(0-Yaw)*0.8)
                    back_motor.run(1000)
                    if timer.time()>time:
                        print(timer.time())
                        break
                while True:
                    Yaw=hub.imu.heading()
                    payload=p.call('blob')
                    front_motor.run_target(1000,-35)
                    back_motor.run((Yaw+0)*25+100)
                    if Yaw<0:
                        break
                color=1
            front_motor.run_target(1000,0)
        elif red!=1 and payload[5]>400:#緑
            if payload[5]>3000:
                near_object=1
                while True:
                    payload=p.call('blob')
                    hub.light.on(Color.GREEN)
                    front_motor.run_target(1000,0)
                    back_motor.run(-1000)
                    if payload[5]<2000:
                        back_motor.stop()
                        break
            while True:#緑回避
                payload=p.call('blob')
                hub.light.on(Color.GREEN)
                direction=(payload[3]-160)*0.15#P制御
                front_motor.run_target(1000,direction)
                back_motor.run(1000) 
                if payload[5]>20000 or payload[5]<0:
                        front_motor.run_target(1000,0)
                        back_motor.run(-200)
                if payload[5]>=3000:#緑に近づいた
                    timer.reset()
                    front_motor.run_target(1000,-35)
                    while True:#左
                        hub.light.off()
                        front_motor.run_target(1000,-35)
                        back_motor.run(1000) 
                        if timer.time()>500:
                            front_motor.run_target(1000,35)
                            break
                    while True:#右yaw>40
                        Yaw=hub.imu.heading()   
                        payload=p.call('blob')
                        front_motor.run_target(1000,35)
                        if near_object!=1 and Yaw>0:
                            Yaw=50
                        if payload[2]>500 or payload[5]>500:
                            back_motor.stop()
                            Yaw=50
                        back_motor.run((40-Yaw)*25+100)
                        if Yaw>40:
                            break
                    if payload[2]<500 and payload[5]<500:
                        obstacle=1
                        while True:
                            Yaw=hub.imu.heading()   
                            payload=p.call('blob')
                            front_motor.run_target(1000,-35)
                            back_motor.run(Yaw*25+100)
                            if Yaw<0:
                                break
                    front_motor.run_target(1000,0)
                    break
            if turn_count==11:
                color=2
        else:#その他
            front_motor.run_target(1000,0)
            time=(700-left_distance)*2.3
            if red==1:
                hub.light.on(Color.RED)
            timer.reset()
            while True:
                Yaw=hub.imu.heading()
                front_motor.run_target(1000,(0-Yaw)*0.8)
                back_motor.run(1000)
                if timer.time()>time:
                    print(timer.time())
                    break
            a=0
            while True:
                Yaw=hub.imu.heading()
                payload=p.call('blob')
                print(payload)
                front_motor.run_target(1000,-35)
                if payload[2]>500 or payload[5]>500:
                    a=1
                    timer.reset()
                    while True:
                        back_motor.stop()
                        if timer.time()>100:
                            break
                    Yaw=-45
                if turn_count==11 and Yaw<0:
                    Yaw=-50
                back_motor.run((Yaw+40)*25+100)
                if Yaw<-40:
                    break
            if a==1:
                back_motor.stop()
                while True:
                    payload=p.call('blob')
                    front_motor.run_target(1000,-35)
                    back_motor.run(-1000)
                    print("a")
                    print(payload)
                    if (payload[2]>500 and payload[0]<160) or (payload[5]>500 and payload[3]<160):
                        back_motor.stop()
                        break
            elif payload[2]<500 and payload[5]<500:
                obstacle=1
                while True:
                    Yaw=hub.imu.heading()
                    payload=p.call('blob')
                    front_motor.run_target(1000,35)
                    back_motor.run(Yaw*-15+100)
                    if Yaw>10:
                        break
            front_motor.run_target(1000,0)  
            if turn_count==11:
                color=2          
def one_set():
    one_set_count=0
    front_motor.run_target(1000,0)
    payload=p.call('blob')
    print(payload)
    if (payload[2]<500 and payload[5]<500 and eyes.distance()>850) or obstacle==1:#赤もしくは緑のpixel数があるもしくは前の距離が850㎝より小さい
        while True:#前の距離が85㎝まで直進
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
            print("not_found")
            print(payload)
            if obstacle==1 and eyes.distance()<850:
                payload=p.call('blob')  
                print(payload)  
                print(eyes.distance())
                break
            elif obstacle!=1 and (eyes.distance()<850 or payload[2]<500 or payload[5]<500):
                payload=p.call('blob')  
                print(payload)  
                print(eyes.distance())
                break
            elif left_sensor.distance()<100:#左の距離が近いときに中央移動
                timer.reset()
                front_motor.run_target(1000,35)
                while True:
                    hub.light.off()
                    front_motor.run_target(1000,35)
                    back_motor.run(1000) 
                    if timer.time()>700:
                        break
                while True:
                    payload=p.call('blob')
                    print(payload)
                    Yaw=hub.imu.heading()
                    if Yaw>20:
                        Yaw=65
                    back_motor.run((Yaw-5)*15+150)
                    front_motor.run_target(1000,-35)
                    if Yaw<0:
                        front_motor.run_target(1000,0)
                        break
            elif right_sensor.distance()<100:#右の距離が近いときに中央移動
                timer.reset()
                front_motor.run_target(1000,-35)
                while True:
                    hub.light.off()
                    front_motor.run_target(1000,-35)
                    back_motor.run(1000) 
                    if timer.time()>700:
                        break
                while True:
                    payload=p.call('blob')
                    print(payload)
                    Yaw=hub.imu.heading()
                    if Yaw<-20:
                        Yaw=-65
                    back_motor.run((Yaw+5)*-15+150)
                    front_motor.run_target(1000,35)
                    if Yaw>0:
                        front_motor.run_target(1000,0)
                        break
    if payload[2]>payload[5] and payload[2]>400 and obstacle!=1:#赤
        print(eyes.distance())
        print(p.call('blob'))
        payload=p.call('blob')
        if payload[2]>3000:
            print("近い")
            while True:
                payload=p.call('blob')
                hub.light.on(Color.RED)
                front_motor.run_target(1000,0)
                back_motor.run(-1000)
                if payload[2]<3000:
                    break
        while True:#赤回避
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
            if payload[2]>=3000:#赤に近づいた
                timer.reset()
                front_motor.run_target(1000,35)
                while True:#右
                    hub.light.off()
                    front_motor.run_target(1000,35)
                    back_motor.run(1000) 
                    if timer.time()>600:
                        front_motor.run_target(1000,-35)
                        break
                while True:#yaw<10まで左に曲がる途中でコーナーセクション読み取り
                    payload=p.call('blob')
                    print(payload)
                    Yaw=hub.imu.heading()
                    front_motor.run_target(1000,-35)
                    if Yaw>30:
                        Yaw=70
                    back_motor.run((Yaw-10)*15+100)
                    if payload[2]>200:
                        global red_or_green
                        hub.light.on(Color.RED)
                        red_or_green=1
                    elif payload[5]>200:
                        global red_or_green
                        hub.light.on(Color.GREEN)
                        red_or_green=2
                    if Yaw<10:
                        break
                break
    elif payload[2]<payload[5] and payload[5]>400 and obstacle!=1:#緑
        print(eyes.distance())
        print(p.call('blob'))
        if payload[2]>3000:
            print("近い")
            while True:
                payload=p.call('blob')
                hub.light.on(Color.GREEN)
                front_motor.run_target(1000,0)
                back_motor.run(-1000)
                if payload[5]<2000:
                    break
        while True:#緑回避
            payload=p.call('blob')
            print(payload)
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
            if payload[5]>=3000:#緑に近づいた
                timer.reset()
                front_motor.run_target(1000,-35)
                while True:#左
                    hub.light.off()
                    front_motor.run_target(1000,-35)
                    back_motor.run(1000) 
                    if timer.time()>500:
                        front_motor.run_target(1000,35)
                        break
                while True:#yaw>-10まで右に曲がる。途中読み取り
                    Yaw=hub.imu.heading()
                    payload=p.call('blob')
                    print(payload)
                    front_motor.run_target(1000,35)
                    if Yaw<-30:
                        Yaw=-70
                    back_motor.run((Yaw+10)*-15+100)
                    if payload[2]>200:
                        global red_or_green
                        hub.light.on(Color.RED)
                        red_or_green=1
                    elif payload[5]>200:
                        global red_or_green
                        hub.light.on(Color.GREEN)
                        red_or_green=2
                    if Yaw>-10:
                        break
                break
    payload=p.call('blob')
    print(eyes.distance())
    print(payload)
    print("red_or_green:",red_or_green)
def last_right():
    if color==1:#赤
        front_motor.run_target(1000,0)
        timer.reset()
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,(0-Yaw))
            back_motor.run(1000)
            if timer.time()>1000:
                back_motor.stop()
                break
        front_motor.run_target(1000,-35)
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run((90-Yaw)*-25-100)
            if Yaw>90:
                Yaw=hub.imu.heading()
                hub.imu.reset_heading(Yaw-90)
                break
        front_motor.run_target(1000,0)
        timer.reset()
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,(0-Yaw))
            back_motor.run(1000)
            if timer.time()>800:
                back_motor.stop()
                break
    else:#緑
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
            back_motor.run((90-Yaw)*-25-100)
            if Yaw>90:
                Yaw=hub.imu.heading()
                hub.imu.reset_heading(Yaw-90)
                break
def last_left():
    if color==2:#緑
        front_motor.run_target(1000,0)
        timer.reset()
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,(0-Yaw))
            back_motor.run(1000)
            if timer.time()>1000:
                back_motor.stop()
                break
        front_motor.run_target(1000,35)
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            back_motor.run((90+Yaw)*-25-100)
            if Yaw<-90:
                Yaw=hub.imu.heading()
                hub.imu.reset_heading(Yaw+90)
                break
        front_motor.run_target(1000,0)
        timer.reset()
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,(0-Yaw))
            back_motor.run(1000)
            if timer.time()>800:
                back_motor.stop()
                break
    else:#赤
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,-35)
            back_motor.run(1000)
            if Yaw<-40:
                back_motor.stop()
                break
        while True:
            Yaw=hub.imu.heading()
            front_motor.run_target(1000,35)
            back_motor.run((90+Yaw)*-25-100)
            if Yaw<-90:
                Yaw=hub.imu.heading()
                hub.imu.reset_heading(Yaw+90)
                break
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
#_______________________________________________________________________________
while True:
    hub.display.char(str(0))
    if Button.RIGHT in hub.buttons.pressed():
        hub.display.off()
        break
hub.imu.reset_heading(0)
turn_count=0
print(right_sensor.distance())
print(left_sensor.distance())
if right_sensor.distance()>left_sensor.distance():
    start_right()
    right_turn()
    right_turn_or_left_turn=1#右回り
else:
    start_left()
    left_turn()
    right_turn_or_left_turn=2#左回り
turn_count=1
while True:
    if turn_count>9:
        hub.display.number(turn_count)
    else:
        hub.display.char(str(turn_count))
    red_or_green=0
    one_set()
    print("red_or_green:",red_or_green)
    if right_turn_or_left_turn==1:
        right_turn()
    else:
        left_turn()
    turn_count=turn_count+1
    print(turn_count,"/４周成功")
    if turn_count==12:
        break
if right_turn_or_left_turn==1:
    last_right()
else:
    last_left()
parking()
