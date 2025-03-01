# rnbKoTracker
Train an AI model to create a count of KOs from Run and Bun streams.

**Steps to Identify Pokémon from Gameplay Sprites**
- rough plan taken from prompting ChatGPT to start this project

Extract Video Frames – Convert the gameplay video into individual images (frames). This can be done using OpenCV or FFmpeg.
Locate Pokémon Sprites – Use object detection or image segmentation to isolate the Pokémon in battle.
Compare with a Pokémon Sprite Dataset –
If using classical image matching, OpenCV’s template matching or feature detection (ORB, SIFT) can compare the detected sprite with known sprites.
If using AI-based classification, a deep learning model (like a CNN trained on Pokémon sprites) could classify which Pokémon is in the scene.
Track Pokémon Over Time – If a Pokémon stays on screen for multiple frames, a tracking algorithm (e.g., SORT or DeepSORT) can maintain consistency.
Display Results – The AI could output the detected Pokémon’s name, stats, or even log encounters.
Tech Stack You’d Need
OpenCV – For frame extraction and sprite detection.
TensorFlow/PyTorch – If using a CNN for classification.
YOLO or Detectron2 – For object detection (if working with dynamic gameplay).
Dataset of Pokémon Sprites – A collection of all Pokémon battle sprites for training or matching.
