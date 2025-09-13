#!/usr/bin/env python3
"""
Test script to verify the math animation project structure and imports
without requiring Manim installation.
"""

import sys
import os
from pathlib import Path

def test_project_structure():
    """Test that all required files and directories exist."""
    print("Testing project structure...")
    
    required_files = [
        'main.py',
        'requirements.txt',
        '.gitignore',
        'README.md',
        'src/__init__.py',
        'src/animations/__init__.py',
        'src/animations/algebra/quadratic_function.py',
        'src/animations/geometry/circle_geometry.py',
        'src/animations/calculus/derivative_visualization.py',
        'src/animations/linear_algebra/vector_operations.py'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files present")
        return True

def test_python_syntax():
    """Test Python syntax for all animation files."""
    print("\nTesting Python syntax...")
    
    python_files = [
        'main.py',
        'src/animations/algebra/quadratic_function.py',
        'src/animations/geometry/circle_geometry.py',
        'src/animations/calculus/derivative_visualization.py',
        'src/animations/linear_algebra/vector_operations.py'
    ]
    
    import py_compile
    
    for file_path in python_files:
        try:
            py_compile.compile(file_path, doraise=True)
            print(f"✅ {file_path} - syntax OK")
        except py_compile.PyCompileError as e:
            print(f"❌ {file_path} - syntax error: {e}")
            return False
    
    return True

def test_main_script():
    """Test main script help functionality."""
    print("\nTesting main script...")
    
    # Test basic import
    try:
        sys.path.insert(0, '.')
        import main
        print("✅ Main script imports successfully")
        
        # Test that ANIMATIONS dictionary is properly defined
        if hasattr(main, 'ANIMATIONS') and len(main.ANIMATIONS) == 4:
            print("✅ All 4 animations properly configured")
            
            # List all animations
            print("\n📋 Configured animations:")
            for key, config in main.ANIMATIONS.items():
                print(f"  - {key}: {config['description']}")
            
            return True
        else:
            print("❌ ANIMATIONS dictionary not properly configured")
            return False
            
    except Exception as e:
        print(f"❌ Main script error: {e}")
        return False

def test_animation_classes():
    """Test that animation classes are properly defined."""
    print("\nTesting animation classes...")
    
    # Since we can't easily mock manim for the imports, let's just check 
    # that the files contain the expected class definitions
    animations = [
        ('src/animations/algebra/quadratic_function.py', 'QuadraticFunctionAnimation'),
        ('src/animations/geometry/circle_geometry.py', 'CircleGeometryAnimation'),
        ('src/animations/calculus/derivative_visualization.py', 'DerivativeVisualization'),
        ('src/animations/linear_algebra/vector_operations.py', 'VectorOperations')
    ]
    
    for file_path, class_name in animations:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Check for class definition
            if f'class {class_name}(Scene):' in content:
                print(f"✅ {class_name} - class properly defined")
            else:
                print(f"❌ {class_name} - class definition not found")
                return False
                
            # Check for construct method
            if 'def construct(self):' in content:
                print(f"✅ {class_name} - construct method found")
            else:
                print(f"❌ {class_name} - construct method not found")
                return False
                
        except Exception as e:
            print(f"❌ {class_name} - file error: {e}")
            return False
    
    return True

def main():
    """Run all tests."""
    print("🧪 Math Animated - Project Test Suite")
    print("=" * 50)
    
    tests = [
        test_project_structure,
        test_python_syntax,
        test_main_script,
        test_animation_classes
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Project is ready for use.")
        print("\n📖 Next steps:")
        print("1. Install system dependencies for Manim:")
        print("   - On Ubuntu/Debian: sudo apt-get install build-essential python3-dev libcairo2-dev libpango1.0-dev")
        print("   - On macOS: brew install cairo pango glib pkg-config")
        print("2. Install Python dependencies: pip install -r requirements.txt")
        print("3. Run animations: python main.py list")
        return True
    else:
        print("❌ Some tests failed. Please check the output above.")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)