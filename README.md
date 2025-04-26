# Health Alert Bot for Hostel Students

A comprehensive CLI-based health monitoring system designed specifically for hostel students, providing symptom analysis, remedy suggestions, health tracking, and personalized health advice.

## 🎯 Project Overview

The Health Alert Bot addresses unique health challenges faced by students living in hostels:
- Limited access to immediate healthcare advice
- Difficulty in tracking recurring health issues
- Challenges in determining when to seek professional help
- Lack of awareness about seasonal diseases and prevention

## ✨ Key Features

### 👤 User Registration System
- Secure patient ID system (format: HST-YYYY-XXXX)
- Comprehensive user profiles with medical history
- Multi-user support with login/logout functionality

### 🩺 Symptom Analysis
- Natural language symptom input with keyword matching
- Customized remedy suggestions based on symptoms
- Symptom severity rating system (scale of 1-4)
- Critical symptom alerts for potentially serious conditions

### 📊 Health Tracking
- Longitudinal symptom tracking across days and weeks
- Visual representation of health trends
- Recovery stage monitoring (ongoing, improving, recovered)
- Pattern recognition for recurring symptoms

### 💊 Medication Management
- Medication tracking with dosage and frequency
- Custom reminder system for medication adherence
- Special instructions and start date tracking

### 🧠 Personalized Health Advice
- Customized recommendations based on symptom history
- Seasonal health advice tailored to current month
- Hostel-specific lifestyle adjustments
- Dietary recommendations based on symptoms

### 📚 Research Component
- Information on common seasonal diseases
- First-aid measures and precautions for each disease
- Focused on conditions relevant to student populations

### 🔒 Data Management
- Secure health logs with user information
- Data backup and export capabilities (CSV format)
- Comprehensive health data visualization

### 🏥 Emergency Resources
- Information about nearby medical facilities
- Emergency contact details
- Operating hours and specialties

## 💻 Technical Implementation
- Modular Python code with clear organization
- Efficient data structures for symptom matching
- Persistent storage with JSON and text files
- Color-coded interface (with optional colorama integration)
- Robust input validation and error handling

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Colorama (optional for enhanced visual experience)

### Installation
1. Clone this repository:
```bash
git clone https://github.com/marrihemanth/Health-Alert-Bot-for-Hostel-Students.git
cd Health-Alert-Bot-for-Hostel-Students
```

2. Install optional dependencies:
```bash
pip install colorama
```

3. Run the Health Alert Bot:
```bash
python health_alert_bot.py
```

## 📝 Usage Guide

1. **First-time setup**: Register as a new user to get your patient ID
2. **Record symptoms**: Enter your symptoms when unwell to get remedy suggestions
3. **Track health trends**: Monitor your symptoms over time to identify patterns
4. **Manage medications**: Keep track of prescribed medicines and set reminders
5. **Get personalized advice**: Receive tailored health recommendations
6. **Learn about seasonal diseases**: Stay informed about common health issues

## 🔍 Project Structure
- `health_alert_bot.py`: Main Python script containing all features
- `health_log.txt`: File storing user health logs
- `user_profiles.json`: File storing user registration information
- `medications.json`: File storing medication data

## 📸 Screenshots

[Screenshots will be added soon]

## 🧪 Future Enhancements
- Mobile app integration
- Machine learning for symptom pattern recognition
- Integration with wearable health devices
- Telemedicine appointment scheduling
- Nutritional planning based on health conditions

## 👥 Contributors
- [Your Name](https://github.com/marrihemanth)

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.