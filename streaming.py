import cv2

import threading
from flask import Flask, Response

app = Flask(__name__)
# camera = cv2.VideoCapture(0)  # 0表示默认摄像头

def generate_frames():
    
    output_width = 640
    output_height = 480
    fps = 30

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'FLV1')
    out = cv2.VideoWriter('output.flv', fourcc, fps, (output_width, output_height))
    while True:
        success, frame = cap.read()
        if not success:
            break
        out.write(frame)
        cv2.imshow('Video Stream', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            break
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
        

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# def main():

#     # 设置输出视频流的参数
#     output_width = 640
#     output_height = 480
#     fps = 30

#     # 创建 VideoWriter 对象，指定输出文件名、FourCC编码、帧率和分辨率
#     fourcc = cv2.VideoWriter_fourcc(*'FLV1')
#     out = cv2.VideoWriter('output.avi', fourcc, fps, (output_width, output_height))

#     # 打开摄像头
#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()  # 读取一帧
#         if not ret:
#             break

#         # 在帧上进行处理，这里只是简单地将帧写入输出
#         out.write(frame)

#         cv2.imshow('Video Stream', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break


#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()

    

# if __name__ == "__main__":
#     main()