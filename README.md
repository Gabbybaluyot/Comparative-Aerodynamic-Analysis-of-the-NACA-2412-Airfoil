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

Pressure contour plots were generated at various angles of attack using the same pressure scale so that changes within the pressure field can be compared directly. The pressure distribution around an airfoil is heavily influenced by its geometry, along with the angle of attack. As the airfoil redirects the incoming fluid flow, areas of acceleration and deceleration form around the surface. In regions of approximately incompressible external flow, an increase in flow velocity is generally accompanied by decreases in static pressure, whereas decreases in flow velocity is associated with an increase in static pressure. These differences in pressure between the upper and lower surfaces of the airfoil produces the majority of the aerodynamic lift. Altering the angle of attack changes both the magnitude and location of these pressure regions.


### -4° Angle of Attack

<img width="568" height="360" alt="pressure-plot-(-4 degrees)-2" src="https://github.com/user-attachments/assets/c6206474-8267-4df4-b044-ae27242471f4" />


At a negative angle of attack, the incoming fluid (air) meets the airfoil such that the stagnation region moves upward around the leading edge. This causes a relatively high-pressure region to develop closer to the upper surface of the leading edge, as seen in the diagram.

At the same time, the pressure difference between the upper and lower surfaces becomes much smaller than at positive angles of attack and may begin to reverse depending on the exact operating condition. The NACA 2412 is cambered, meaning that its zero-lift angle occurs at a slightly negative geometric angle of attack rather than exactly 0°. Therefore, at -4°, the airfoil is operating below its approximate zero-lift condition and is expected to produce reduced or negative lift.

The weaker pressure difference visible in the contour is therefore consistent with the reduction and eventual reversal of lift as the angle of attack becomes increasingly negative.

### 0° Angle of Attack

<img width="650" height="304" alt="pressure-plot-(0 degrees)-2" src="https://github.com/user-attachments/assets/30e3d99c-c7c7-4ed3-a872-499cf85dd9f6" />

Despite an angle of attack of 0°, the pressure field is not symmetric because the NACA 2412 is a cambered airfoil.

The curved mean camber line causes the fluid to be redirected even when the chord line is aligned with the freestream. Flow over the upper surface accelerates more strongly, producing a lower-pressure region over the forward portion of the airfoil. At the same time, the lower surface remains at a comparatively higher pressure.

The resulting pressure difference produces positive lift at 0° angle of attack. This is an important distinction between the NACA 2412 and a symmetric airfoil, which would ideally produce approximately zero lift at 0° under comparable conditions.

The lowest pressure typically occurs relatively close to the leading edge, where the surface curvature and flow acceleration are strongest. Moving toward the trailing edge, the pressure gradually recovers toward the freestream value.

This pressure recovery creates an adverse pressure gradient, meaning the pressure increases in the direction of the flow. The boundary layer must move against this increasing pressure while losing momentum because of viscous effects. At moderate angles of attack, the boundary layer still has sufficient momentum to remain largely attached.

### 12° Angle of Attack

<img width="580" height="281" alt="pressure-plot-(12 degrees)" src="https://github.com/user-attachments/assets/7a02e297-5ec4-4606-8ac4-4326ef7af99f" />

At an angle of attack of 12°, the pressure difference between the upper and lower surfaces becomes much larger. The stagnation point moves farther onto the lower surface of the leading edge, creating a strong high-pressure region below the nose of the airfoil.

Above the leading edge, the fluid must accelerate rapidly around the strongly curved upper surface. This produces a much larger region of low static pressure, often referred to as the upper-surface suction region.

The combination of increased pressure on the lower surface and decreased pressure on the upper surface produces a much larger pressure difference along the airfoil. This corresponds directly to the increased positive lift coefficient expected at higher angles of attack.

The pressure along the upper surface of the airfoil also has to recover from its low value near the leading edge back toward the freestream pressure near the trailing edge. At 12°, this recovery occurs over a stronger adverse pressure gradient than at the lower angles of attack.

A strong adverse pressure gradient is important because the low-momentum air inside the boundary layer can eventually become unable to continue moving downstream against the increasing pressure. If this occurs, the flow begins to separate from the surface.

