import face_recognition
import os, sys
import cv2
import numpy as np
import math


def face_confidence(face_dist, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    lin_val = (1.0 - face_dist) / (range * 2.0)

    if face_dist > face_match_threshold:
        return str(round(lin_val * 100, 2)) + '%'
    else:
        value = (lin_val + ((1.0 - lin_val) * math.pow((lin_val - 0.5) * 2, 0.2)))
        return str(round(value, 2)) + '%'