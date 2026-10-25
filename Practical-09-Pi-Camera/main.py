from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from time import sleep

def main():
    camera = Picamera2()
    try:
        camera.configure(camera.create_still_configuration())
        camera.start()
        sleep(2)
        camera.capture_file("captured_image.jpg")
        camera.stop()
        print("Image captured.")
        camera.configure(camera.create_video_configuration())
        camera.start_recording(H264Encoder(), "captured_video.h264")
        try:
            sleep(10)
        finally:
            camera.stop_recording()
        print("Video recorded.")
    finally:
        camera.close()

if __name__ == "__main__":
    main()
