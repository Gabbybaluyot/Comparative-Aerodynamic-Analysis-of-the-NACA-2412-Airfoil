# NACA 2412 Aerodynamic Simulation and Validation
<img width="1564" height="546" alt="12deg(iso view)" src="https://github.com/user-attachments/assets/d34bd0a5-a8f7-4785-bd8f-aec3b48a155c" />


A computational aerodynamics project analyzing the performance of a NACA 2412 airfoil using XFOIL, SolidWorks Flow Simulation (2D), Python, and digitized published aerodynamic data.

The project compares lift and drag coefficients, along with lift-to-drag ratio across multiple angles of attack while also visualizing changes in pressure and velocity around the airfoil.

---

## Project Overview

The goal of this project is to evaluate how closely computational aerodynamic methods reproduce published NACA 2412 airfoil data, along with how these different softwares vary in analyzing and computation while modifying the angle of attack. 

Three sources of aerodynamic data are used

- XFOIL
- SolidWorks Flow Simulation (2D)
- Digitized published NACA 2412 data

Python is used to automatically process the datasets and generate comparison plots for

- Lift coefficient $C_L$
- Drag coefficient $C_D$
- Lift-to-drag ratio $C_L/C_D$

SolidWorks Flow Simulation is also used to visualize pressure distribution, velocity distribution, and flow trajectories around the airfoil at selected angles of attack.

---

## Airfoil Geometry

The NACA 2412 is a cambered four-digit NACA airfoil.

The SolidWorks model used in this project has a chord length of

$$
c = 0.75 \text{ m}
$$

<p align="center">
  <img width="47%" alt="Screenshot 2026-09-03 200754" src="https://github.com/user-attachments/assets/788de58a-6b41-4e93-96f7-c4aead3f18a8" />
  <img width="47%" alt="naca2412-iso" src="https://github.com/user-attachments/assets/8b67eaab-eb76-47d0-94d8-1c54e908967c" />
</p>

---

## Simulation Methods

### XFOIL

XFOIL, a two-dimensional aerodynamic solver, was used to generate aerodynamic polar data for the NACA 2412 airfoil over a range of angles of attack.

The XFOIL output contains

- Angle of attack
- Lift coefficient
- Drag coefficient
- Pressure drag coefficient
- Pitching moment coefficient
- Upper and lower transition locations

For the current comparison, only angle of attack, lift coefficient, and drag coefficient are used.

The current XFOIL dataset was generated using

| Parameter | Value |
| --- | --- |
| Airfoil | NACA 2412 |
| Reynolds number | $2.2 \times 10^6$ |
| Mach number | 0.13 |
| Ncrit | 9 |

<img width="3300" height="2550" alt="plot" src="https://github.com/user-attachments/assets/a71c8e1d-92ad-42b2-ba65-c91256252832" />


---

### SolidWorks Flow Simulation

SolidWorks Flow Simulation was used to perform CFD analysis of the same NACA 2412 geometry.

Simulation results were exported as CSV files and processed using Python.

Selected flow conditions were also visualized using

- Pressure contours
- Velocity contours
- Flow trajectories

These visualizations were created at selected angles of attack to demonstrate how the aerodynamic flow field changes as the airfoil orientation changes.

---

## Pressure Distribution

Pressure contours were generated at several angles of attack using the same pressure scale so that the results can be visually compared.

### -4° Angle of Attack

<img width="568" height="360" alt="pressure-plot-(-4 degrees)-2" src="https://github.com/user-attachments/assets/c6206474-8267-4df4-b044-ae27242471f4" />


At negative angle of attack, the pressure distribution is relatively weak and the higher-pressure region shifts toward the upper side of the leading edge.

### 0° Angle of Attack

<img width="650" height="304" alt="pressure-plot-(0 degrees)-2" src="https://github.com/user-attachments/assets/30e3d99c-c7c7-4ed3-a872-499cf85dd9f6" />

Because the NACA 2412 is cambered, a pressure difference still develops between the upper and lower surfaces even at zero geometric angle of attack.

### 12° Angle of Attack

<img width="580" height="281" alt="pressure-plot-(12 degrees)" src="https://github.com/user-attachments/assets/7a02e297-5ec4-4606-8ac4-4326ef7af99f" />

