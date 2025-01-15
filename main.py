import cv2
import mediapipe as mp
import numpy as np

def load_obj(filename):
    vertices = []
    faces = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertices.append(list(map(float, line.strip().split()[1:4])))
            elif line.startswith('f '):
                face = line.strip().split()[1:4]
                face = [int(face[i].split('/')[0]) - 1 for i in range(3)]
                faces.append(face)
    return np.array(vertices), np.array(faces)

def project_3d_to_2d(vertices, translation, scale, frame_shape):
    h, w = frame_shape[:2]
    projection_matrix = np.array([
        [scale, 0, 0, 0],
        [0, -scale, 0, 0],  # Flipping along y-axis
        [0, 0, 1, 0]
    ])
    vertices_homogeneous = np.hstack([vertices, np.ones((vertices.shape[0], 1))])
    vertices_transformed = vertices_homogeneous @ projection_matrix.T
    vertices_2d = vertices_transformed[:, :2]
    vertices_2d[:, 0] += w // 2 + translation[0]
    vertices_2d[:, 1] += h // 2 + translation[1]  # Adjusting the y-translation
    return vertices_2d.astype(np.int32)

def render_model(frame, vertices_2d, faces):
    for face in faces:
        pts = vertices_2d[face]
        cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=1)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

NOSE_BRIDGE = 5
LEFT_TEMPLE = 162
RIGHT_TEMPLE = 389

vertices, faces = load_obj('oculos.obj')  # Replace 'oculos.obj' with your .obj file path

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            nose_bridge_coords = face_landmarks.landmark[NOSE_BRIDGE]
            left_temple_coords = face_landmarks.landmark[LEFT_TEMPLE]
            right_temple_coords = face_landmarks.landmark[RIGHT_TEMPLE]

            h, w, _ = frame.shape
            nose_bridge_x, nose_bridge_y = int(nose_bridge_coords.x * w), int(nose_bridge_coords.y * h)
            left_temple_x, left_temple_y = int(left_temple_coords.x * w), int(left_temple_coords.y * h)
            right_temple_x, right_temple_y = int(right_temple_coords.x * w), int(right_temple_coords.y * h)

            translation = [(left_temple_x + right_temple_x) // 2 - w // 2, (nose_bridge_y + left_temple_y + right_temple_y) // 3 - h // 2, 0]
            scale = (right_temple_x - left_temple_x) / np.max(vertices[:, 0] - np.min(vertices[:, 0]))

            vertices_2d = project_3d_to_2d(vertices, translation, scale, frame.shape)
            render_model(frame, vertices_2d, faces)

    cv2.imshow('Face with 3D Model', frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
