import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        self.root.configure(bg="#212121")

        self.song_label = tk.Label(root, text="No song playing", font=("Helvetica", 14), fg="#FFFFFF", bg="#212121")
        self.song_label.pack(pady=20)

        self.play_button = tk.Button(root, text="Play", command=self.play_music, font=("Helvetica", 12), fg="#FFFFFF", bg="#FF5722")
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music, font=("Helvetica", 12), fg="#FFFFFF", bg="#FF5722")
        self.stop_button.pack(pady=10)

    def play_music(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select Music", filetypes=(("MP3 Files", "*.mp3"),))
        if file_path:
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.song_label.config(text="Now playing: " + file_path)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.song_label.config(text="No song playing")

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
