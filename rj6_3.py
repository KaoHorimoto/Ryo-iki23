import tkinter as tk
import json
import zipfile

with zipfile.ZipFile("kabeposter.zip", "r") as zip_ref:
    zip_ref.extractall()

json_file_paths = [
    f"kabeposter/kabeposter_0000000000{i:02d}_keypoints.json" for i in range(100)
]

root = tk.Tk()
root.geometry("1400x1000")

canvas = tk.Canvas(root, width=1400, height=1000)
canvas.pack()

frames = len(json_file_paths)
joint_positions = [[[] for _ in range(25)] for _ in range(2)]

for frame, json_file_path in enumerate(json_file_paths):
    with open(json_file_path) as f:
        data = json.load(f)
    
    for i in range(2):
        positions = data["people"][i]["pose_keypoints_2d"]
        for j in range(25):
            x = positions[j * 3] / 2 + 200
            y = positions[j * 3 + 1] / 2 + 200

            joint_positions[i][j].append((x, y))

def animation(frame):
    canvas.delete("all")
    for i in range(2):
        for j in range(25):
            x, y = joint_positions[i][j][frame]
            canvas.create_oval(x-2, y-2, x+2, y+2, fill = "black")
            
        lines = [
            (2, 3), (3, 4), (5, 6), (6, 7),  # 腕
            (11, 24), (11, 22), (22, 23), (8, 9), (9, 10), (10, 11),  # 右脚
            (8, 12), (12, 13), (13, 14), (14, 21), (14, 19), (19, 20),  # 左脚
            (0, 1), (15, 17), (16, 18), (0, 16), (0, 15) ,# 首と頭部
            (1, 2),  (1, 5), (1, 8)
        ]
        
        for start, end in lines:
            x1, y1 = joint_positions[i][start][frame]
            x2, y2 = joint_positions[i][end][frame]
            canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
        
    root.after(100, lambda: animation((frame + 1) % frames))

animation(0)

root.mainloop()

