import json
import os

# Define paths
json_folder = "C:/Users/ASUS/Desktop/json"  # Folder containing JSON files
audio_folder = "C:/Users/ASUS/Desktop/audio"  # Folder containing audio files
output_file = "C:/Users/ASUS/Desktop/transcript.txt" # Final transcripts.txt file

# Open the output file in write mode with UTF-8 encoding
with open(output_file, "w", encoding="utf-8") as out_f:
    # Iterate over each JSON file in the folder
    for json_filename in os.listdir(json_folder):
        if json_filename.endswith(".json"):
            # Load the JSON data with UTF-8 encoding
            json_path = os.path.join(json_folder, json_filename)
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Extract the audio filename based on JSON file's basename (assuming audio file matches JSON filename)
            audio_filename = os.path.splitext(json_filename)[0] + ".wav"
            
            # Check if corresponding audio file exists
            audio_path = os.path.join(audio_folder, audio_filename)
            if not os.path.exists(audio_path):
                print(f"Warning: Audio file {audio_filename} not found for JSON {json_filename}")
                continue

            # Concatenate all text segments in "verbatim" to form a single transcription
            transcription = " ".join([segment["text"] for segment in data["verbatim"]])
            
            # Write the filename and transcription in the desired format
            out_f.write(f"{audio_filename}|{transcription}\n")
