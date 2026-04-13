# 🚀 3D Transformation Visualizer

### Interactive Linear Algebra & Graphics Playground

---

## ✨ Overview

The **3D Transformation Visualizer** is an interactive Python project that helps you understand **linear algebra and computer graphics concepts visually**.

Built using **Pygame** and **NumPy**, this application allows real-time interaction with 3D objects and demonstrates transformations like rotation, scaling, translation, and shearing — along with advanced concepts such as **Eigenvalues, Eigenvectors, and PCA (Principal Component Analysis)**.

> 💡 This project converts abstract mathematical concepts into clear visual understanding.

---

## 🎯 Features

* 🔷 Real-time 3D object manipulation
* 🔶 Multiple 3D shapes (Cube, Pyramid, Sphere, Cylinder, Cone, Prism, etc.)
* 🔁 Transformations:

  * Rotation (X, Y, Z axes)
  * Scaling
  * Translation
  * Shearing
* 📐 Projection modes:

  * Perspective Projection
  * Orthographic Projection
* 📊 Linear Algebra Visualizations:

  * Eigenvalues & Eigenvectors
  * Live Eigen transformations
  * Principal Component Analysis (PCA)
* 🎮 Interactive controls using keyboard and UI

---

## 🧠 Concepts Covered

* Linear Transformations
* Matrix Multiplication
* Eigenvalues & Eigenvectors
* Covariance Matrix
* Principal Component Analysis (PCA)
* 3D to 2D Projection

---

## 🎮 Controls

| Action            | Key                   |
| ----------------- | --------------------- |
| Rotate X/Y        | Arrow Keys            |
| Rotate Z          | Q / E                 |
| Scale             | W / S                 |
| Translate         | A / D / R / F / Z / X |
| Toggle Shear      | H                     |
| Toggle Live Eigen | V                     |

🖱️ Use the sidebar buttons to:

* Change shapes
* Toggle projection mode
* Enable Eigen / PCA features

---

## 🏗️ Project Structure

```
3D-Transformation-Visualizer/
│
├── main.py              # Main application loop & UI
├── shapes.py            # 3D shape definitions
├── transformation.py    # Transformation logic
├── projection.py        # 3D to 2D projection
├── visualization.py     # Eigen & PCA visualization
└── README.md
```

---

## ⚙️ Installation & Run

```bash
git clone https://github.com/your-username/3D-Transformation-Visualizer.git
cd 3D-Transformation-Visualizer
pip install pygame numpy
python main.py
```



## 🔬 How It Works

The program follows this pipeline:

1. Apply scaling
2. Apply rotations (X, Y, Z axes)
3. Apply shearing (optional)
4. Apply translation
5. Convert 3D coordinates into 2D projection
6. Render using Pygame

Transformation matrix composition:

```python
T = Sh @ Rz @ Ry @ Rx @ S
```



## 🎓 Learning Outcomes

* Better understanding of linear algebra concepts
* Visualization of transformations in real-time
* Practical implementation of Eigenvalues and PCA
* Experience with graphics rendering using Python



## 🚀 Future Improvements

* Lighting and shading effects
* Mouse-based interaction
* Surface rendering instead of wireframes
* Export animations (GIF/video)
* OpenGL integration



## 👩‍💻 Authors

* Khushi Patel
* Kirthana Shetty
* Porla Neha
* Karanam Sreehitha



## 📜 License

This project is created for academic and educational purposes.



## ⭐ If You Like This Project

If you found this project useful, consider giving the repository a star ⭐ on GitHub.


