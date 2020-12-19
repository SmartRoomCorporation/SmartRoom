import face_recognition
import numpy as np



class FaceRecon:

    def __init__(self):
        self.face_locations = []
        self.face_encodings = []

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
        
