# Color Quantization

Simple image color quantization implementation using OpenCV library.

### With pip3 Install the Following
- opencv-python
- numpy
- argparse

### Run with
```
python3 color_quantization.py [numberOfClusters] [imageFile] [outputFile]
```

### Example:
```
python3 color_quantization.py 8 ../images/image5.jpg ./quantizedImages/image5_q8.jpg
```

### Default Values
- numberOfClusters: 5
- imageFile: ../images/image1.jpg
- outputFile: ./quantizedImages/image1_q.jpg
