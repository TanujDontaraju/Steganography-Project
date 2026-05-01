# 🕵️‍♂️ Pixel Parse 🖼️

Pixel Parse is a steganography web application that allows you to hide and reveal secret messages within images. It provides an intuitive interface to encode text into a PNG image and decode hidden messages from previously encoded images. 

🌐 **Live Website:** [Pixel Parse on GitHub Pages](https://ud-f25-cs1.github.io/cs1-website-f25-TanujDontaraju/)

## ✨ Features

- 🔒 **Encrypt (Encode):** Select a PNG image and write a secret message. The application will hide your message within the least significant bits of the image's red color channel, producing a new encrypted image that you can save.
- 🔓 **Decrypt (Decode):** Upload a previously encrypted PNG image to extract and read the hidden secret message.

## ⚙️ How it Works

The steganography algorithm works by altering the Least Significant Bit (LSB) of the red color channel for each pixel in the image:
- To hide a `1` bit, the color intensity value is forced to be odd.
- To hide a `0` bit, the color intensity value is forced to be even.

A header containing the length of the secret message is prepended to the data before it is converted to binary and written to the image. This allows the decoder to know exactly how many characters to extract.

## 💻 Technologies Used

- **Python** 🐍 for the core logic.
- **Pillow (PIL)** 🎨 for image processing and manipulation.
- **Drafter** 🕸️ for the web application framework and user interface.

## 🚀 Setup and Execution

1. Ensure you have Python installed and run `pip install drafter bakery Pillow`.
2. Run the application: `python main.py`
3. The web server will start, allowing you to interact with the steganography web interface.
