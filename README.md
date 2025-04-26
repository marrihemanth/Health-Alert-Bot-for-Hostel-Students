# Health Alert Bot for Hostel Students

A comprehensive CLI-based health monitoring system designed specifically for hostel students, providing symptom analysis, remedy suggestions, health tracking, personalized health advice, medication management, and more.

## 🎯 Project Overview

The Health Alert Bot addresses unique health challenges faced by students living in hostels:
- Limited access to immediate healthcare advice
- Difficulty in tracking recurring health issues
- Challenges in determining when to seek professional help
- Lack of awareness about seasonal diseases and prevention
- Need for medication reminders and tracking

## ✨ Key Features

### 👤 User Management
- Secure patient ID system (format: HST-YYYY-XXXX)
- Comprehensive user profiles (name, age, gender, room, contacts, medical history)
- Multi-user support with login/logout functionality
- Ability to update personal information

### 🩺 Symptom Analysis & Remedies
- Natural language symptom input (comma-separated) with keyword matching
- Symptom severity rating system (scale of 1-4)
- Suggests both Modern and Ayurvedic remedies based on identified symptoms
- Critical symptom alerts for potentially serious conditions, advising professional consultation

### 📊 Health Tracking & Insights
- Logs symptoms with severity ratings and timestamps
- Analyzes logs to show health trends (most frequent symptoms in the past week)
- Identifies recurring symptoms and provides insights
- Basic visualization of symptom frequency over time

### 💊 Medication Management
- Add, view, and remove personal medications (name, dosage, frequency, instructions)
- Set and update medication reminders (specific times in HH:MM format)
- Automatic reminder checks upon login

### 🧠 Personalized Health Advice
- Customized recommendations based on current symptoms and potential conditions
- Hostel-specific lifestyle advice linked to symptoms
- Seasonal health advice tailored to the current month

### 🍎 Dietary Recommendations
- Provides food suggestions based on current symptoms (e.g., BRAT diet for diarrhea)

### 🏥 Resources & Information
- Information on common seasonal diseases (description, first-aid, precautions)
- List of nearby medical facilities with contact details, hours, and emergency status

### 🔒 Data Management
- Securely stores user profiles (`user_profiles.json`), health logs (`health_log.txt`), and medication data (`medications.json`)
- Option to back up all user data (profiles, logs, meds) into a timestamped zip file
- Option to export individual user health records (logs) to a CSV file

## 💻 Technical Implementation
- Modular Python code with clear functions for each feature
- Efficient data structures (dictionaries, sets, lists, Counter) for symptom matching and analysis
- Persistent storage using JSON and text files
- User-friendly, color-coded terminal interface (requires `colorama` library)
- Robust input validation and error handling

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- `colorama` library (for colored output)

### Installation
1.  Clone this repository:
    ```bash
    git clone https://github.com/marrihemanth/Health-Alert-Bot-for-Hostel-Students.git
    cd Health-Alert-Bot-for-Hostel-Students
    ```

2.  Install dependencies:
    ```bash
    pip install colorama
    ```
    *(Note: The script checks for `colorama` and runs without it, but the experience is enhanced with colors.)*

3.  Run the Health Alert Bot:
    ```bash
    python health_alert_bot.py
    ```

## 📝 Usage Guide

1.  **First-time setup**: Run the script and choose option '2' to register as a new user. You will receive a unique patient ID (e.g., `HST-2025-1234`). Remember this ID for future logins.
2.  **Login**: Run the script and choose option '1', then enter your patient ID.
3.  **Main Menu**: Once logged in, you can:
    *   **Record Symptoms (1)**: Enter symptoms, rate severity, get remedies/advice, and save the log.
    *   **View Health Trends (2)**: See recent symptom frequency and visualizations.
    *   **Get Customized Advice (3)**: Input current symptoms to receive tailored advice.
    *   **Learn About Diseases (4)**: Read about common seasonal illnesses.
    *   **Manage Medications (5)**: Add/remove meds, view list, set reminders.
    *   **Track Recovery (6)**: View symptom timeline and current recovery stage (Note: This feature might be under development).
    *   **Nearby Facilities (7)**: See local clinic/hospital information.
    *   **Dietary Advice (8)**: Get food recommendations for specific symptoms.
    *   **Data Management (9)**: Backup all data or export your logs.
    *   **Update Info (10)**: Modify your profile details.
    *   **Logout (11)**: Return to the login screen.
    *   **Exit (12)**: Close the application.

## 📁 Project Structure

-   `health_alert_bot.py`: Main Python script containing all logic and functions.
-   `health_log.txt`: Stores timestamped health logs for all users, including symptoms and severity.
-   `user_profiles.json`: Stores registered user profile information (keyed by patient ID).
-   `medications.json`: Stores medication details for all users (keyed by patient ID).
-   `README.md`: This file.
-   *(Backup zip files will be created in the same directory when using the backup feature)*
-   *(Exported CSV files will be created in the same directory when using the export feature)*

## 📸 Screenshots

[Screenshots can be added here to showcase the interface]

## 🧪 Future Enhancements
- More sophisticated recovery tracking and analysis.
- Machine learning for more accurate symptom pattern recognition and prediction.
- Integration with external health APIs or databases.
- GUI or web-based interface.

## 👥 Contributors
- Hemanth Marri ([@marrihemanth](https://github.com/marrihemanth))

## 📄 License

This project is licensed under the MIT License.
