from FaceRecon import FaceRecon
import face_recognition
import cv2
import numpy as np
from pprint import pprint
import glob
import os
from pathlib import Path



dirname = Path(os.path.dirname(__file__)).parent
known_ppl_img_files = glob.glob(str(dirname)+"/res/known_people/*.*")

known_ppl_encoding = []
unknown_ppl_encoding = []

for i in range(len(known_ppl_img_files)):
    img = face_recognition.load_image_file(known_ppl_img_files[i])
    img_encoding = face_recognition.face_encodings(img)[0]
    known_ppl_encoding.append(img_encoding)




# Initialize some variables
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_locations = []
face_encodings = []
face_names = []
face_recon = FaceRecon()
process_this_frame = True
count = 0
access = False

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    if process_this_frame:
        match_index = face_recon.faceRecon(face_encodings, known_ppl_encoding)
        if match_index >= 0:
              access = True              
        else:
            access = False
            match_index = face_recon.faceRecon(face_encodings, unknown_ppl_encoding)
            if match_index < 0:
                filename = str(dirname)+'/res/unknown_people/unknown'+str(count)+'.jpg' 
                cv2.imwrite(filename, frame)
                unkown_images_encoding = face_recon.encodeUnknown(filename)
                if len(unkown_images_encoding) > 0:
                    unknown_ppl_encoding.append(unkown_images_encoding)
                    count = count + 1

    process_this_frame = not process_this_frame
    
    for (top, right, bottom, left) in face_locations:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        if access:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "Access Granted", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "Access Deined", (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()