import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2


def Cartoon(image_color):
    output_image= cv2.stylization(image_color, sigma_s=100, sigma_r=0.3)
    """
    sigma_s görüntünün ne kadar düzgünleştiğini kontrol eder - değeri ne kadar büyük 
    olursa görüntü o kadar düzgünleşir, ancak hesaplaması da yavaşlar. 
    
    sigma_r görüntüyü düzeltirken kenarları korumak istediğimiz zaman çok önemlidir.
    Sadece çok benzer renklerin ortalaması alınmasına neden olur. (diğer bir deyişle pürüzsüz)
    çok farklı renkler bozulmadan kalacaktır. 
    """
    return output_image


def LiveCamEdgeDetection_canny(image_color):
    threshold_1 = 30
    threshold_2 = 80
    image_gray = cv2.cvtColor(image_color,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(image_gray, threshold_1, threshold_2)

    return canny

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    # Cap.read() reutnr a ret bool to indicate succes.

    cv2.imshow("Live Edge Detection", Cartoon(frame))
    cv2.imshow("Live Edge Detection", LiveCamEdgeDetection_canny(frame))
    cv2.imshow("Webcam Video", frame)
    if cv2.waitKey(1) == 13: # 13 Enter Key
        break

cap.release() # camera release
cv2.destroyAllWindows()