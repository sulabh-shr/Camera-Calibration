import cv2
import glob

rows = 6
columns = 8

def find_corners(filenames):
    filenames = list(set(filenames))
    while True:
        for filename in filenames:
            img = cv2.imread(filename)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            yield cv2.findChessboardCorners(gray, (columns, rows), None)
            if filenames.index(filename) == len(filenames)-1:
                break
        break


images = glob.glob('img_chessboard/GOPR0*.jpg')
f = []
c = []
for a,b in find_corners(images):
    f.append(a)
    c.append(b)






print(f)
