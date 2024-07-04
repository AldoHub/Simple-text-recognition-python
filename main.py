import cv2
import easyocr
import matplotlib.pyplot as ptl

#read the image
image_path = '<full_image_path>'
image = cv2.imread(image_path)

#text detector
reader = easyocr.Reader(['en'], gpu=False)

#detect text on image
text_read = reader.readtext(image)
threshold = 0.75
#print(text_reader)

#loop and grab the data from the text reader response
for t in text_read:
    bbox, text, score = t

    if score > threshold:
        #draw a rectangle using the bbox to-left and bottom-right values
        cv2.rectangle(image, bbox[0], bbox[2], (255, 0, 0), 5)
        cv2.putText(image, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,0,0), 2)

ptl.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGBA))
ptl.show()    