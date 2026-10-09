# Content
* `Engineering Journal` includes strategy, robot structure, programming, and systems thinking.
* `t-photos` contains 2 photos of the team (an official one and one funny photo with all team members)
* `v-photos` contains 6 photos of the vehicle (from every side, from top and bottom)
* `video` contains the video.md file with the link to a video where driving demonstration exists
* `schemes` contains two schematic diagrams in form of PNG of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `program code` contains code of control software for all components which were programmed.
* `models` is a model file used to manufacture vehicle parts.

# Engineering Journal
- [1:Strategy](#1strategy)
  - [1.1:Open challenge rounds](#11open-challenge-rounds)
  -  [1.2:Obstacle challenge rounds](#12obstacle-challenge-rounds)
  - [1.3:Testing, Tuning, and Trade-offs](#13testing-tuning-and-trade-offs)
- [2:Robot design](#2robot-design)
  - [2.1:Robot materials](#21robot-materials)
  - [2.2:Robot Structure and Actuation](#22robot-structure-and-actuation)
  - [2.3:Power Supply and Wiring](#23power-supply-and-wiring)
    - [2.3.1:Reasons for Power Supply Selection and Wiring Diagram](#231reasons-for-power-supply-selection-and-wiring-diagram)
    - [2.3.2:Power Balance](#232power-balance)
  - [2.4:Motor](#24motor)
    - [2.4.1:Drive Motor](#241drive-motor)
    - [2.4.2:Steering Motor](#242steering-motor)
  - [2.5:Front-wheel steering](#25front-wheel-steering)
  - [2.6:Tires](#26tires)
    - [2.6.1:Front wheel](#261front-wheel)
    - [2.6.2:Rear Wheel](#262rear-wheel)
  - [2.7:Sensors and Sensor Architecture](#27sensors-and-sensor-architecture)
    - [2.7.1:Forward](#271forward)
    - [2.7.2:Left and right](#272left-and-right)
  - [2.8:Camera](#28camera)
- [3:Program](#3program)
  - [3.1:Programming Software (Pybricks, OpenMV)](#31programming-software-pybricks-openmv)
    - [3.1.1:About Pybricks](#311about-pybricks)
    - [3.1.2:About OpenMV](#312about-openmv)
    - [3.1.3:Communication Method](#313communication-method)
  - [3.2:Gyro](#32gyro)
  - [3.3:Design considerations for the Open Challenge rounds](#33design-considerations-for-the-open-challenge-rounds)
    - [3.3.1:P control using a gyro sensor](#331p-control-using-a-gyro-sensor)
    - [3.3.2:Turning method](#332turning-method)
  - [3.4:Design considerations for Obstacle Challenge rounds](#34design-considerations-for-obstacle-challenge-rounds)
- [4:Systems Thinking](#4systems-thinking)
  - [4.1:Interactions Between Subsystems](#41interactions-between-subsystems)
  - [4.2:Vehicle Restrictions](#42vehicle-restrictions)
  - [4.3:Risk Identification and Mitigation Measures](#43risk-identification-and-mitigation-measures)

# 1:Strategy
 To tackle the Open Challenge and Obstacle Challenge rounds, we devised specific strategies for each and built our robots and programs accordingly. We will now explain these strategies.
## 1.1:Open challenge rounds
<img width="2128" height="816" alt="IMG_0444" src="https://github.com/user-attachments/assets/220562c7-5161-4c83-9e9b-d3d0de6793d4" />

 For the Open Challenge rounds, we programmed a strategy aiming for a lap time of 35 seconds: driving at maximum speed on straight sections and decelerating when approaching corners.
 
 We also modularized the movements into functions, enabling rapid parameter adjustments during the tuning phase. Furthermore, we implemented a deceleration routine for 90-degree turns using the gyro sensor, thereby minimizing positional errors that occur after navigating corner sections. Based on this strategy, the robot operates according to the state transition diagram shown below.  
 (For details of the program, see section [3.3](#33design-considerations-for-the-open-challenge-rounds).)

<img width="329" alt="IMG_0396" src="https://github.com/user-attachments/assets/4902cd1f-1dea-48a8-8247-e0e43beadcc0" />. 

## 1.2:Obstacle challenge rounds
　The strategy for the Obstacle Challenge rounds of this tournament is primarily based on the Open Challenge rounds.oundsIt is based on the following. Also, the goal is1 week 30 secondsI created the program with that goal in mind.
Also, as a strategy, in the parking lotChoosing a parking spotI did that. I will proceed with departing from the parking lot. However, regarding parking, initially I was focused on accuracy and didn't have much time to dedicate to it. Therefore, I focused all my efforts on maximizing the accuracy of other missions. However, ultimately, both accuracy improved and I was able to allocate sufficient time for parking, so I decided to proceed with parking. Also,Obstacle detection logicIt operates according to the following state transition diagram.For details about the program, see section [3.4](#34design-considerations-for-obstacle-challenge-rounds).)
<img width="1749" height="1195" alt="IMG_0450" src="https://github.com/user-attachments/assets/d16fad4d-54ea-4150-bda1-f6ac368767b7" />
　　　　　　　　　　　　　　　　　　
                   　　　　　　　State machine diagram

## 1.3:Testing, Tuning, and Trade-offs
To complete the mission more accurately, we consistently aimed to score at least 80% on each challenge and repeatedly ran test workflows such as experiments to measure the distance between the robot and objects to fine-tune our system (see Section 3.4.1 for details). We also made trade-offs regarding parts and programming based on these tests.
 
The table below shows the scores achieved within the time limit during the Open Challenge rounds (open) and Obstacle Challenge rounds (obstacle) across 10 test runs.
<img width="1184" height="792" alt="IMG_0440" src="https://github.com/user-attachments/assets/af8019d3-96aa-457c-8e61-a6926b966361" />

# 2:Robot design
## 2.1:Robot materials
 Our robot wasn’t made using a 3D printer; we built it completely out of LEGO. When we tried making parts with a 3D printer, there would be a few millimeters of error, so things like the steering didn’t work properly. By using LEGO, we were able to rebuild the robot quickly and spend more time on programming.

 Additionally, shown below is a 3D model of our robot created in Studio 2.0; this model serves as a blueprint, enabling anyone to replicate the design.  
 
### ["3D model"](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/models/How%20to%20use%20the%20Robot%203Dmodel.ldr%20file.md)
### ["Robot Assembly Instructions"](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Robot%20Assembly%20Instructions.pdf)
 
## 2.2:Robot Structure and Actuation
<img height="548" alt="image" src="https://github.com/user-attachments/assets/70334450-e47b-4438-85e9-7923fe3e3e13" />

<img height="446" alt="image" src="https://github.com/user-attachments/assets/0d12f19a-05b1-4f6d-aa1e-61b9674fa910" />

 The robot was designed to be compact overall to minimize contact with traffic signs during the Obstacle Challenge rounds. Stability was also enhanced by lowering the chassis height and eliminating internal hollow spaces.  

 Furthermore, the center of gravity (indicated by the red circle) was positioned slightly toward the front wheels rather than directly over the rear wheels to prevent slipping.  
 
<img width="705" alt="image" src="https://github.com/user-attachments/assets/cef562ec-1e1e-4291-a276-66949b6a4136" />

 We selected a rear-wheel drive configuration. This choice reduces the load on the front tires, thereby minimizing measurement errors at the front wheels. In contrast, a front-wheel drive setup tends to drift outward during turns, creating a risk of colliding with obstacles. To improve straight-line accuracy, we positioned the wheel hubs slightly toward the front, effectively eliminating wheel spin.  
 
## 2.3:Power Supply and Wiring
### 2.3.1:Reasons for Power Supply Selection and Wiring Diagram
<img width="1211" height="372" alt="IMG_0414" src="https://github.com/user-attachments/assets/eb4c1120-a182-4412-9657-2020a6df0e03" />

 Since the robot built this time did not require many sensors or motors, a large number of ports was not necessary. Although the clock speed is the lowest, the absence of an operating system eliminates wasteful processing. Furthermore, because the robot can be quickly reconfigured, more time can be devoted to tasks such as program modification.  
 
<img width="1104" height="660" alt="IMG_0434" src="https://github.com/user-attachments/assets/d2936727-a5f5-4118-beb7-8ad10aeb0bf0" />

<img width="2037" height="645" alt="IMG_0401" src="https://github.com/user-attachments/assets/ae9079a7-c838-4897-bd8e-98a3eea6d24b" />


For more details, please visit the link below.
### ["Robot circuit diagram"](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/schemes.md#electromechanical-diagrams)

 With the SPIKE Prime Hub, power is distributed evenly across all six ports. Additionally, the Open MV camera minimizes errors by utilizing only four pins.  

### 2.3.2:Power Balance
 The table below summarizes the actual measured power consumption for each device.  
Furthermore, based on the SPIKE Prime battery used in this instance [Output voltage (V): Rated 7.3V (approx. 8.4V when fully charged); Capacity: 2100mAh], the calculated power margin is 33.3%, indicating that the robot's design is safe.  
※Margin (%) = (1 - (Total maximum current consumption ÷ Maximum current supply capability of the power source)) × 100   
<img width="1216" height="709" alt="IMG_0415" src="https://github.com/user-attachments/assets/58fa5709-6be0-42e0-b0f9-d63807b62309" />

## 2.4:Motor
<img width="677" alt="image" src="https://github.com/user-attachments/assets/c9e81d66-03cd-4705-acef-0b75573ad09e" />

 As described in section 2.2, we used the SPIKE Prime Hub; consequently, we limited our motor selection to SPIKE Prime motors and chose specific motors for the drive and steering systems based on the aforementioned considerations. Calculations regarding the robot's weight (650.8 g) and torque—factoring in a safety margin—indicated that the required torque was 7.7 Ncm for the front wheels and 5.4 Ncm for the rear wheels.  

 ※The formula for calculating torque is "Torque = Applied force x Distance from rotation axis to point of force."  
 The speed calculation formula was "Speed = π x Diameter of rotating body x Number of revolutions per minute / 60"  
 Calculation of the required torque at the front wheels is "Frictional resistance moment = coefficient of friction x weight on      one front wheel x scrub radius."  

### 2.4.1:Drive Motor
　Since the drive motor only needs to perform simple forward and backward movements, I used the "SPIKE Prime M Motor," which is compact, lightweight, and easy to mount on the robot.  

### 2.4.2:Steering Motor
　Since the weight of the robot bears down on the steering mechanism, a motor torque greater than 7.7 Ncm was required to operate it. Therefore, the high-torque "SPIKE Prime L-Motor" was used.  

## 2.5:Front-wheel steering
<img width="828" alt="image" src="https://github.com/user-attachments/assets/eea00792-96e5-41ae-acad-dc8d2ea9165d" />
[Steering Section]

　For this competition, we employed the Ackermann-Jeantaud steering mechanism. We had previously used the rack-and-pinion system—which is easier to implement—but poor meshing between the pinion and rack caused lateral slipping and resistance during turns, resulting in a success rate of only about 50%.
Switching to the Ackermann-Jeantaud mechanism reduced the number of failures, raising our success rate to approximately 90%. Since turning accuracy is crucial for this competition, we decided to adopt this mechanism.  

Additionally, by installing a physical stopper on the steering assembly, we eliminated the need to limit the steering range via programming.  

## 2.6:Tires
###  2.6.1:Front wheel
<img width="380" alt="image" src="https://github.com/user-attachments/assets/7b3f6dec-f834-4c38-91df-4e157a5d072f" />

 For the front wheels, I used tires with design ID 55976, a diameter of 56 mm, and a width of 26 mm. Although the width is 26 mm—making them nearly the same size as the rear tires—I chose them because they have a smaller contact area with the ground; this reduces friction, making it easier to steer the vehicle left and right.  

### 2.6.2:Rear Wheel
<img width="380" alt="IMG_0429" src="https://github.com/user-attachments/assets/35e5861f-a23f-4bdc-8023-6a5007324925" />

 For the rear wheel, we used a tire with design ID 41897, 56mm in diameter and 28mm in width. We chose this tire because its large contact surface with the ground increases friction, resulting in greater propulsion and making it easier to increase speed.  

## 2.7:Sensors and Sensor Architecture
<img width="1256" height="1098" alt="IMG_0430" src="https://github.com/user-attachments/assets/e708f746-7482-4457-b785-3cc193ba4d20" />

### 2.7.1:Forward
<img  height="348" alt="image" src="https://github.com/user-attachments/assets/d310ef52-c1d7-471b-88f6-9f8c3b2d1c0e" />

 Through repeated testing with this robot, it was discovered that during the Open Challenge rounds, the angle of incidence error would be at least ±5° when completing the corner section.  
 Therefore, to ensure that the wall could be read even with this error, a distance sensor with a wide measurement range was used, as can be seen in Graph 1.  
 
### 2.7.2:Left and right
<img  height="348" alt="image" src="https://github.com/user-attachments/assets/38cd2c0b-a8cf-43cb-9d08-de35d7f445a2" />

 The left and right distance sensors are used to determine the proximity to the left and right walls, confirm the direction of rotation, and act as a safety device to prevent contact with the walls. (See 3.4.4 for details.) Therefore, by mounting the distance sensors vertically as shown in the image above, the error is reduced. The reason for using distance sensors is that they can read within 30 cm when performing high-speed detection, so we judged them to be suitable sensors for use as a safety device.  
 
## 2.8:Camera
<img width="1985" height="936" alt="IMG_0436" src="https://github.com/user-attachments/assets/774ea911-0749-4429-92f4-10428d290cb2" />

 We used a camera with the front part of the distance sensor removed and an OpenMV Cam H7 Plus attached.  

 The OpenMV Cam H7 Plus has the advantages of lower power consumption, a larger memory capacity (making it less likely to crash), and high image quality (reducing the likelihood of failing to read traffic signs). In addition, it has no packet loss or OS overhead delays. The table below compares the cameras we considered.  
<img width="1225" height="739" alt="IMG_0417" src="https://github.com/user-attachments/assets/8c2f6672-50a0-420d-8091-32b4a7ce8812" />

## 2.9:Starting and stopping in a parking lot
<img width="500" alt="IMG_0454" src="https://github.com/user-attachments/assets/a73bf5e9-adaf-4039-8a8f-91c45c56b8bd" />

In the Obstacle Challenge rounds, we often struggled to complete the course within the time limit due to the time it took to launch from the parking area and park. Therefore, to increase the distance between parking areas and reduce the time, we added a protrusion (hereinafter referred to as Part A) to the robot, extending from the bottom of the front ultrasonic sensor (as shown by the blue circle in the image above), making it as thin as possible to avoid contact with the parking area.
To determine the length of Part A, we used the following formula:

(Robot's total length + Length of Part A) * 1.5 >= Distance the robot is closest to the parking area

The robot's total length is 22.5cm, and the closest distance the robot is to the parking area is approximately 36cm. Letting the length of Part A be xcm, we substitute these values ​​into the above formula:

(22.5 + x) * 1.5 >= 36

x >= 1.5

Therefore, we determined that Part A should be at least 1.5cm long. We adjusted the length to approximately 4.5cm, ensuring it did not exceed the robot's size limit, providing a margin of safety. Furthermore, by using Part A, we succeeded in reducing both the time it takes to start and the time it takes to park by 8 seconds each. Moreover, while previously we could only complete the course 4 out of 10 times, with Part A installed, we can now complete the course within the time limit every time.
<img width="600" alt="IMG_0456" src="https://github.com/user-attachments/assets/f533c13c-9176-46fd-9062-c8f73f0bfa55" />
[How the robot starts moving]

# 3:Program
## 3.1:Programming Software (Pybricks, OpenMV)
### 3.1.1:About Pybricks
<img width="1218" height="731" alt="IMG_0407" src="https://github.com/user-attachments/assets/d1deb840-45f8-4b11-a0bb-22c190155b49" />
This robot uses Pybricks.The reason is compared to other program sites, it has the shortest startup time and control loop period.ExcellentWe chose this because of its advantage of having a motor synchronous control with an error of less than 1 degree and virtually no error.

### 3.1.2:About OpenMV
We used a camera with the front part of the distance sensor removed and an OpenMV Cam H7 Plus attached. The reasons for this choice (from a programming perspective) are as follows.
<img width="1216" height="809" alt="IMG_0408" src="https://github.com/user-attachments/assets/a4cf96ad-8d9e-4b4c-bb55-0a9699268195" />
As you can see from this table, we chose openMV because of its advantages, such as requiring fewer lines of code for data transmission and significantly less code than other cameras for transmitting coordinate data. Furthermore, since it uses the same language as pybricks, we didn't need to learn a new language, allowing us to dedicate more time to editing other programs.
（For the reasons for its use (from a robot's perspective), please refer to section [2.8](#28camera).）

### 3.1.3:Communication Method
<img width="2056" height="1210" alt="IMG_0421" src="https://github.com/user-attachments/assets/d5c9773c-a531-4fde-bfc2-78ca0d4cada8" />
<img width="1371" height="1140" alt="IMG_0422" src="https://github.com/user-attachments/assets/0ad3b567-a031-48e7-85db-4fabb50f9b42" />
Communication methodThe main program within Open MV receives data from three Open MV modules. Open MV then sends this data to pybricks via pupremote.

## 3.2:Gyro
We attempted to precisely control the aircraft's trajectory using the "yaw angle" obtained from the built-in gyro sensor. However, due to the risk of "drift error" in the gyro sensor, we were only successful in 4 out of 10 attempts.Measures are taken based on the following iterative cycle.I did it.

• Risk "Drift Error" : The angle changes slightly when turning, and in the latter half of the competition straight line accuracy decreases.

• Countermeasure : Incorporate code to automatically reset the gyroscope's current angle to 0° in software when the robot is completely stationary (such as immediately after starting or after detecting a wall).

These measures resulted in a success rate of 9 out of 10 attempts, reducing the trajectory deviation of the aircraft due to the gyro.We were able to increase the success rate.

## 3.3:Design considerations for the Open Challenge rounds
In the Open Challenge rounds, which have no obstacles, precise straight-line driving and 90° turns are required.We have introduced an algorithm that optimizes the trade-off between "driving speed" and "recovery accuracy".I did.
<img width="1126" height="884" alt="IMG_0424" src="https://github.com/user-attachments/assets/af71fd45-adcf-491f-b119-8c4593d38cc6" />

### 3.3.1:P control using a gyro sensor
To automatically correct uneven friction on the tires during straight-line driving, proportional control was introduced, which determines the steering amount based on the error between the target yaw angle and the current gyro sensor value, using the program shown in line 6 of Image 3.
<img width="1233" height="184" alt="IMG_0425" src="https://github.com/user-attachments/assets/4c2e0a42-385c-4021-b1c7-db41bc9a1ceb" />
Initially, we used PID control with added differentiation and integration,Results of actually running it on the courseIn this competition, it was found that incorporating differential and integral calculus into the control system actually made the robot's behavior unstable. Furthermore, when measuring the lateral deviation over a straight 5m distance, the deviation was 7cm with PID control and 5cm with PD control, but the deviation was reduced to within 3cm with P control alone. Therefore, for the purpose of simplifying the system and stabilizing the behavior, ultimately, we adopted "P control".

### 3.3.2:Turning method
According to the variable in line 14 of Image 3, the rotation starts at the fastest speed.It slows down as it approaches the target value.By incorporating this program, we completely eliminated inertial overshoot and achieved precise turning with an accuracy of within ±0.5° of the target value.
<img width="1242" height="184" alt="IMG_0426" src="https://github.com/user-attachments/assets/24d969de-4038-4685-8ea2-5a6854c2be26" />

## 3.4:Design considerations for Obstacle Challenge rounds
In the Obstacle Challenge rounds, we believed the key was how to simplify the process of dynamically recognizing traffic signs using cameras and switching between complex driving patterns accordingly. Based on this, we implemented the following improvements.

# 4:Systems Thinking
## 4.1:Interactions Between Subsystems
<img width="1693" height="1181" alt="IMG_0437" src="https://github.com/user-attachments/assets/0feb5de7-3d26-4800-841b-3499fa1e8290" />
   
<img width="1694" height="1170" alt="IMG_0438" src="https://github.com/user-attachments/assets/aee40241-c785-4dda-a6df-aae956f75e4a" />

<img width="1684" height="1126" alt="IMG_0439" src="https://github.com/user-attachments/assets/610b2512-00f7-47a1-955e-f0f6c0dde551" />
　　　　　　　　　　　　　　　　　［Subsystem Diagram］

To make it easier to identify where changes would have an impact when redesigning our robot’s subsystems, we created a subsystem diagram illustrating the interrelationships among the drive, sensor, power supply, and processing components mentioned above. From this diagram, we realized that the sensor system utilized various subsystems, so we decided to use OpenMV to reduce the number of lines of code within the camera in order to minimize program execution time as much as possible. In addition, this reduced the load on the Spike Hub and improved the control cycle. (See Section [3.1.2](#312about-openmv)) for details.)  

Furthermore, this diagram allows others to easily understand the interrelationships and interactions among our robot’s subsystems at a glance.  

## 4.2:Vehicle Restrictions
Because the weight limit at the competition was 1.5 kg, the number of things on the robot was limited. Although the robot originally made did not exceed the restrictions, it weighed 689.2g. Therefore, the time to capture was limited, but it was a little longer. Therefore, by reducing the number of parts used for fixing by lowering the height of the robot, the weight of the robot can be 650.8g, and the capture time can be reduced by an average of 15 seconds, making it possible to capture quickly and accurately. I did.

## 4.3:Risk Identification and Mitigation Measures
<img width="1064" height="601" alt="IMG_0441" src="https://github.com/user-attachments/assets/d8ee7cc0-894b-4410-b92d-e2a279366637" />
　　　　　　　　　[A place where everyone can check the corrections in Japanese]

By consistently identifying and analyzing these risks and ensuring that everyone is aware of them, we are able to improve the robots’ accuracy. In addition, by working together to tackle problems that are difficult to solve through programming, we are reducing the burden on programmers.  

# How to build a robot
* 
