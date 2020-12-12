import unittest
import glob
import os,sys,inspect
import face_recognition
import cv2
import numpy as np
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)
from main.python.FaceRecon import FaceRecon

known_ppl_img_files = glob.glob(parent_dir+"/main/res/known_people/*.*")
test_negative_img_files = glob.glob(parent_dir+"/test/res/test_negative_images/*.*")
test_positive_img_files = glob.glob(parent_dir+"/test/res/test_positive_images/*.*")
known_ppl_encoding = []
test_negative_ppl_encoding = []
test_positive_ppl_encoding = []
fr = FaceRecon()

for i in range(len(known_ppl_img_files)): # known
    img = face_recognition.load_image_file(known_ppl_img_files[i])
    img_encoding = face_recognition.face_encodings(img)[0]
    known_ppl_encoding.append(img_encoding)

for i in range(len(test_negative_img_files)): # negatives
    img = cv2.imread(test_negative_img_files[i])
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    test_negative_ppl_encoding.append(face_encodings)

for i in range(len(test_positive_img_files)): # positives
    img = cv2.imread(test_positive_img_files[i])
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    test_positive_ppl_encoding.append(face_encodings)


class TestFaceRecon(unittest.TestCase):

    def testSetup(self):
        self.assertEqual(2, len(test_positive_ppl_encoding))
        self.assertEqual(1, len(test_negative_ppl_encoding))
        self.assertEqual(3, len(known_ppl_encoding))

    def testPositive(self):
        for i in range(len(test_positive_ppl_encoding)):
            self.assertGreaterEqual(fr.faceRecon(test_positive_ppl_encoding[i], known_ppl_encoding), 0)

    def testNegative(self):
        for i in range(len(test_negative_ppl_encoding)):
            self.assertEqual(-1, fr.faceRecon(test_negative_ppl_encoding[i], known_ppl_encoding))

if __name__ == '__main__':
    unittest.main()
