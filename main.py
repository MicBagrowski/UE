import cv2
import urllib
from flask import Flask
from flask_restful import Resource, Api


# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

app = Flask(__name__)
api = Api(app)

class PeopleCounter(Resource):
    def get(self):
        # load image
        image = cv2.imread('ludzie.jpg')
        image = cv2.resize(image, (700, 400))

        # detect people in the image
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

        return {'peopleCount': len(rects)}

    def get(self):
        url="https://www.shutterstock.com/pl/image-photo/happy-business-colleagues-having-discussion-over-2262759289"
        image = cv2.imread('ludzie.jpg')
        image = cv2.resize(image, (700, 400))

        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

        return {'peopleCount2': len(rects)}

api.add_resource(PeopleCounter, '/')




if __name__ == '__main__':
    app.run(debug=True)
