[app]

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

requirements = python3,kivy,kivymd

# Orientation

orientation = portrait

# Fullscreen

fullscreen = 0

# Permissions

android.permissions = INTERNET

# Android Config (stable versions)

android.api = 31
android.minapi = 21
android.ndk = 25b
android.build_tools = 33.0.2

# Entry point

entrypoint = main.py

# (optional)

# icon.filename = icon.png

# presplash.filename = presplash.png

[buildozer]

# Log level

log_level = 2

# Build directory

build_dir = .buildozer

# Warn on root

warn_on_root = 1
