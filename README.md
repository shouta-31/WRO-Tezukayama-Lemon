# Content
* `Engineering Journal` includes strategy, robot structure, programming, and systems thinking.
* `t-photos` contains 2 photos of the team (an official one and one funny photo with all team members)
* `v-photos` contains 6 photos of the vehicle (from every side, from top and bottom)
* `video` contains the video.md file with the link to a video where driving demonstration exists
* `schemes` contains two schematic diagrams in form of PNG of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `program code` contains code of control software for all components which were programmed.
* `models` is a model file used to manufacture vehicle parts.

# Engineering Journal
- ## [1:Strategy](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/1_Strategy.md#1strategy)
  In tackling the Open Challenge rounds and the Obstacle Challenge rounds, we developed strategies for each and built our robots and programs accordingly. I will now explain them.
  - ### [1.1:Open challenge rounds](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/1_Strategy.md#11open-challenge-rounds)
  - ### [1.2:Obstacle challenge rounds](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/1_Strategy.md#12obstacle-challenge-rounds)
  - ### [1.3:Testing, Tuning, and Trade-offs](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/1_Strategy.md#13testing-tuning-and-trade-offs)
- ## [2:Robot design](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#2robot-design)
  - ### [2.1:Robot materials](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#22robot-structure-and-actuation)
  - ### [2.2:Robot Structure and Actuation](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#23power-supply-and-wiring)
  - ### [2.3:Power Supply and Wiring](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#23power-supply-and-wiring)
    - #### [2.3.1:Reasons for Power Supply Selection and Wiring Diagram](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#231reasons-for-power-supply-selection-and-wiring-diagram)
    - #### [2.3.2:Power Balance](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#232power-balance)
  - ### [2.4:Motor](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#24motor)
    - #### [2.4.1:Drive Motor](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#241drive-motor)
    - #### [2.4.2:Steering Motor](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#242steering-motor)
  - ### [2.5:Front-wheel steering](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#25front-wheel-steering)
  - ### [2.6:Tires](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#26tires)
    - #### [2.6.1:Front wheel](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#261front-wheel)
    - #### [2.6.2:Rear Wheel](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#262rear-wheel)
  - ### [2.7:Sensors and Sensor Architecture](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#27sensors-and-sensor-architecture)
    - #### [2.7.1:Forward](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#271forward)
    - #### [2.7.2:Left and right](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#272left-and-right)
  - ### [2.8:Camera](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/2_Robot%20design.md#28camera)
- ## [3:Program]()
  - ### [3.1:Programming Software (Pybricks, OpenMV)](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#3program)
    - #### [3.1.1:About Pybricks](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#311about-pybricks)
    - #### [3.1.2:About OpenMV](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#312about-openmv)
    - #### [3.1.3:Communication Method](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#313communication-method)
  - ### [3.2:Gyro](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#32gyro)
  - ### [3.3:Design considerations for the Open Challenge rounds](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#33design-considerations-for-the-open-challenge-rounds)
    - #### [3.3.1:P control using a gyro sensor](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#331p-control-using-a-gyro-sensor)
    - #### [3.3.2:Turning method](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#332turning-method)
  - ### [3.4:Design considerations for Obstacle Challenge rounds](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/3_Program.md#34design-considerations-for-obstacle-challenge-rounds)
- ## [4:Systems Thinking](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/4_Systems%20Thinking.md#4systems-thinking)
  - ### [4.1:Interactions Between Subsystems](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/4_Systems%20Thinking.md#41interactions-between-subsystems)
  - ### [4.2:Vehicle Restrictions](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/4_Systems%20Thinking.md#42vehicle-restrictions)
  - ### [4.3:Risk Identification and Mitigation Measures](https://github.com/shouta-31/WRO-Tezukayama-Lemon/blob/main/Engineering%20Journal/4_Systems%20Thinking.md#43risk-identification-and-mitigation-measures)

# How to build a robot
* 
