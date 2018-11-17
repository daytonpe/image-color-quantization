import cv2
import numpy as np
import argparse

# parse arguments
parser = argparse.ArgumentParser(description='Cluster tweets')
parser.add_argument(
                   'numberOfClusters',
                   action="store",
                   default=5,
                   type=int,
                   nargs='?')
parser.add_argument(
                   'imgFile',
                   action="store",
                   default='../images/image1.jpg',
                   type=str,
                   nargs='?')
parser.add_argument(
                   'outputFile',
                   action="store",
                   default='./quantizedImages/image1_q.jpg',
                   type=str,
                   nargs='?')
args = parser.parse_args()

K = args.numberOfClusters

img = cv2.imread(args.imgFile)
Z = img.reshape((-1, 3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imwrite(args.outputFile, res2)
