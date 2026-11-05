# WRO 2026 Future Engineers - Tezukayama Lemon 🇯🇵
<div align="center"><img height="548" alt="image" src="https://github.com/user-attachments/assets/70334450-e47b-4438-85e9-7923fe3e3e13" /></div>

This is the official repository of Teizukayama Lemon, a representative of Japan in the World Robot Olympiad (WRO) 2026 Future Engineers category. This repository contains comprehensive engineering texts on robot design, strategy, programming, and system thinking. The robot, the program, and this book were created by a team of three students with the support of a coach.

# Content
* `README.md` detailing our entire engineering process. `The Engineering Journal` covers our strategy, robot structure, programming, and system thinking.
* `t-photos` contains 2 photos of the team (an official one and one funny photo with all team members)
* `v-photos` contains 6 photos of the vehicle (from every side, from top and bottom)
* `video` contains the video.md file with the link to a video where driving demonstration exists
* `schemes` contains two schematic diagrams in form of PNG of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `program code (src)` contains code of control software for all components which were programmed.
* `models` is a model file used to manufacture vehicle parts.
* `flow_chart` contains the flowchart used in the README.
  
# A team
## Team introduction
Hello. We are Teizukayama Lemon, the representative of Japan in the World Robot Olympiad (WRO) 2026 Future Engineers category. I am very happy to be able to participate in high-level world competitions, fight, and interact with teams from various countries. Teizukayama Lemon consists of three high school students enrolled in Teizukayama High School in Japan. For six months, we have been testing many times, tuning each time, and preparing for the world championship by trial and error so that we can get higher scores quickly in time. We will aim to win the championship, which is our goal, by making use of this effort and preparation!

## Team members
- Kyosuke Esumi : A programmer
  - Date of birth : January 19th
  - Age : 15 years old

- Shuta Morita : Document preparation
  - Date of birth : March 6th
  - Age : 15 years old

- Shota Ueno : A builder
  - Date of birth : March 1st
  - Age : 15 years old

- Mr.Hiroshi Yahiro : A team coach
  - Occupation : A teacher
