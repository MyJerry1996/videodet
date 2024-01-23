# 检测前准备工作：配置环境和进入主目录

打开终端，输入：
```bash
conda activate yolov7
cd /home/zhongliankuangye/yolov7-trans/yolov7
```

# 模型地址：https://drive.google.com/file/d/1QF5QbLjAcoGLzibdWuNi85BLCnJOT2tU/view?usp=drive_link

# 检测图片

输入：
```bash
python detect.py --view-img --weights best.pt --conf 0.25 --img-size 320 --source <待测图片路径> --device 0 --name <测试项目自定义命名>
```

# 检测视频

输入：
```bash
python detect.py --view-img --weights best.pt --conf 0.25 --img-size 320 --source <待测视频路径> --device 0 --name <测试项目自定义命名>
```

# 检测视频流

输入：
```bash
python detect.py --view-img --weights best.pt --conf 0.25 --img-size 320 --source <待测视频流地址> --device 0 --name <测试项目自定义命名>
```

# 检测视频实时推流
输入：
```bash
python detect_app.py （可选）(--view-img) --weights best.pt --conf 0.25 --img-size 320 --source <待测视频流地址> --device 0 --name <测试项目自定义命名> --stream_ip <推流地址，默认0.0.0.0> --stream_port <推流端口>
```
在接收端打开浏览器，输入```http://<本地ip>:<推流端口>/stream```即可显示视频流

# 查看结果

检测过程结束后，进入 ```/home/zhongliankuangye/yolov7-trans/yolov7/runs/```下，找到对应测试项目名称文件夹，打开即为检测结果。

# 注意事项

- 先推视频流，再启动算法；
- 可将 ```--conf```后的阈值调小来减少漏检数量，调大减少误检数量；
- 若要更换不同的检测源，修改 ```--source```后的参数即可（图片、视频直接写地址，视频流支持 ```rtmp```、```rtsp```、```https```、```http```等协议）；
- 若要中途停止检测，在终端界面按```Ctrl```+```c```即可。

# 检测算法调用示例

```bash
python detect.py --view-img --weights best.pt --conf 0.25 --img-size 320 --source rtsp://111.39.110.124:554/6278E501-03C4-0000-8D15-EB38A153E9C5/stream2 --device 0 --name test
```

```bash
python detect_app.py --weights best.pt --conf 0.25 --img-size 320 --source 23331.mp4 --device 0 --name test_stream
```
