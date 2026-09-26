# 3:Program
## 3.1:Programming Software (Pybricks, OpenMV)
### 3.1.1:About Pybricks
<img width="1218" height="731" alt="IMG_0407" src="https://github.com/user-attachments/assets/d1deb840-45f8-4b11-a0bb-22c190155b49" />
This robot uses Pybricks.The reason isCompared to other program sites, it has the shortest startup time and control loop period.ExcellentWe chose this because of its advantage of having a motor synchronous control with an error of less than 1 degree and virtually no error.

### 3.1.2:About OpenMV
We used a camera with the front part of the distance sensor removed and an OpenMV Cam H7 Plus attached. The reasons for this choice (from a programming perspective) are as follows.
<img width="1216" height="809" alt="IMG_0408" src="https://github.com/user-attachments/assets/a4cf96ad-8d9e-4b4c-bb55-0a9699268195" />
As you can see from this table, we chose openMV because of its advantages, such as requiring fewer lines of code for data transmission and significantly less code than other cameras for transmitting coordinate data. Furthermore, since it uses the same language as pybricks, we didn't need to learn a new language, allowing us to dedicate more time to editing other programs.
（For the reasons for its use (from a robot's perspective), please refer to section [2.8](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#28camera).）

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
