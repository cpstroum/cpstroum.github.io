#!/usr/bin/env python3
"""
SO-101 follower arm wave motion.

Prerequisites:
    pip install lerobot

Usage:
    python so101_wave.py --port /dev/ttyUSB0

Find your port with: python -m lerobot.find_port
"""

import argparse
import time
import math

from lerobot.common.robot_devices.motors.feetech import FeetechMotorsBus

# SO-101 follower joint layout
MOTORS = {
    "shoulder_pan":  (1, "sts3215"),
    "shoulder_lift": (2, "sts3215"),
    "elbow_flex":    (3, "sts3215"),
    "wrist_flex":    (4, "sts3215"),
    "wrist_roll":    (5, "sts3215"),
    "gripper":       (6, "sts3215"),
}

# Positions in degrees (after calibration the bus reads/writes in degrees)
NEUTRAL = {
    "shoulder_pan":  0.0,
    "shoulder_lift": 0.0,
    "elbow_flex":    0.0,
    "wrist_flex":    0.0,
    "wrist_roll":    0.0,
    "gripper":       0.0,
}

# Arm raised, ready to wave
WAVE_READY = {
    "shoulder_pan":  0.0,
    "shoulder_lift": -60.0,  # lift arm up
    "elbow_flex":    60.0,   # bend elbow so hand is up
    "wrist_flex":    0.0,
    "wrist_roll":    0.0,
    "gripper":       0.0,
}

WAVE_AMPLITUDE = 30.0   # degrees, wrist_roll side-to-side
WAVE_FREQUENCY = 1.0    # Hz
WAVE_DURATION  = 4.0    # seconds (number of full cycles = freq * duration)
MOVE_DURATION  = 1.5    # seconds to travel between poses
STEP_INTERVAL  = 0.02   # seconds between servo writes (~50 Hz)


def lerp(a: dict, b: dict, t: float) -> dict:
    return {k: a[k] + (b[k] - a[k]) * t for k in a}


def move_to(bus: FeetechMotorsBus, target: dict, duration: float) -> None:
    names = list(target.keys())
    start_values = {
        k: bus.read("Present_Position", k)[0] for k in names
    }
    t0 = time.monotonic()
    while True:
        elapsed = time.monotonic() - t0
        t = min(elapsed / duration, 1.0)
        # Smooth step
        t_smooth = t * t * (3 - 2 * t)
        pose = lerp(start_values, target, t_smooth)
        for name, value in pose.items():
            bus.write("Goal_Position", value, name)
        if t >= 1.0:
            break
        time.sleep(STEP_INTERVAL)


def wave(bus: FeetechMotorsBus) -> None:
    t0 = time.monotonic()
    while True:
        elapsed = time.monotonic() - t0
        if elapsed >= WAVE_DURATION:
            break
        angle = WAVE_AMPLITUDE * math.sin(2 * math.pi * WAVE_FREQUENCY * elapsed)
        pose = {**WAVE_READY, "wrist_roll": angle}
        for name, value in pose.items():
            bus.write("Goal_Position", value, name)
        time.sleep(STEP_INTERVAL)


def main():
    parser = argparse.ArgumentParser(description="SO-101 wave demo")
    parser.add_argument("--port", default="/dev/ttyUSB0", help="Serial port of the arm")
    parser.add_argument("--calibration-dir", default=None,
                        help="Path to calibration directory (default: lerobot default)")
    args = parser.parse_args()

    motor_names  = list(MOTORS.keys())
    motor_models = [v[1] for v in MOTORS.values()]
    motor_ids    = [v[0] for v in MOTORS.values()]

    bus = FeetechMotorsBus(
        port=args.port,
        motors={name: (mid, model) for name, (mid, model) in MOTORS.items()},
    )

    print(f"Connecting to SO-101 follower on {args.port} …")
    bus.connect()

    try:
        print("Moving to neutral …")
        move_to(bus, NEUTRAL, MOVE_DURATION)
        time.sleep(0.3)

        print("Raising arm …")
        move_to(bus, WAVE_READY, MOVE_DURATION)
        time.sleep(0.3)

        print("Waving …")
        wave(bus)

        print("Returning to neutral …")
        move_to(bus, NEUTRAL, MOVE_DURATION)

        print("Done!")
    finally:
        bus.disconnect()


if __name__ == "__main__":
    main()
