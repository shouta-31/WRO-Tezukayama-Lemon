# [1:Strategy](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/1_Strategy.md#1strategy)
 To tackle the Open Challenge and Obstacle Challenge rounds, we devised specific strategies for each and built our robots and programs accordingly. We will now explain these strategies.
## [1.1:Open challenge rounds](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/1_Strategy.md#11open-challenge-rounds)
 For the Open Challenge rounds, we programmed a strategy aiming for a lap time of 35 seconds: driving at maximum speed on straight sections and decelerating when approaching corners.
 
 We also modularized the movements into functions, enabling rapid parameter adjustments during the tuning phase. Furthermore, we implemented a deceleration routine for 90-degree turns using the gyro sensor, thereby minimizing positional errors that occur after navigating corner sections. Based on this strategy, the robot operates according to the state transition diagram shown below.  
 (For details of the program, see section [3.3](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#33design-considerations-for-the-open-challenge-rounds).)

<img width="329" alt="IMG_0396" src="https://github.com/user-attachments/assets/4902cd1f-1dea-48a8-8247-e0e43beadcc0" />. 

## [1.2:Obstacle challenge rounds](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/1_Strategy.md#12obstacle-challenge-rounds)

## [1.3:Testing, Tuning, and Trade-offs](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/1_Strategy.md#13testing-tuning-and-trade-offs)
To complete the mission more accurately, we consistently aimed to score at least 80% on each challenge and repeatedly ran test workflows such as experiments to measure the distance between the robot and objects to fine-tune our system (see Section 3.4.1 for details). We also made trade-offs regarding parts and programming based on these tests.
 
The table below shows the scores achieved within the time limit during the Open Challenge rounds (open) and Obstacle Challenge rounds (obstacle) across 10 test runs.
