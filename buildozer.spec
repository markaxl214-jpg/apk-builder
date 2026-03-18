[app]

title = Calculator
package.name = calculator
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# FIXED CONFIG 👇
android.api = 31
android.minapi = 21
# android.sdk REMOVE ❌
# android.ndk REMOVE ❌
android.archs = arm64-v8a, armeabi-v7a

entrypoint = main.py

[buildozer]

log_level = 2
build_dir = .buildozer
warn_on_root = 1
