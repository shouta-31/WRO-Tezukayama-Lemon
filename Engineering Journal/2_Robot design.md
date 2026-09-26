# [2:Robot design](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#2robot-design)
## [2.1:Robot materials](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#21robot-materials)
 By constructing the majority of our robot using LEGO bricks and incorporating some 3D-printed parts, we were able to rebuild the robot quickly and dedicate more time to programming. The use of 3D-printed components also allowed for immediate repairs in the event of breakage.  

 Additionally, shown below is a 3D model of our robot created in Studio 2.0; this model serves as a blueprint, enabling anyone to replicate the design.  

3D modelを貼るところ
 
## [2.2:Robot Structure and Actuation](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#22robot-structure-and-actuation)
<img width="599" alt="IMG_0427" src="https://github.com/user-attachments/assets/31360c6c-fa7c-43ed-9386-0d519ea2efbf" />

<img width="681" alt="image" src="https://github.com/user-attachments/assets/ff01cee0-06ad-47a6-a6f4-e2ac6951378d" />

 The robot was designed to be compact overall to minimize contact with traffic signs during the Obstacle Challenge rounds. Stability was also enhanced by lowering the chassis height and eliminating internal hollow spaces.  

 Furthermore, the center of gravity (indicated by the red circle) was positioned slightly toward the front wheels rather than directly over the rear wheels to prevent slipping.  
 
<img width="705" alt="image" src="https://github.com/user-attachments/assets/cef562ec-1e1e-4291-a276-66949b6a4136" />

 We selected a rear-wheel drive configuration. This choice reduces the load on the front tires, thereby minimizing measurement errors at the front wheels. In contrast, a front-wheel drive setup tends to drift outward during turns, creating a risk of colliding with obstacles. To improve straight-line accuracy, we positioned the wheel hubs slightly toward the front, effectively eliminating wheel spin.  
 
## [2.3:Power Supply and Wiring](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#23power-supply-and-wiring) 
### [2.3.1:Reasons for Power Supply Selection and Wiring Diagram](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#231reasons-for-power-supply-selection-and-wiring-diagram)
<img width="1211" height="372" alt="IMG_0414" src="https://github.com/user-attachments/assets/eb4c1120-a182-4412-9657-2020a6df0e03" />

 Since the robot built this time did not require many sensors or motors, a large number of ports was not necessary. Although the clock speed is the lowest, the absence of an operating system eliminates wasteful processing. Furthermore, because the robot can be quickly reconfigured, more time can be devoted to tasks such as program modification.  
<img width="1104" height="660" alt="IMG_0434" src="https://github.com/user-attachments/assets/d2936727-a5f5-4118-beb7-8ad10aeb0bf0" />

<img width="2037" height="645" alt="IMG_0401" src="https://github.com/user-attachments/assets/ae9079a7-c838-4897-bd8e-98a3eea6d24b" />

 With the SPIKE Prime Hub, power is distributed evenly across all six ports. Additionally, the Open MV camera minimizes errors by utilizing only four pins.  

### [2.3.2:Power Balance](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#232power-balance)
 The table below summarizes the actual measured power consumption for each device.  
Furthermore, based on the SPIKE Prime battery used in this instance [Output voltage (V): Rated 7.3V (approx. 8.4V when fully charged); Capacity: 2100mAh], the calculated power margin is 33.3%, indicating that the robot's design is safe.  
※Margin (%) = (1 - (Total maximum current consumption ÷ Maximum current supply capability of the power source)) × 100   
<img width="1216" height="709" alt="IMG_0415" src="https://github.com/user-attachments/assets/58fa5709-6be0-42e0-b0f9-d63807b62309" />

## [2.4:Motor](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#24motor)
<img width="677" alt="image" src="https://github.com/user-attachments/assets/c9e81d66-03cd-4705-acef-0b75573ad09e" />

 As described in section 2.2, we used the SPIKE Prime Hub; consequently, we limited our motor selection to SPIKE Prime motors and chose specific motors for the drive and steering systems based on the aforementioned considerations. Calculations regarding the robot's weight (650.8 g) and torque—factoring in a safety margin—indicated that the required torque was 7.7 Ncm for the front wheels and 5.4 Ncm for the rear wheels.  

 ※The formula for calculating torque is "Torque = Applied force x Distance from rotation axis to point of force."  
 The speed calculation formula was "Speed = π x Diameter of rotating body x Number of revolutions per minute / 60"  
 Calculation of the required torque at the front wheels is "Frictional resistance moment = coefficient of friction x weight on      one front wheel x scrub radius."  

