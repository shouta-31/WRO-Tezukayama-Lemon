# 1:Strategy
 To tackle the Open Challenge and Obstacle Challenge rounds, we devised specific strategies for each and built our robots and programs accordingly. We will now explain these strategies.
## 1.1:Open challenge rounds
<img width="2128" height="816" alt="IMG_0444" src="https://github.com/user-attachments/assets/220562c7-5161-4c83-9e9b-d3d0de6793d4" />

 For the Open Challenge rounds, we programmed a strategy aiming for a lap time of 35 seconds: driving at maximum speed on straight sections and decelerating when approaching corners.
 
 We also modularized the movements into functions, enabling rapid parameter adjustments during the tuning phase. Furthermore, we implemented a deceleration routine for 90-degree turns using the gyro sensor, thereby minimizing positional errors that occur after navigating corner sections. Based on this strategy, the robot operates according to the state transition diagram shown below.  
 (For details of the program, see section [3.3](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#33design-considerations-for-the-open-challenge-rounds).)

<img width="329" alt="IMG_0396" src="https://github.com/user-attachments/assets/4902cd1f-1dea-48a8-8247-e0e43beadcc0" />. 

## 1.2:Obstacle challenge rounds
　The strategy for the Obstacle Challenge rounds of this tournament is primarily based on the Open Challenge rounds.oundsIt is based on the following. Also, the goal is1 week 30 secondsI created the program with that goal in mind.
Also, as a strategy, in the parking lotChoosing a parking spotI did that. I will proceed with departing from the parking lot. However, regarding parking, initially I was focused on accuracy and didn't have much time to dedicate to it. Therefore, I focused all my efforts on maximizing the accuracy of other missions. However, ultimately, both accuracy improved and I was able to allocate sufficient time for parking, so I decided to proceed with parking. Also,Obstacle detection logicIt operates according to the following state transition diagram.For details about the program, see section 3.4.)
<img width="1749" height="1195" alt="IMG_0450" src="https://github.com/user-attachments/assets/d16fad4d-54ea-4150-bda1-f6ac368767b7" />

## 1.3:Testing, Tuning, and Trade-offs
To complete the mission more accurately, we consistently aimed to score at least 80% on each challenge and repeatedly ran test workflows such as experiments to measure the distance between the robot and objects to fine-tune our system (see Section 3.4.1 for details). We also made trade-offs regarding parts and programming based on these tests.
 
The table below shows the scores achieved within the time limit during the Open Challenge rounds (open) and Obstacle Challenge rounds (obstacle) across 10 test runs.
<img width="1184" height="792" alt="IMG_0440" src="https://github.com/user-attachments/assets/af8019d3-96aa-457c-8e61-a6926b966361" />
