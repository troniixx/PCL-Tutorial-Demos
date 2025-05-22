import os
import argparse
from moviepy.editor import VideoFileClip

def parse_srt(srt_file):  # Defines a function to parse the .srt subtitle file
    with open(srt_file, 'r', encoding='utf-8') as file:
        content = file.read().strip()  # Reads the entire .srt file and removes leading/trailing whitespace
            
    blocks = content.split('\n\n')  # Splits subtitles into blocks separated by blank lines
    subtitles = []  # List to store subtitle text lines
    time_periods = []  # List to store corresponding start and end times

    for block in blocks:  # Iterates through each subtitle block
        lines = block.split('\n')  # Splits a block into individual lines
        if len(lines) >= 3:  # Ensures the block has at least an index, timing, and text
            # Extract start and end time
            start_end = lines[1].split(' --> ')  # Splits the timing line into start and end timestamps
            start_time = start_end[0]  # Captures the start timestamp
            end_time = start_end[1]  # Captures the end timestamp
            
            # Extract subtitle text
            subtitle_text = ' '.join(lines[2:]).replace('\n', ' ').strip()  # Joins all subtitle lines into a single string
            subtitles.append(subtitle_text)  # Appends the text to the subtitles list
            time_periods.append((start_time, end_time))  # Appends the time tuple to the time_periods list
        
    return subtitles, time_periods  # Returns both lists for further processing


def save_subtitles(subtitles, base_filename, outdir):  # Defines a function to save each subtitle to a separate .txt file
    os.makedirs(outdir, exist_ok=True)  # Creates the output directory if it doesn't already exist
    for i, subtitle in enumerate(subtitles):  # Iterates through all subtitles with their index
        output_filename = os.path.join(outdir, f"{base_filename}_{i+1}.txt")  # Constructs an output filename for each subtitle
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(subtitle)  # Writes subtitle text into the file
        print(f"Saved: {output_filename}")  # Prints confirmation of saved file


def process_srt(input_file, outdir='.'):
    base_filename = os.path.splitext(os.path.basename(input_file))[0]  # Derives the base filename without extension
    subtitles, time_periods = parse_srt(input_file)  # Parses the .srt file into subtitles and time_periods lists
    # Save subtitles to individual text files
    save_subtitles(subtitles, base_filename, outdir)  # Calls save_subtitles to output .txt files
    return time_periods  # Returns the list of time tuples for audio extraction


def create_audio_clips(video_file, time_periods, output_dir, output_prefix):  # Defines a function to extract audio segments
    os.makedirs(output_dir, exist_ok=True)  # Ensures the audio output directory exists
    for idx, (start, end) in enumerate(time_periods):  # Iterates through each time period with its index
        clip = VideoFileClip(video_file).subclip(start, end)  # Subclips the video between specified start and end times
        audio_file = os.path.join(output_dir, f"{output_prefix}_{idx + 1}.wav")  # Constructs the output .wav filename
        clip.audio.write_audiofile(audio_file, codec='pcm_s16le')  # Exports the audio track as WAV with PCM codec
        print(f"Exported: {output_prefix}_{idx + 1}.wav")  # Prints confirmation of exported audio file


if __name__ == "__main__":  # Ensures this block runs only when script is executed directly
    parser = argparse.ArgumentParser(description='Extract audio clips and subtitles from video based on SRT file')  # Sets up argument parser
    parser.add_argument('video_file', type=str, help='Path to the video file')  # Adds required video file argument
    parser.add_argument('srt_file', type=str, help='Path to the SRT file')  # Adds required subtitle file argument
    parser.add_argument('--outdir', type=str, default='output', help='Output directory')  # Adds optional output directory argument
    parser.add_argument('--prefix', type=str, default='output', help='Output prefix for audio clips')  # Adds optional prefix for audio filenames
    args = parser.parse_args()  # Parses the provided command-line arguments

    time_periods = process_srt(args.srt_file, args.outdir)  # Processes the .srt file and saves subtitles
    create_audio_clips(args.video_file, time_periods, args.outdir, args.prefix)  # Extracts and saves audio clips based on time_periods