import os
def convert_avi_to_mp4(avi_file_path, output_name):
  os.popen("ffmpeg -i '{input}' -ac 2 -b:v "
           "2000k -c:a aac -c:v libx264 -b:a "
           "160k -vprofile high -bf 0 -strict experimental "
           "-f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
  return True


path="alphapose-video1/AlphaPose-video1.avi"
path2="alphapose-video1/AlphaPose-video1.mp4"
convert_avi_to_mp4(path, path2)
