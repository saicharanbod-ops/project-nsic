# 🎨 Easy Cartoonify

A simple and intuitive Streamlit web application that transforms your images into cartoon-style artwork with customizable styles.

## Features

- **Dual Input Methods**: Upload images directly or search for them by filename
- **Multiple Cartoon Styles**: Choose between two distinct cartoonification styles
  - **Style 1 (Subtle)**: Gentle cartoon effect with moderate stylization
  - **Style 2 (Bold)**: Strong cartoon effect with pronounced stylization
- **Side-by-Side Comparison**: View original and cartoonified images simultaneously
- **Download Capability**: Export your cartoonified images as PNG files
- **User-Friendly Interface**: Clean, intuitive design with a two-column layout

## Requirements

- Python 3.7 or higher
- OpenCV (cv2)
- Streamlit
- NumPy

## Installation

1. **Clone or download the project**:
   ```bash
   git clone https://github.com/saicharanbod-ops/project-nsic/
   cd project-nsic
   ```

2. **Install required dependencies**:
   ```bash
   pip install opencv-python streamlit numpy
   ```

## Usage

### Running the Application

Start the Streamlit app by running:
```bash
streamlit run easy_cartoonify.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Application

1. **Choose Input Method**:
   - **Upload File**: Click to select an image from your computer (supports .jpg, .jpeg, .png, .bmp)
   - **Search by Filename**: Enter a filename and directory path to locate an image on your system

2. **Select Cartoon Style**:
   - Choose between "Style 1 (Subtle)" for a gentle effect or "Style 2 (Bold)" for a more pronounced effect

3. **View Results**:
   - The original and cartoonified images are displayed side-by-side

4. **Download**:
   - Click the "💾 Download Cartoonified Image" button to save your image

## File Structure

```
project-nsic/
├── easy_cartoonify.py    # Main Streamlit application
└── README.md             # This file
```

## How It Works

The application uses OpenCV's `stylization` filter to create cartoon effects. The two styles use different parameters:

- **Style 1 (Subtle)**: `sigma_s=150, sigma_r=0.25` - Preserves more image details
- **Style 2 (Bold)**: `sigma_s=60, sigma_r=0.5` - Creates a more abstract cartoon effect

The `find_the_image()` function provides a file search utility that recursively searches directories for the specified image filename.

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)

## Troubleshooting

- **Image not found**: Ensure the filename and directory path are correct. For system-wide search, use `/` as the directory
- **Performance issues**: Large images may take longer to process. Consider resizing before upload for faster results
- **Download not working**: Check that your browser allows downloads and you have write permissions in the application directory

## Future Enhancements

Potential improvements could include:
- Additional cartoon style presets
- Image resizing options
- Batch processing capability
- Custom parameter adjustments for users
- Additional artistic filters

## License

Include your license information here

## Support

For issues or questions, please create an issue in the repository.
