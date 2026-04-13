\# 3D Transformation Visualizer



\## Overview



The 3D Transformation Visualizer is an interactive application built using Python and Pygame that demonstrates core concepts of linear algebra and computer graphics. It allows users to explore how 3D objects behave under various transformations such as rotation, scaling, translation, and shearing, along with advanced concepts like eigenvectors, eigenvalues, and Principal Component Analysis (PCA).



This project is designed as an educational tool to help understand how mathematical transformations are applied in real-time graphical systems.



\---



\## Features



\### 1. Interactive 3D Shapes



\* Cube

\* Pyramid

\* Tetrahedron

\* Octahedron

\* Prism variants

\* Sphere, Cylinder, Cone



Users can switch between shapes dynamically.



\### 2. Transformations



\* Rotation along X, Y, Z axes

\* Scaling (uniform and non-uniform)

\* Translation in 3D space

\* Shearing transformation



\### 3. Projection Modes



\* Perspective Projection (realistic depth)

\* Orthographic Projection (no depth distortion)

\* Side-by-side comparison of both projections



\### 4. Linear Algebra Visualizations



\* Eigenvectors and Eigenvalues visualization

\* Live eigenvector updates based on transformation matrix

\* Principal Component Analysis (PCA)



&#x20; \* Covariance matrix display

&#x20; \* Principal directions (eigenvectors)

&#x20; \* Variance representation (eigenvalues)



\### 5. Coordinate System Visualization



\* Dynamic X, Y, Z axes

\* Origin labeling

\* Axes transform along with object



\---



\## Technologies Used



\* Python

\* Pygame (for rendering and UI)

\* NumPy (for matrix and vector operations)



\---



\## Mathematical Concepts Covered



\### Linear Transformations



All object transformations are performed using matrices:



\* Rotation matrices

\* Scaling matrices

\* Shear matrices



\### Eigenvalues and Eigenvectors



Used to identify invariant directions under transformations:

A v = λ v



\### Principal Component Analysis (PCA)



\* Data centering

\* Covariance matrix computation

\* Eigen decomposition for principal directions



\### 3D to 2D Projection



\* Perspective projection (depth-based scaling)

\* Orthographic projection (parallel projection)



\---



\## Controls



\### Keyboard Controls



\* Arrow Keys: Rotate object (X and Y axes)

\* Q / E: Rotate along Z-axis

\* W / S: Increase / decrease scale

\* A / D: Move along X-axis

\* R / F: Move along Y-axis

\* Z / X: Move along Z-axis

\* H: Toggle shear transformation

\* V: Toggle live eigenvector visualization



\### Mouse Controls



\* Click on shape buttons to change object

\* Toggle:



&#x20; \* Projection mode

&#x20; \* Eigenvector display

&#x20; \* PCA visualization



\---



\## Installation and Setup



\### Prerequisites



\* Python 3.11.8 installed



\### Install Dependencies



```bash

pip install pygame numpy

```



\### Run the Project



```bash

python main.py



```



\---



\## Project Structure



```

project/

│── main.py

│── README.md

```



\---



\## Learning Outcomes



This project helps in understanding:



\* How linear algebra is applied in graphics

\* How matrices control transformations

\* Visualization of abstract concepts like eigenvectors and PCA

\* Real-time rendering and event-driven programming



\---



\## Future Enhancements



\* Add GUI sliders for transformations

\* Implement camera controls

\* Add lighting and shading models

\* Export transformation matrices

\* Support for custom user-defined shapes



\---



\## Team Members



\* Kirthana Shetty

\* Porla Neha

\* Khushi Patel

\* Karanam Sreehitha

\---



\## License



This project is intended for educational purposes.



