# SmartTennis: AI Driven Tennis Feedback

## Abstract

Tennis is an enjoyable and competitive sport that requires proper technique, skill, and physical fitness. Regardless of one’s skills in tennis, coaching is needed to continue improving. Coaches provide tennis players with feedback on their tennis strokes, footwork drills, and general motivation. However, a coach cannot be present at every practice or match of their students to provide feedback. Even with a coach, a player’s technique cannot fully be monitored due to the distance between a player and a coach.

Enter SmartTennis: a tennis system that provides instant feedback to a tennis player so they can improve no matter where they are and immediately after a shot. By capturing videos, SmartTennis offers feedback 24/7 allowing tennis players to fix their technique instantly right when they make a mistake. This feedback can be sent audibly while a player is practicing or can be viewed at every break. This flexibility allows tennis players to receive feedback during practice sessions (immediately) and view it during break times in official tennis matches. By using automatic analysis over manual analysis, players do not have to depend on a coach for their feedback and will always have the feedback stored on a device to view later.

## Introduction

Tennis shot analysis is critical for consistent improvement. A single shot can determine the result of an entire match, so analyzing every shot is important. Automatic tennis feedback is currently still in development, and the most advanced technologies are only used by professional tennis players. However, post-shot analysis can help players of all skill levels improve, and my goal is to make this more accessible to a bigger audience.

As a tennis player myself, I only have access to a coach once per week. The rest of the practices and matches I play on my own. The goal of this project is to eventually create a tennis system that provides post-shot feedback for tennis players. While the prominent competitor SwingVision uses advanced technology to provide feedback, their feedback is more about ball placement and consists of short video replays. The problem is that players can only view this feedback after they finish a session or game. In a match, it is pointless to view feedback after losing. Instead, receiving feedback during play or break times allows for on-the-spot improvement.

## Project Overview and Implementation

### Functional Requirements

1. Player Position Mapping: Map players' positions precisely using open-source position mapping AI.  
2. Determining Important Joints / Calculation: Decide what ratios, angles, and lengths are important for good tennis technique and how to calculate these values and compare them to a professional player's precise positioning.  
3. User Receives Feedback: Send the feedback to the user so they can easily interpret and improve.

### 1. Player Position Mapping

Player position mapping is very complex and data-intensive to develop from scratch. The model needed to input videos and images, producing outputs easy for code integration. After researching open-source pose estimation models, I found OpenPose—a complex model developed by Carnegie Mellon students for full body position mapping. Due to its complexity, installation, and integration difficulties, it was hard to install OpenPose on my device and add my own algorithms.

I decided to look for a user-friendly website using similar models but easier to integrate into my code. This led to Saiwa AI. Saiwa AI offers many AI and ML services, including pose estimation. Saiwa AI’s ‘Pose Estimation’ uses OpenPose and MediaPipe, two deep learning frameworks for full-body position estimation. Saiwa AI takes images and videos as inputs and outputs the locations of any recognized joints and body components.

Once an image is processed, Saiwa AI returns:  
- A new image of a player’s position mapped,  
- A coordinate plane of the x, y, z positions of certain body parts (plot),  
- Most importantly, a JSON file including every body part organized in separate dictionaries.

### Example of a Dictionary for the “Nose” Body Part

- 0.60 represents the X value of the nose joint (between 0-1; larger x means more to the right in the image).  
- 0.23 represents the Y value (between 0-1; smaller y means closer to the top of the image).  
- -0.37 represents the Z value (between -1 and 1; -1 is closest to the camera, 1 is farthest).  
- 0.99 represents the confidence score (between 0-1; closer to 1 means higher confidence in detection).

### 2. Determining Important Joints / Calculation

With access to accurate position mapping, I decided which joints are most important for tennis players, starting with the ready position. I found a professional ready position image to serve as the reference for comparison against user input images.

The ready position requires good hip, elbow, knee, and ankle positions to ensure good technique. I calculated distances between certain joints and the angles formed by these distances.

To calculate distances in 3D space, I used the Euclidean distance formula because the regular distance formula does not work in 3D.

After finding distances, I calculated angles using the Law of Cosines, which uses side lengths to find the central angle.

By applying the `calculate_distance` function for two joints and then inputting these distances into the `calculate_angle` function, I obtained angles for the vital joints. I subtracted the user’s angle values from the reference image values to see deviations.

Since natural variation is expected, I added a 10-degree buffer, so if the user’s angles fall within plus or minus 10 degrees of the reference, they are considered acceptable.

### 3. User Receives Feedback

Feedback is initially printed to the terminal and later converted to audible feedback for users wearing headphones during practice or matches. This is the last step, delivering feedback once it is determined.

## Overall Code Structure

The project consists of three files: two JSON files and one Python file.

- **OriginalImg.json:** Provided by Saiwa AI, it contains body joint locations for the reference image, with dictionaries storing x, y, z, and confidence values for 34 joints. No modifications were made so reference images can be changed easily by replacing dictionary values without altering the Python code.

- **NewImg.json:** A new image analyzed by Saiwa AI producing a similar JSON output format. No changes were made for compatibility with the rest of the code.

- **InterpretJson.py:** This Python backend handles computing distances, angles, and stores variables and dictionaries to generate feedback.

### Global Function Definitions

- `calculate_distance`: Calculates the 3D distance between any two points.  
- `calculate_angle`: Returns the central angle given the side lengths, using the Law of Cosines.

### Classes and Reference to JSON Files

Two classes (`OriginalImg` and `NewImg`) calculate lengths and angles for reference and input images respectively. They accept x, y, z, and confidence as arguments to maintain compatibility with the JSON structure.

When loading the JSON files, arrays are converted to Python lists and stored in dictionaries (`original_data` and `new_data`), which then feed into their respective classes. After this, the JSON files no longer need direct referencing.

### Assigning Key-Value Pairs to Python Classes

Lists from JSON arrays contain joint data (x, y, z, confidence). These are unpacked using Python’s unpacking operator (`*`) and passed as separate arguments to the class constructors.

For example, the key `Right_knee` in the dictionary maps to values `[x, y, z, confidence]`.

### Calculations

The functions `calculate_distance` and `calculate_angle` are used to find joint angles such as the knee angle. All calculations done for the `OriginalImg` class are repeated for the `NewImg` class.

### Comparing Data

The new input image joint data is compared to the reference image data to identify how a player can improve compared to a professional. Because a player’s angles can never exactly match another’s, a buffer of plus or minus 10 degrees was included to assess acceptable positioning.

Telemetry data is provided for debugging and program validation. For example, feedback such as “extend your knee” helps users focus on specific improvements.

## Terminal Output for One Test Case (Truncated)

Parts underlined in red in the output are returned to the user and can be sent audibly. The rest of the printout visualizes code execution and aids debugging.
