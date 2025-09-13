# Math Animated 📊🎬

A collection of mathematical animations created with [Manim](https://www.manim.community/), designed to visualize and explain mathematical concepts through engaging animated videos.

## 🎯 Features

This repository contains animated visualizations for:

- **Algebra**: Quadratic functions, transformations, and vertex analysis
- **Geometry**: Circle properties, area, circumference calculations
- **Calculus**: Derivatives, limits, and rate of change visualization
- **Linear Algebra**: Vector operations, addition, subtraction, and dot products

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rasikasrimal/math_animated.git
cd math_animated
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Animations

Use the main script to run animations:

```bash
# List all available animations
python main.py list

# Run a specific animation
python main.py quadratic
python main.py circle
python main.py derivative
python main.py vectors

# Run all animations
python main.py all

# Specify video quality (low_quality, medium_quality, high_quality)
python main.py quadratic --quality high_quality
```

## 📋 Available Animations

| Animation | Command | Description |
|-----------|---------|-------------|
| Quadratic Functions | `quadratic` | Visualizes quadratic function transformations and vertex properties |
| Circle Geometry | `circle` | Demonstrates circle area, circumference, and geometric relationships |
| Derivative Visualization | `derivative` | Shows derivatives as limits of secant lines |
| Vector Operations | `vectors` | Illustrates vector addition, subtraction, and dot products |

## 📁 Project Structure

```
math_animated/
├── main.py                          # Main runner script
├── requirements.txt                 # Python dependencies
├── src/
│   └── animations/
│       ├── algebra/
│       │   └── quadratic_function.py    # Quadratic function animations
│       ├── geometry/
│       │   └── circle_geometry.py       # Circle geometry animations
│       ├── calculus/
│       │   └── derivative_visualization.py  # Calculus concepts
│       └── linear_algebra/
│           └── vector_operations.py     # Vector mathematics
└── media/                           # Generated video outputs (created after running)
```

## 🎨 Animation Details

### Quadratic Functions
- Visualizes parabolas with different coefficients
- Shows vertex transformations
- Demonstrates the effect of the 'a' coefficient on curve shape

### Circle Geometry
- Interactive visualization of radius, diameter, and center
- Real-time calculation of area and circumference
- Dynamic resizing to show relationship changes

### Derivative Visualization
- Shows secant lines approaching tangent lines
- Visualizes the limit process
- Demonstrates instantaneous rate of change

### Vector Operations
- Vector addition using parallelogram method
- Vector subtraction visualization
- Scalar multiplication effects
- Dot product calculation and interpretation

## 🛠️ Development

### Adding New Animations

1. Create a new Python file in the appropriate category folder
2. Import Manim and create a Scene class
3. Implement the `construct` method with your animation logic
4. Update `main.py` to include your new animation in the `ANIMATIONS` dictionary

Example structure:
```python
from manim import *

class YourAnimationName(Scene):
    def construct(self):
        # Your animation code here
        pass
```

### Dependencies

- **Manim**: Mathematical animation engine
- **NumPy**: Numerical computations
- **Matplotlib**: Additional plotting utilities
- **SciPy**: Scientific computing functions
- **Pillow**: Image processing

## 🎥 Output

All animations are rendered as MP4 videos and saved in the `media/` directory. The default quality is set to medium for a balance between file size and visual quality.

## 📖 Learning Resources

- [Manim Documentation](https://docs.manim.community/)
- [Manim Tutorial](https://docs.manim.community/en/stable/tutorials.html)
- [Mathematical Animation Examples](https://github.com/3b1b/manim)

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Add new mathematical animations
- Improve existing visualizations
- Fix bugs or enhance documentation
- Suggest new mathematical concepts to visualize

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Created with [Manim Community Edition](https://www.manim.community/)
- Inspired by 3Blue1Brown's mathematical visualizations
- Thanks to the open-source community for making mathematical education accessible