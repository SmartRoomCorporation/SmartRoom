import face_recognition
import numpy as np
import glob
import os,sys,inspect
import cv2


class FaceRecon:

    face_locations = []
    face_encodings = []
    known_ppl_encoding = []
    unknown_ppl_encoding = []

    def __init__(self):
        self.learnInit()

    def learnInit(self):
        known_ppl_img_files = glob.glob(self.getResDir()+"/res/known_people/*.*")
        for i in range(len(known_ppl_img_files)):
            img = face_recognition.load_image_file(known_ppl_img_files[i])
            img_encoding = face_recognition.face_encodings(img)[0]
            self.known_ppl_encoding.append(img_encoding)

    def faceRecon(self, face_encodings, known_face_encodings):
        for face_encoding in face_encodings: # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            if face_distances.size:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]: # if face is a match return the index in array passed else -1
                    return best_match_index
            else: return -1
        else:
            return -1

    def encodeUnknown(self, filename):
        unkown_images = face_recognition.load_image_file(filename)
        new_face_recon = face_recognition.face_encodings(unkown_images)
        unkown_images_encoding = []
        if len(new_face_recon) > 0:
            unkown_images_encoding = new_face_recon[0]
        return unkown_images_encoding
        
    def getResDir(self):
        current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        parent_dir = os.path.dirname(current_dir)
        dirname = os.path.dirname(parent_dir)
        return str(dirname)

    def processFrame(self, frame, process):
        if(not process): return None
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        self.face_locations = face_recognition.face_locations(rgb_small_frame)
        self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
        if(self.faceRecon(self.face_encodings, self.known_ppl_encoding) >= 0): return True, self.grantAccess(frame, self.face_locations)
        else: return False, self.denyAccess(frame, self.face_locations)

    def grantAccess(self, frame, face_locations):
        for (top, right, bottom, left) in face_locations:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "Access Granted", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        return frame

    def denyAccess(self, frame, face_locations):
        for (top, right, bottom, left) in face_locations:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "Access Deined", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        return frame
