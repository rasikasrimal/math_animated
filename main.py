#!/usr/bin/env python3
"""
Math Animated - A collection of mathematical animations using Manim

This script provides a convenient way to run different mathematical animations.
Each animation demonstrates a specific mathematical concept.

Usage:
    python main.py [animation_name]
    
Available animations:
    - quadratic: Quadratic function visualization
    - circle: Circle geometry (area and circumference)
    - derivative: Derivative and rate of change
    - vectors: Vector operations (addition, subtraction, dot product)
    - all: Run all animations in sequence
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

# Animation configurations
ANIMATIONS = {
    'quadratic': {
        'file': 'src/animations/algebra/quadratic_function.py',
        'scene': 'QuadraticFunctionAnimation',
        'description': 'Quadratic function transformations and vertex analysis'
    },
    'circle': {
        'file': 'src/animations/geometry/circle_geometry.py',
        'scene': 'CircleGeometryAnimation',
        'description': 'Circle area, circumference, and geometric properties'
    },
    'derivative': {
        'file': 'src/animations/calculus/derivative_visualization.py',
        'scene': 'DerivativeVisualization',
        'description': 'Derivative as the limit of secant lines'
    },
    'vectors': {
        'file': 'src/animations/linear_algebra/vector_operations.py',
        'scene': 'VectorOperations',
        'description': 'Vector addition, subtraction, and dot product'
    }
}

def check_dependencies():
    """Check if Manim is installed and available."""
    try:
        import manim
        print(f"✓ Manim version {manim.__version__} found")
        return True
    except ImportError:
        print("✗ Manim not found. Please install dependencies:")
        print("  pip install -r requirements.txt")
        return False

def run_animation(animation_key, quality='medium_quality', output_dir='media'):
    """Run a specific animation using Manim."""
    if animation_key not in ANIMATIONS:
        print(f"Error: Animation '{animation_key}' not found.")
        print(f"Available animations: {', '.join(ANIMATIONS.keys())}")
        return False
    
    config = ANIMATIONS[animation_key]
    file_path = config['file']
    scene_name = config['scene']
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: Animation file '{file_path}' not found.")
        return False
    
    print(f"Running animation: {config['description']}")
    print(f"File: {file_path}")
    print(f"Scene: {scene_name}")
    
    # Build the manim command
    cmd = [
        'python', '-m', 'manim',
        f'--{quality}',
        f'--output_file={animation_key}',
        file_path,
        scene_name
    ]
    
    try:
        # Run the animation
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Animation '{animation_key}' completed successfully!")
            print(f"Output saved to: {output_dir}/")
            return True
        else:
            print(f"✗ Animation '{animation_key}' failed:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"✗ Error running animation: {e}")
        return False

def list_animations():
    """List all available animations."""
    print("Available Animations:")
    print("=" * 50)
    for key, config in ANIMATIONS.items():
        print(f"{key:12} - {config['description']}")
    print()

def main():
    parser = argparse.ArgumentParser(description='Math Animated - Mathematical Animation Runner')
    parser.add_argument('animation', nargs='?', default='', 
                       help='Animation to run (use "list" to see all available)')
    parser.add_argument('--quality', choices=['low_quality', 'medium_quality', 'high_quality'], 
                       default='medium_quality', help='Video quality')
    parser.add_argument('--output-dir', default='media', help='Output directory')
    
    args = parser.parse_args()
    
    # Check dependencies first
    if not check_dependencies():
        sys.exit(1)
    
    # Handle different commands
    if args.animation == '' or args.animation == 'help':
        parser.print_help()
        print()
        list_animations()
        return
    
    if args.animation == 'list':
        list_animations()
        return
    
    if args.animation == 'all':
        print("Running all animations...")
        success_count = 0
        for key in ANIMATIONS.keys():
            print(f"\n{'='*50}")
            if run_animation(key, args.quality, args.output_dir):
                success_count += 1
        
        print(f"\n{'='*50}")
        print(f"Completed {success_count}/{len(ANIMATIONS)} animations successfully.")
        return
    
    # Run specific animation
    if not run_animation(args.animation, args.quality, args.output_dir):
        sys.exit(1)

if __name__ == '__main__':
    main()