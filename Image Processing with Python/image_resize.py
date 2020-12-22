#Import  libraries
import cv2
import  numpy as np
import sys
import os
import fnmatch

class ImageProcessing():

    def resize(fname, width, height):
        image = cv2.imread(fname)
        cv2.imshow("Original image ",image)
        cv2.waitKey(0)
        org_height, org_width = image.shape[0:2]
        print("Width: ", org_width)
        print("Height ", org_height)

        if org_width >= org_height:
            new_image = cv2.resize(image, (width, height))
        else:
            new_image = cv2.resize(image, (height,width))

        cv2.imshow("Resized image ",new_image)
        cv2.waitKey(0)
        
        return fname, new_image
    
    def blur(fname):
        image = cv2.imread(fname)
        kernels = [3, 5, 9, 13]
        for idx, k in enumerate(kernels):
            image_bl = cv2.blur(image, ksize =(k, k))
            cv2.imshow(str(k), image_bl)
            cv2.waitKey(0)

        return fname,image_bl
    
    def sharpen(fname):
        image2 = cv2.imread(fname)
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        image_sharpen = cv2.filter2D(src=image2, ddepth= -1, kernel= kernel)
        cv2.imshow("Sharpened",image_sharpen)
        cv2.waitKey(0)
        
        return fname, image_sharpen
    
    def batch_process(self):
        listofFiles = os.listdir(".")
        pattern = "*.jpg"
        n = len(sys.argv)
        
        if n == 3:
            width = int(sys.argv[1])
            height = int(sys.argv[2])

        else:
            width = 1280
            height = 960

        if not os.path.exists("resize"):
            os.makedirs("resize")
        
        if not os.path.exists("blur"):
            os.makedirs("blur")
        
        if not os.path.exists("sharpen"):
            os.makedirs("sharpen")
        

        for filename in listofFiles:
            if fnmatch.fnmatch(filename, pattern):
                filename, new_image = ImageProcessing.resize(filename, width, height)
                cv2.imwrite("resize\\" + filename, new_image)
        

        for filename in listofFiles:
            if fnmatch.fnmatch(filename, pattern):
                filename2, new_image2 = ImageProcessing.blur(filename)
                cv2.imwrite("blur\\" + filename2, new_image2)
        

        for filename in listofFiles:
            if fnmatch.fnmatch(filename, pattern):
                filename3, new_image3 = ImageProcessing.sharpen(filename)
                cv2.imwrite("sharpen\\" + filename3, new_image3)


def main():
    img = ImageProcessing()
    img.batch_process()
    

if __name__ == "__main__" : 
    main()

