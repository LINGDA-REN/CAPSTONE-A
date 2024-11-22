import jetson.inference
import jetson.utils


#display=jetson.utils.videoOutput("display://0")
# 加载深度学习模型
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
display = jetson.utils.videoOutput("display://0") # 你可以改为适合的输出方式
# 加载图像文件
while display.IsStreaming():
    img=jetson.utils.loadImage("/home/nvidia/Desktop/cat.58.jpg")

    if img is None:
        print("无法加载图像")
    else:
    # 进行目标检测
        detections = net.Detect(img)

    # 输出检测结果
    for detection in detections:
        class_id = detection.ClassID
        confidence = detection.Confidence
        left = detection.Left
        top = detection.Top
        right = detection.Right
        bottom = detection.Bottom
        width = detection.Width
        height = detection.Height
        area = detection.Area
        center_x = detection.Center[0]
        center_y = detection.Center[1]

    # 打印检测到的参数
    print(f"Class ID: {class_id}")
    print(f"Confidence: {confidence:.2f}")
    print(f"Left: {left:.2f}, Top: {top:.2f}, Right: {right:.2f}, Bottom: {bottom:.2f}")
    print(f"Width: {width:.2f}, Height: {height:.2f}, Area: {area:.2f}")
    print(f"Center: ({center_x:.2f}, {center_y:.2f})")

    # 在检测框上绘制边界框 - 使用 jetson.utils 的图形绘制功能
    #img = net.DrawBoundingBoxes(img, detections) # 绘制边界框

    # 使用 videoOutput 显示检测结果
    #display = jetson.utils.videoOutput("display://0") # 你可以改为适合的输出方式
    display.Render(img)
    display.SetStatus("Detecting objects...")


