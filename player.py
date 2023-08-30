import tkinter as tk
import os
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        
        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create a list to store music files
        self.playlist = []

        # Create a label to display the current playing song
        self.current_song_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.current_song_label.pack(pady=10)

        # Create buttons for controlling playback
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.play_button.pack()
        self.pause_button.pack()
        self.stop_button.pack()

        # Create a listbox to display the playlist
        self.playlist_box = tk.Listbox(root, selectmode=tk.SINGLE, activestyle="none", font=("Helvetica", 12))
        self.playlist_box.pack(fill="both", expand="true")

        # Create buttons for adding and removing songs
        self.add_button = tk.Button(root, text="Add Song", command=self.add_song)
        self.remove_button = tk.Button(root, text="Remove Song", command=self.remove_song)
        self.add_button.pack()
        self.remove_button.pack()

    def add_song(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.playlist.append(file_path)
            filename = os.path.basename(file_path)
            self.playlist_box.insert(tk.END, filename)

    def remove_song(self):
        selected_song = self.playlist_box.curselection()
        if selected_song:
            index = int(selected_song[0])
            self.playlist_box.delete(index)
            self.playlist.pop(index)

    def play_music(self):
        selected_song = self.playlist_box.curselection()
        if selected_song:
            index = int(selected_song[0])
            song_path = self.playlist[index]

            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

            # Update the current song label
            self.current_song_label.config(text="Now Playing: " + os.path.basename(song_path))

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_song_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
