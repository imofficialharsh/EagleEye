# 🦅 EagleEye: Smart Surveillance System

EagleEye is a Python-based smart surveillance system that uses deep learning and computer vision to detect and respond to real-time events. It integrates multiple detection modules into a unified GUI interface for seamless user interaction.

## 🧠 Features

- 🚗 Car Accident Detection  
- 👥 Crowd Detection  
- 🙂 Face Detection  
- 🤕 Fall Detection  
- 🔫 Weapon Detection  
- 🚓 License Plate Recognition (LPR)

---

## 📂 Project Structure

```
EagleEye/
│   app.py                   # Main application file to run
│   page2.py                 # Secondary UI script
│   requirements.txt         # Required Python packages
│
├───Models/                  # Pretrained models and detection scripts
├───Input Video/             # Sample input videos for testing
├───Output/                  # Output video frames or results
└───Src/                     # UI images and icons
```

---

## 📦 Installation Guide

### 🔧 1. Clone the Repository

```bash
git https://github.com/imofficialharsh/EagleEye.git
cd EagleEye
```

### 📁 2. Download Required Files

⚠️ **Only one pretrained weight file is used in Weapon Detection.**  
📥 **[Download yolov3_training_2000.weights](https://drive.google.com/file/d/15_5JIgPdkNJqjejdFTqibuVjst7VoPQJ/view?usp=sharing)**  
Place the file inside:

```
Models/Weapon_Detection/yolov3_training_2000.weights
```

📥 **[Download Sample Input Videos](https://drive.google.com/file/d/1ecGiZQi2qHK8she0C3RqM8BQ9dqxErYe/view?usp=sharing)**  
Extract and place them inside the `Input Video/` folder.

---

### 🐍 3. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Then install required libraries:

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application

Start the application by running:

```bash
python app.py
```

The app will open a GUI for selecting the type of detection (car accident, weapon, fall, etc.), input video, and display the detection output.

---

## 🖼️ Screenshots

Here are some screenshots of the application:

### Main Menu
![Main Menu](https://github.com/user-attachments/assets/98f5930f-f107-4ba6-a8b9-888e31b5ce34)


### Detection Selection UI
Detection page:
![Detection UI](https://github.com/user-attachments/assets/5b2b5343-a073-462e-8ecf-d48d576de0df)

Browse File:
![Detection UI](https://github.com/user-attachments/assets/4787ddbe-33fe-4448-892f-5165e38e4149)

Fall Detection:
![Detection UI](https://github.com/user-attachments/assets/b59a5c46-d843-4ec0-9f7e-561fd5123912)

License Plate Recognition:
![Detection UI](https://github.com/user-attachments/assets/7c568087-c603-46ee-9ca3-877c371e04de)

Crowd Detection:
![Detection UI](https://github.com/user-attachments/assets/82000c92-7481-41f0-aa14-256ebcceb1e0)

Weapon Detection:
![Detection UI](https://github.com/user-attachments/assets/7630118e-8781-45ff-b570-c120eac7e343)

Car Accident Detection:
![Detection UI](https://github.com/user-attachments/assets/f5020954-20d6-4cf2-bc98-a402095ffb0e)


---

## 🤖 Future Enhancements

- Fire and smoke detection  
- Object theft detection  
- Web app version of EagleEye  
- Real-time camera integration  


---

## 👤 Author

**Harsh Kumar**  
B.Tech - Artificial Intelligence & Data Science  
[GitHub](https://github.com/imofficialharsh)

---

## ⚠️ License

This project is licensed under the MIT License – feel free to use and modify.

---
