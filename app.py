import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from page2 import DetectionPage

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class SurveillanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EagleEye - Smart Surveillance System")
        self.iconbitmap("./Src/Image/logo-survillence.ico")
        # self.pack(fill="both", expand=True)
        self.geometry("1280x720")
        self.configure(fg_color="#808080")  # grey background
        self.resizable(False, False)

        # Top Frame (Header)
        top_frame = ctk.CTkFrame(
            self, fg_color="#f0f0f0", height=60, corner_radius=0)
        top_frame.pack(side="top", fill="x")

        # Logo + Title
        icon_img = ctk.CTkImage(light_image=Image.open(
            "./Src/Image/logo-survillence.png"), size=(40, 40))
        icon_label = ctk.CTkLabel(top_frame, image=icon_img, text="")
        icon_label.place(x=10, y=10)

        title = ctk.CTkLabel(top_frame, text="EagleEye", font=(
            "Arial Black", 18), text_color="black")
        title.place(x=60, y=15)

        # Admin Details button
        admin_btn = ctk.CTkButton(top_frame, text="Admin Details",
                                  corner_radius=20, fg_color="#00bfff", hover_color="#00aadd", command=self.open_admin_popup)
        admin_btn.place(relx=0.87, rely=0.2)

        # Center Icon
        # cam_icon = ctk.CTkImage(light_image=Image.open(
        #     "./Src/Image/EagleEye-Logo.png"), size=(150, 150))
        cam_icon = ctk.CTkImage(light_image=Image.open(
            "./Src/Image/EagleEye-Logo.png"), size=(600, 352))
        cam_label = ctk.CTkLabel(self, image=cam_icon, text="")
        cam_label.place(relx=0.5, rely=0.37, anchor="center")

        # Center Text
        main_text = ctk.CTkLabel(
            self, text="SMART SURVEILLANCE SYSTEM", font=("Arial Black", 28))
        main_text.place(relx=0.5, rely=0.66, anchor="center")


        # START Button
        # start_btn = ctk.CTkButton(self, text="START", font=(
        #     "Arial Black", 20), fg_color="green", hover_color="#0f0", corner_radius=20, width=400, command=self.open_second_page)
        start_btn = ctk.CTkButton(self, text="START", font=(
            "Arial Black", 20), fg_color="green", hover_color="#227818", corner_radius=20, width=400, command=self.open_second_page)
        start_btn.place(relx=0.5, rely=0.73, anchor="center")

        # Bottom Icons (placeholder - you can use your own icons)
        icon_frame = ctk.CTkFrame(self, fg_color="transparent")
        icon_frame.pack(side="bottom", pady=10)

        icons = ["./Src/Image/crashed-car-icon.png", "./Src/Image/crowd-detection-icon.png", "./Src/Image/face-detection-icon.png",
                 "./Src/Image/fall-detection-icon.png", "./Src/Image/gun-detection-icon.png", "./Src/Image/LPR-Detection Logo.png"]
        for icon in icons:
            img = ctk.CTkImage(light_image=Image.open(icon), size=(80,80))
            lbl = ctk.CTkLabel(icon_frame, image=img, text="")
            lbl.pack(side="left", padx=30)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        print("Selected file:", file_path)

    def open_admin_popup(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Admin Details")
        popup.geometry("400x300")
        popup.grab_set()  # Lock focus to popup

        sender_val = tk.StringVar()
        app_pass_val = tk.StringVar()
        receiver_val = tk.StringVar()

        # Try loading saved data
        try:
            with open("admin_details.txt", "r") as f:
                lines = f.read().splitlines()
                if len(lines) == 3:
                    sender_val.set(lines[0])
                    app_pass_val.set(lines[1])
                    receiver_val.set(lines[2])
        except FileNotFoundError:
            pass

        # Entry fields
        ctk.CTkLabel(popup, text="Sender Email ID:").pack(pady=(10, 2))
        sender_entry = ctk.CTkEntry(popup, textvariable=sender_val, width=300)
        sender_entry.pack()

        ctk.CTkLabel(popup, text="App Password:").pack(pady=(10, 2))
        app_pass_entry = ctk.CTkEntry(
            popup, textvariable=app_pass_val, show="*", width=300)
        app_pass_entry.pack()

        ctk.CTkLabel(popup, text="Receiver Email ID:").pack(pady=(10, 2))
        receiver_entry = ctk.CTkEntry(
            popup, textvariable=receiver_val, width=300)
        receiver_entry.pack()

        def save_details():
            with open("admin_details.txt", "w") as f:
                f.write(sender_val.get() + "\n")
                f.write(app_pass_val.get() + "\n")
                f.write(receiver_val.get() + "\n")
            popup.destroy()

        ctk.CTkButton(popup, text="Save", command=save_details).pack(pady=20)

    # def open_second_page(self):
    #     self.withdraw()
    #     second_window = DetectionPage(self)
    #     second_window.grab_set()  # Lock focus to second window
    
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
