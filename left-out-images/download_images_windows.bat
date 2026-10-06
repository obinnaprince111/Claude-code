@echo off
REM Double-click this file. It downloads all images into an "images" folder next to it.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0download_images.ps1"