### [2.4.1:Drive Motor](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#241drive-motor)
　Since the drive motor only needs to perform simple forward and backward movements, I used the "SPIKE Prime M Motor," which is compact, lightweight, and easy to mount on the robot.  

### [2.4.2:Steering Motor](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#242steering-motor)
　Since the weight of the robot bears down on the steering mechanism, a motor torque greater than 7.7 Ncm was required to operate it. Therefore, the high-torque "SPIKE Prime L-Motor" was used.  

## [2.5:Front-wheel steering](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#25front-wheel-steering)
<img width="828" alt="image" src="https://github.com/user-attachments/assets/eea00792-96e5-41ae-acad-dc8d2ea9165d" />
[Steering Section]

　For this competition, we employed the Ackermann-Jeantaud steering mechanism. We had previously used the rack-and-pinion system—which is easier to implement—but poor meshing between the pinion and rack caused lateral slipping and resistance during turns, resulting in a success rate of only about 50%.
Switching to the Ackermann-Jeantaud mechanism reduced the number of failures, raising our success rate to approximately 90%. Since turning accuracy is crucial for this competition, we decided to adopt this mechanism.  

Additionally, by installing a physical stopper on the steering assembly, we eliminated the need to limit the steering range via programming.  

## [2.6:Tires](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#26tires)
###  [2.6.1:Front wheel](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#261front-wheel)
<img width="380" alt="image" src="https://github.com/user-attachments/assets/7b3f6dec-f834-4c38-91df-4e157a5d072f" />

 For the front wheels, I used tires with design ID 55976, a diameter of 56 mm, and a width of 26 mm. Although the width is 26 mm—making them nearly the same size as the rear tires—I chose them because they have a smaller contact area with the ground; this reduces friction, making it easier to steer the vehicle left and right.  

### [2.6.2:Rear Wheel](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#262rear-wheel)
<img width="380" alt="IMG_0429" src="https://github.com/user-attachments/assets/35e5861f-a23f-4bdc-8023-6a5007324925" />

 For the rear wheel, we used a tire with design ID 41897, 56mm in diameter and 28mm in width. We chose this tire because its large contact surface with the ground increases friction, resulting in greater propulsion and making it easier to increase speed.  

## [2.7:Sensors and Sensor Architecture](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#27sensors-and-sensor-architecture)
<img width="1256" height="1098" alt="IMG_0430" src="https://github.com/user-attachments/assets/e708f746-7482-4457-b785-3cc193ba4d20" />

### [2.7.1:Forward](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#271forward)
<img width="277" height="293" alt="IMG_0431" src="https://github.com/user-attachments/assets/3f4f5938-eede-44cc-a5f0-2a4c358da770" />

 Through repeated testing with this robot, it was discovered that during the Open Challenge rounds, the angle of incidence error would be at least ±5° when completing the corner section.  
 Therefore, to ensure that the wall could be read even with this error, a distance sensor with a wide measurement range was used, as can be seen in Graph 1.  
 
### [2.7.2:Left and right](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#272left-and-right)
<img width="430" height="288" alt="IMG_0432" src="https://github.com/user-attachments/assets/a9f84f56-5a69-4ce2-959d-f1c226110ec8" />

 The left and right distance sensors are used to determine the proximity to the left and right walls, confirm the direction of rotation, and act as a safety device to prevent contact with the walls. (See 3.4.4 for details.) Therefore, by mounting the distance sensors vertically as shown in the image above, the error is reduced. The reason for using distance sensors is that they can read within 30 cm when performing high-speed detection, so we judged them to be suitable sensors for use as a safety device.  
 
## [2.8:Camera](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#28camera)
<img width="1985" height="936" alt="IMG_0436" src="https://github.com/user-attachments/assets/774ea911-0749-4429-92f4-10428d290cb2" />

 We used a camera with the front part of the distance sensor removed and an OpenMV Cam H7 Plus attached.  

 The OpenMV Cam H7 Plus has the advantages of lower power consumption, a larger memory capacity (making it less likely to crash), and high image quality (reducing the likelihood of failing to read traffic signs). In addition, it has no packet loss or OS overhead delays. The table below compares the cameras we considered.  
<img width="1225" height="739" alt="IMG_0417" src="https://github.com/user-attachments/assets/8c2f6672-50a0-420d-8091-32b4a7ce8812" />
