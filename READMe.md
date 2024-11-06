YouTube Music Downloader

This is a command-line tool for downloading audio from YouTube videos, designed specifically for quick and easy music downloads. Users can enter a song name and/or artist, view search results, and select the desired video to download the audio in `.m4a` format. The tool also keeps track of search history, allowing users to view previously downloaded songs.

## Features

- **YouTube Search**: Enter a song name, artist, or both, and get YouTube search results.
- **Audio Download**: Select a video from the results and download the audio in `.m4a` format.
- **Search History**: Stores each search with the query, title, and download date in a history file (`history.json`).
- **Global Access**: Run the program from any terminal location using the symbolic link created in the setup.

## Requirements

- Python 3.6+
- `yt-dlp` (YouTube video downloader)
- `ffmpeg` (for audio conversion to `.m4a`)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/JoeSaf/YouTube-Music-Downloader.git
   cd YouTube-Music-Downloader
   ```

2. Run the `setup.py` script, which:
   - Creates a virtual environment.
   - Installs necessary requirements from `requirements.txt`.
   - Creates a symbolic link to make the program globally accessible.

   ```bash
   python setup.py
   ```

3. Make sure `~/.local/bin` is in your `PATH` to use the tool globally. You can add it to your `~/.bashrc` or `~/.zshrc` if needed:

   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```

## Usage

### Downloading a Song

To download a song, simply run:

```bash
musicx.py "Song Title Artist"
```

1. The tool will search YouTube for the given query.
2. You’ll see a list of search results with the option to select the one you want to download.
3. The selected video’s audio will be downloaded in `.m4a` format.

### Viewing Search History

To view your previous searches, use the `history` argument:

```bash
musicx.py history
```

This will display a list of previous searches saved in `history.json`, showing the query, video title, and download date.

## Example Use Case

Let’s say you want to download the song “Shape of You” by Ed Sheeran. Here’s how it works:

1. **Run the Download Command**:
   
   ```bash
   musicx.py "Shape of You Ed Sheeran"
   ```

2. **View Search Results**:
   - You’ll see a list of videos related to your search term.
   - Select the number corresponding to the desired video.

3. **Download Completion**:
   - The audio file will download as `Shape_of_You.m4a` (or the title of the selected video).
   - Your search query, selected video title, and video ID will be saved in `history.json`.

4. **View History**:
   - Later, you can view the search history by running:

     ```bash
     musicx.py history
     ```

   This will display all past downloads, including timestamps.