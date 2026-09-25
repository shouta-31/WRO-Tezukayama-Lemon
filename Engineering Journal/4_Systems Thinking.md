# 4:Systems Thinking
## 4.1:Interactions Between Subsystems
To make it easier to identify where changes would have an impact when redesigning our robot’s subsystems, we created a subsystem diagram illustrating the interrelationships among the drive, sensor, power supply, and processing components mentioned above. From this diagram, we realized that the sensor system utilized various subsystems, so we decided to use OpenMV to reduce the number of lines of code within the camera in order to minimize program execution time as much as possible. In addition, this reduced the load on the Spike Hub and improved the control cycle. (See Section 3.1.2 for details.)

Furthermore, this diagram allows others to easily understand the interrelationships and interactions among our robot’s subsystems at a glance.
