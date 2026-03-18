[app]

# SDK path (important)
android.sdk_path = /home/runner/android-sdk

# App Info
title = Calculator
package.name = calculator
package.domain = org.test

# Source
source.dir = .
source.include_exts = py,png,jpg,kv

# Version
version = 1.0

# Requirements
requirements = python3,kivy

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Permissions
android.permissions = INTERNET

# Android Config (stable)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.build_tools = 33.0.2

# Entry point
entrypoint = main.py

[buildozer]

log_level = 2
build_dir = .buildozer
warn_on_root = 1
