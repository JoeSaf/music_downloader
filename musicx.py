import argparse
import json
import os
import subprocess
from datetime import datetime

HISTORY_FILE = "history.json"

def save_to_history(query, title, video_id):
    """
    Saves a search entry to the history JSON file.
    """
    entry = {
        "query": query,
        "title": title,
        "video_id": video_id,
        "downloaded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Load existing history and append the new entry
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
    else:
        history = []

    history.append(entry)
    
    # Save updated history
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

def view_history():
    """
    Displays the search history stored in the JSON file.
    """
    if not os.path.exists(HISTORY_FILE):
        print("No search history found.")
        return
    
    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    print("\nSearch History:")
    for entry in history:
        print(f"Query: {entry['query']}")
        print(f"Title: {entry['title']}")
        print(f"Video ID: {entry['video_id']}")
        print(f"Downloaded At: {entry['downloaded_at']}")
        print("-" * 40)

def search_and_download(query):
    """
    Search for a song on YouTube, display results, and allow the user to choose one to download.
    """
    # Use yt-dlp to search for the song on YouTube and retrieve video IDs and titles
    print("Searching for the song on YouTube...")
    search_command = [
        "yt-dlp", "--get-id", "--get-title", f"ytsearch10:{query}"
    ]
    result = subprocess.run(search_command, capture_output=True, text=True)
    
    # Parse the output
    lines = result.stdout.strip().split("\n")
    video_results = [(lines[i], lines[i + 1]) for i in range(0, len(lines), 2)]

    # Display search results
    print("\nSearch Results:")
    for index, (title, video_id) in enumerate(video_results):
        print(f"{index + 1}. {title}")
    
    # Prompt user to select a video
    choice = input("\nEnter the number of the song you want to download: ")
    
    try:
        choice_index = int(choice) - 1
        if choice_index < 0 or choice_index >= len(video_results):
            print("Invalid choice. Exiting.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Get selected video ID and title
    selected_title, selected_video_id = video_results[choice_index]
    print(f"Selected: {selected_title}")
    
    # Download the selected video as an M4A
    download_command = f'yt-dlp -x --audio-format m4a https://www.youtube.com/watch?v={selected_video_id}'
    print(f"Downloading {selected_title} as M4A...")
    os.system(download_command)
    print("Download complete.")

    # Save to history
    save_to_history(query, selected_title, selected_video_id)

def main():
    parser = argparse.ArgumentParser(description="Terminal-based YouTube Music Downloader with Search History")
    parser.add_argument("query", type=str, help="Search query for the song (e.g., 'Song Title Artist') or 'history' to view past searches")
    args = parser.parse_args()
    
    # View search history if the user enters "history" as the query
    if args.query.lower() == "history":
        view_history()
        return
    
    # If only a song title is provided, prompt for additional details
    if len(args.query.split()) < 2:
        artist = input("Would you like to add an artist name to refine the search? (Leave blank to skip): ")
        if artist:
            args.query = f"{args.query} {artist}"
    
    # Perform search and download based on query
    search_and_download(args.query)

if __name__ == "__main__":
    main()