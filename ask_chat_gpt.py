import os
import tkinter as tk
from pyChatGPT import ChatGPT

session_token = os.getenv("chatgpt_key")
api = ChatGPT(session_token, moderation=False)

def setup_interface():
    root = tk.Tk()
    root.title("GPT-IDE")
    root.geometry("500x500")
    root.resizable(True, True)
    root.configure(bg="#3d3d3d")

    user_input = tk.Text(root, height=10, width=50, bg="#61555e",
    fg="#e3e3e3", font=("Helvetica",15,"bold"))
    user_input.pack(expand=True, fill="both")

    def send_to_gpt(user_input):
        user_input = user_input.get("1.0", "end-1c")

        if user_input:
            response = api.send_message("Provide a code snippet without any explanation to solve the following task in Python: " + user_input)
            response = "".join(response.get("message"))
            response = response[6:(len(response)-6)]
            with open("gpt_answers.py", "a") as f:
                f.write(response)
                f.close()
            # Create label
            l = tk.Label(root, text = "Code solution")
            l.config(font =("Helvetica",20,"bold"))
            l.pack()
            T = tk.Text(root)
            T.insert(tk.END, response)
            T.pack()

    button = tk.Button(root, text="Ask ChatGPT", bg="#1565C0", fg="#FBFBFB",
    font=("Helvetica",20,"bold"), command=lambda: send_to_gpt(user_input))
    button.pack(expand=True, fill="both")
    
    root.mainloop()

setup_interface()