At higher positive angle of attack, a much stronger low-pressure region develops over the upper surface while pressure increases beneath the leading edge.

This larger pressure difference corresponds to increased positive lift.

---

## Velocity Distribution

Velocity contours were also generated using a common scale so that the flow fields can be directly compared.

### -4° Angle of Attack

<img width="721" height="289" alt="velocity-plot-(-4 degrees)-2" src="https://github.com/user-attachments/assets/73cf302e-8975-4dd5-8313-8e4ff94d2b81" />

### 0° Angle of Attack

<img width="704" height="337" alt="velocity-plot-(0 degrees)-2" src="https://github.com/user-attachments/assets/5bd0fba9-e61d-43e7-be49-483df994ce05" />

### 12° Angle of Attack

<img width="648" height="307" alt="velocity-plot-(12 degrees)" src="https://github.com/user-attachments/assets/1aa57ca8-d924-4ce9-ba04-598ef002ef9d" />


As angle of attack increases, the simulations show greater acceleration over the upper surface and a more pronounced downstream velocity deficit.

The velocity plots are primarily used as qualitative flow-field visualizations rather than detailed boundary-layer measurements.

---

## Flow Trajectories

Flow trajectories provide an additional visualization of how the airflow bends and accelerates around the airfoil.

### 0° Angle of Attack

<img width="1448" height="542" alt="0deg(side view)" src="https://github.com/user-attachments/assets/22ecfad2-028a-4539-829a-0bcabb762a5f" />


### 12° Angle of Attack

<img width="1564" height="502" alt="12deg(side view)" src="https://github.com/user-attachments/assets/c0fe35e5-d66b-4c78-b82e-5cf90655b20b" />


The higher-angle case demonstrates stronger streamline curvature and increased upper-surface acceleration compared with the zero-angle case.

---

## Published NACA 2412 Data

Digitized published NACA 2412 aerodynamic data is used as the reference dataset for evaluating the computational results.

The dataset contains

- Angle of attack
- Lift coefficient
- Drag coefficient
- Pitching moment coefficient

The current Python analysis uses the angle of attack, lift coefficient, and drag coefficient values.

The lift-to-drag ratio is calculated using

$$
\frac{L}{D} = \frac{C_L}{C_D}
$$

> Add the original publication or dataset citation here once finalized.

---

## Python Data Analysis

A Python program was developed to automate the comparison process.

The program uses

- Pandas for data processing
- Matplotlib for visualization
- Glob for automatic file detection

The program automatically searches the project directory for aerodynamic result files, loads the available datasets, calculates lift-to-drag ratio, and generates comparison plots.

This allows additional SolidWorks, XFOIL, or published datasets to be added without manually rewriting the plotting code.

---

## Aerodynamic Comparison

The program generates three primary comparison plots.

### Lift and Drag Coefficients, Lift-to-Drag Ratio

$$
C_L \text{ vs } \alpha
$$

<img width="1800" height="500" alt="plots(1)" src="https://github.com/user-attachments/assets/21dcd2bc-500c-4b21-be20-466416453622" />


These plots allow the XFOIL and SolidWorks results to be directly compared with the digitized published NACA 2412 data.

---

## Current Status Summary

The current version of the project successfully

- Generates aerodynamic data using XFOIL
- Produces CFD results using SolidWorks Flow Simulation
- Imports XFOIL TXT files and aerodynamic CSV files using Python
- Automatically calculates lift-to-drag ratio
- Generates comparison plots for $C_L$, $C_D$, and $C_L/C_D$
- Compares computational results with digitized published NACA 2412 data
- Visualizes pressure, velocity, and flow trajectories at selected angles of attack

The next stage of development is focused on expanding the Python program so that it can quantitatively evaluate how much the XFOIL and SolidWorks results deviate from the published reference data.

Planned additions include

- Absolute error in lift coefficient
- Absolute error in drag coefficient
- Error in lift-to-drag ratio
- Percentage error where appropriate
- Mean absolute error
- Root mean square error
- Identification of angles of attack where the simulations deviate most strongly from the reference data

The goal is to move beyond visual comparison and provide a quantitative assessment of the accuracy of each aerodynamic simulation method.

