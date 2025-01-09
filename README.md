Receipt OCR Project

Welcome to the Receipt OCR Project! This repository is a work in progress as I continue to develop a robust engine for extracting and rendering data from the receipt images. My goal is to create a solution that processes receipt images, extracts key info like the total amount, and renders the data in a structured and user friendly format.

Project Overview

The project involves:

Receipt Detection: Identifying the receipt's boundaries in an image.

Perspective Transformation: Aligning the receipt to a top-down, scanned-like view.

Text Recognition: Extracting text from the receipt using OCR.

Data Rendering: Processing the extracted text to display structured information (e.g., total amount, itemized lists).

Current Status

I am actively working on this project, and the hardest part—rendering and structuring data from the receipt images—is still under development. Honestly this  is the hardest part.

Progress

✅ Image preprocessing and edge detection.

✅ Contour detection and perspective transformation.

✅ Basic text extraction using Tesseract OCR.

🚧 Data rendering engine (ongoing).

Estimated Completion

I am passionate about this project and aim to complete it by February 2024.

Motivation

This project reflects my passion for computer vision and its practical applications. I started this repository to:

Learn advanced image processing techniques.

Build a practical tool for extracting structured data from images.

Challenge myself with solving real-world OCR problems.



How to Run

Clone this repository:

git clone https://github.com/noahlunberry/EZsplit.git

Install the required dependencies:

pip install -r requirements.txt

Place receipt images in the images folder.

Run the main script:

python main.py

Future Goals

Beyond rendering data from receipts, I plan to:

Add a user-friendly interface (web or mobile app).

Implement support for multiple languages in OCR.

Include machine learning models for improved text recognition.

Optimize performance for large datasets of receipts.

Thank you for visiting this repository! I look forward to sharing more updates as I progress.
