#!/usr/bin/env python3
"""
Demo script that shows what the animations demonstrate without requiring Manim.
This gives users a preview of what each animation does.
"""

def demo_quadratic():
    print("🎬 QUADRATIC FUNCTION ANIMATION")
    print("=" * 40)
    print("This animation demonstrates:")
    print("• Plotting quadratic functions f(x) = ax² + bx + c")
    print("• Showing how coefficient 'a' affects the parabola shape")
    print("• Vertex identification and transformation")
    print("• Function: f(x) = x² - 2x + 1 → f(x) = 2x² - 4x + 3")
    print("• Vertex moves from (1, 0) to (1, 1)")
    print()

def demo_circle():
    print("🎬 CIRCLE GEOMETRY ANIMATION")
    print("=" * 40)
    print("This animation demonstrates:")
    print("• Circle with center, radius, and diameter visualization")
    print("• Formula calculations: C = 2πr and A = πr²")
    print("• Dynamic resizing showing relationship changes")
    print("• For r = 2: C = 4π, A = 4π")
    print("• For r = 3: C = 6π, A = 9π")
    print()

def demo_derivative():
    print("🎬 DERIVATIVE VISUALIZATION ANIMATION")
    print("=" * 40)
    print("This animation demonstrates:")
    print("• Function f(x) = x² with secant lines")
    print("• Secant slope calculation as h approaches 0")
    print("• Transition from secant to tangent line")
    print("• At x = 1.5: secant slopes approach f'(1.5) = 3")
    print("• Shows derivative as instantaneous rate of change")
    print()

def demo_vectors():
    print("🎬 VECTOR OPERATIONS ANIMATION")
    print("=" * 40)
    print("This animation demonstrates:")
    print("• Vector a⃗ = (3, 2) and b⃗ = (1, 3)")
    print("• Vector addition: a⃗ + b⃗ = (4, 5)")
    print("• Vector subtraction: a⃗ - b⃗ = (2, -1)")
    print("• Scalar multiplication: 1.5a⃗ = (4.5, 3)")
    print("• Dot product: a⃗ · b⃗ = 9")
    print("• Parallelogram method for addition")
    print()

def main():
    print("📊 MATH ANIMATED - ANIMATION PREVIEWS")
    print("=" * 50)
    print("This demo shows what each animation demonstrates.")
    print("Install Manim to see the actual animated visualizations!")
    print()
    
    animations = [
        ("1", "Quadratic Functions", demo_quadratic),
        ("2", "Circle Geometry", demo_circle),
        ("3", "Derivative Visualization", demo_derivative),
        ("4", "Vector Operations", demo_vectors)
    ]
    
    while True:
        print("Available animation previews:")
        for num, name, _ in animations:
            print(f"  {num}. {name}")
        print("  5. Show all")
        print("  0. Exit")
        
        choice = input("\nChoose an animation to preview (0-5): ").strip()
        
        if choice == "0":
            print("Goodbye! 👋")
            break
        elif choice == "5":
            for _, _, demo_func in animations:
                demo_func()
                print("-" * 50)
        elif choice in ["1", "2", "3", "4"]:
            idx = int(choice) - 1
            animations[idx][2]()
            input("Press Enter to continue...")
        else:
            print("Invalid choice. Please try again.")
        
        print()

if __name__ == "__main__":
    main()