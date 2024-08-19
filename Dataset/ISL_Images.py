import cv2 as cv
import os
import time
import uuid

IMAGES_PATH = "H:\##IIT KGP\DIY\DIY Project\Dataset\Signs Img Dataset"

labels = ['go']
number_imgs = 50

for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    os.mkdir(path)
    input("Press key to continue")
    print('Collecting images for {}'.format(label))
    cap = cv.VideoCapture(0)

    time.sleep(3)
    for imgnum in range(number_imgs):
        isTrue, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv.imwrite(imagename, frame)
        cv.imshow('frame', frame)
        time.sleep(.5)
        cv.waitKey(30)
    print('Done collecting images for {}'.format(label))

    cap.release()