Therefore, any region of disturbed or detached flow visible toward the rear of the airfoil at 12° may indicate the beginning of significant flow separation. As the angle of attack continues to increase, this separation would grow and eventually contribute to aerodynamic stall, where the airfoil can no longer maintain the expected increase in lift.

---

## Velocity Distribution

Velocity contour plots were generated using a common scale so that changes in flow acceleration around the airfoil can be directly compared.

The velocity and pressure distributions are closely related. Regions where the external flow accelerates around the airfoil generally correspond to reductions in static pressure, while regions of lower velocity are generally associated with pressure recovery or stagnation.

The contours also help demonstrate how the angle of attack changes the location and strength of flow acceleration as well as the wake that develops downstream of the airfoil.


### -4° Angle of Attack

<img width="721" height="289" alt="velocity-plot-(-4 degrees)-2" src="https://github.com/user-attachments/assets/73cf302e-8975-4dd5-8313-8e4ff94d2b81" />

At -4°, the flow acceleration around the upper surface is relatively weak compared with the positive-angle cases.

Because the airfoil is oriented downward relative to the incoming flow, the stagnation region moves toward the upper side of the leading edge. The flow passing around the lower portion of the airfoil can therefore experience comparatively greater acceleration than it does at positive angles of attack.

This redistribution of velocity is consistent with the reduced or negative pressure difference across the airfoil at this operating condition.

Behind the airfoil, a wake is still present because viscous effects cause momentum losses within the boundary layer. However, the wake structure is comparatively modest because the airfoil is not operating at a large positive angle of attack.

### 0° Angle of Attack

<img width="704" height="337" alt="velocity-plot-(0 degrees)-2" src="https://github.com/user-attachments/assets/5bd0fba9-e61d-43e7-be49-483df994ce05" />

At 0°, the effects of the NACA 2412's camber become visible within the velocity field.

The airflow accelerates over the curved upper surface even though the geometric angle of attack is zero. The maximum velocity generally occurs near the forward portion of the upper surface, near the same region where the pressure contour shows its strongest pressure reduction.

As the flow travels farther downstream, the velocity outside the boundary layer gradually decreases as pressure recovers toward the trailing edge.

Near the airfoil surface, viscosity slows the airflow due to friction with the surface. The velocity increases from zero at the wall to the external flow velocity farther away, forming a boundary layer.

As the airflow leaves the trailing edge, it forms a wake where the velocity is lower than the surrounding flow. This happens because the air loses some momentum due to friction and drag. Meshing within the software can also affect how the wake appears, since a coarse mesh may make it look wider or more spread out than it actually is.

### 12° Angle of Attack

<img width="648" height="307" alt="velocity-plot-(12 degrees)" src="https://github.com/user-attachments/assets/1aa57ca8-d924-4ce9-ba04-598ef002ef9d" />

At 12°, the most significant upper-surface acceleration occurs near the leading edge.

The increased angle of attack forces the incoming flow to turn more sharply around the upper surface. This produces a larger velocity increase than at 0°, which corresponds to the much lower pressure observed in the same region of the pressure contour.

After reaching this high velocity near the front of the airfoil, the flow must decelerate as it moves toward the trailing edge and the pressure begins to recover. This deceleration occurs within a strong adverse pressure gradient.

Because the boundary-layer flow has relatively low momentum, a strong adverse pressure gradient can slow it down significantly. If it slows enough, the airflow can detach from the airfoil surface, causing flow separation.

At 12° angle of attack, a larger low-velocity region can develop over the rear portion of the upper surface as the airflow begins to slow down and possibly separate. This can create a wider wake behind the airfoil, which is associated with greater momentum loss and increased drag.

The appearance of this wake can also be affected by the mesh. A coarse mesh may smooth out the velocity gradients or make the wake appear wider than it actually is, so some of the details in the contour may be influenced by the mesh resolution.

Overall, the velocity contours follow the same general trends as the pressure contours. As the angle of attack increases, the airflow accelerates more strongly over the upper surface, creating a larger pressure difference and more lift. At higher angles of attack, the stronger pressure recovery can also cause the boundary layer to slow down and separate, leading to a larger wake and increased drag.

---

## Flow Trajectories

