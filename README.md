# NASA SPACE APPS CHALLENGE

CHALLENGE - Immersed in the Sounds of Space

Computer vision details
Video analysis is done for every frame following these steps:

We detect stars using a combination of binary thresholding and DAOStarFinder from Photutils.
We use SORT to track stars.
We erase all found stars from the image.
Using binary thresholding we detect the contours of planets and nebulae. We discern them by roundness and area. Finally we approximate contour with a polygon using OpenCV.
You can see the work of this algorithm on this image. Notice the blue circle in the middle right - it represents a star that just went off-screen (previous location drawn).

![izobrazhenie_qHw17W2 width-1024](https://github.com/Hort1934/NASA-Space-Apps-Challenge/assets/61141309/f09c3d66-4db3-498a-8593-25c2b08e0dbc)
