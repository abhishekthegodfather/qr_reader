# Importing lib

import cv2
import numpy as np
from pyzbar.pyzbar import decode


# testing a image 
# img = cv2.imread('test.png');

cap = cv2.VideoCapture(0);

# url = "http://192.168.0.102:8080/shot.jpg"

while True:
    frame, img = cap.read();
    # img_resp = requests.get(url)
    # img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    # img = cv2.imdecode(img_arr, -1)
    # img = imutils.resize(img, width=1000, height=1800)
    decode_things = decode(img);

    for code in decode_things:
        #if data is present in other form say binary it will
        # convert the data in the human readable format using 
        # UTF-8 standards
        print("The bar code data ----------->", code.data);
        qrdata = code.data.decode('utf-8');
        print("The human readable form of qr data ------->"
        , qrdata);


        #extracting the polygon point and making an numpy array 
        # and reshaping the array in (-1, 1, 2) shape form
        ply_pts = np.array([code.polygon], np.int64);
        ply_pts = ply_pts.reshape((-1, 1, 2));

        #Drawing the polygon shape using the opencv functions
        cv2.polylines(img, [ply_pts], True, (255, 0, 255), 3);

        #extracting the rectangle point for putting text
        qr_rect = code.rect;

        #now putting text in the img using opencv functions
        cv2.putText(img, qrdata, (qr_rect[0], qr_rect[1]), 
        cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2);

    # showing the images with message on the screen
    cv2.imshow("results", img);
    # print(decode_things);
    c = cv2.waitKey(1);
    if c == 27:
        break;


# decode_things = decode(img);
# print(type(decode_things));
# print(decode_things);
# cv2.imshow('results', img);
# for waiting the window screen
# cv2.waitKey(0);
# cap.release()
cv2.destroyAllWindows();




