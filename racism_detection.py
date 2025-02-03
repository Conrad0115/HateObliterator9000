import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

MIN_MATCH_COUNT = 10

if __name__ == '__main__':
    racist_img = cv.imread('racistpics/racist_7.png', cv.IMREAD_GRAYSCALE)
    uscoa = cv.imread('racistpics/racist_12.png', cv.IMREAD_GRAYSCALE)


    sift = cv.SIFT_create()
    kp1, des1 = sift.detectAndCompute(racist_img,None)
    kp2, des2 = sift.detectAndCompute(uscoa,None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)

    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()
    
        h,w = racist_img.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv.perspectiveTransform(pts,M)
    
        uscoa = cv.polylines(uscoa,[np.int32(dst)],True,255,3, cv.LINE_AA)
 
    else:
        print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
        matchesMask = None

    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)
 
    img3 = cv.drawMatches(racist_img,kp1,uscoa,kp2,good,None,**draw_params)
 
    plt.savefig('img.png')
