# 2:Robot design
## 2.1:Robot materials
By constructing the majority of our robot using LEGO bricks and incorporating some 3D-printed parts, we were able to rebuild the robot quickly and dedicate more time to programming. The use of 3D-printed components also allowed for immediate repairs in the event of breakage.  

Additionally, shown below is a 3D model of our robot created in Studio 2.0; this model serves as a blueprint, enabling anyone to replicate the design.  
## 2.2:Robot Structure and Actuation
The robot was designed to be compact overall to minimize contact with traffic signs during the Obstacle Challenge rounds. Stability was also enhanced by lowering the chassis height and eliminating internal hollow spaces.

Furthermore, the center of gravity (indicated by the red circle) was positioned slightly toward the front wheels rather than directly over the rear wheels to prevent slipping.
<img width="1205" height="537" alt="image" src="https://github.com/user-attachments/assets/cef562ec-1e1e-4291-a276-66949b6a4136" />

We selected a rear-wheel drive configuration. This choice reduces the load on the front tires, thereby minimizing measurement errors at the front wheels. In contrast, a front-wheel drive setup tends to drift outward during turns, creating a risk of colliding with obstacles. To improve straight-line accuracy, we positioned the wheel hubs slightly toward the front, effectively eliminating wheel spin.
## 2.3:Power Supply and Wiring. 
### 2.3.1:Reasons for Power Supply Selection and Wiring Diagram
Since the robot built this time did not require many sensors or motors, a large number of ports was not necessary. Although the clock speed is the lowest, the absence of an operating system eliminates wasteful processing. Furthermore, because the robot can be quickly reconfigured, more time can be devoted to tasks such as program modification.
### 2.3.2:Power Balance
The table below summarizes the actual measured power consumption for each device.  
Furthermore, based on the SPIKE Prime battery used in this instance [Output voltage (V): Rated 7.3V (approx. 8.4V when fully charged); Capacity: 2100mAh], the calculated power margin is 33.3%, indicating that the robot's design is safe. 
※Margin (%) = (1 - (Total maximum current consumption ÷ Maximum current supply capability of the power source)) × 100. 
$. 
## 2.4:Motor
<img width="1177" height="865" alt="image" src="https://github.com/user-attachments/assets/c9e81d66-03cd-4705-acef-0b75573ad09e" />
As described in section 2.2, we used the SPIKE Prime Hub; consequently, we limited our motor selection to SPIKE Prime motors and chose specific motors for the drive and steering systems based on the aforementioned considerations. Calculations regarding the robot's weight (650.8 g) and torque—factoring in a safety margin—indicated that the required torque was 7.7 Ncm for the front wheels and 5.4 Ncm for the rear wheels.  

※The formula for calculating torque is "Torque = Applied force x Distance from rotation axis to point of force.". 
The speed calculation formula was "Speed = π x Diameter of rotating body x Number of revolutions per minute / 60". 
Calculation of the required torque at the front wheels is "Frictional resistance moment = coefficient of friction x weight on one front wheel x scrub radius."
