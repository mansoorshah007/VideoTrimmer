from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def trimAndCompressVideo(inputPath, outputPath, startTime = 0, endTime = 10, bitrate = "1500k"):
    _, inputExtension = os.path.splitext(inputPath)
    videoClip = VideoFileClip(inputPath)

    # Check if endTime exceeds the video duration
    if endTime > videoClip.duration:
        print("Error: endTime exceeds the duration of the video.")
        videoClip.close()
        return

    trimmedClip  = videoClip.subclip(startTime, endTime)
    outputFormat = "mp4"

    _, outputExtension = os.path.splitext(outputPath)
    if outputExtension.lower() != '.mp4':
        outputPath = os.path.splitext(outputPath)[0] + ".mp4"

    trimmedClip.write_videofile(outputPath, codec = "libx264", audio_codec = "aac", bitrate = bitrate)

    videoClip.close()
    trimmedClip.close()

if __name__ == "__main__":
    inputVideoPath  = "video-12.avi"
    outputVideoPath = "output-video.mp4"

    # You can pass startTime and endTime while calling the function
    trimAndCompressVideo(inputVideoPath, outputVideoPath, startTime = 5, endTime = 15)

