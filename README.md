# aerospace-python-projects
here i upload my projects that i create related to rocket science and research

THE ROCKET DELTA V CALCULAROR 
# Delta-V Calculator

A Python implementation of the Tsiolkovsky Rocket Equation 
for calculating achievable delta-v and orbital feasibility.

Built as part of an aerospace engineering portfolio.

Variables:
- Ve: Exhaust velocity (m/s)
- m0: Initial mass including fuel (kg)
- mf: Final dry mass (kg)

Tested with real Falcon 9 specifications.


**Vertical Ascent Simulator (VAS-1)**
Aerospace Propulsion & Physics Model
🚀 Project Overview
This repository contains a Python-based flight dynamics simulator designed to model the vertical ascent of a heavy-lift launch vehicle (inspired by SpaceX Merlin-class propulsion). The simulation accounts for dynamic mass depletion, gravitational variance based on altitude, and Main Engine Cut-Off (MECO) parameters.
🛠️ Technical Specifications
The simulator utilizes Euler Integration to calculate the state of the vehicle at every 1-second interval.Gravitational Modeling: Uses the Universal Law of Gravitation rather than a constant 9.8/m/s^2accounting for the decrease in gravity as the rocket gains altitude.
Mass Flow Rate: Simulates a fuel burn rate of 2,000 kg/s, affecting the Thrust-to-Weight ratio (TWR) in real-time.

.📊 Mission Profile Data
The simulation outputs three primary telemetry graphs:
Altitude (km): Tracking the trajectory from sea level through the upper atmosphere.
Velocity (m/s): Monitoring acceleration curves and kinetic energy gain.
Mass Depletion (kg): Visualizing the inverse relationship between fuel consumption and acceleration.


💻 Setup & ExecutionPrerequisites:
Python 3.x
Matplotlib (pip install matplotlib)
