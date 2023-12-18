
import cv2
from ultralytics import YOLO
import time

#ввод переменных для отслеживания FPS камеры/видео
pre_timeframe = 0
new_timeframe = 0

# импорт модели йоло
model = YOLO("ZOME.pt")

# открываем вебку
cap = cv2.VideoCapture(0)

#захват видео с видеокамеры
while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()

        #растягивание окна вывода с помощью cv2
        annotated_frame = cv2.resize(annotated_frame, (2560, 1440))

        #вывод FPS
        new_timeframe = time.time()
        fps = 1 / (new_timeframe - pre_timeframe)
        pre_timeframe = new_timeframe
        fps = int(fps)
        cv2.putText(frame, str(fps), (8, 80), cv2.FONT_HERSHEY_SIMPLEX, 3, (100, 255, 0), 4)

        #вывод обработанного видео
        cv2.imshow("YOLO Inference", annotated_frame)

        annotated_frame = cv2.resize(annotated_frame, (2560, 1440))
        #стоп ключ
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

