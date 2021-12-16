#!/bin/bash

rm -r ../target/dist
mkdir ../target/dist
ffmpeg -framerate $1 -i ../target/final-frames/%03d.jpg -c:v libx264 ../target/dist/output.mp4
ffmpeg -i ../target/dist/output.mp4 ../target/dist/output.gif
rm ../target/dist/output.mp4