Flow trajectory plots were included to visually demonstrate the path the air takes as it moves around the airfoil. They help visualize how strongly the flow is being turned, where it speeds up, whether it remains attached to the surface, and how the wake develops behind the airfoil. 

As the angle of attack changes, the location of the stagnation region and the amount of flow turning around the airfoil also change. These trajectory plots should mainly be interpreted qualitatively, since the exact appearance of the flow paths can also be influenced by mesh resolution and other simulation settings.

### -4° Angle of Attack

<img width="1454" height="596" alt="(-4)deg(side view)" src="https://github.com/user-attachments/assets/03ffc0dd-5bdb-4089-8983-3cbaeb356030" />

At -4° angle of attack, the stagnation region shifts toward the upper side of the leading edge compared with the 0° and 12° cases. This introduces a region with nearly zero velocity, along with high static pressure.

The flow remains mostly smooth and attached around the airfoil, with no obvious large separated region. The airflow over the upper surface is not forced to turn as sharply as it is at positive angles of attack, resulting in a weaker airflow acceleration on the upper-surface.

The lower surface experiences relatively greater flow acceleration than it does at positive angles of attack. This is consistent with the smaller, and potentially reversed, pressure difference between the upper and lower surfaces.

Because the NACA 2412 is cambered, its zero-lift angle is slightly negative rather than exactly 0°. At -4°, the airfoil is therefore near or below its zero-lift condition, so the lift is much smaller and may become negative.

A wake is still present behind the airfoil because of viscous effects and drag. Its exact width and shape may also be affected by the mesh resolution, especially near the trailing edge.

### 0° Angle of Attack

<img width="1448" height="542" alt="0deg(side view)" src="https://github.com/user-attachments/assets/22ecfad2-028a-4539-829a-0bcabb762a5f" />

At 0° angle of attack, the airflow follows the shape of the NACA 2412 relatively smoothly and remains mostly attached to the surface.

Because the airfoil is cambered, the flow pattern is not perfectly symmetric. The air is turned more strongly over the upper surface, where it also accelerates near the front of the airfoil.

This agrees with the velocity contours, which show higher upper-surface velocity, and the pressure contours, which show lower pressure over the same region. The resulting difference between the upper and lower surface pressure allows the airfoil to produce positive lift even at 0° angle of attack.

As the airflow approaches the trailing edge, the upper and lower flows leave the airfoil and form a wake downstream. This wake appears because the airflow has lost some momentum due to friction and drag.

The mesh can influence how clearly the wake and near-surface trajectories are captured, as a coarse mesh may smooth out some of the smaller changes in flow direction.

### 12° Angle of Attack

<img width="1564" height="502" alt="12deg(side view)" src="https://github.com/user-attachments/assets/c0fe35e5-d66b-4c78-b82e-5cf90655b20b" />


At 12° angle of attack, the airflow is turned much more strongly around the airfoil.

The stagnation region shifts farther toward the lower side of the leading edge, while the airflow over the upper surface must make a sharper turn around the airfoil. This results in stronger acceleration near the upper leading edge.

The more tightly curved trajectories in this region are consistent with the velocity contours, which show higher flow speeds, and the pressure contours, which show a stronger low-pressure region over the upper surface.

Farther downstream, the airflow over the upper surface begins to slow as the pressure increases again. This creates a stronger adverse pressure gradient.

Because the boundary-layer flow has relatively low momentum, it can have difficulty remaining attached under this stronger pressure gradient. If it slows down enough, the flow may begin to separate from the upper surface near the rear of the airfoil.

This can create a larger disturbed region near the trailing edge and a wider wake downstream. A larger wake is generally associated with greater momentum loss and increased aerodynamic drag.

The 12° case should still be interpreted carefully. As mentioned before, the exact location and size of any separated region may be influenced by the mesh and the simulation model. A coarse mesh can make the wake appear wider or smooth out the point where separation begins.

Overall, the three trajectory plots show a clear change in flow behavior as the angle of attack increases. At -4°, the flow is relatively smooth with weaker upper-surface turning. At 0°, the camber of the airfoil produces noticeable upper-surface acceleration and positive lift. At 12°, the airflow is turned much more sharply, producing stronger acceleration, a larger pressure difference, and a greater possibility of flow separation and increased drag.

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

