from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def trimAndCompressVideo(inputPath, outputPath, startTime = 0, endTime = 10, bitrate = "1500k"):

    _, inputExtension = os.path.splitext(inputPath)
    videoClip   = VideoFileClip(inputPath)
    trimmedClip = videoClip.subclip(startTime, endTime)

    outputFormat = "mp4"

    _, outputExtension = os.path.splitext(outputPath)
    if outputExtension.lower() != '.mp4':
        outputPath = os.path.splitext(outputPath)[0] + ".mp4"

    trimmedClip.write_videofile(outputPath, codec = "libx264", audio_codec = "aac", bitrate = bitrate)

    videoClip.close()
    trimmedClip.close()

if __name__ == "__main__":
    inputVideoPath  = "input-video.mp4"
    outputVideoPath = "output-video.mp4"

    #You can pass startTime and setTime while calling the function trimAndCompressVideo(inputVideoPath, outputVideoPath, startTime = 10, endTime = 20)
    trimAndCompressVideo(inputVideoPath, outputVideoPath)

