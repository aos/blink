# Demo - Capturing any Webcam/Screen/Window

This demo shows how to find all the windows whose titles match specific
regular expressions and save their contents as images. It currently
only works on Windows because the library that finds windows by
title is for windows only. If you already know the coordinates of
the window you can remove that dependency and run it on any
platform.

## Setup

Install the dependencies (mss, pywin32) by running:

	pip install -r requirements.txt

## Run Demo

	python main.py
