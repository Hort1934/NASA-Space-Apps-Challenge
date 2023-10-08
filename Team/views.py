# Ваш views.py
from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import VideoFile
import cv2
from analyze_video import track_objects
from sort_tracking import SortTracker


def process_video(video_path):
    visualize = True
    video_w = 960
    video_h = 540
    video_cap = cv2.VideoCapture(video_path)
    if not video_cap.isOpened():
        return None

    tracked_objects = {}
    tracker = SortTracker()
    frames_to_go_static = 150
    result_frames = []  # Створимо список для збереження всіх кадрів результуючого відео
    while True:
        ret, frame = video_cap.read()
        if not ret:
            break

        objects, visualized_frame = track_objects(frame, video_w, video_h, tracked_objects, tracker, visualize=True)
        result_frames.append(visualized_frame)  # Додаємо кадр до списку

        if visualize:
            cv2.imshow("Visualization", visualized_frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    video_cap.release()
    cv2.destroyAllWindows()
    return result_frames


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = form.cleaned_data['video_file']
            video_path = 'videos/' + video_file.name
            with open(video_path, 'wb') as destination:
                for chunk in video_file.chunks():
                    destination.write(chunk)

            result_frames = process_video(video_path)
            if result_frames is not None:
                # Збережемо всі кадри як новий відеофайл
                output_video_path = 'media/results/result_video.mp4'
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(output_video_path, fourcc, 25.0, (960, 540))
                for frame in result_frames:
                    out.write(frame)
                out.release()

                return render(request, 'result.html',
                              {'video_file': video_file, 'output_video_path': output_video_path})
            else:
                return render(request, 'error.html', {'message': "Error processing the video."})
    else:
        form = VideoForm()
    return render(request, 'upload.html', {'form': form})
