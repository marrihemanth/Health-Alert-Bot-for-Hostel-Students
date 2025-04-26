# 🌡️ Health Alert Bot for Hostel Students

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A **Command Line Interface (CLI)-based Health Alert Bot** designed to assist hostel students in managing their health by providing symptom-based remedies, tracking recurring symptoms, and offering personalized advice. The bot also includes a research component on common seasonal illnesses and their treatments.

---

## 📝 Overview

The **Health Alert Bot** is a CLI-based tool aimed at helping hostel students:
- Input symptoms and receive basic remedies.
- Track recurring symptoms over time.
- Get alerts for when to seek medical attention.
- Access customized advice based on their health history.

This project is part of a hackathon submission and demonstrates the integration of **Modern Medicine**, **Ayurveda**, and **Homeopathy** to provide holistic health advice.

---

## 🌟 Features

### **Basic Features**
- **Symptom Input**: Users can input symptoms in plain text.
- **Remedy Suggestion**: Provides basic remedies for common symptoms.
- **Session Output**: Displays suggestions in a readable format.

### **Medium Features**
- **Symptom Matching**: Matches user input to predefined lists of symptoms using keyword matching.
- **Log Storage**: Stores health logs in a JSON file for future reference.
- **Consultation Alert**: Alerts users to consult a doctor if symptoms persist.
- **Input Validation**: Ensures valid inputs and rejects blanks or invalid entries.

### **Advanced Features**
- **Daily Health Tracker**: Tracks recurring symptoms and highlights trends.
- **Customized Advice**: Offers personalized advice based on past health logs.
- **Research Component**: Includes insights on 5 common seasonal illnesses and their remedies.

---

## 💻 Installation

### Prerequisites
- Python 3.x installed on your system. Download it from [here](https://www.python.org/downloads/).

## 💻 Setup  
```bash
# Clone and run
git clone https://github.com/your-username/health-alert-bot.git
cd health-alert-bot
pip install -r requirements.txt
python health_bot.py
```
### 🚀 Usage Example
```bash
Enter Symptoms: fever, sore throat  
Do you want to save this log? (yes/no): yes  

# Output:
Possible Issue: Common Cold  
Remedy: Take paracetamol, rest.  
Advice: Consult a doctor if fever lasts >3 days.  
Log Saved Successfully.
```
### 📚 Research Insights
**Common Illnesses & Remedies :**
   **Flu** : Rest (Modern), Tulsi tea (Ayurveda), Oscillococcinum (Homeopathy).
   **Allergies** : Antihistamines (Modern), Neem water (Ayurveda), Natrum Mur (Homeopathy).
   **Acidity** : Antacids (Modern), Amla juice (Ayurveda), Nux Vomica (Homeopathy).

### 👥 Team
Hemanth Marri (Developer), Swathi Parvatham (Modern Medicine/Homeopathy), Preetham Rao (Ayurveda/UI).

### 📞 Feedback
**Email:** marrihemanth@gmail.com
