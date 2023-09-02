# Vacuum_agent
This repository contains answers to questions on the vacuum agent from Stuart Russel and Peter Norwig textbook.

2.8 Implement a performance-measuring environment simulator for the vacuum-cleaner world depicted in Figure 2.2 and specified on page 38. Your implementation should be modular so that the sensors, actuators, and environment characteristics (size, shape, dirt placement, etc.) can be changed easily. (Note: for some choices of programming language and operating system there are already implementations in the online code repository.)

2.9 Implement a simple reflex agent for the vacuum environment in Exercise 2.8. Run the environment with this agent for all possible initial dirt configurations and agent locations. Record the performance score for each configuration and the overall average score.

2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.
a. A simple reflex agent for this environment.
The peformance score in the output shows that this agent is indeed irrational.
b. Design a reflex agent with state for such an environment.

2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right).

2.12. Repeat Exercise 2.11 for the case in which the location sensor is replaced with a “bump” sensor that detects the agent’s attempts to move into an obstacle or to cross the boundaries of the environment. Suppose the bump sensor stops working; how should the agent behave?
b. Design a simple reflex agent with randomized agent function and measure its performance on several environments.

2.11.d. & 2.12.d. Design a reflex agent with state and measure its performance on several environments.
(Using the same code for 2.12- because a reflex agent with state knows the locations of the obstacles too, hence its the same as having a bump sensor).
