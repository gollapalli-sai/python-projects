import tkinter as tk
import pyttsx3
import threading
import time

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Global flags
is_paused = False
is_speaking = False

# Function to speak text word-by-word
def speak_text():
    global is_paused, is_speaking
    text = text_entry.get("1.0", tk.END).strip()

    if not text:
        return

    words = text.split()
    is_speaking = True

    for word in words:
        if not is_speaking:
            break  # Stop if user exits
        while is_paused:
            time.sleep(0.1)  # Wait while paused
        engine.say(word)
        engine.runAndWait()

    is_speaking = False

# Function to start speaking in a separate thread
def start_speaking():
    global is_speaking, is_paused
    if is_speaking:
        return  # Prevent multiple clicks
    is_paused = False
    threading.Thread(target=speak_text, daemon=True).start()

# Toggle pause/resume
def pause_resume():
    global is_paused
    if not is_speaking:
        return
    is_paused = not is_paused
    pause_btn.config(text="Resume" if is_paused else "Pause")

# Exit the application safely
def stop_app():
    global is_speaking, is_paused
    is_paused = False
    is_speaking = False
    root.destroy()

# ------------------ GUI ------------------

# Create main window
root = tk.Tk()
root.title("Text to Speech with Pause/Resume")
root.geometry("450x330")
root.configure(bg="#f4f4f4")

# Heading
heading = tk.Label(root, text="🗣️ Text-to-Speech App", font=("Arial", 16, "bold"), bg="#f4f4f4")
heading.pack(pady=10)

# Text Entry Box
text_entry = tk.Text(root, height=6, width=45, font=("Arial", 12))
text_entry.pack(pady=10)

# Speak Button
speak_btn = tk.Button(root, text="Speak", command=start_speaking, font=("Arial", 12), bg="#4CAF50", fg="white", width=12)
speak_btn.pack(pady=5)

# Pause/Resume Button
pause_btn = tk.Button(root, text="Pause", command=pause_resume, font=("Arial", 12), bg="#FFC107", fg="black", width=12)
pause_btn.pack(pady=5)

# Exit Button
exit_btn = tk.Button(root, text="Exit", command=stop_app, font=("Arial", 12), bg="#f44336", fg="white", width=12)
exit_btn.pack(pady=5)

# Start GUI loop
root.mainloop()
