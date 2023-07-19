import json
import zipfile
import tkinter as tk

with zipfile.ZipFile("kabeposter.zip", "r") as zip_ref:
    zip_ref.extractall()

json_file_path = "kabeposter/kabeposter_000000000000_keypoints.json"

with open(json_file_path, "r") as file:
    data = json.load(file)

people_data=data["people"]
person1 = people_data[0]
person2 = people_data[1]

root = tk.Tk()
root.geometry("1300x800")

canvas = tk.Canvas(root, width=1300, height=800)
canvas.pack()

right_shoulder_x = person1["pose_keypoints_2d"][6]
right_shoulder_y = person1["pose_keypoints_2d"][7]
left_shoulder_x = person1["pose_keypoints_2d"][15]
left_shoulder_y = person1["pose_keypoints_2d"][16]
neck_x = person1["pose_keypoints_2d"][3]
neck_y = person1["pose_keypoints_2d"][4]

canvas.create_line(neck_x, neck_y, right_shoulder_x, right_shoulder_y, fill = "red", width=2)
canvas.create_line(neck_x, neck_y, left_shoulder_x, left_shoulder_y, fill = "red", width=2)

right_shoulder_x = person2["pose_keypoints_2d"][6]
right_shoulder_y = person2["pose_keypoints_2d"][7]
left_shoulder_x = person2["pose_keypoints_2d"][15]
left_shoulder_y = person2["pose_keypoints_2d"][16]
neck_x = person2["pose_keypoints_2d"][3]
neck_y = person2["pose_keypoints_2d"][4]

canvas.create_line(neck_x, neck_y, right_shoulder_x, right_shoulder_y, fill = "black", width=2)
canvas.create_line(neck_x, neck_y, left_shoulder_x, left_shoulder_y, fill = "black", width=2)

root.mainloop()