import json
import math

# Function to calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2 + (point1.z - point2.z)**2)

# Function to calculate angle using law of cosines
def calculate_angle(a, b, c):
    """Calculate angle using law of cosines."""
    return math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

# OriginalImg class
class OriginalImg:  # self as parameter to be used outside the class, self.x allows this attribute to persist beyond init method(check)
    def __init__(self, x, y, z, confidence):
        self.x = x
        self.y = y
        self.z = z
        self.confidence = confidence

   # def __repr__(self): goes here
      

# NewImg class
class NewImg:  # Same parameters as OriginalImg for compatibility with the JSON format
    def __init__(self, x, y, z, confidence):
        self.x = x
        self.y = y
        self.z = z
        self.confidence = confidence

   # def __repr__(self): debug goes here
       
"""json file for OriginalImg"""

with open('OriginalImg.json', 'r') as f:  # 'r' is for read mode to tell python
    # Returns JSON object as a dictionary
    original_data = json.load(f)  # convert into python object(dictionary)

# Create instances of OriginalImg for key points
right_shoulder_original = OriginalImg(*original_data["Right_shoulder"])# "right_shoulder" is the key in the json file and it accesses it from the json file
right_hip_original = OriginalImg(*original_data["Right_hip"])# *original_data Unpacks list into separate arguments so you dont have to do it manually and can access it as a variable

right_knee_original = OriginalImg(*original_data["Right_knee"])
right_ankle_original = OriginalImg(*original_data["Right_ankle"])
right_elbow_original = OriginalImg(*original_data["Right_elbow"])
right_wrist_original = OriginalImg(*original_data["Right_wrist"])
right_foot_index_original = OriginalImg(*original_data["Right_foot_index"])

"""OriginalImg calculations"""

# Knee Joint Calculations of OriginalImg
distance_hip_knee_original = calculate_distance(right_hip_original, right_knee_original)  # Side S OriginalImg calcualtes the distance by giving the two arguements right_hip and right_knee to point 1 and point 2 to use the function
distance_knee_ankle_original = calculate_distance(right_knee_original, right_ankle_original)  # Side T OriginalImg
distance_hip_ankle_original = calculate_distance(right_hip_original, right_ankle_original)  # Side U OriginalImg
knee_angle_original = calculate_angle(distance_hip_knee_original, distance_knee_ankle_original, distance_hip_ankle_original)

# Hip Joint Calculations of OriginalImg
distance_shoulder_hip_original = calculate_distance(right_shoulder_original, right_hip_original)  # Side A OriginalImg
distance_shoulder_knee_original = calculate_distance(right_shoulder_original, right_knee_original)  # Side C OriginalImg
hip_angle_original = calculate_angle(distance_shoulder_hip_original, distance_hip_knee_original, distance_shoulder_knee_original)

# Elbow Joint Calculations of OriginalImg
distance_shoulder_elbow_original = calculate_distance(right_shoulder_original, right_elbow_original)  # Side P OriginalImg
distance_elbow_wrist_original = calculate_distance(right_elbow_original, right_wrist_original)  # Side Q OriginalImg
distance_shoulder_wrist_original = calculate_distance(right_shoulder_original, right_wrist_original)  # Side R OriginalImg
elbow_angle_original = calculate_angle(distance_shoulder_elbow_original, distance_elbow_wrist_original, distance_shoulder_wrist_original)

# Ankle Joint Calculations of OriginalImg
distance_knee_ankle_original = calculate_distance(right_knee_original, right_ankle_original)  # Side X OriginalImg
distance_ankle_foot_index_original = calculate_distance(right_ankle_original, right_foot_index_original)  # Side Y OriginalImg
distance_knee_foot_index_original = calculate_distance(right_knee_original, right_foot_index_original)  # Side Z OriginalImg
ankle_angle_original = calculate_angle(distance_knee_ankle_original, distance_ankle_foot_index_original, distance_knee_foot_index_original)

"""Print results of OriginalImg"""

# Print Results of OriginalImg( distances are 4 decimal places and angles are 2 decimal places)
print("Original Image Joint Measurements:\n")
print("\nKnee Joint:\n")
print(f"  Side S (Right Hip to Right Knee): {distance_hip_knee_original:.4f}")# roudn to 4 decimal places and f makes it a decimal value
print(f"  Side T (Right Knee to Right Ankle): {distance_knee_ankle_original:.4f}")# f string formatting so {}
print(f"  Side U (Right Hip to Right Ankle): {distance_hip_ankle_original:.4f}")
print(f"  Knee Angle (between Right Hip and Right Ankle): {knee_angle_original:.2f} degrees\n")