# Our Robot
| | |
|---|---|
| **Front** <img width="564" alt="image" src="https://github.com/user-attachments/assets/00c84796-dd00-4a39-b207-10faf451d491" /> | **Rear side** <img width="564" alt="image" src="https://github.com/user-attachments/assets/aa577b3c-ef56-4591-8b7e-dc55126ac665" /> |
| **Left side** <img width="564" alt="image" src="https://github.com/user-attachments/assets/0b4a38e3-5ffb-40f7-98de-13d36cab832d" /> | **Right side** <img width="564" alt="image" src="https://github.com/user-attachments/assets/9dad31b1-82e9-49de-838c-c85e7d5bf97d" /> |
| **Top surface** <img width="448" alt="image" src="https://github.com/user-attachments/assets/6ce8dc47-2df8-437a-b372-b483424ec9dc" /> | **Bottom surface** <img width="448" alt="image" src="https://github.com/user-attachments/assets/98fff5eb-049d-4bff-824f-0a288c104d05" /> |

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
  - [2.7:Sensors, sensor architecture, and sensor calibration methods](#27Sensors,-sensor-architecture,-and-sensor-calibration-methods)
    - [2.7.1:Forward](#271forward)
    - [2.7.2:Left and right](#272left-and-right)
    - [2.7.3:Sensor calibration methods](#273Sensor-calibration-methods)
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
    - [3.4.1:Measuring the distance to traffic signs based on the number of pixel](#341measuring-the-distance-to-traffic-signs-based-on-the-number-of-pixel)
    - [3.4.2:A program that reads nearby traffic signs and transmits the values ​​obtained](#342a-program-that-reads-nearby-traffic-signs-and-transmits-the-values-obtained)
    - [3.4.3:Turning Method](#343turning-method)
    - [3.4.4:How to drive a straight line section](#344how-to-drive-a-straight-line-section)
    - [3.4.5:How to prevent misidentification](#345how-to-prevent-misidentification)
    - [3.4.6:Destination setting](#346destination-setting)
    - [3.4.7:Parking](#347parking)
  - [3.5:Other ingenuity points](#35other-ingenuity-points)
    - [3.5.1:Visualization of mistakes in print statements](#351visualization-of-mistakes-in-print-statements)
    - [3.5.2:How to determine the turning direction](#352how-to-determine-the-turning-direction)
- [4:Systems Thinking](#4systems-thinking)
  - [4.1:Interactions Between Subsystems](#41interactions-between-subsystems)
  - [4.2:Vehicle Restrictions](#42vehicle-restrictions)
  - [4.3:Risk Identification and Mitigation Measures](#43risk-identification-and-mitigation-measures)
- [5:Reference materials](#5Reference-materials)

# 1:Strategy
To tackle the Open Challenge and Obstacle Challenge rounds, we devised specific strategies for each and built our robots and programs accordingly. We will now explain these strategies.
## 1.1:Open challenge rounds
<img width="2128" height="816" alt="IMG_0444" src="https://github.com/user-attachments/assets/220562c7-5161-4c83-9e9b-d3d0de6793d4" />

For the Open Challenge rounds, we programmed a strategy aiming for a lap time of 35 seconds: driving at maximum speed on straight sections and decelerating when approaching corners.
 
We also modularized the movements into functions, enabling rapid parameter adjustments during the tuning phase. Furthermore, we implemented a deceleration routine for 90-degree turns using the gyro sensor, thereby minimizing positional errors that occur after navigating corner sections. Based on this strategy, the robot operates according to the state transition diagram shown below.  
(For details of the program, see section [3.3](#33design-considerations-for-the-open-challenge-rounds).)

<div align="center"><img width="329" alt="IMG_0396" src="https://github.com/user-attachments/assets/4902cd1f-1dea-48a8-8247-e0e43beadcc0" /></div>

## 1.2:Obstacle challenge rounds
The strategy for the Obstacle Challenge rounds of this tournament is primarily based on the Open Challenge rounds.oundsIt is based on the following. Also, the goal is1 week 30 secondsI created the program with that goal in mind.
Also, as a strategy, in the parking lotChoosing a parking spotI did that. I will proceed with departing from the parking lot. However, regarding parking, initially I was focused on accuracy and didn't have much time to dedicate to it. Therefore, I focused all my efforts on maximizing the accuracy of other missions. However, ultimately, both accuracy improved and I was able to allocate sufficient time for parking, so I decided to proceed with parking. Also,Obstacle detection logicIt operates according to the following state transition diagram.For details about the program, see section [3.4](#34design-considerations-for-obstacle-challenge-rounds).)

<img width="1749" height="1195" alt="IMG_0450" src="https://github.com/user-attachments/assets/d16fad4d-54ea-4150-bda1-f6ac368767b7" />
<p align="center"><b>[State machine diagram]</b></p>

## 1.3:Testing, Tuning, and Trade-offs
To complete the mission more accurately, we consistently aimed to score at least 80% on each challenge and repeatedly ran test workflows such as experiments to measure the distance between the robot and objects to fine-tune our system. We also made trade-offs regarding parts and programming based on these tests.
The table below shows the scores achieved within the time limit during the Open Challenge rounds (open) and Obstacle Challenge rounds (obstacle) across 10 test runs.
<img width="1184" height="792" alt="IMG_0440" src="https://github.com/user-attachments/assets/af8019d3-96aa-457c-8e61-a6926b966361" />

# 2:Robot design
## 2.1:Robot materials
Our robot wasn’t made using a 3D printer; we built it completely out of LEGO. When we tried making parts with a 3D printer, there would be a few millimeters of error, so things like the steering didn’t work properly. By using LEGO, we were able to rebuild the robot quickly and spend more time on programming.
Additionally, shown below is a 3D model of our robot created in Studio 2.0; this model serves as a blueprint, enabling anyone to replicate the design.  
 
### ["3D model"](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/models/How%20to%20use%20the%20Robot%203Dmodel.ldr%20file.md)
### ["Robot Assembly Instructions"](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Robot%20Assembly%20Instructions.pdf)
 
## 2.2:Robot Structure and Actuation
<div align="center"><img height="548" alt="image" src="https://github.com/user-attachments/assets/70334450-e47b-4438-85e9-7923fe3e3e13" /></div>

<div align="center"><img height="446" alt="IMG_0492" src="https://github.com/user-attachments/assets/9b071c70-5171-4b5f-aa37-73eb3409209f" /></div>

<p align="center"><b>[Center of gravity of the robot]</b></p>

The robot was designed to be compact overall to minimize contact with traffic signs during the Obstacle Challenge rounds. Stability was also enhanced by lowering the chassis height and eliminating internal hollow spaces.  

Furthermore, the center of gravity (indicated by the red circle) was positioned slightly toward the front wheels rather than directly over the rear wheels to prevent slipping.  

 |  | Front-wheel drive | Rear-wheel drive |  
 |:---:|---|---|  
 | **Mechanism** | The front wheels are both the drive and steering wheels. | The front wheels steer, and the rear wheels drive. |
 | **traction** | Expanding outwards | Less likely to expand outwards |
 | **accelerate** | Easy to spin freely | Because the weight is shifted to the rear, it is easier to accelerate. |
 | **Accuracy of straight-line movement** | It provides stability due to its high grip. | The low grip can make it unstable.  |
 
And I chose rear-wheel drive as the drive system. This is because rear-wheel drive makes it difficult to load the front tire and reduces the numerical error of the front wheel. In addition, if you use front-wheel drive, you may hit an obstacle because it is easy to swell out in the curve. There are other four-wheel drives, but in four-wheel drive, if you use gears from the rear wheel to bring power to the front wheel, the tires of the rear wheel will move a little faster, resulting in errors such as parking.
In order to increase the accuracy of straight ahead, the hub was slightly brought to the front wheel side to eliminate empty spinning. 
 
## 2.3:Power Supply and Wiring
### 2.3.1:Reasons for Power Supply Selection and Wiring Diagram

<div align="center">

 |  | SPIKE Prime Hub | Raspberry Pi | EV3 |
 |:---:|---|---|---|
 | **Number of ports** | 6 ports | GPIO 40-pin | 4 input ports, 4output ports | 1 core |
 | **Clock period** | 100MHz | 1.5GHz | 300MHz |
 | **OS** | none | Linux | Linux-based OS |

</div>

Since the robot built this time did not require many sensors or motors, a large number of ports was not necessary. Although the clock speed is the lowest, the absence of an operating system eliminates wasteful processing. Furthermore, because the robot can be quickly reconfigured, more time can be devoted to tasks such as program modification.  
 
<img width="1104" height="660" alt="IMG_0434" src="https://github.com/user-attachments/assets/d2936727-a5f5-4118-beb7-8ad10aeb0bf0" />

<img width="2037" height="645" alt="IMG_0401" src="https://github.com/user-attachments/assets/ae9079a7-c838-4897-bd8e-98a3eea6d24b" />

<p align="center"><b>[Wiring diagram inside the hub]&[OpenMV wiring diagram]</b></p>

For more details, please visit the link below.
### ["Robot circuit diagram"](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/schemes/Schematic.md)

With the SPIKE Prime Hub, power is distributed evenly across all six ports. Additionally, the Open MV camera minimizes errors by utilizing only four pins.  

### 2.3.2:Power Balance
The table below summarizes the actual measured power consumption for each device.  
Furthermore, based on the SPIKE Prime battery used in this instance [Output voltage (V): Rated 7.3V (approx. 8.4V when fully charged); Capacity: 2100mAh], the calculated power margin is 33.3%, indicating that the robot's design is safe.  

$$
\text{Margin [\\%]} = \left(1 - \frac{\text{Total maximum current consumption}}{\text{Maximum current supply capability of the power source}} \right) \times 100
$$

<div align="center">
 
 |  | device | At rest (mA) | During action (mA) |
 |:---:|---|---|---|
 | **Hub body** | SPIKE Hub Gyroscope sensor etc. | 50 | 100|
 | **Port A** | Distance sensor | 15 | 30 |
 | **Port B** | Distance sensor | 15 | 30 |
 | **Port C** | M motor | 50 | 250 |
 | **Port D** | L motor | 100 | 500 |
 | **Port E** | Distance sensor | 15 | 30 |
 | **Port F** | OpenMV H7 Cam Plus | 100 | 200 |
 | **Total** | Entire system | 345 | 1140 |  

</div>
<p align="center"><b>[Table of electricity balance]</b></p>

## 2.4:Motor

|  | SPIKE Prime M Motor <img width="300" height="200" alt="image" src="https://github.com/user-attachments/assets/00032b75-2055-453e-a9f2-e9383d24ad08" /> | SPIKE Prime L Motor <img width="300" height="200" alt="image" src="https://github.com/user-attachments/assets/b349e044-b045-4d70-bab0-5f2c46cf8896" /> |
| :--- | :--- | :--- |
| **Output /<br>Operating<br>Voltage Range** | Minimum: 5 V<br>Maximum: 9 V | Minimum: 5 V<br>Maximum: 9 V |
| **Performance** | **No load:**<br>• Torque: 0 Ncm<br>• Speed: 185 RPM ±15%<br>• Current: 110 mA ±15%<br><br>**Maximum efficiency:**<br>• Torque: 3.5 Ncm<br>• Speed: 135 RPM ±15%<br>• Current: 280 mA ±15%<br><br>**Stall:**<br>• Torque: 18 Ncm<br>• Speed: 0 RPM<br>• Current: 800 mA ±15%<br><br>*(The data above is based on a 7.2 V power supply.)* | **No load:**<br>• Torque: 0 Ncm<br>• Speed: 175 RPM ±15%<br>• Current: 135 mA ±15%<br><br>**Maximum efficiency:**<br>• Torque: 8 Ncm<br>• Speed: 135 RPM ±15%<br>• Current: 430 mA ±15%<br><br>**Stall:**<br>• Torque: 25 Ncm<br>• Speed: 0 RPM<br>• Current: 1400 mA ±15%<br><br>*(The data above is based on a 7.2 V power supply.)* |
| **Rotation Sensor** | Resolution: 1 rotation = 360 counts<br>Accuracy: ±3 degrees<br>Update rate: 100 Hz | Resolution: 1 rotation = 360 counts<br>Accuracy: ±3 degrees<br>Update rate: 100 Hz |

<p align="center"><b>[SPIKE Prime motor data]</b></p>

As described in section [2.2](#22robot-structure-and-actuation), we used the SPIKE Prime Hub; consequently, we limited our motor selection to SPIKE Prime motors and chose specific motors for the drive and steering systems based on the aforementioned considerations. Calculations regarding the robot's weight (650.8 g) and torque—factoring in a safety margin—indicated that the required torque was 6.72 Ncm for the front wheels and 2.1 Ncm for the rear wheels.  

**1:Torque calculation formula**

$$
T = F_{\text{app}} \times r
$$

* $T = \text{Torque}$
* $F_{\text{app}} = \text{Applied force}$
* $r = \text{Distance from rotation axis to point of force}$

**2:Speed ​​calculation formula**

$$
v = \frac{\pi \times d \times n}{60}
$$

* $v = \text{Speed}$
* $d = \text{Diameter of rotating body}$
* $n = \text{Number of revolutions per minute}$

**3:Formula for calculating the torque required for the front wheel (frictional moment of resistance)**

$$
M = μ \times P \times \frac{d}{2}
$$

* $M = \text{Frictional resistance moment}$
* $μ = \text{coefficient of friction of bearings}$
* $P = \text{Load on the bearing}$
* $d = \text{Inner diameter of the bearing}$

### 2.4.1:Drive Motor
Since the drive motor only needs to perform simple forward and backward movements, I used the "SPIKE Prime M Motor," which is compact, lightweight, and easy to mount on the robot.  

### 2.4.2:Steering Motor
Since the weight of the robot rests on the steering mechanism, a motor with a torque greater than 6.72 Ncm was required to operate it. For this reason, we used the "SPIKE Prime L-motor," which offers high torque and minimal speed reduction under load.  

## 2.5:Front-wheel steering
<div align="center"><img width="828" alt="image" src="https://github.com/user-attachments/assets/eea00792-96e5-41ae-acad-dc8d2ea9165d" /></div>

<p align="center"><b>[Steering Section]</b></p>

For this competition, we used "parallel steering." Previously, we used the easily implementable "rack and pinion" system, but the poor meshing of the pinion and rack resulted in significant sideways slippage and resistance during turns, limiting smooth turns to approximately 50%.
Therefore, we decided to implement a new steering mechanism. We considered either the Ackermann steering system or the parallel steering system as suitable for this robot.
To determine which to use, we compared the two by setting the maximum steering angle.
Here, using 

$$
R = \frac{L}{tanθ}
$$

* $θ = \text{steering angle}$
* $L = \text{distance between the front and rear wheels}$
* $R = \text{turning radius}$

—and noting that for this robot, $L = 12.7 cm$—the data is as presented in the table below.

 | steering angle | turning radius |
 |:---:|---|
 | **20°** | 34.89cm |
 | **25°** | 27.21cm |
 | **30°** | 22.00cm |
 | **35°** | 18.14cm |
 | **40°** | 15.14cm |

The following is a line graph of this data.

<div align="center"><img height="427" alt="IMG_0482" src="https://github.com/user-attachments/assets/e0a4e5f2-59e6-4dac-be5a-f4f842eb8afd" /></div>

From this graph, we can see the following:
* 25°: Difficult to make tight turns.
* 30°: Good balance between turning performance and driving stability.
* 35°: Even easier to make tight turns, advantageous for turning in narrow spaces.
* 40° or more: May increase the likelihood of tire-to-body interference and tire skidding.

Therefore, based on this data, we set the maximum steering angle to 30 degrees.

<div align="center"><img height="564" alt="IMG_0483" src="https://github.com/user-attachments/assets/24a054bc-1715-4ca6-92be-6945e5c78ee7" /></div>

Our robot has a relatively short distance of 12.7 cm between the front and rear wheels, and the maximum steering angle is assumed to be 30°. Furthermore, the tires we use on the front wheels have a small contact area (see section 2.6.1 for details on tires), so even with a parallel steering mechanism, the robot would skid sideways, preventing significant deviations in the numerical values.
Also, using an Ackermann steering mechanism would increase the number of parts and weight compared to the parallel steering mechanism, making numerical errors more likely due to the robot's momentum. Even if the parts are made thin, there is a possibility of breakage, so our robot uses a parallel steering mechanism.
When we actually mounted the "parallel steering" on the robot, the number of failures decreased, and we were able to achieve a success rate of approximately 90%. Since the key to this project is how accurately the robot can turn, we decided to use this mechanism.
Furthermore, by adding a stopper to the steering, we eliminated the need to programmatically limit the steering range.

## 2.6:Tires
###  2.6.1:Front wheel
<img width="380" alt="image" src="https://github.com/user-attachments/assets/7b3f6dec-f834-4c38-91df-4e157a5d072f" />

For the front wheels, I used tires with design ID 55976, measuring 56 mm in diameter and 26 mm in width. Although their 26 mm width is nearly identical to that of the rear tires, I chose them because they have a smaller contact patch with the ground; this reduces friction, making it easier to steer the vehicle.

### 2.6.2:Rear Wheel
<img width="380" alt="IMG_0429" src="https://github.com/user-attachments/assets/35e5861f-a23f-4bdc-8023-6a5007324925" />

For the rear wheel, we used a tire with design ID 41897, 56mm in diameter and 28mm in width. We chose this tire because its large contact surface with the ground increases friction, resulting in greater propulsion and making it easier to increase speed.  

## 2.7:Sensors, sensor architecture, and sensor calibration methods
<img width="300" height="200" alt="image" src="https://github.com/user-attachments/assets/78838e3b-042f-49ae-bca4-7167ef6f03e3" />

 |  |  |
 | :--- | :--- |
 | **Function** | Distance measurement / LED emission |
 | **Sampling rate** | 100Hz |
 | **Distance<br>measurement** | Normal<br>Measurement range: 50–2000 mm +/- 20 mm<br>Incident angle: +/- 35 degrees (varies depending on distance)<br>Resolution: 1 mm<br><br>High-speed detection<br>Measurement range: 50–300 mm +/- 15 mm<br>Incident angle: +/- 35 degrees (varies depending on distance)<br>Resolution: 1 mm |
 | **LED emission** | Color: White (color temperature: 4000K)<br>The illuminated area can be individually controlled in four segments<br>Output power: Adjustable from 0 to 100% in 1% increments |
 | **Wire** | 250 mm / Integrated with sensor (not removable) |
 | **Other** | By removing the screws on the back, the front part of the sensor can be detached, allowing a third-party<br>sensor to be attached (support timing for third-party sensors has not been determined). |

<p align="center"><b>[Graph 1]</b></p>

### 2.7.1:Forward
<img  height="348" alt="image" src="https://github.com/user-attachments/assets/d310ef52-c1d7-471b-88f6-9f8c3b2d1c0e" />

Through repeated testing with this robot, it was discovered that during the Open Challenge rounds, the angle of incidence error would be at least ±5° when completing the corner section.  
Therefore, to ensure that the wall could be read even with this error, a distance sensor with a wide measurement range was used, as can be seen in Graph 1.  

### 2.7.2:Left and right
<img  height="348" alt="image" src="https://github.com/user-attachments/assets/38cd2c0b-a8cf-43cb-9d08-de35d7f445a2" />

The left and right distance sensors are used to determine the proximity to the left and right walls, confirm the direction of rotation, and act as a safety device to prevent contact with the walls. (See [3.4.4](#344how-to-drive-a-straight-line-section) for details.) Therefore, by mounting the distance sensors vertically as shown in the image above, the error is reduced. The reason for using distance sensors is that they can read within 30 cm when performing high-speed detection, so we judged them to be suitable sensors for use as a safety device.

### 2.7.3:Sensor calibration methods
In addition, we took data on the error between the reference distance (actual distance) and the actual measured value when using this distance sensor on the robot. The following is a summary of data on the actual distance and measurements for the course wall.

 | Actual distance | Measured value |
 |:---:|---|
 | **20 cm** | 20.1 cm |
 | **30 cm** | 30.3 cm |
 | **40 cm** | 40.4 cm |
 | **50 cm** | 50.3 cm |
 | **60 cm** | 60.7 cm |
 | **70 cm** | 70.7 cm |

 <img width="1202" height="795" alt="IMG_0491" src="https://github.com/user-attachments/assets/03cd795e-a513-4a51-a597-ab5718ab9d8f" />

<p align="center"><b>[Calibration Data]</b></p>

We considered the calibration method of the sensor and created the program, taking into account the measured error. This allows our robot to move without being affected by this error.

## 2.8:Camera
<img width="1985" height="936" alt="IMG_0436" src="https://github.com/user-attachments/assets/774ea911-0749-4429-92f4-10428d290cb2" />

We used a camera with the front part of the distance sensor removed and an OpenMV Cam H7 Plus attached.  
The OpenMV Cam H7 Plus has the advantages of lower power consumption, a larger memory capacity (making it less likely to crash), and high image quality (reducing the likelihood of failing to read traffic signs). In addition, it has no packet loss or OS overhead delays. The table below compares the cameras we considered.  

 |  | OpenMV Cam H7 Plus | Raspberry Pi | ESP32-CAM | OAK-1 |
 |:---:|---|---|---|---|
 | **Mobility** | Less than 1 second | Approximately 20-40 seconds | Approximately 2-15 seconds | Approximately 2-5 seconds |
 | **Electricity consumption** | Approximately 0.5W to 0.6W | Approximately 3.0W to 6.0W | Approximately 0.5 W to 1.0 W | Approximately 2.5 W to 4.5 W |
 | **Memory capacity** | 32MB SDRAM + 1MB SRAM | 1GB/2GB/4GB/8GB It varies slightly depending on the model. | 8MB PSRAM + 520KB SRAM | 512MB |
 | **Understanding speed** | Standard (medium speed) | High speed | Low speed to medium speed | Ultra-high speed |
 | **External connection** | USB, SPI, I2C, UART, PWM, MicroSD | USB x4, HDMI ×2, LAN, Wi-Fi, Bluetooth, GPIO | Wi-Fi, Bluetooth, MicroSD, GPIO, UART | USB Type-C |

## 2.9:Starting and stopping in a parking lot
<img width="500" alt="IMG_0454" src="https://github.com/user-attachments/assets/a73bf5e9-adaf-4039-8a8f-91c45c56b8bd" />

In the Obstacle Challenge rounds, we often struggled to complete the course within the time limit due to the time it took to launch from the parking area and park. Therefore, to increase the distance between parking areas and reduce the time, we added a protrusion (hereinafter referred to as Part A) to the robot, extending from the bottom of the front ultrasonic sensor (as shown by the blue circle in the image above), making it as thin as possible to avoid contact with the parking area.
To determine the length of Part A, we used the following formula:

$(\text{Robot's total length} + \text{Length of Part A}) \times 1.5 \geqq \text{Distance the robot is closest to the parking area}$

The robot's total length is 22.5cm, and the closest distance the robot is to the parking area is approximately 36cm. Letting the length of Part A be xcm, we substitute these values ​​into the above formula:

$(22.5 + x) \times 1.5 \geqq 36$

$x \geqq 1.5$

Therefore, we determined that Part A should be at least 1.5cm long. We adjusted the length to approximately 4.5cm, ensuring it did not exceed the robot's size limit, providing a margin of safety. Furthermore, by using Part A, we succeeded in reducing both the time it takes to start and the time it takes to park by 8 seconds each. Moreover, while previously we could only complete the course 4 out of 10 times, with Part A installed, we can now complete the course within the time limit every time.

<div align="center"><img width="805" alt="IMG_0456" src="https://github.com/user-attachments/assets/f533c13c-9176-46fd-9062-c8f73f0bfa55" /></div>
<p align="center"><b>[A diagram showing how the robot departs from the parking space.]</b></p>

# 3:Program
## 3.1:Programming Software (Pybricks, OpenMV)
### 3.1.1:About Pybricks

 |  | Pybricks | LEGO Official App | Micro Python |
 |:---:|---|---|---|
 | **Programming language** | Python | Visual Language | Python, C++, etc. |
 | **Startup time** | Approximately 0.5 to 1 second | Approximately 5 to 10 seconds | Approximately 2 to 5 seconds |
 | **Control loop period** | per second Processing 200 to 1000 times | per second 20 to 50 times is the limit. | per second 100-200 processing cycles |
 | **Motor synchronous control** | Less than once | Degree 3 to 5 | Degree 1 to 3 |
 | **Compatible devices** | SPIKE, Technic, City, Move, etc. | Each app has a fixed hub. | SPIKE Prime /Robot Inventor only |
 | **Simultaneous Bluetooth connection** | 7-8 units | Connection unavailable | Construction is extremely difficult. |
 
This robot used Pybricks. The reason is that compared to other program sites, it is the best in terms of start-up time and control loop cycle, and I chose it because of the advantage that the motor synchronous control is less than 1 degree and there is almost no error.

### 3.1.2:About OpenMV
We used a camera with the front part of the distance sensor removed and an OpenMV Cam H7 Plus attached. The reasons for this choice (from a programming perspective) are as follows.

 |  | OpenMV | HuskyLens | Raspberry Pi |
 |:---:|---|---|---|
 | **Number of program lines required to send data for one obstacle** | Approximately 20 lines | Approximately 50 lines | Approximately 60 lines |
 | **Number of lines of code for the image lines recognition part** | 3 lines | 0 lines | Approximately 15v lines |
 | **Number of lines of code required to transmit coordinate data** | 1 line | Approximately 15 lines | Approximately 10 lines |
 | **Number of lines of code required to display the debug screen** | 0 lines | Indicates no | 3 lines |
 | **Language matching with pybricks** | 〇 | × | 〇 |

As you can see from this table, we chose OpenMV because of its advantages, such as requiring fewer lines of code for data transmission and significantly less code than other cameras for transmitting coordinate data. Furthermore, since it uses the same language as pybricks, we didn't need to learn a new language, allowing us to dedicate more time to editing other programs.
（For the reasons for its use (from a robot's perspective), please refer to section [2.8](#28camera).）

### 3.1.3:Communication Method
<img width="2056" height="1210" alt="IMG_0421" src="https://github.com/user-attachments/assets/d5c9773c-a531-4fde-bfc2-78ca0d4cada8" />
<img width="1371" height="1140" alt="IMG_0422" src="https://github.com/user-attachments/assets/0ad3b567-a031-48e7-85db-4fabb50f9b42" />
As a communication method, the main program in the Open MV receives data from the three modules of Open MV. And Open MV sends the data to pybricks via pupremote.

## 3.2:Gyro
We tried to accurately control the course of the aircraft using the "yo angle" obtained from the built-in gyro sensor. However, due to the risk of "drift error" that occurs in the gyro sensor, only 4 out of 10 times succeeded. Therefore, we took measures based on the following iteration cycle.

* Risk "Drift Error" : The angle changes slightly when turning, and in the latter half of the competition straight line accuracy decreases.

* Countermeasure : Incorporate code to automatically reset the gyroscope's current angle to 0° in software when the robot is completely stationary (such as immediately after starting or after detecting a wall).

With these measures, I was able to succeed 9 out of 10 times, and I was able to increase the success rate by reducing the trajectory of the aircraft in the gyro.  

## 3.3:Design considerations for the Open Challenge rounds
In the obstacle-free Open Challenge rounds, an accurate straight forward and a 90° turn are required. Here, we have introduced an algorithm that optimizes the trade-off of "running speed" and "return accuracy".  

<details>
<summary><b>Code 1[Program for P control (proportionality constant=1) and 90° turn(clockwise) in Open Challenge rounds]</b></summary>

```py
  print("Clock_turn")
  while True:
    print(right_sensor.distance())
    print(left_sensor.distance())
    Yaw=hub.imu.heading()
    front_motor.run_target(1000,0-Yaw)
    speed=100+eyes.distance()
    back_motor.run(speed)
    print(Yaw)
    if eyes. distance()<450:
        while True:
          Yaw=hub.imu.heading()
          front_motor.run_target(1000,45)
          speed=(90-Yaw)*11+200
          back_motor.run(speed)
          print(Yaw)
          if Yaw>90:
            back_motor.stop()
            front_motor.run_target(1000,0)
            turn_count=turn_count+1
            print（turn_count/4，"周成功"）
            break
```

</details>

### 3.3.1:P control using a gyro sensor
To automatically compensate for uneven friction acting on the tires during straight-line travel, we implemented proportional control—defined in line 6 of the code in "Code 1"—which determines the steering angle based on the error between the target yaw angle and the current value from the gyro sensor.  

<details>
<summary><b>Line 6 of Code1</b></summary>

```py
    front_motor.run_target(1000,0-Yaw)
```

</details>

Initially, we employed PID control—incorporating both derivative and integral terms—but testing on the course revealed that these components actually made the robot’s behavior less stable. Furthermore, when measuring lateral deviation over a 5-meter straight run, we found a deviation of 7 cm with PID control and 5 cm with PD control; in contrast, using P control alone kept the deviation within 3 cm. Consequently, we opted for P control to simplify the system and ensure more stable performance.  

### 3.3.2:Turning method
By utilizing the variable on line 14 of Code 1, we implemented a program that initiates rotation at maximum speed and decelerates as the target value is approached; this completely eliminates overshoot caused by inertia, enabling precise rotation with an accuracy of within ±0.5° of the target value.

<details>
<summary><b>Line 14 of Code 1</b></summary>

```py
        speed=(90-Yaw)*11+200
```
</details>

## 3.4:Design considerations for Obstacle Challenge rounds
In the Obstacle Challenge rounds, we believed the key was how to simplify the process of dynamically recognizing traffic signs using cameras and switching between complex driving patterns accordingly. Based on this, we implemented the following improvements.  

### 3.4.1:Measuring the distance to traffic signs based on the number of pixel
To accurately determine the actual physical distance between the robot and the sign, we conducted repeated experiments using the robot, input the following distance data, and obtained the results shown in Table 1 below. 

<div align="center">
  
 | distance(cm) | Area (number of pixels) |
 |---|---|
 | 10 | 3.0*10<sup>4</sup> |
 | 20 | 1.1*10<sup>4</sup> |
 | 30 | 5.1*10<sup>3</sup> |
 | 40 | 2.9*10<sup>3</sup> |
 | 50 | 2.0*10<sup>3</sup> |

</div>
<p align="center"><b>Table 1 [Area at each distance (rounded to two significant figures due to numerical uncertainty)]</b></p>

This test made it possible to avoid it without hitting an object, saying, "by using the number of pixels 20 to 30 cm as an indicator, the steering wheel is accurately cut and transitioned to the avoidance state".  

### 3.4.2:A program that reads nearby traffic signs and transmits the values ​​obtained
There are instances where two objects of the same color appear simultaneously within the OpenMV camera's field of view. To address this, the program identifies the most relevant traffic sign from the list of detected color blobs by selecting the one with the largest pixel area (as implemented in "Code 2"), and then extracts its X-coordinate, Y-coordinate, and pixel count. Furthermore, since the data transmitted to Pybricks includes the X-coordinate, Y-coordinate, and pixel count for both red and green objects, the program is designed—as shown in the red-boxed section of "Code 3"—to compare the pixel counts on the Pybricks side and prioritize the object with the larger pixel count. These measures effectively eliminate edge cases where a distant sign might be incorrectly prioritized, potentially causing the system to fail to avoid an obstacle located closer to the camera.  
<img width="1317" height="218" alt="IMG_0462" src="https://github.com/user-attachments/assets/e553c7fd-1dc7-49f6-895d-678325cc13ea" />
<p align="center"><b>[Code 2 [Countermeasures in openMV]]</b></p>

<img width="1195" height="107" alt="IMG_0463" src="https://github.com/user-attachments/assets/903ac714-2f6a-4cd9-a3c2-7987eb75ec1f" />
<p align="center"><b>[Code 3 [Countermeasures with pybricks]]</b></p>

### 3.4.3:Turning Method
We reasoned that categorizing our cornering methods would reduce execution time and improve accuracy; consequently, we implemented the following classification system for use when entering corner sections.

<details>
<summary><b>Code 4</b></summary>

```py
  payload=p.call('blob')
  if payload[5]>500: ...
  elif left_sensor.distance()>400: ...
  else: ...
```

</details>

The details of this program are as follows.  
(i) "Green detected"  
>In this case, the color green has been detected; please turn and proceed as shown in the diagram.
>
><div align="center"><img width="357" alt="IMG_0461" src="https://github.com/user-attachments/assets/682058ec-74b8-481f-9c3a-181c14c78f45" /></div>
><p align="center"><b>[Image 3]</b></p>
>
>Therefore, the program will look like the code below.

<details>
<summary><b>Code 5</b></summary>

```py
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
```

</details>

>The flowchart for this code is as follows.
><img width="1199" height="1312" alt="image" src="https://github.com/user-attachments/assets/249e8937-55a4-434d-9515-31bd0b8e9902" />
><p align="center"><b>[Flowchart 1]</b></p>

(ii) "Green was not detected" AND "the distance on the left is greater than 40 cm"
>At this point, since it is impossible to determine whether the object on the right is green, red, or non-existent, I have implemented the following method to make that determination.

<details>
<summary><b>Code 6</b></summary>

```py
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
```

</details>

>The flowchart in this code is as follows.
>
><img width="1794" height="4550" alt="image" src="https://github.com/user-attachments/assets/571f391e-e0f4-493a-a3c3-2d9f07fa13fc" />
><p align="center"><b>[Flowchart 2]</b></p>
>
>The path taken when this program is executed is shown in the figure below.
>
><div align="center"><img width="350" alt="image" src="https://github.com/user-attachments/assets/f475b963-59a9-4079-b998-641b68665048" /></div>
><p align="center"><b>[Image 4 [When the object beyond the corner is red or colorless]]</b></p>
>
><img width="1520" height="1017" alt="IMG_0489" src="https://github.com/user-attachments/assets/93a139d0-0cf4-4fcf-83d6-3914896e2625" />
><p align="center"><b>[Image 5 [When the object around the corner is green]]</b></p>

(iii) Other
>In this case as well, since it is impossible to determine whether the object on the right is green, red, or non-existent, the system—much like in scenario (ii)—decides based on whether a green object appears while the robot is turning. Furthermore, when the distance to the left is short, there is no space to turn toward the left; therefore, the robot performs a turn as shown in the figure below, which differs from the method used in scenario (ii).
>
><img width="1216" height="423" alt="IMG_0490" src="https://github.com/user-attachments/assets/0d937d59-6b6f-4287-8065-752c8db33ad6" />
><p align="center"><b>[Image 6 [Does not detect green AND distance on the left is less than 40 cm]]</b></p>
>
>The flowchart for case (iii) is as follows.
><img width="2090" height="3960" alt="image" src="https://github.com/user-attachments/assets/b3dace65-af62-494a-8827-8ead14a0b330" />
><p align="center"><b>[Flowchart 3]</b></p>

By categorizing the turning methods in this way, it became possible to limit the number of obstacles to be detected in the subsequent segment to just one, thereby reducing the time required.

### 3.4.4:How to drive a straight line section
Since the objects in the foreground have already been loaded by the time a turn is made, I have categorized the scenarios as follows:

(i) "There are no objects in this section at the moment (only objects read when turning)"

<details>
<summary><b>Code 7</b></summary>

```py
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
```

</details>

>At this time, I decided that there was no object in this section when turning, or I passed the straight section and went straight using the yaw angle until I was in a position to enter the corner section (the distance in front is 850 cm). In addition, this program used the left and right distance to prevent the aircraft from crashing into the wall when it passed by the wall. The flowchart in Code 7 is as follows.
>
><img width="1213" height="1297" alt="image" src="https://github.com/user-attachments/assets/084bfafe-88a6-4398-ba52-bbb67fa75137" />
><p align="center"><b>[Flowchart 4]</b></p>
>
>Also, if you run this program, it will work as shown in the figure below.

(ii) "There is a red object in the center or back"

<details>
<summary><b>Code 8</b></summary>

```py
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
```

</details>

>At this time, considering the delay of the reaction time until the program starts in order for the red distance to approach 30 cm, we try to track based on the value of the pixel number 3000, which is 40 cm in front of the distance (see [3.4.1](#341measuring-the-distance-to-traffic-signs-based-on-the-number-of-pixel)). In addition, if the previous distance is closer than 40 cm, there is a possibility of hitting the object, so the previous distance was reduced to 40 cm, and then the object was tracked. In addition, after avoiding the red object, I created a program to move the car body to the position with a yaw angle of 0 in order to go straight, and tested it, but it saved time and accurately avoided objects in the corner section. After turning right to avoid red, read the red or green object or turn left until the yaw angle is 0 (in fact, 10 is used to shift from the center due to the delay in the processing speed of the robot).
>
>The flowchart for this program is as follows.
>
><img width="1206" height="1305" alt="image" src="https://github.com/user-attachments/assets/cffbbba1-e679-4757-9bf2-69014d13cd02" />
><p align="center"><b>[Flowchart 5]</b></p>

(iii) "There is a green object in the center or back"

<details>
<summary><b>Code 9</b></summary>

```py
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
```

</details>

>In the case of green, like red, if it is too close, the robot is distanced from the object, then track the green object, turn left if the distance is 40 cm in front, read the red or green object, or turn right until the yaw angle is greater than 0 (as in the case of (iii)).
>
>The flowchart for this program is as follows.
>
><img width="1199" height="1312" alt="image" src="https://github.com/user-attachments/assets/6a5a7b05-f1bf-447f-88b8-d25caf20de83" />
><p align="center"><b>[Flowchart 6]</b></p>

(ii) (iii) allows you to accurately avoid objects, and even if there is no object by (i), you can avoid the mistake of returning to the center when the left and right distance gets closer when you go in a straight line, and do not make a mistake before turning. I did. These make it possible to operate accurately without mistakes even when turning. In addition, (ii) (iii) has read the object in the corner section in advance, so we succeeded in reducing the number of seconds by about 10 seconds.

### 3.4.5:How to prevent misidentification
When reading traffic signs, objects outside the course may be the same color as traffic signs. At that time, if it is subject to detection, the obstacle cannot be read correctly. Therefore, we have considered the following countermeasures.

<div align="center"><img height="120" alt="image" src="https://github.com/user-attachments/assets/b406d735-02de-46f6-95e1-560e369b32e2" /></div>
<p align="center"><b>[Code 10]</b></p>

* Risk: Objects outside the course will be detected.

* Countermeasures: As an example, the pixel number of the object is less than 500, as shown in Code 10 (red frame), "payload [2] (number of red pixels) < 500 and payload [5] (number of green pixels) <500" (in the course If the object is greater than 500 and there is basically no object outside the course that is larger than that, assuming that the number of pixels is <500), the object is not subject to tracking. ( Originally, the object was excluded using the value of the y coordinate, but there may be objects other than the green object at almost the same position as the height of the green object that detects, so I thought that the judgment at the y coordinate was meaningless)
This program reduces the reading of objects outside the course and allows only traffic signs to be detected

### 3.4.6:Destination setting
One of the reasons for the high number of mistakes in this robot running was that the position was different depending on the pattern and it was difficult to adjust. Therefore, by setting the destination, it became better to run the same program in all patterns after arriving at the destination, which led to the simplification of the program and the prevention of mistakes.
For example, in the case of the following corner section program, align it on the same line after turning, and then move the same control to prevent mistakes.

<img width="988" height="1030" alt="image" src="https://github.com/user-attachments/assets/228bb970-df63-4895-9010-c3d9bf0d91ed" />

<p align="center"><b>Calculations are performed using the distance measured beforehand—<br>specifically the distance on the left side (assuming a clockwise direction)—<br>within the area enclosed by the red box, in order to align the elements along the same line<br> (as shown in the position in the diagram below). Code 11</b></p>

In the place surrounded by this red frame, the left distance (in the case of right turn) that was calculated in advance is used, and it is aligned on the same line (position in the figure below).

<div align="center"><img height="442" alt="image" src="https://github.com/user-attachments/assets/68ae61c8-0e8a-4ab4-9e6f-1c3736fb1e68" /></div>
<p align="center"><b>[Image 7]</b></p>

### 3.4.7:Parking

<details>
<summary><b>Code 12[Program for the interval between the end of the right turn and the start of parking]</b></summary>

```py
if right_turn_or_left_turn==1:
    last_right()
else:
    last_left()
parking()
```

</details>

<details>
<summary><b>Code 13[Program for parking when turning clockwise, and for parallel parking when turning counter-clockwise]</b></summary>
  
```py
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
```

```py
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
```

</details>

The diagram below illustrates the behavior when the program in Code 13 is executed.

<div align="center"><img width="562" alt="image" src="https://github.com/user-attachments/assets/511f0440-893a-4a88-bcca-d8187ab806ba" /></div>
<p align="center"><b>[Image 8[Operational diagram for Code 13 (in the case of red or colorless)]]</b></p>

<div align="center"><img width="562" alt="image" src="https://github.com/user-attachments/assets/940fccf5-b2bf-4872-a7ce-1073c53b2987" /></div>
<p align="center"><b>[Image 9[Operational diagram for Code 13 (in the green case)]]</b></p>

The program content for Codes 12 and 13 is as shown in the flowchart below.

<img width="1312" height="1199" alt="image" src="https://github.com/user-attachments/assets/8326f029-c759-4ba3-850a-7cf68ab81aa3" />
<p align="center"><b>[Flowchart 7[Program details for Codes 12 and 13 (flowchart)]]</b></p>

The operation diagram for the `parking()` function in the Code 12 program is shown below.

<div align="center"><img width="433" alt="image" src="https://github.com/user-attachments/assets/f8ffda23-8d0a-4661-8d1d-bb0e10afd8c8" /></div>
<p align="center"><b>[Image 10[Parking 1]]</b></p>

<div align="center"><img width="429" alt="image" src="https://github.com/user-attachments/assets/e26025c2-2d3f-4548-a5bc-86f92c0b9c1b" /></div>
<p align="center"><b>[Image 11[Parking 2]]</b></p>

By incorporating a parallel parking maneuver—using the same program employed for the subsequent perpendicular parking—during both counter-clockwise and clockwise runs, we aimed to reduce the time required for corrections in the event of a parking error during the competition.

## 3.5:Other ingenuity points
### 3.5.1:Visualization of mistakes in print statements

<details>
<summary><b>Code 14 [Verifying operation using print statements]</b></summary>

```py
    if Yaw>90:
        back_motor.stop()
        print("緑p :",payload[5])
        break
Yaw=hub.imu.heading()
hub.imu.reset_heading(Yaw-90)
print("Yaw:",hub.imu.heading())
payload=p.call('blob')
```

</details>

<details>
<summary><b>Code 15 [Visualizing errors in a mobile robot using a 'home' button]</b></summary>

```py
print("no")
while True:#前80cmまで前進
    hub.light.on(Color.BLUE)
    Yaw=hub.imu.heading()
    direction=(0-Yaw)*0.5
    front_motor.run_target (1000,direction)
    payload=p.call('blob')
    back motor.run(1000)
    if eyes.distance()<700:
        hub.light.off()
        left distance=left_sensor.distance()
        print(eyes.distance())
        break
```

</details>

As shown in Code 14, by inserting print statements for each action, we can quickly identify which part of the sequence is failing, thereby reducing the time required for debugging. Furthermore, as demonstrated in the third line of Code 15, we configured the hub’s home button to light up in specific colors—which can even change based on certain conditions. This enhancement allows us to conduct more test runs and experiment with—as well as compare—different functional approaches, ultimately leading to greater accuracy and faster development. Additionally, because these features make it clear to the entire team how far the program executed correctly, any team member—not just the programmer—can spot errors or instances of unstable behavior. This ensures that every issue occurring during a single run can be identified and addressed.

### 3.5.2:How to determine the turning direction

<details>
<summary><b>Code 16[Program that determines the turning direction during obstacle rounds (start_right() and start_left() are the routines for exiting the parking area and entering the turning section)]</b></summary>

```py
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
```

</details>

The turning direction is determined by the program logic in Code 16. The flowchart below illustrates this process. (The contents of `start_right()` and `start_left()` are also included.)

<img width="1224" height="1285" alt="image" src="https://github.com/user-attachments/assets/9719157c-9709-4f49-8788-dcbd1e1469a7" />
<p align="center"><b>[Flowchart 8]</b></p>

This allows for the correct determination of the turning direction, ensuring that no mistakes are made regarding which way to turn.

# 4:Systems Thinking
## 4.1:Interactions Between Subsystems
<img width="1693" height="1181" alt="IMG_0437" src="https://github.com/user-attachments/assets/0feb5de7-3d26-4800-841b-3499fa1e8290" />
   
<img width="1694" height="1170" alt="IMG_0438" src="https://github.com/user-attachments/assets/aee40241-c785-4dda-a6df-aae956f75e4a" />

<img width="1684" height="1126" alt="IMG_0439" src="https://github.com/user-attachments/assets/610b2512-00f7-47a1-955e-f0f6c0dde551" />

### ["Subsystem Diagram"](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/schemes/Subsystem%20Diagram.pdf)

To make it easier to identify the potential impact of modifying any of our robot’s subsystems, we created a diagram illustrating the interrelationships between the drive, sensor, power, and processing subsystems. This diagram revealed that we were utilizing a variety of sensor-related subsystems; consequently, we opted to incorporate OpenMV to handle some of the processing—thereby reducing the amount of code that needed to run on the main controller. This change also lessened the load on the Spike hub, resulting in a faster control cycle. (For further details, please refer to [3.1.2](#312about-openmv).)
Furthermore, this diagram allows others to quickly grasp the interrelationships and interactions among our robot’s subsystems at a single glance.

## 4.2:Vehicle Restrictions
The competition imposed a 1.5 kg weight limit, which restricted the components that could be mounted on the robot. Although our initial design met this requirement, it weighed 689.2 g; consequently, while our completion times were within the allowed limits, they were somewhat longer than desired. By lowering the robot’s profile, we were able to reduce the number of parts used for securing components, bringing the total weight down to 650.8 g. This adjustment improved our average completion time by 15 seconds, enabling faster and more precise performance.

## 4.3:Risk Identification and Mitigation Measures
<img width="1064" height="601" alt="IMG_0441" src="https://github.com/user-attachments/assets/d8ee7cc0-894b-4410-b92d-e2a279366637" />
<p align="center"><b>[A place where everyone can check the corrections in Japanese]</b></p>

In the document provided above, we have compiled the risks encountered by each team member. By ensuring that everyone reviews and understands these risks—and by consistently identifying and analyzing them—we are able to improve the robot's precision. Furthermore, we distribute tasks related to problems that are difficult to resolve through programming alone, which helps to alleviate the burden on our programmers.
The table below summarizes a selection of the risks we have encountered and subsequently resolved.

 | Risk | Issue Encountered | Countermeasure |
 |:---:|---|---|
 | **Gyro drift** | Reduced straight-line accuracy | Resetting the angle when stopped |
 | **Camera misidentification** | Incorrect detection of obstacles | Detection based on pixel count |
 | **Rack-and-pinion steering** | Inability to complete turns in corner sections | Parallel steering mechanism |
 | **Time required for starting and stopping in parking areas** | Inability to complete the course within the time limit | Adding adjustable protrusions to modify the robot's length |
 | **Robot weight** | Reduced movement speed | Selective optimization of components |

As this table demonstrates, we minimize errors by identifying, reviewing, and addressing a wide range of risks.

# 5:Reference materials
https://openmv.io/?srsltid=AfmBOoqMECnVVz4SrByaDgChDQRdEArLA4LqDyji2U2_NY6ZKVAIU-h
https://pybricks.com/
https://openmv.io/pages/download
https://www.switch-science.com/products/6560
https://grabcad.com/library/h7-plus-1
https://afrel.co.jp/product/spike/prime/
https://github.com/GianCann/SpikePrimeHub
https://store.bricklink.com/v2/studio/download.page

# How to build a robot
**① Build the robot itself**
* Click `Robot Assembly Instructions.pdf` and build the robot.
* If you are unsure
  (Click in the order of `models` → `How to use the Robot 3Dmodel.ldr file.md` to view the 3D model of the robot.)

**② Import the program**
* Click `program code` and download all the files contained within it.

**1 About OpenMV**
* Download and install OpenMV IDE from **[here](https://openmv.io/pages/download)**
* Launch OpenMV IDE and connect the OpenMV board to your computer using a USB cable (USB Type-A to Micro USB Type-B).
* If a camera is connected to the SPIKE hub via a cable (i.e., the camera is plugged into a SPIKE port), be sure to disconnect the cable.
* Press the Windows key, search for "Explorer" (the file management app), and click to open it. Select `pupremote.py` and `lpf2.py` (using Ctrl+Shift+↓), then copy them (Ctrl+C). In the left-hand menu, select "This PC," open the OpenMV drive, and paste the files there (Ctrl+V).
* Press the Connect button (bottom left of the screen)

| When connected | When not connected |
|---|---|
| <img width="150" alt="image" src="https://github.com/user-attachments/assets/b694c78a-8bfc-4f37-882d-d0b042cf8365" /> | <img width="150" alt="image" src="https://github.com/user-attachments/assets/c938ffab-042f-4242-b412-324d07418876" /> |

* If not connected, press the Connect button or use Ctrl+E.
* File > Open File (or Ctrl+O) → Click `wro_2026_openMV` → Click Open
* Press the Run button (or Ctrl+R). (The camera is activated at this point.)
* Have the system detect the green and red objects.
* If no bounding box appears around the object, stop execution. Go to Tools > Machine Vision > Threshold Editor at the top, then click "Frame Buffer." Adjust the L-min and L-max values ​​to isolate the object so that only the object itself appears white. (If the object is red, adjusting A-min first—or A-max first if it is green—will make the process easier.) Copy the LAB threshold values. Clear all existing content within "thresholds" (for red) or "thresholds2" (for green), and paste the copied values.
(Run the program; if a bounding box appears around the object, the setup is correct. If no box appears, readjust the threshold values.)
* Stop execution.
* Go to Tools > Save open script to OpenMV Cam (as main.py). If a prompt appears asking, "Remove comments and replace spaces/tabs?", select "No" (if it does not appear, you can simply skip this step).
* The OpenMV camera will light up red; wait until the light turns off.

**2 About Pybricks**
* First, plug the camera cable into port F on the Spike.
* Access **[Pybricks Code](https://pybricks.com/)** and follow the on-screen instructions to flash the firmware.
<img width="965" alt="image" src="https://github.com/user-attachments/assets/d0995590-e614-4436-878b-b9cc83826c8e" />

* Import all of the following files using the "Import a file" option in the top-left corner: `pupremote_hub.py`, `uartremote.py`, `Obstacle_rounds.py`, and `Open_rounds.py`.
<img width="303" alt="image" src="https://github.com/user-attachments/assets/97b2acd3-f654-47cb-ac49-c847b8fe23d4" />

* Open `Obstacle_rounds.py` and `Open_rounds.py`
* Click the Bluetooth button → click the name you assigned when installing the Pybricks firmware → click "Pair"

**③ Driving**
* Open `Open_rounds.py` if you are running Open rounds, or `Obstacle_rounds.py` if you are running obstacle rounds.
* Place the robot on the course and press the Run button (or F5).


