****3D Transformation Visualizer****

An interactive and visually rich application built using Python and Pygame to demonstrate core concepts of linear algebra and 3D computer graphics.

The system allows real-time visualization of 3D objects under various transformations such as rotation, scaling, translation, and shearing, along with advanced mathematical concepts like eigenvectors, eigenvalues, and Principal Component Analysis (PCA).

---

****Overview****

This project demonstrates the implementation of:

3D transformation using matrices  
Real-time graphical rendering using Pygame  
Eigenvalues and eigenvectors visualization  
Principal Component Analysis (PCA)  
Perspective and orthographic projections  
Interactive UI with keyboard and mouse controls  

The application was developed as an academic project focusing on both **mathematical concepts and graphical visualization**.

---

****Features****

****Transformation Features****

Rotation along X, Y, Z axes  
Scaling (uniform and non-uniform)  
Translation in 3D space  
Shearing transformation  

****Visualization Features****

Real-time rendering of multiple 3D shapes  
Dynamic coordinate axes visualization  
Perspective projection (depth-based)  
Orthographic projection (parallel projection)  
Side-by-side projection comparison  

****Mathematical Features****

Eigenvectors and eigenvalues visualization  
Live eigenvectors based on transformation matrix  
Principal Component Analysis (PCA)  

• Covariance matrix display  
• Principal components (eigenvectors)  
• Variance representation (eigenvalues)  

****System Features****

Interactive keyboard controls  
Mouse-based UI for shape selection  
Smooth rendering using game loop  
Event-driven architecture  

---

****System Architecture****

                ┌──────────────────────────┐
                │   Transformation Engine  │
                │ (Rotation, Scale, Shear) │
                └────────────┬─────────────┘
                             │
                ┌────────────▼────────────┐
                │   Projection Engine     │
                │ Perspective / Orthographic │
                └────────────┬────────────┘
                             │
                ┌────────────▼────────────┐
                │   Rendering (Pygame)    │
                │   Real-time Display     │
                └────────────┬────────────┘
                             │
                ┌────────────▼────────────┐
                │        User Input       │
                │ Keyboard / Mouse Events│
                └────────────────────────┘

The system processes transformations, projects them into 2D space, and renders them dynamically using Pygame.

---

****Communication Flow****

User selects a shape using UI  
Transformation inputs are applied (rotation, scaling, translation, shear)  
Transformation matrix is computed  
Points are projected from 3D → 2D  
Object is rendered on screen  
Eigenvectors and PCA are computed and displayed  
System continuously updates in real time  

---

****📂 Project Structure****

3D-Visualizer/
│
├── main.py
├── shapes.py
├── transformations.py
├── projection.py
├── visualization.py
│
├── demo.gif (optional)
├── README.md
└── .gitignore

---

****Technologies Used****

Python 3.x  
Pygame  
NumPy  
Linear Algebra Concepts  

---

****Setup Instructions****

1️) Clone the Repository

git clone https://github.com/Khushi-patel05/3D-Visualizer.git
cd 3D-Visualizer

---

2️) Install Dependencies

pip install pygame numpy

---

3️) Run the Application

python main.py

---

****Controls****

****Keyboard Controls****

Arrow Keys → Rotate object (X and Y axes)  
Q / E → Rotate along Z-axis  
W / S → Increase / decrease scale  
A / D → Move along X-axis  
R / F → Move along Y-axis  
Z / X → Move along Z-axis  
H → Toggle shear transformation  
V → Toggle live eigenvectors  

****Mouse Controls****

Click on shape buttons to change object  
Toggle projection mode  
Toggle eigenvector visualization  
Toggle PCA visualization  

---

****Mathematical Concepts****

Linear Transformations

All transformations are implemented using matrices:

Rotation matrices  
Scaling matrices  
Shear matrices  

---

****Eigenvalues and Eigenvectors****

Used to identify invariant directions under transformation:

A v = λ v  

---

****Principal Component Analysis (PCA)****

Data centering  
Covariance matrix computation  
Eigen decomposition for principal components  

---

****Projection Techniques****

Perspective projection (depth-based scaling)  
Orthographic projection (parallel projection)  

---

****Learning Outcomes****

By building this project, you learn:

How linear algebra is applied in computer graphics  
How transformation matrices work in real-time systems  
Visualization of eigenvectors and PCA  
Event-driven programming using Pygame  
Building interactive graphical applications  

---

****Future Improvements****

Add GUI sliders for transformations  
Implement camera controls  
Add lighting and shading  
Export transformation matrices  
Support custom user-defined shapes  

---

****Author****

Khushi Patel  
Kirthana Shetty  
Porla Neha  
Karanam Sreehitha  

---

****License****

This project is created for academic and educational purposes.

---

⭐ If You Like This Project

If you found this project useful, consider giving the repository a star ⭐ on GitHub.
