import os
import time

# Ask user to input directory path containing video files
directory = input("Enter directory path containing video files: ")

# Initialize a list to hold video file names and their modified times
video_files = []

# Loop through files in the directory and add video files to the list
for file_name in os.listdir(directory):
    if file_name.endswith(".mp4"):
# or file_name.endswith(".avi"):
        file_path = os.path.join(directory, file_name)
        modified_time = os.path.getmtime(file_path)
        video_files.append((file_name, modified_time))

# Sort the video files list by modified time
video_files.sort(key=lambda x: x[1])

# Loop through video files and rename them to "01.mp4", "02.mp4", etc.
for i, video_file in enumerate(video_files):
    new_file_name = f"{i+1:02d}.mp4"
    old_file_path = os.path.join(directory, video_file[0])
    new_file_path = os.path.join(directory, new_file_name)
    os.rename(old_file_path, new_file_path)
    print(f"Renamed {old_file_path} to {new_file_path}")

#softy_plug