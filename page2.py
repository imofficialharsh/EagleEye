from tkinter import BooleanVar
import tkinter as tk
import os
import sys
from Models.Weapon_Detection.weapon import detect as detect_weapon
from Models.Crowd_Detection.crowd import detect as detect_crowd
from Models.Fall_Detection.Fall import detect as fall_detect
from Models.Face_detection.face import detect as face_detect
from Models.Car_Accident_Detection.Car import detect as accident_detect
from Models.License_Plate_Recognition.lpr import detect as lpr_detect

import tkinter.filedialog as fd
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2

# Get the absolute path of the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class DetectionPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#808080")
        
        self.using_video_file = False
        self.cap = cv2.VideoCapture(0)
        self.video_label = ctk.CTkLabel(self, text="", width=1000, height=625)
        self.video_label.place(x=10, y=80)
        
        # --- Header ---
        top_frame = ctk.CTkFrame(self, fg_color="#f0f0f0", height=60, corner_radius=0)
        top_frame.pack(side="top", fill="x")

        # FIX: Using an absolute path and corrected the typo in the filename
        header_logo_path = os.path.join(SCRIPT_DIR, "Src", "Image", "logo-Surveillance.png")
        icon_img = ctk.CTkImage(light_image=Image.open(header_logo_path), size=(40, 40))
        icon_label = ctk.CTkLabel(top_frame, image=icon_img, text="")
        icon_label.place(x=10, y=10)

        title = ctk.CTkLabel(top_frame, text="EagleEye", font=("Arial Black", 18), text_color="black")
        title.place(x=60, y=15)

        admin_btn = ctk.CTkButton(top_frame, text="Admin Details", corner_radius=20, 
                                  fg_color="#00bfff", hover_color="#00aadd", 
                                  command=self.open_admin_popup)
        admin_btn.place(relx=0.87, rely=0.2)
        

        # --- Right panel: Select Models ---
        sidebar = ctk.CTkFrame(self, width=250, height=625, fg_color="#bfbfbf") # Adjusted width
        sidebar.place(x=1020, y=80)

        label_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        label_frame.pack(pady=(20, 10), padx=19, anchor="w")

        # FIX: Using an absolute path for the AI model logo
        ai_logo_path = os.path.join(SCRIPT_DIR, "Src", "Image", "AI_model_logo.png")
        icon_img_ai = ctk.CTkImage(light_image=Image.open(ai_logo_path), size=(30, 30))
        icon_label_ai = ctk.CTkLabel(label_frame, image=icon_img_ai, text="")
        icon_label_ai.pack(side="left", padx=(0, 8))

        model_label = ctk.CTkLabel(label_frame, text="Select ML Models", font=("Arial Black", 18), text_color="black")
        model_label.pack(side="left")

        # --- Detection model checkboxes ---
        self.vars = {}
        models = ["Face Detection", "Crash Detection", "Fall Detection",
                  "LPR Detection", "Crowd Detection", "Weapon Detection"]
        for model in models:
            var = BooleanVar(value=False)
            cb = ctk.CTkCheckBox(sidebar, text=model, variable=var)
            cb.pack(pady=5, anchor="w", padx=30)
            self.vars[model] = var
            
        # --- Upload file frame and button ---
        file_label = ctk.CTkLabel(sidebar, text="Select Video File", font=("Arial Black", 18), text_color="black")
        file_label.pack(pady=(140, 0), padx=25, anchor="w")

        upload_outer = ctk.CTkFrame(sidebar, fg_color="#bfbfbf")
        upload_outer.pack(pady=(10, 0), padx=25, anchor="s", side="bottom", fill="x")

        upload_box = ctk.CTkFrame(upload_outer, fg_color="transparent", border_color="gray",
                                  border_width=2, corner_radius=15)
        upload_box.pack(padx=0, pady=0, fill="x", expand=True)

        # FIX: Using an absolute path for the upload image icon
        upload_icon_path = os.path.join(SCRIPT_DIR, "Src", "Image", "image.png")
        upload_img = ctk.CTkImage(light_image=Image.open(upload_icon_path), size=(35, 35))
        upload_icon = ctk.CTkLabel(upload_box, image=upload_img, text="")
        upload_icon.pack(pady=(10, 5))

        upload_label = ctk.CTkLabel(upload_box, text="Drag and Drop file\nor", justify="center",
                                    text_color="black", font=("Arial", 12))
        upload_label.pack(pady=(0, 5))
        
        self.browse_btn = ctk.CTkButton(upload_box, text="Browse", width=100, command=self.browse_file)
        self.browse_btn.pack(pady=(0, 10))
        
        self.show_frame()

    def browse_file(self):
        file_path = fd.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi *.webm *.mov *.mkv")])
        if file_path:
            self.using_video_file = True
            if self.cap:
                self.cap.release()
            self.cap = cv2.VideoCapture(file_path)

    def show_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, (1000, 625))
                
                if self.vars["Weapon Detection"].get():
                    frame = detect_weapon(frame)
                if self.vars["Crowd Detection"].get():
                    frame,_ = detect_crowd(frame)
                if self.vars["Fall Detection"].get():
                    frame,_ = fall_detect(frame)
                if self.vars["Face Detection"].get():
                    frame = face_detect(frame)
                if self.vars["Crash Detection"].get():
                    frame = accident_detect(frame)
                if self.vars["LPR Detection"].get():
                    frame = lpr_detect(frame)
                    
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                ctk_img = ctk.CTkImage(light_image=img, size=(1000, 625))

                self.video_label.configure(image=ctk_img)
                self.video_label.image = ctk_img

                self.after(30, self.show_frame)
            else:
                self.cap.release()
                if self.using_video_file:
                    self.cap = cv2.VideoCapture(0)
                    self.using_video_file = False
                    self.after(30, self.show_frame)


    def open_admin_popup(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Admin Details")
        popup.geometry("400x300")
        popup.grab_set()

        sender_val = tk.StringVar()
        app_pass_val = tk.StringVar()
        receiver_val = tk.StringVar()

        admin_file_path = os.path.join(SCRIPT_DIR, "admin_details.txt")

        try:
            with open(admin_file_path, "r") as f:
                lines = f.read().splitlines()
                if len(lines) == 3:
                    sender_val.set(lines[0])
                    app_pass_val.set(lines[1])
                    receiver_val.set(lines[2])
        except FileNotFoundError:
            pass

        ctk.CTkLabel(popup, text="Sender Email ID:").pack(pady=(10, 2))
        sender_entry = ctk.CTkEntry(popup, textvariable=sender_val, width=300)
        sender_entry.pack()

        ctk.CTkLabel(popup, text="App Password:").pack(pady=(10, 2))
        app_pass_entry = ctk.CTkEntry(popup, textvariable=app_pass_val, show="*", width=300)
        app_pass_entry.pack()

        ctk.CTkLabel(popup, text="Receiver Email ID:").pack(pady=(10, 2))
        receiver_entry = ctk.CTkEntry(popup, textvariable=receiver_val, width=300)
        receiver_entry.pack()

        def save_details():
            with open(admin_file_path, "w") as f:
                f.write(sender_val.get() + "\n")
                f.write(app_pass_val.get() + "\n")
                f.write(receiver_val.get() + "\n")
            popup.destroy()

        ctk.CTkButton(popup, text="Save", command=save_details).pack(pady=20)