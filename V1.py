import cv2
import socket

# กำหนดขนาดของหน้าต่างเกี่ยวกับภาพ
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# กำหนด IP และ Port ของเครื่องที่จะรับภาพ
RECEIVER_IP = '192.168.1.100'
RECEIVER_PORT = 12345

# สร้าง socket object สำหรับส่งข้อมูลภาพ
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((RECEIVER_IP, RECEIVER_PORT))

cap = cv2.VideoCapture(0)

cv2.namedWindow('Sender', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Sender', WINDOW_WIDTH, WINDOW_HEIGHT)

# วน loop เพื่ออ่านภาพจากการ์ดวีดีโอและส่งไปยังเครื่องอื่น
while True:
    # อ่านภาพจากการ์ดวีดีโอ
    ret, frame = cap.read()

    # เขียนภาพเป็น byte array และส่งไปยังเครื่องอื่น
    data = cv2.imencode('.jpg', frame)[1].tostring()
    s.sendall((str(len(data))).encode().ljust(16) + data)

    # รอรับข้อมูลการตอบกลับจากเครื่องอื่น
    reply = s.recv(1024)

    # แสดงภาพบนหน้าต่าง 'Camera' และรอการกด 'q' เพื่อจบโปรแกรม
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# ปิดการทำงานของการ์ดวีดีโอและหน้าต่าง 'Camera'
cap.release()
cv2.destroyAllWindows()
