#NASA SPACE APP COMPETITION

CHALLENGE - Immersing yourself in the sounds of space

Developed by the Cosmic composers team 

Team website - https://www.spaceappschallenge.org/2023/find-a-team/cosmic-composers

Details of computer vision
The video analysis is performed for each frame as follows:

We detect stars using a combination of binary thresholding and DAOStarFinder from Photutils.
Use SORT to track the stars.
Remove all found stars from the image.
Using binary thresholding, we detect the outlines of planets and nebulae. We distinguish them by their roundness and area. Finally, we approximate the contour with a polygon using OpenCV.
You can see how this algorithm works in this image. Note the blue circle in the middle right - this is a star that has just moved off the screen (the previous location is drawn).

![izobrazhenie_qHw17W2 width-1024](https://github.com/Hort1934/NASA-Space-Apps-Challenge/assets/61141309/f09c3d66-4db3-498a-8593-25c2b08e0dbc)
