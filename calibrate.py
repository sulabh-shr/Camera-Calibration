import cv2
import glob
import numpy as np


rows = 6
columns = 8

images = glob.glob('img_chessboard/GOPR0*.jpg')
image_pts = []  # 2D coordinates of images
object_pts = []  # 3D coordinates of images in the world
object_pt = np.zeros((rows * columns, 3), np.float32)  # predefined 3D coord of 1 image
object_pt[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2)

for filename in images:
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    found, corners = cv2.findChessboardCorners(gray, (columns, rows), None)

    if found:
        print(found, filename)
        image_pts.append(corners)
        object_pts.append(object_pt)
        combined_img = cv2.drawChessboardCorners(img, (columns, rows), corners, found)
        # plt.imshow(combined_img)
        # plt.show()
        cv2.imwrite('detected/cb_' + filename.split('/')[-1], combined_img)

h, w = gray.shape[:2]
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(object_pts, image_pts, (w, h), None, None)

for filename in images:
    img = cv2.imread(filename)
    undistorted = cv2.undistort(img, mtx, dist, None, mtx)
    cv2.imwrite('undistorted/un_' + filename.split('/')[-1]+'.png', undistorted)

