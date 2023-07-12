import json
import zipfile

zip_file_path = "kabeposter.zip"

with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    zip_ref.extractall()

json_file_path = "kabeposter/kabeposter_000000000000_keypoints.json"

with open(json_file_path, "r") as file:
    data = json.load(file)

# 2人の人の情報を取得
people_data = data["people"]
person1, person2 = people_data[0], people_data[1]

# 0フレーム目の鼻と首の情報を取得 
nose_x, nose_y, nose_confidence = person1["pose_keypoints_2d"][:3] #リストの最初から3つの要素を取得
neck_x, neck_y, neck_confidence = person1["pose_keypoints_2d"][3:6] #リストの3番目から6番目の要素を取得

print("Person1")
print("Nose  X:", nose_x, "Y:", nose_y, "Confidence:", nose_confidence)
print("Neck  X:", neck_x, "Y:", neck_y, "Confidence:", neck_confidence)


nose_x, nose_y, nose_confidence = person2["pose_keypoints_2d"][:3]
neck_x, neck_y, neck_confidence = person2["pose_keypoints_2d"][3:6]

print("\nPerson2")
print("Nose  X:", nose_x, "Y:", nose_y, "Confidence:", nose_confidence)
print("Neck  X:", neck_x, "Y:", neck_y, "Confidence:", neck_confidence)