print("Hip Joint:\n")
print(f"  Side A (Right Shoulder to Right Hip): {distance_shoulder_hip_original:.4f}")
print(f"  Side B (Right Hip to Right Knee): {distance_hip_knee_original:.4f}")
print(f"  Side C (Right Shoulder to Right Knee): {distance_shoulder_knee_original:.4f}")
print(f"  Hip Angle (between Right Shoulder and Right Knee): {hip_angle_original:.2f} degrees\n")

print("Elbow Joint:\n")
print(f"  Side P (Right Shoulder to Right Elbow): {distance_shoulder_elbow_original:.4f}")
print(f"  Side Q (Right Elbow to Right Wrist): {distance_elbow_wrist_original:.4f}")
print(f"  Side R (Right Shoulder to Right Wrist): {distance_shoulder_wrist_original:.4f}")
print(f"  Elbow Angle: {elbow_angle_original:.2f} degrees\n")

print("Ankle Joint:\n")
print(f"  Side X (Right Knee to Right Ankle): {distance_knee_ankle_original:.4f}")
print(f"  Side Y (Right Ankle to Right Foot Index): {distance_ankle_foot_index_original:.4f}")
print(f"  Side Z (Right Knee to Right Foot Index): {distance_knee_foot_index_original:.4f}")
print(f"  Ankle Angle (between Right Knee and Right Foot Index): {ankle_angle_original:.2f} degrees")

"""json file for NewImg"""

with open('NewImg.json', 'r') as f:  # 'r' is for read mode to tell python
    # Returns JSON object as a dictionary
    new_data = json.load(f)  # convert into python object

# Create instances of NewImg for key points
right_shoulder_new = NewImg(*new_data["Right_shoulder"])# to use the jsons' now list to get the dat for right shoulder
right_hip_new = NewImg(*new_data["Right_hip"])# *new_data Unpacks list into separate arguments so you dont have to do it manually and can access it as a variable
right_knee_new = NewImg(*new_data["Right_knee"])
right_ankle_new = NewImg(*new_data["Right_ankle"])
right_elbow_new = NewImg(*new_data["Right_elbow"])
right_wrist_new = NewImg(*new_data["Right_wrist"])
right_foot_index_new = NewImg(*new_data["Right_foot_index"])

"""NewImg calculations"""

# Knee Joint Calculations of NewImg
distance_hip_knee_new = calculate_distance(right_hip_new, right_knee_new)  # Side S NewImg
distance_knee_ankle_new = calculate_distance(right_knee_new, right_ankle_new)  # Side T NewImg
distance_hip_ankle_new = calculate_distance(right_hip_new, right_ankle_new)  # Side U NewImg
knee_angle_new = calculate_angle(distance_hip_knee_new, distance_knee_ankle_new, distance_hip_ankle_new)

# Hip Joint Calculations of NewImg
distance_shoulder_hip_new = calculate_distance(right_shoulder_new, right_hip_new)  # Side A NewImg
distance_shoulder_knee_new = calculate_distance(right_shoulder_new, right_knee_new)  # Side C NewImg
hip_angle_new = calculate_angle(distance_shoulder_hip_new, distance_hip_knee_new, distance_shoulder_knee_new)

# Elbow Joint Calculations of NewImg
distance_shoulder_elbow_new = calculate_distance(right_shoulder_new, right_elbow_new)  # Side P NewImg
distance_elbow_wrist_new = calculate_distance(right_elbow_new, right_wrist_new)  # Side Q NewImg
distance_shoulder_wrist_new = calculate_distance(right_shoulder_new, right_wrist_new)  # Side R NewImg
elbow_angle_new = calculate_angle(distance_shoulder_elbow_new, distance_elbow_wrist_new, distance_shoulder_wrist_new)

# Ankle Joint Calculations of NewImg
distance_knee_ankle_new = calculate_distance(right_knee_new, right_ankle_new)  # Side X NewImg
distance_ankle_foot_index_new = calculate_distance(right_ankle_new, right_foot_index_new)  # Side Y NewImg
distance_knee_foot_index_new = calculate_distance(right_knee_new, right_foot_index_new)  # Side Z NewImg
ankle_angle_new = calculate_angle(distance_knee_ankle_new, distance_ankle_foot_index_new, distance_knee_foot_index_new)

"""Print results of NewImg"""

