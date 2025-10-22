# ProjMotion

A projectile motion simulator built with pygame that visualizes the physics of projectile motion in real-time.

  - Blue ball representing the projectile
  - Trail dots showing the path
  - Grid (each grid represents one real life metre) overlay for reference
  - Real-time display of physics parameters
    - Displacement (dx) in meters
    - Velocity (v) in m/s
    - Launch angle (θ) in degrees
    - Time elapsed (dt) in seconds

Click on any trail dot to replay the motion from that point

## Requirements

- Python 3.x
- pygame library

## Installation

1. Clone or download this repository
2. Install pygame if you haven't already:
   ```bash
   pip install pygame
   ```

## Usage

Run the simulation:
```bash
python main.py
```

### Controls

- The simulation runs automatically showing the projectile motion
- Once the ball lands, you can click on any trail dot to replay the motion from that point
- Close the window to exit

## Physics

The simulator uses realistic physics with:
- Initial velocity: 5 m/s horizontal, 10 m/s vertical
- Gravity: 9.8 m/s²
- Scale: 1 meter = 50 pixels
- Frame rate: 60 FPS

These parameters can be easily adjusted in main.py.

## Project Structure

- `main.py` - Main simulation code
- `README.md` - This file

## How It Works

The simulation calculates projectile motion using basic physics equations:
- Horizontal position: x = x₀ + vₓt
- Vertical position: y = y₀ + vᵧt + ½gt²
- Velocity updates: vᵧ = vᵧ₀ + gt

The trail system records checkpoints every 0.1 seconds, allowing you to replay the motion from any point in the trajectory.
