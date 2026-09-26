# 4:Systems Thinking
## 4.1:Interactions Between Subsystems
<img width="1693" height="1181" alt="IMG_0437" src="https://github.com/user-attachments/assets/0feb5de7-3d26-4800-841b-3499fa1e8290" />
   
<img width="1694" height="1170" alt="IMG_0438" src="https://github.com/user-attachments/assets/aee40241-c785-4dda-a6df-aae956f75e4a" />

<img width="1684" height="1126" alt="IMG_0439" src="https://github.com/user-attachments/assets/610b2512-00f7-47a1-955e-f0f6c0dde551" />

To make it easier to identify where changes would have an impact when redesigning our robot’s subsystems, we created a subsystem diagram illustrating the interrelationships among the drive, sensor, power supply, and processing components mentioned above. From this diagram, we realized that the sensor system utilized various subsystems, so we decided to use OpenMV to reduce the number of lines of code within the camera in order to minimize program execution time as much as possible. In addition, this reduced the load on the Spike Hub and improved the control cycle. (See Section [3.1.2](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#33design-considerations-for-the-open-challenge-rounds) for details.)  

Furthermore, this diagram allows others to easily understand the interrelationships and interactions among our robot’s subsystems at a glance.  

## 4.2:Vehicle Restrictions

## 4.3:Risk Identification and Mitigation Measures
$   
$  
By consistently identifying and analyzing these risks and ensuring that everyone is aware of them, we are able to improve the robots’ accuracy. In addition, by working together to tackle problems that are difficult to solve through programming, we are reducing the burden on programmers.  
