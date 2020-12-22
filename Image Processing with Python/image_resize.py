#Import  libraries
import cv2

class ImageProcessing():

    def resize(self, fname, width, height):
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

        return fname, new_image


def main():
    img = ImageProcessing()
    filename, new_image = img.resize("bird.jpg", 1280, 960)
    cv2.imshow("Resized image ",new_image)
    cv2.waitKey(0)

if __name__ == "__main__" : main()

