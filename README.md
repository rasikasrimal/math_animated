# How to Run the Derivative Animation

## Installation
1. Install Python 3.8 or higher
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Animation
1. To render the first scene (DerivativeExplanation):
   ```bash
   manim derivative_animation.py DerivativeExplanation
   ```

2. To render the second scene (DerivativeApplications):
   ```bash
   manim derivative_animation.py DerivativeApplications
   ```

3. To render both scenes:
   ```bash
   manim derivative_animation.py DerivativeExplanation DerivativeApplications
   ```

## Rendering Options
- For high quality (slower): `manim derivative_animation.py DerivativeExplanation -qh`
- For preview (faster): `manim derivative_animation.py DerivativeExplanation -ql`
- For 4K quality: `manim derivative_animation.py DerivativeExplanation -qk`

## Output
- Videos will be saved in `media/videos/derivative_animation/`
- Default resolution: 1920x1080 (Full HD)
- Frame rate: 30 FPS

## Customization
- Modify colors by changing color constants (BLUE, RED, GREEN, etc.)
- Adjust timing by changing `self.wait()` values
- Change functions by modifying the `func()`, `derivative_func()` definitions
- Modify axes ranges in the `Axes()` constructor