# Print Results of NewImg( distances are 4 decimal places and angles are 2 decimal places)
print("\n\nNew Image Joint Measurements:")
print("\nYour Knee Joint:\n")
print(f"  Side S (Right Hip to Right Knee): {distance_hip_knee_new:.4f}")# f string formatting so {}
print(f"  Side T (Right Knee to Right Ankle): {distance_knee_ankle_new:.4f}")
print(f"  Side U (Right Hip to Right Ankle): {distance_hip_ankle_new:.4f}")
print(f"  Knee Angle (between Right Hip and Right Ankle): {knee_angle_new:.2f} degrees\n")

print("Your Hip Joint:\n")
print(f"  Side A (Right Shoulder to Right Hip): {distance_shoulder_hip_new:.4f}")
print(f"  Side B (Right Hip to Right Knee): {distance_hip_knee_new:.4f}")
print(f"  Side C (Right Shoulder to Right Knee): {distance_shoulder_knee_new:.4f}")
print(f"  Hip Angle (between Right Shoulder and Right Knee): {hip_angle_new:.2f} degrees\n")

print("Your Elbow Joint:\n")
print(f"  Side P (Right Shoulder to Right Elbow): {distance_shoulder_elbow_new:.4f}")
print(f"  Side Q (Right Elbow to Right Wrist): {distance_elbow_wrist_new:.4f}")
print(f"  Side R (Right Shoulder to Right Wrist): {distance_shoulder_wrist_new:.4f}")
print(f"  Elbow Angle: {elbow_angle_new:.2f} degrees\n")

print("Your Ankle Joint:\n")
print(f"  Side X (Right Knee to Right Ankle): {distance_knee_ankle_new:.4f}")
print(f"  Side Y (Right Ankle to Right Foot Index): {distance_ankle_foot_index_new:.4f}")
print(f"  Side Z (Right Knee to Right Foot Index): {distance_knee_foot_index_new:.4f}")
print(f"  Ankle Angle (between Right Knee and Right Foot Index): {ankle_angle_new:.2f} degrees")

knee_angle_dif = (knee_angle_new - knee_angle_original)
hip_angle_dif = (hip_angle_new - hip_angle_original)
elbow_angle_dif = (elbow_angle_new - elbow_angle_original)
ankle_angle_dif = (ankle_angle_new - ankle_angle_original)

# positive dif means the new angle is greater than the original angle
# negative dif means the new angle is less than the original angle
# range is -10 to 10 degrees for acceptable range

if knee_angle_dif < -10:
    print(f"\n{knee_angle_dif}\n Your knee angle is too narrow.Please extend your knee more.\n")
elif knee_angle_dif > 10:
    print(f"\n {knee_angle_dif}\n Your knee angle is too wide. Please bend your knee more.\n")
else:
    print(f"\n {knee_angle_dif}\n Your knee angle is within the acceptable range.\n")

if hip_angle_dif < -10:
    print(f"\n {hip_angle_dif}\n Your hip angle is too narrow. Please extend your hip more.\n")
elif hip_angle_dif > 10:
    print(f"\n {hip_angle_dif}\n Your hip angle is too wide. Please bend your hip more.\n")
else:
    print(f"\n {hip_angle_dif}\n Your hip angle is within the acceptable range.\n")

if elbow_angle_dif < -10:
    print(f"\n {elbow_angle_dif}\n Your elbow angle is too narrow. Please extend your elbow more.\n")
elif elbow_angle_dif > 10:
    print(f"\n {elbow_angle_dif}\n Your elbow angle is too wide. Please bend your elbow more.\n")
else:
    print(f"\n {elbow_angle_dif}\n Your elbow angle is within the acceptable range.\n")

if ankle_angle_dif < -10:
    print(f"\n {ankle_angle_dif}\n Your ankle angle is too narrow. Please extend your ankle more.\n")
elif ankle_angle_dif > 10:
    print(f"\n {ankle_angle_dif}\n Your ankle angle is too wide. Please bend your ankle more.\n")
else:
    print(f"\n {ankle_angle_dif}\n Your ankle angle is within the acceptable range.\n")

# TODO: for original image- might need to change it to an image of you and then keep the camera angle consistent
# debuggging-
# """String representation for debugging."""
       # return f"OriginalImg(x={self.x:.6f}, y={self.y:.6f}, z={self.z:.6f}, confidence={self.confidence:.6f})"

# commands to execute in terminal- 

#  cd /Users/rishabh/TennisFeedback/TennisFeedback/code/
#  python3 InterpretJson.py