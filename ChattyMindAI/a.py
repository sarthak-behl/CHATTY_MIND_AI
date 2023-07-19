import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import pyttsx3
import openai

# Make sure to provide your OpenAI API key
openai.api_key = "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"

engine = pyttsx3.init()
listener = sr.Recognizer()

def on_click():
    with sr.Microphone() as source:
        try:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Speak now...")
            voice = listener.listen(source)
            data = listener.recognize_google(voice)
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "You said: " + data)

            if "exit" in data.lower():
                root.quit()
                return

            model = "text-davinci-003"
            completion = openai.Completion.create(
                model=model,
                prompt=data,
                max_tokens=1024,
                temperature=0.5,
                n=1,
                stop=None
            )
            response = completion.choices[0].text

            # Print and hear the response
            print(response)
            engine.say(response)
            engine.runAndWait()
            output_text.insert(tk.END, "\nResponse: " + response)
        except sr.UnknownValueError:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Sorry, I couldn't understand the audio.")
        except sr.RequestError:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Sorry, the speech recognition service is currently unavailable.")

# GUI Setup
root = tk.Tk()
root.title("Chatty Mind Ai")
root.geometry("400x250")

style = ttk.Style()
style.theme_use("vista")  # Use the "vista" theme

title_label = ttk.Label(root, text="Chatty Mind Ai", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

start_button = ttk.Button(root, text="Speak", command=on_click)
start_button.pack(pady=10)

output_text = tk.Text(root, height=10, wrap=tk.WORD, font=("Helvetica", 12), foreground="#ffc000")
output_text.config(bg="black")
output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Add some padding to the labels and buttons
title_label.config(padding=10)
start_button.config(padding=10)

# Change the background color of the GUI
root.config(background="black")

root.mainloop()
