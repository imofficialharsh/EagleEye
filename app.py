import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from page2 import DetectionPage
import os

# Set GUI appearance
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Get the absolute path of the directory where the script is located
# This is crucial for making all file paths reliable
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


class SurveillanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EagleEye - Smart Surveillance System")
        self.geometry("1280x720")
        self.resizable(False, False)

        # --- Window Icon ---
        # Using an absolute path to set the window icon
        icon_path = os.path.join(SCRIPT_DIR, "Src", "Image", "logo-Surveillance.png")
        icon_image = tk.PhotoImage(file=icon_path)
        self.iconphoto(True, icon_image)

        # --- Top Frame (Header) ---
        top_frame = ctk.CTkFrame(self, fg_color="#f0f0f0", height=60, corner_radius=0)
        top_frame.pack(side="top", fill="x")

        # Logo + Title in Header
        logo_path = os.path.join(SCRIPT_DIR, "Src", "Image", "logo-Surveillance.png")
        header_icon_img = ctk.CTkImage(light_image=Image.open(logo_path), size=(40, 40))
        header_icon_label = ctk.CTkLabel(top_frame, image=header_icon_img, text="")
        header_icon_label.place(x=10, y=10)

        title = ctk.CTkLabel(top_frame, text="EagleEye", font=("Arial Black", 18), text_color="black")
        title.place(x=60, y=15)

        # Admin Details button
        admin_btn = ctk.CTkButton(top_frame, text="Admin Details", corner_radius=20, 
                                  fg_color="#00bfff", hover_color="#00aadd", 
                                  command=self.open_admin_popup)
        admin_btn.place(relx=0.87, rely=0.2)

        # --- Center Content ---
        # Center Logo Image - using an absolute path
        center_logo_path = os.path.join(SCRIPT_DIR, "Src", "Image", "EagleEye-Logo.png")
        cam_icon = ctk.CTkImage(light_image=Image.open(center_logo_path), size=(600, 352))
        cam_label = ctk.CTkLabel(self, image=cam_icon, text="")
        cam_label.place(relx=0.5, rely=0.37, anchor="center")

        # Center Text
        main_text = ctk.CTkLabel(self, text="SMART SURVEILLANCE SYSTEM", font=("Arial Black", 28))
        main_text.place(relx=0.5, rely=0.66, anchor="center")

        # START Button
        start_btn = ctk.CTkButton(self, text="START", font=("Arial Black", 20), 
                                  fg_color="green", hover_color="#227818", 
                                  corner_radius=20, width=400, 
                                  command=self.open_second_page)
        start_btn.place(relx=0.5, rely=0.73, anchor="center")

        # --- Bottom Icons ---
        icon_frame = ctk.CTkFrame(self, fg_color="transparent")
        icon_frame.pack(side="bottom", pady=10)

        # Using absolute paths for all bottom icons in a loop
        icon_names = [
            "crashed-car-icon.png", "crowd-detection-icon.png", "face-detection-icon.png",
            "fall-detection-icon.png", "gun-detection-icon.png", "LPR-Detection Logo.png"
        ]
        for icon_name in icon_names:
            icon_path = os.path.join(SCRIPT_DIR, "Src", "Image", icon_name)
            try:
                img = ctk.CTkImage(light_image=Image.open(icon_path), size=(80, 80))
                lbl = ctk.CTkLabel(icon_frame, image=img, text="")
                lbl.pack(side="left", padx=30)
            except FileNotFoundError:
                print(f"Warning: Icon file not found at {icon_path}")


    def open_admin_popup(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Admin Details")
        popup.geometry("400x300")
        popup.grab_set()  # Lock focus to popup

        sender_val = tk.StringVar()
        app_pass_val = tk.StringVar()
        receiver_val = tk.StringVar()

        # Using an absolute path for the admin details file
        admin_file_path = os.path.join(SCRIPT_DIR, "admin_details.txt")

        # Try loading saved data
        try:
            with open(admin_file_path, "r") as f:
                lines = f.read().splitlines()
                if len(lines) == 3:
                    sender_val.set(lines[0])
                    app_pass_val.set(lines[1])
                    receiver_val.set(lines[2])
        except FileNotFoundError:
            pass # File doesn't exist yet, which is fine

        # Entry fields
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

    def open_second_page(self):
        # Hide the current content of the main window
        for widget in self.winfo_children():
            widget.pack_forget()

        # Create and display the DetectionPage frame
        detection_page = DetectionPage(self)
        detection_page.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = SurveillanceApp()
    app.mainloop()