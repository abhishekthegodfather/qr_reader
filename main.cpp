#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/objdetect.hpp>
#include <opencv2/imgcodecs.hpp>

using namespace std;
using namespace cv;

void display(Mat &img, Mat &bbox)
{
    int n = bbox.rows;
    for (int i = 0; i < n; i++)
    {
        line(img, Point2i(bbox.at<float>(i, 0), bbox.at<float>(i, 1)), Point2i(bbox.at<float>((i + 1) % n, 0), bbox.at<float>((i + 1) % n, 1)), Scalar(255, 0, 0), 3);
    }
    imshow("Results", img);
}

int main(int argc, char **argv)
{

    // Mat image;
    // image = imread("C:/Users/abhis/OneDrive/Desktop/opencv/test.png");
    // if ( !image.data )
    // {
    //     //
    //     cout << "data not found" << endl;
    //     return -1;
    // }
    // namedWindow("Display Image", WINDOW_AUTOSIZE );
    // imshow("Display Image", image);
    // waitKey(0);
    // return 0;

    Mat img, img1;
    // namedWindow("QR Scanner");
    VideoCapture cap(0);

    while (true)
    {
        cap.read(img);


        QRCodeDetector qr = QRCodeDetector::QRCodeDetector();

        Mat bbox, rectimage;

        string data = qr.detectAndDecode(img, bbox, rectimage);

        cout << "Decoded Data"
             << ":" << data << endl;
        display(img, bbox);

        // rectimage.convertTo(rectimage, CV_8UC3);

        // imshow("QR Scanner", rectimage);
        // imshow("QR Scanner", img);
        // waitKey(27);
        if (waitKey(27) == 27)
        {
            break;
        }
    }

    return 0;
}