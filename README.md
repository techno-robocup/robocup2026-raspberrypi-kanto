# robocup2026-raspberrypi-kanto

> **⚠️ ARCHIVE NOTICE**
> 
> This repository has been archived and is no longer actively maintained.
> 
> **Please visit the new repository:** [techno-robocup/robocup2026-raspberrypi-program](https://github.com/techno-robocup/robocup2026-raspberrypi-program)

---

## About

This is a Raspberry Pi-based robot control system for RoboCup 2026. It includes:
- YOLO-based object detection for rescue operations
- Depth estimation using Depth-Anything-V2
- Line tracing capabilities
- Serial communication with robot hardware (ESP32)
- Systemd service integration for automatic startup

## Initial Setup

### User Permissions

Add the user to required groups for camera and serial access:
```bash
sudo usermod -aG video robo
sudo usermod -aG dialout robo
```

### Python Environment

Create a virtual environment with system site packages:
```bash
python3 -m venv .venv --system-site-packages
```

Install uv package manager:
```bash
pip install --break-system-packages uv
```

Initialize uv and install dependencies:
```bash
uv init
uv add opencv-python ultralytics gradio_imageslider gradio matplotlib torch torchvision pyserial Pillow huggingface-hub depth-anything-v2
```

Modify `.venv/pyvenv.cfg` to include:
```
include-system-site-packages = true
```

## How to run

### Manual execution
```bash
uv run python main.py
```

### Systemd service setup

The robot runs as a systemd service with automatic restart capabilities.

#### Installation

1. Copy service files to systemd directory:
```bash
sudo cp robot.service robot.path robot-restart.service /etc/systemd/system/
```

2. Reload systemd and enable services:
```bash
sudo systemctl daemon-reload
sudo systemctl enable robot.service robot.path
sudo systemctl start robot.service robot.path
```

3. Check status:
```bash
sudo systemctl status robot.service
sudo systemctl status robot.path
```

#### Restart trigger

To restart the robot service remotely or via automation:
```bash
touch /home/robo/restart.trigger
```

This will automatically trigger a service restart via the path monitoring mechanism.

#### Service architecture

- **robot.service**: Main robot process (runs continuously)
- **robot.path**: Monitors `/home/robo/restart.trigger` for changes
- **robot-restart.service**: Oneshot service that restarts robot.service when triggered

## Additional Configuration

Remove SSH configuration if needed:
```bash
rm /etc/ssh/sshd_config.d/rename_user.conf
```

## More Information

For depth estimation setup details, see [DEPTH_SETUP.md](DEPTH_SETUP.md).
