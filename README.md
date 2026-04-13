\# 3D Transformation Visualizer



An interactive 3D visualization tool built using Python and Pygame to demonstrate linear algebra concepts such as transformations, eigenvectors, and Principal Component Analysis (PCA) in real time.



\---



\*\*Overview\*\*



The 3D Transformation Visualizer allows users to explore how geometric objects behave under different transformations including rotation, scaling, translation, and shearing.



It also provides visual insights into advanced mathematical concepts such as eigenvectors, eigenvalues, and PCA, making it a useful educational tool for understanding linear algebra in computer graphics.



\---



\*\*Features\*\*



\*\*Interactive 3D Shapes\*\*



\* Cube

\* Pyramid

\* Tetrahedron

\* Octahedron

\* Prism

\* Triangular Prism (tri\_prism)

\* Pentagonal Prism (pent\_prism)

\* Sphere

\* Cylinder

\* Cone



Users can dynamically switch between different shapes.



\---



\*\*Transformations\*\*



\* Rotation along X, Y, Z axes

\* Scaling (uniform and non-uniform)

\* Translation in 3D space

\* Shearing transformation



\---



\*\*Projection Modes\*\*



\* Perspective projection (realistic depth perception)

\* Orthographic projection (no depth distortion)

\* Side-by-side comparison of both projections



\---



\*\*Linear Algebra Visualizations\*\*



\* Eigenvectors and eigenvalues visualization

\* Live eigenvector updates based on transformation matrix

\* Principal Component Analysis (PCA)

\* Covariance matrix display

\* Principal directions (eigenvectors)

\* Variance representation (eigenvalues)



\---



\*\*Coordinate System Visualization\*\*



\* Dynamic X, Y, Z axes

\* Origin labeling

\* Axes transform along with the object



\---



\*\*Technologies Used\*\*



\* Python

\* Pygame

\* NumPy



\---



\*\*Mathematical Concepts Covered\*\*



\*\*Linear Transformations\*\*



\* Rotation matrices

\* Scaling matrices

\* Shear matrices



\*\*Eigenvalues and Eigenvectors\*\*



A v = λ v



\*\*Principal Component Analysis (PCA)\*\*



\* Data centering

\* Covariance matrix computation

\* Eigen decomposition



\*\*3D to 2D Projection\*\*



\* Perspective projection

\* Orthographic projection



\---



\*\*Controls\*\*



\*\*Keyboard Controls\*\*



\* Arrow Keys – Rotate object (X and Y axes)

\* Q / E – Rotate along Z-axis

\* W / S – Increase / decrease scale

\* A / D – Move along X-axis

\* R / F – Move along Y-axis

\* Z / X – Move along Z-axis

\* H – Toggle shear transformation

\* V – Toggle live eigenvector visualization



\*\*Mouse Controls\*\*



\* Click on shape buttons to change object

\* Toggle projection mode

\* Toggle eigenvector display

\* Toggle PCA visualization



\---



\*\*Project Structure\*\*



3D-Visualizer/

│── main.py

│── projection.py

│── shapes.py

│── transformation.py

│── visualization.py

│── README.md

│── .gitignore

│── \*\*pycache\*\*/



\---



\*\*File Description\*\*



\* \*\*main.py\*\* – Entry point of the application and main execution loop

\* \*\*projection.py\*\* – Handles perspective and orthographic projection logic

\* \*\*shapes.py\*\* – Contains definitions of 3D shapes and their vertices/edges

\* \*\*transformation.py\*\* – Implements rotation, scaling, translation, and shear transformations

\* \*\*visualization.py\*\* – Responsible for rendering, UI elements, and drawing

\* \*\*README.md\*\* – Project documentation

\* \*\*.gitignore\*\* – Specifies files ignored by Git

\* \*\*\*\*pycache\*\*/\*\* – Stores compiled Python files (auto-generated)



\---



\*\*Learning Outcomes\*\*



\* Understanding linear algebra in computer graphics

\* Applying matrix transformations

\* Visualizing eigenvectors and PCA

\* Working with real-time rendering systems



\---



\*\*Future Enhancements\*\*



\* GUI sliders for transformations

\* Camera controls

\* Lighting and shading models

\* Export transformation matrices

\* Custom user-defined shapes



\---



\*\*Team Members\*\*



\* Kirthana Shetty

\* Porla Neha

\* Khushi Patel

\* Karanam Sreehitha



\---



\*\*License\*\*



This project is intended for academic and educational purposes.



