"""
💊 Health Alert Bot for Hostel Students

🔹 STEP 1: Symptom Input + Session Output
Task:
✔️ Allow the user to input symptoms (comma-separated text)
✔️ Validate the input (no blanks allowed)
✔️ Display a simple session output confirming symptoms received

🔹 STEP 2: Remedy Suggestion Based on Symptoms
Task:
✔️ Match user input symptoms to known symptom keywords
✔️ Use keyword synonyms to improve accuracy
✔️ Suggest remedies based on identified symptoms

🔹 STEP 3: Log Storage
Task:
✔️ After showing remedies, ask user if they want to save the log
✔️ If yes, write symptoms with current date/time to 'health_log.txt'
✔️ Append mode so multiple logs are saved over time

🔹 STEP 4: Critical Symptoms Alert
Task:
✔️ Define symptoms that need urgent medical attention
✔️ Use this list to trigger alerts for users

🔹 STEP 5: Daily Health Tracker
Task:
✔️ Track recurring symptoms across days
✔️ Identify most frequent symptoms
✔️ Show health trends and patterns

🔹 STEP 6: Customized Advice
Task:
✔️ Provide personalized health recommendations based on symptom history
✔️ Identify patterns and suggest lifestyle adjustments
✔️ Offer targeted preventive measures
yes 
🔹 STEP 8: User Registration System
Task:
✔️ Collect user personal details
✔️ Assign a unique patient number
✔️ Store user profiles for future sessions

🔹 STEP 9: Medication Tracking System
Task:
✔️ Track medications prescribed to students
✔️ Set reminders for medication times
✔️ Monitor medication adherence

🔹 STEP 10: Symptom Severity Rating
Task:
✔️ Allow users to rate severity of their symptoms
✔️ Track changes in symptom intensity over time
✔️ Provide targeted advice based on severity
"""

# Import modules
import datetime
import os
import json
import random
import string
import time
from collections import Counter
from datetime import datetime, timedelta
import csv
from datetime import date
import shutil
try:
    from colorama import init, Fore, Back, Style
    COLORAMA_AVAILABLE = True
    init()  # Initialize colorama
except ImportError:
    COLORAMA_AVAILABLE = False

# Symptom keywords dictionary
SYMPTOM_KEYWORDS = {
    "fever": ["fever", "high temperature", "hot body"],
    "sore throat": ["throat pain", "sore throat", "scratchy throat"],
    "cough": ["cough", "dry cough", "wet cough"],
    "cold": ["cold", "runny nose", "sneezing"],
    "headache": ["headache", "head pain", "migraine"],
    "body ache": ["body ache", "muscle pain", "joint pain"],
    "diarrhea": ["diarrhea", "loose motion"],
    "vomiting": ["vomiting", "throwing up"],
    "fatigue": ["tiredness", "fatigue", "weakness"],
    "nausea": ["nausea", "feeling sick", "queasy"]
}

# Remedies dictionary
REMEDIES = {
    "fever": "Take paracetamol, rest, and stay hydrated. Cold compress may help.",
    "sore throat": "Gargle with warm salt water, suck on throat lozenges, drink warm tea with honey.",
    "cough": "Drink warm fluids, use honey (if not allergic), and stay in a humid environment.",
    "cold": "Rest, drink plenty of fluids, and use saline nasal drops.",
    "headache": "Rest in a dark quiet room, apply cold or warm compress, and take paracetamol if needed.",
    "body ache": "Rest, take warm baths, gentle stretching, and proper hydration.",
    "diarrhea": "Stay hydrated with ORS, eat bland foods, and avoid dairy and spicy foods.",
    "vomiting": "Sip clear fluids slowly, avoid solid foods, and try ginger tea.",
    "fatigue": "Get adequate rest, stay hydrated, and eat nutritious foods.",
    "nausea": "Try ginger tea, eat small frequent meals, and avoid strong odors."
}

# Critical symptoms that need urgent medical attention
CRITICAL_SYMPTOMS_ALERT = [
    "fever", "breathing difficulty", "chest pain", "vomiting", "diarrhea", "unconscious", "high fever"
]

# Dictionary of common health conditions based on symptom combinations
HEALTH_CONDITIONS = {
    frozenset(["fever", "cough", "sore throat"]): {
        "condition": "Common Cold or Flu",
        "advice": "Rest, stay hydrated, and boost immunity with vitamin C. Consider wearing a mask if you live in a hostel to prevent spreading."
    },
    frozenset(["headache", "fatigue"]): {
        "condition": "Stress or Lack of Sleep",
        "advice": "Practice stress management techniques like deep breathing. Ensure 7-8 hours of sleep. Take short breaks during study sessions."
    },
    frozenset(["nausea", "vomiting", "diarrhea"]): {
        "condition": "Food Poisoning or Stomach Bug",
        "advice": "Be careful about where you eat. Avoid mess food that looks undercooked or has been sitting out for long periods."
    },
    frozenset(["headache", "body ache", "fever"]): {
        "condition": "Viral Infection",
        "advice": "Maintain hygiene in shared spaces. Don't share personal items with roommates when sick."
    }
}

# Seasonal health advice based on current month
SEASONAL_ADVICE = {
    # Winter months
    1: "Winter season: Stay warm, boost immunity with vitamin C, and be cautious of seasonal flu.",
    2: "Late winter: Keep hydrated despite cold weather, and be vigilant about flu symptoms.",
    # Spring months
    3: "Spring: Watch out for seasonal allergies. Keep windows closed during high pollen times.",
    4: "Mid-spring: Allergy season is high. Consider antihistamines if you have allergies.",
    5: "Late spring: Stay hydrated as temperatures rise and protect against sun exposure.",
    # Summer months
    6: "Early summer: Prevent dehydration. Drink plenty of water, especially before sports.",
    7: "Peak summer: Heat exhaustion risk is high. Avoid midday sun and drink electrolytes.",
    8: "Late summer: Continue hydration and watch for fungal infections in humid weather.",
    # Fall months
    9: "Early fall: Transitional weather can trigger cold symptoms. Keep a jacket handy.",
    10: "Mid-fall: Flu season begins. Consider getting a flu shot at the campus health center.",
    11: "Late fall: Cold and flu season in full swing. Boost immunity and practice good hygiene.",
    # Winter again
    12: "Early winter: Cold season peak. Keep warm and wash hands frequently."
}

# User profiles storage
USER_PROFILES_FILE = "user_profiles.json"
MEDICATIONS_FILE = "medications.json"

SEVERITY_LEVELS = {
    1: "Mild - Noticeable but not interfering with daily activities",
    2: "Moderate - Somewhat interfering with daily activities",
    3: "Severe - Significantly interfering with daily activities",
    4: "Very Severe - Unable to perform daily activities"
}

# Nearby medical facilities data
MEDICAL_FACILITIES = [
    {
        "name": "University Health Center",
        "address": "Campus Main Building, Ground Floor",
        "contact": "123-456-7890",
        "hours": "Mon-Fri: 8:00 AM - 8:00 PM, Sat: 9:00 AM - 2:00 PM",
        "emergency": False
    },
    {
        "name": "City General Hospital",
        "address": "123 Healthcare Avenue, 2km from campus",
        "contact": "123-555-9999",
        "hours": "24/7",
        "emergency": True
    },
    {
        "name": "Campus Pharmacy",
        "address": "Student Union Building, First Floor",
        "contact": "123-456-7000",
        "hours": "Mon-Fri: 9:00 AM - 6:00 PM",
        "emergency": False
    }
]

# Dietary recommendations based on symptoms
DIETARY_RECOMMENDATIONS = {
    "fever": ["Clear broths", "Herbal teas", "Fresh fruits high in vitamin C", "Stay hydrated with water and electrolyte drinks"],
    "sore throat": ["Warm soups", "Honey with warm water or tea", "Soft foods like yogurt", "Avoid spicy and acidic foods"],
    "cough": ["Honey (unless allergic)", "Ginger tea with honey", "Warm liquids", "Avoid dairy which can thicken mucus"],
    "cold": ["Chicken soup", "Citrus fruits", "Garlic", "Spicy foods to clear sinuses"],
    "headache": ["Stay hydrated", "Magnesium-rich foods like nuts and seeds", "Avoid processed foods", "Limit caffeine"],
    "body ache": ["Anti-inflammatory foods like turmeric and ginger", "Omega-3 rich foods", "Hydrating foods", "Avoid processed foods"],
    "diarrhea": ["BRAT diet (Bananas, Rice, Applesauce, Toast)", "Clear liquids", "Avoid dairy and spicy food", "Avoid high-fiber foods"],
    "vomiting": ["Small sips of clear liquids", "Ice chips", "Avoid solid foods until vomiting stops", "Ginger tea"],
    "fatigue": ["Iron-rich foods like leafy greens", "Protein-rich foods", "Complex carbohydrates", "Avoid sugar and processed foods"],
    "nausea": ["Ginger", "Small, frequent meals", "Avoid greasy and spicy foods", "Stay hydrated with small sips"]
}

# Helper functions for colorized output
def colorize(text, color=None, bg=None, style=None):
    """Add color to terminal text if colorama is available"""
    if not COLORAMA_AVAILABLE:
        return text
    
    colored_text = ""
    if color:
        colored_text += getattr(Fore, color.upper())
    if bg:
        colored_text += getattr(Back, bg.upper())
    if style:
        colored_text += getattr(Style, style.upper())
        
    colored_text += text + Style.RESET_ALL
    return colored_text

def print_header(text):
    """Print a formatted header"""
    if COLORAMA_AVAILABLE:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}{text}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'-' * 40}{Style.RESET_ALL}")
    else:
        print(f"\n{text}")
        print("-" * 40)

def generate_patient_number():
    """Generate a unique patient number in format HST-YYYY-XXXX"""
    year = datetime.now().year
    random_chars = ''.join(random.choices(string.digits, k=4))
    return f"HST-{year}-{random_chars}"

def load_user_profiles():
    """Load existing user profiles from file"""
    if not os.path.exists(USER_PROFILES_FILE):
        return {}
    
    try:
        with open(USER_PROFILES_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading user profiles: {e}")
        return {}

def save_user_profiles(profiles):
    """Save user profiles to file"""
    try:
        with open(USER_PROFILES_FILE, "w") as file:
            json.dump(profiles, file, indent=4)
    except Exception as e:
        print(f"Error saving user profiles: {e}")

def load_medications():
    """Load medications data from file"""
    if not os.path.exists(MEDICATIONS_FILE):
        return {}
    
    try:
        with open(MEDICATIONS_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading medications: {e}")
        return {}

def save_medications(medications_data):
    """Save medications data to file"""
    try:
        with open(MEDICATIONS_FILE, "w") as file:
            json.dump(medications_data, file, indent=4)
    except Exception as e:
        print(f"Error saving medications: {e}")

def validate_input(prompt, required=True, input_type="text"):
    """Validate user input based on type and requirements"""
    while True:
        value = input(prompt).strip()
        
        if not value and required:
            print("❌ This field is required. Please try again.")
            continue
            
        if input_type == "number" and value:
            if not value.isdigit():
                print("❌ Please enter a valid number.")
                continue
                
        if input_type == "email" and value:
            if "@" not in value or "." not in value:
                print("❌ Please enter a valid email address.")
                continue
                
        return value

def register_user():
    """Register a new user and assign a patient number"""
    print("\n📋 User Registration")
    print("-" * 40)
    
    # Collect user information
    name = validate_input("Enter your full name: ")
    age = validate_input("Enter your age: ", input_type="number")
    gender = validate_input("Enter your gender (M/F/Other): ").upper()
    hostel_room = validate_input("Enter your hostel room number: ")
    contact_number = validate_input("Enter your contact number: ", input_type="number")
    emergency_contact = validate_input("Enter emergency contact number: ", input_type="number")
    email = validate_input("Enter your email (optional): ", required=False, input_type="email")
    medical_history = validate_input("Any pre-existing medical conditions (optional): ", required=False)
    
    # Generate unique patient number
    patient_number = generate_patient_number()
    
    # Create user profile
    user_profile = {
        "patient_number": patient_number,
        "name": name,
        "age": age,
        "gender": gender,
        "hostel_room": hostel_room,
        "contact_number": contact_number,
        "emergency_contact": emergency_contact,
        "email": email,
        "medical_history": medical_history,
        "registration_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Load existing profiles
    profiles = load_user_profiles()
    
    # Add new profile
    profiles[patient_number] = user_profile
    
    # Save updated profiles
    save_user_profiles(profiles)
    
    print(f"\n✅ Registration successful!")
    print(f"🔢 Your patient number is: {patient_number}")
    print("Please remember this number for future sessions.")
    
    return user_profile

def user_login():
    """Handle user login or registration"""
    profiles = load_user_profiles()
    
    print("\n🔐 User Login / Registration")
    print("-" * 40)
    print("1. I have a patient number")
    print("2. I'm a new user")
    
    while True:
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            patient_number = input("Enter your patient number: ").strip()
            if patient_number in profiles:
                print(f"\n👋 Welcome back, {profiles[patient_number]['name']}!")
                return profiles[patient_number]
            else:
                print("❌ Patient number not found.")
                if input("Would you like to register as a new user? (yes/no): ").strip().lower() in ["yes", "y"]:
                    return register_user()
                else:
                    continue
        
        elif choice == "2":
            return register_user()
        
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

# Symptom input function
def get_symptoms():
    symptoms_input = input("Enter your symptoms (separated by commas): ").strip()

    if not symptoms_input:
        print("❌ Symptoms input cannot be blank.")
        return None

    raw_inputs = [s.strip().lower() for s in symptoms_input.split(",") if s.strip()]
    
    if not raw_inputs:
        print("❌ No valid symptoms entered.")
        return None

    matched_symptoms = []
    for raw in raw_inputs:
        matched = False
        for key_symptom, keywords in SYMPTOM_KEYWORDS.items():
            if any(k in raw for k in keywords):
                matched_symptoms.append(key_symptom)
                matched = True
                break
        if not matched:
            matched_symptoms.append(raw)  # still log it

    print("\n🩺 Symptoms detected:")
    for symptom in matched_symptoms:
        print(f"- {symptom.capitalize()}")

    return matched_symptoms

# Function to suggest remedies based on matched symptoms
def suggest_remedies(matched_symptoms):
    if not matched_symptoms:
        print("\n❓ I couldn't match your symptoms to any known conditions.")
        print("Please try describing them differently or consult a medical professional.")
        return

    print("\n💊 Suggested remedies:")
    for symptom in matched_symptoms:
        if symptom in REMEDIES:
            print(f"\n🔸 For {symptom.capitalize()}:")
            print(f"  {REMEDIES[symptom]}")

"""
🟡 STEP 4: Critical Symptom Alert Function
Task:
✔️ Check if any entered symptom matches the critical symptom list
✔️ If yes, display a doctor consultation warning message
"""

def check_consultation_alert(symptoms_list):
    alert_needed = any(symptom in CRITICAL_SYMPTOMS_ALERT for symptom in symptoms_list)

    if alert_needed:
        print("\n⚠️ Alert: Some of your symptoms are potentially serious.")
        print("🩺 Recommendation: Please consult a doctor if symptoms persist more than 2–3 days.")

# Function to save logs to file
def save_log(symptoms_list, user_profile=None):
    """Save symptoms log with user information"""
    while True:
        choice = input("Do you want to save this log? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            with open("health_log.txt", "a") as log_file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"Date: {timestamp}\n")
                
                # Add user information if available
                if user_profile:
                    log_file.write(f"Patient: {user_profile['name']} (ID: {user_profile['patient_number']})\n")
                    log_file.write(f"Age: {user_profile['age']}, Room: {user_profile['hostel_room']}\n")
                
                log_file.write("Symptoms: " + ", ".join(symptoms_list) + "\n")
                log_file.write("-" * 40 + "\n")
            print("✅ Log saved successfully.")
            break
        elif choice in ["no", "n"]:
            print("🗃️ Log not saved.")
            break
        else:
            print("❌ Invalid input. Please type 'yes' or 'no'.")

"""
🔴 STEP 5: Daily Health Tracker
Task:
✔️ Analyze health logs to identify recurring symptoms
✔️ Track symptoms frequency over time
✔️ Display health trends and patterns to the user
"""

def parse_health_logs():
    """Parse the health_log.txt file and extract dates and symptoms"""
    if not os.path.exists("health_log.txt"):
        return []
    
    logs = []
    try:
        with open("health_log.txt", "r") as file:
            current_date = None
            current_symptoms = []
            
            for line in file:
                line = line.strip()
                if line.startswith("Date:"):
                    # Save previous entry if exists
                    if current_date and current_symptoms:
                        logs.append((current_date, current_symptoms))
                    
                    # Start new entry
                    date_str = line[5:].strip()
                    try:
                        current_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                        current_symptoms = []
                    except ValueError:
                        current_date = None
                
                elif line.startswith("Symptoms:"):
                    symptoms_str = line[9:].strip()
                    current_symptoms = [s.strip().lower() for s in symptoms_str.split(",")]
            
            # Add the last entry if exists
            if current_date and current_symptoms:
                logs.append((current_date, current_symptoms))
                
        return logs
    except Exception as e:
        print(f"Error reading health log: {e}")
        return []

def analyze_recent_symptoms(days=7):
    """Analyze symptoms from the past specified number of days"""
    logs = parse_health_logs()
    if not logs:
        return None
    
    # Get current date (based on the date you mentioned in context)
    current_date = datetime.now()
    cutoff_date = current_date - timedelta(days=days)
    
    # Filter logs from the past specified days
    recent_logs = [(date, symptoms) for date, symptoms in logs if date >= cutoff_date]
    
    if not recent_logs:
        return None
    
    # Count symptoms
    all_symptoms = []
    for _, symptoms in recent_logs:
        all_symptoms.extend(symptoms)
    
    symptom_counts = Counter(all_symptoms)
    return symptom_counts

def show_health_trends():
    """Display health trends based on logged symptoms"""
    print("\n📊 Health Trends Analysis")
    print("-" * 40)
    
    # Check if health log exists
    if not os.path.exists("health_log.txt"):
        print("No health logs found. Start logging your symptoms to see trends.")
        return
    
    # Analyze recent symptoms (past week)
    recent_symptoms = analyze_recent_symptoms(7)
    if not recent_symptoms:
        print("No recent health logs found from the past week.")
        return
    
    # Show most common symptoms
    print("🔄 Your most frequent symptoms in the past week:")
    for symptom, count in recent_symptoms.most_common(3):
        if count > 1:
            print(f"  • {symptom.capitalize()}: {count} times")
    
    # Check for recurring symptoms (symptoms that appear more than once)
    recurring = [symptom for symptom, count in recent_symptoms.items() if count > 1]
    if recurring:
        print("\n⚠️ Recurring symptoms detected:")
        for symptom in recurring:
            print(f"  • You've had {symptom} {recent_symptoms[symptom]} times this week")
            if symptom in CRITICAL_SYMPTOMS_ALERT:
                print(f"    🔴 Note: {symptom.capitalize()} is a critical symptom. Consider medical attention.")
    
    print("\n💡 Health Insight:")
    if recurring:
        print("  Recurring symptoms may indicate an ongoing health issue.")
        print("  Consider consulting a healthcare professional if symptoms persist.")
    else:
        print("  No recurring symptoms detected in the past week. Keep monitoring your health!")

def get_customized_advice(user_symptoms):
    """Generate customized health advice based on user's symptom history"""
    
    advice_list = []
    
    # 1. Check for matched health conditions based on symptom combinations
    user_symptom_set = frozenset(user_symptoms)
    
    for condition_symptoms, details in HEALTH_CONDITIONS.items():
        # Check if the user's symptoms match or are a subset of a known condition
        if condition_symptoms.issubset(user_symptom_set) or user_symptom_set.issubset(condition_symptoms):
            if len(condition_symptoms.intersection(user_symptom_set)) >= 2:  # At least 2 matching symptoms
                advice_list.append(f"🔍 Based on your symptoms, you might be experiencing: {details['condition']}")
                advice_list.append(f"🧠 Hostel-specific advice: {details['advice']}")
    
    # 2. Add seasonal advice based on current month
    current_month = datetime.now().month
    advice_list.append(f"🌦️ Seasonal health tip: {SEASONAL_ADVICE[current_month]}")
    
    # 3. Check symptom history for personalized advice
    recent_symptoms = analyze_recent_symptoms(7)
    if recent_symptoms:
        recurring = [symptom for symptom, count in recent_symptoms.items() if count > 1]
        
        if recurring:
            advice_list.append("\n🔄 Based on your recurring symptoms:")
            
            # Specific advice for recurring symptoms
            if "headache" in recurring:
                advice_list.append("  • For recurring headaches: Ensure proper lighting when studying. Take screen breaks every 30 minutes.")
            
            if "sore throat" in recurring:
                advice_list.append("  • For recurring sore throat: Check if your room is too dry. Consider a humidifier or placing a bowl of water near your bed.")
            
            if "fatigue" in recurring:
                advice_list.append("  • For persistent fatigue: Evaluate your sleep schedule. Avoid caffeine after 4 PM.")
            
            if "cold" in recurring or "cough" in recurring:
                advice_list.append("  • For ongoing cold/cough: Your room may be dusty. Consider cleaning air vents and changing bedding more frequently.")
            
            if "fever" in recurring:
                advice_list.append("  • For recurring fever: This requires medical attention. Please visit your hostel's medical center or nearby hospital.")
    
    # If no specific advice could be generated
    if not advice_list:
        advice_list.append("📝 General advice: Maintain a balanced diet, stay hydrated, and get enough rest.")
        advice_list.append("💪 For students: Balance study with physical activity. Take 5-minute breaks every hour while studying.")
    
    return advice_list

def show_customized_advice(symptoms):
    """Display customized health advice to the user"""
    print("\n🧠 Generating Customized Health Advice...")
    print("-" * 40)
    
    advice_list = get_customized_advice(symptoms)
    
    for advice in advice_list:
        print(advice)
    
    print("\n⚠️ Remember: This bot provides basic guidance only. For persistent issues, please consult a healthcare professional.")

"""
🔴 STEP 7: Research Component
Task:
✔️ Provide information about 5 common seasonal diseases
✔️ Include first-aid and precautionary measures for each
"""

# Research data for common seasonal diseases
SEASONAL_DISEASES = {
    "Common Cold": {
        "description": "A viral infection affecting the nose and throat, often caused by rhinoviruses.",
        "first_aid": "Rest, stay hydrated, and use over-the-counter decongestants or pain relievers.",
        "precautions": "Wash hands frequently, avoid close contact with sick individuals, and maintain good hygiene."
    },
    "Influenza (Flu)": {
        "description": "A contagious respiratory illness caused by influenza viruses.",
        "first_aid": "Rest, drink plenty of fluids, and take antiviral medications if prescribed.",
        "precautions": "Get vaccinated annually, avoid crowded places during flu season, and practice good hygiene."
    },
    "Dengue Fever": {
        "description": "A mosquito-borne viral infection causing high fever, severe headache, and joint pain.",
        "first_aid": "Rest, stay hydrated, and take paracetamol for fever. Avoid aspirin or ibuprofen.",
        "precautions": "Use mosquito repellents, wear long-sleeved clothing, and eliminate standing water around living areas."
    },
    "Heat Exhaustion": {
        "description": "A condition caused by prolonged exposure to high temperatures, leading to dehydration.",
        "first_aid": "Move to a cool place, drink water or electrolyte solutions, and rest.",
        "precautions": "Stay hydrated, avoid outdoor activities during peak heat, and wear light, breathable clothing."
    },
    "Allergic Rhinitis": {
        "description": "An allergic reaction causing sneezing, runny nose, and itchy eyes, often triggered by pollen.",
        "first_aid": "Use antihistamines, decongestants, or nasal sprays as needed.",
        "precautions": "Keep windows closed during high pollen times, use air purifiers, and avoid outdoor activities when pollen counts are high."
    }
}

def show_research_component():
    """Display information about common seasonal diseases and their first-aid measures"""
    print("\n📚 Research on Common Seasonal Diseases")
    print("-" * 40)
    
    for disease, details in SEASONAL_DISEASES.items():
        print(f"\n🔹 {disease}")
        print(f"  Description: {details['description']}")
        print(f"  First Aid: {details['first_aid']}")
        print(f"  Precautions: {details['precautions']}")
    
    print("\n💡 Tip: Stay informed and take preventive measures to protect your health during seasonal changes.")

# Update main menu to include registration system
def main():
    while True:  # Outer loop for user login sessions
        print("\n=== Welcome to the Health Alert Bot for Hostel Students ===")
        print("A health monitoring system designed for hostel students")
        
        # Check if colorama is available
        if not COLORAMA_AVAILABLE:
            print("\nTip: Install colorama for improved visual experience:")
            print("Run: pip install colorama")
        
        # User login or registration
        current_user = user_login()
        
        # Check medication reminders immediately after login
        check_medication_reminders(current_user)
        
        while True:  # Inner loop for current user session
            print_header(f"Health Alert Bot | Patient: {current_user['name']} | ID: {current_user['patient_number']}")
            print("1. Record new symptoms")
            print("2. View health trends")
            print("3. Get customized health advice")
            print("4. Learn about seasonal diseases")
            print("5. Manage medications")
            print("6. Track recovery progress")
            print("7. Nearby medical facilities")
            print("8. Dietary recommendations")
            print("9. Data management")
            print("10. Update personal information")
            print("11. Logout / Switch User")
            print("12. Exit application")
            
            choice = input("\nEnter your choice (1-12): ").strip()
            
            if choice == "1":
                # Record new symptoms with severity
                symptoms = get_symptoms()
                if symptoms:
                    suggest_remedies(symptoms)
                    check_consultation_alert(symptoms)
                    severity_ratings = rate_symptom_severity(symptoms)
                    save_log_with_severity(symptoms, severity_ratings, current_user)
                    show_dietary_recommendations(symptoms)
                    print(colorize("\n✅ Session completed.", color="green"))
                else:
                    print(colorize("\n⚠️ Please try entering your symptoms again.", color="yellow"))
            
            elif choice == "2":
                # View health trends with visualization
                visualize_health_data(current_user)
                show_health_trends()
            
            elif choice == "3":
                # Get customized health advice
                symptoms = get_symptoms()
                if symptoms:
                    show_customized_advice(symptoms)
                else:
                    print(colorize("\n⚠️ Please try entering your symptoms again.", color="yellow"))
            
            elif choice == "4":
                # Learn about seasonal diseases
                show_research_component()
            
            elif choice == "5":
                # Manage medications
                manage_medications(current_user)
            
            elif choice == "6":
                # Track recovery progress
                track_recovery(current_user)
            
            elif choice == "7":
                # Show nearby medical facilities
                show_nearby_medical_facilities()
            
            elif choice == "8":
                # Get dietary recommendations
                symptoms = get_symptoms()
                if symptoms:
                    show_dietary_recommendations(symptoms)
                else:
                    print(colorize("\n⚠️ Please try entering your symptoms again.", color="yellow"))
            
            elif choice == "9":
                # Data management submenu
                print_header("Data Management")
                print("1. Back up all data")
                print("2. Export my health records to CSV")
                print("3. Back to main menu")
                
                data_choice = input("\nEnter your choice (1-3): ").strip()
                
                if data_choice == "1":
                    backup_path = backup_user_data()
                    if backup_path:
                        print(f"Your data has been backed up to: {backup_path}")
                
                elif data_choice == "2":
                    export_health_data(current_user)
                
                elif data_choice == "3":
                    continue
                
                else:
                    print(colorize("\n❌ Invalid choice.", color="red"))
            
            elif choice == "10":
                # Update personal information
                new_user_profile = register_user()
                current_user = new_user_profile
                print(colorize("\n✅ Personal information updated successfully.", color="green"))
            
            elif choice == "11":
                # Logout and return to login screen
                print(colorize(f"\n👋 Goodbye, {current_user['name']}! Returning to login screen...", color="cyan"))
                break  # Break inner loop to return to login screen
            
            elif choice == "12":
                # Exit application completely
                print(colorize(f"\n👋 Thank you for using Health Alert Bot. Stay healthy!", color="green"))
                return  # Exit the entire function
            
            else:
                print(colorize("\n❌ Invalid choice. Please enter a number between 1 and 12.", color="red"))

def show_nearby_medical_facilities():
    """Display information about nearby medical facilities"""
    print_header("🏥 Nearby Medical Facilities")
    
    for facility in MEDICAL_FACILITIES:
        if facility["emergency"]:
            print(colorize(f"\n🚨 {facility['name']} (EMERGENCY SERVICES)", color="red", style="bright"))
        else:
            print(colorize(f"\n🔹 {facility['name']}", color="cyan"))
        
        print(f"  Address: {facility['address']}")
        print(f"  Contact: {facility['contact']}")
        print(f"  Hours: {facility['hours']}")
    
    print("\nℹ️ In case of medical emergency, please call campus security at 123-EMERGENCY")

def show_dietary_recommendations(symptoms):
    """Show dietary recommendations based on symptoms"""
    print_header("🍎 Dietary Recommendations")
    
    recommendations = set()
    for symptom in symptoms:
        if symptom in DIETARY_RECOMMENDATIONS:
            for rec in DIETARY_RECOMMENDATIONS[symptom]:
                recommendations.add(rec)
    
    if recommendations:
        print(colorize("Based on your symptoms, consider the following dietary adjustments:", color="green"))
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
    else:
        print("No specific dietary recommendations for your symptoms.")
        print("General advice: Stay hydrated, eat nutritious meals, and avoid processed foods.")
    
    print("\nNote: These are general recommendations. Consult a nutritionist for personalized advice.")

def rate_symptom_severity(symptoms):
    """Allow user to rate the severity of symptoms"""
    severity_ratings = {}
    
    print_header("📊 Symptom Severity Rating")
    print("Rate the severity of each symptom on a scale of 1-4:")
    
    for level, description in SEVERITY_LEVELS.items():
        print(f"{level} - {description}")
    
    for symptom in symptoms:
        while True:
            try:
                rating = int(input(f"\nRate the severity of '{symptom}' (1-4): ").strip())
                if 1 <= rating <= 4:
                    severity_ratings[symptom] = rating
                    break
                else:
                    print(colorize("❌ Please enter a number between 1 and 4.", color="red"))
            except ValueError:
                print(colorize("❌ Please enter a valid number.", color="red"))
    
    return severity_ratings

def save_log_with_severity(symptoms_list, severity_ratings, user_profile=None):
    """Save symptoms log with severity ratings"""
    while True:
        choice = input("Do you want to save this log? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            with open("health_log.txt", "a") as log_file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"Date: {timestamp}\n")
                
                # Add user information if available
                if user_profile:
                    log_file.write(f"Patient: {user_profile['name']} (ID: {user_profile['patient_number']})\n")
                    log_file.write(f"Age: {user_profile['age']}, Room: {user_profile['hostel_room']}\n")
                
                log_file.write("Symptoms: " + ", ".join(symptoms_list) + "\n")
                
                # Add severity ratings
                log_file.write("Severity Ratings:\n")
                for symptom, rating in severity_ratings.items():
                    log_file.write(f"  - {symptom}: {rating}/4 ({SEVERITY_LEVELS[rating]})\n")
                
                log_file.write("-" * 40 + "\n")
            print(colorize("✅ Log saved successfully with severity ratings.", color="green"))
            break
        elif choice in ["no", "n"]:
            print(colorize("🗃️ Log not saved.", color="yellow"))
            break
        else:
            print(colorize("❌ Invalid input. Please type 'yes' or 'no'.", color="red"))

# Recovery tracking stages
RECOVERY_STAGES = {
    "ongoing": "Symptoms still present, monitoring required",
    "improving": "Symptoms lessening, continue current remedies",
    "recovered": "Symptoms resolved, continue preventive measures"
}

def track_recovery(user_profile):
    """Track recovery progress for current health issues"""
    print_header("🔄 Recovery Tracking")
    
    # Get recent symptoms from logs for this user
    recent_logs = parse_health_logs_for_user(user_profile["patient_number"])
    
    if not recent_logs:
        print(colorize("No recent health logs found. Start logging your symptoms to track recovery.", color="yellow"))
        return
    
    # Group logs by date to see progression
    symptoms_by_date = {}
    for log_date, symptoms, severity in recent_logs:
        date_str = log_date.strftime("%Y-%m-%d")
        if date_str not in symptoms_by_date:
            symptoms_by_date[date_str] = []
        symptoms_by_date[date_str].append((symptoms, severity))
    
    # Display symptoms progression
    print(colorize("\nYour Symptoms Timeline:", color="cyan"))
    for date_str in sorted(symptoms_by_date.keys()):
        print(f"\n📅 {date_str}")
        for symptoms, severity in symptoms_by_date[date_str]:
            print(f"  Symptoms: {', '.join(symptoms)}")
            if severity:
                print("  Severity:")
                for symptom, rating in severity.items():
                    print(f"   - {symptom}: {rating}/4")
    
    # Calculate recovery stage
    recovery_stage = determine_recovery_stage(symptoms_by_date)
    
    print(colorize(f"\nRecovery Status: {recovery_stage.upper()}", color="green", style="bright"))
    print(f"  {RECOVERY_STAGES[recovery_stage]}")
    
    # Provide recovery recommendations
    if recovery_stage == "ongoing":
        print("\nRecommendations:")
        print("  • Continue following prescribed remedies")
        print("  • Keep monitoring your symptoms daily")
        print("  • Ensure adequate rest and hydration")
    elif recovery_stage == "improving":
        print("\nRecommendations:")
        print("  • Continue following prescribed remedies but at reduced frequency")
        print("  • Start gradually resuming normal activities")
        print("  • Maintain good nutrition and hydration")
    else:  # recovered
        print("\nRecommendations:")
        print("  • Resume normal activities")
        print("  • Continue preventive measures")
        print("  • Consider a follow-up health check if symptoms were serious")

def determine_recovery_stage(symptoms_by_date):
    """Determine recovery stage based on symptom progression"""
    dates = sorted(symptoms_by_date.keys())
    if len(dates) < 2:
        return "ongoing"  # Not enough data to determine progress
    
    # Get earliest and latest symptoms
    earliest_symptoms = []
    earliest_severity = {}
    for symptoms, severity in symptoms_by_date[dates[0]]:
        earliest_symptoms.extend(symptoms)
        if severity:
            earliest_severity.update(severity)
    
    latest_symptoms = []
    latest_severity = {}
    for symptoms, severity in symptoms_by_date[dates[-1]]:
        latest_symptoms.extend(symptoms)
        if severity:
            latest_severity.update(severity)
    
    # Check if all symptoms are gone
    if not latest_symptoms:
        return "recovered"
    
    # Check if fewer symptoms or lower severity
    if len(latest_symptoms) < len(earliest_symptoms):
        return "improving"
    
    # Check severity reduction
    if latest_severity and earliest_severity:
        total_earliest = sum(earliest_severity.values())
        total_latest = sum(latest_severity.values())
        if total_latest < total_earliest:
            return "improving"
    
    return "ongoing"

def parse_health_logs_for_user(patient_id):
    """Parse health logs for a specific user with severity ratings"""
    if not os.path.exists("health_log.txt"):
        return []
    
    logs = []
    try:
        with open("health_log.txt", "r") as file:
            current_date = None
            current_user = None
            current_symptoms = []
            current_severity = {}
            in_severity_section = False
            
            for line in file:
                line = line.strip()
                
                if line.startswith("Date:"):
                    # Save previous entry if exists
                    if current_date and current_symptoms and current_user == patient_id:
                        logs.append((current_date, current_symptoms, current_severity))
                    
                    # Reset for new entry
                    current_date = None
                    current_user = None
                    current_symptoms = []
                    current_severity = {}
                    in_severity_section = False
                    
                    # Parse new date
                    date_str = line[5:].strip()
                    try:
                        current_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        current_date = None
                
                elif line.startswith("Patient:"):
                    # Extract patient ID
                    if "ID:" in line:
                        id_part = line.split("ID:")[1].strip().rstrip(")")
                        current_user = id_part.strip()
                
                elif line.startswith("Symptoms:"):
                    symptoms_str = line[9:].strip()
                    current_symptoms = [s.strip().lower() for s in symptoms_str.split(",")]
                
                elif line.startswith("Severity Ratings:"):
                    in_severity_section = True
                
                elif in_severity_section and line.startswith("  -"):
                    # Parse severity rating
                    parts = line.split(":")
                    if len(parts) >= 2:
                        symptom = parts[0].strip().strip("- ")
                        rating_str = parts[1].split("/")[0].strip()
                        try:
                            rating = int(rating_str)
                            current_severity[symptom] = rating
                        except ValueError:
                            pass
                
                elif line.startswith("-" * 10):  # End of entry marker
                    in_severity_section = False
            
            # Add the last entry if exists
            if current_date and current_symptoms and current_user == patient_id:
                logs.append((current_date, current_symptoms, current_severity))
                
        return logs
    except Exception as e:
        print(f"Error reading health log: {e}")
        return []

def backup_user_data():
    """Create a backup of all user data"""
    print_header("💾 Data Backup")
    
    backup_dir = "health_bot_backup"
    backup_date = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{backup_dir}_{backup_date}"
    
    try:
        # Create backup directory
        os.makedirs(backup_path, exist_ok=True)
        
        # Copy data files
        files_to_backup = ["health_log.txt", USER_PROFILES_FILE, MEDICATIONS_FILE]
        
        for file in files_to_backup:
            if os.path.exists(file):
                shutil.copy2(file, os.path.join(backup_path, file))
        
        print(colorize(f"✅ Backup created successfully at {backup_path}", color="green"))
        return backup_path
    except Exception as e:
        print(colorize(f"❌ Backup failed: {e}", color="red"))
        return None

def export_health_data(user_profile):
    """Export user's health data to CSV format"""
    print_header("📊 Export Health Data")
    
    patient_id = user_profile["patient_number"]
    export_filename = f"health_data_{patient_id}_{datetime.now().strftime('%Y%m%d')}.csv"
    
    try:
        # Get user's health logs
        logs = parse_health_logs_for_user(patient_id)
        
        if not logs:
            print(colorize("No health data to export.", color="yellow"))
            return
        
        # Create CSV file
        with open(export_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            writer.writerow(["Date", "Symptoms", "Severity"])
            
            # Write log entries
            for log_date, symptoms, severity in logs:
                date_str = log_date.strftime("%Y-%m-%d %H:%M:%S")
                symptoms_str = ", ".join(symptoms)
                
                severity_str = ""
                for symptom, rating in severity.items():
                    severity_str += f"{symptom}:{rating}, "
                severity_str = severity_str.rstrip(", ")
                
                writer.writerow([date_str, symptoms_str, severity_str])
        
        print(colorize(f"✅ Health data exported to {export_filename}", color="green"))
    except Exception as e:
        print(colorize(f"❌ Export failed: {e}", color="red"))

def visualize_health_data(user_profile=None):
    """Create text-based visualization of health data trends"""
    print_header("📈 Health Data Visualization")
    
    # Get user health logs
    if user_profile:
        logs = parse_health_logs_for_user(user_profile["patient_number"])
    else:
        logs = parse_health_logs()
    
    if not logs:
        print(colorize("No health data available for visualization.", color="yellow"))
        return
    
    # Group symptoms by date
    symptom_trends = {}
    date_list = []
    
    for log_date, symptoms, _ in logs:
        date_str = log_date.strftime("%Y-%m-%d")
        
        if date_str not in date_list:
            date_list.append(date_str)
        
        for symptom in symptoms:
            if symptom not in symptom_trends:
                symptom_trends[symptom] = {}
            
            if date_str not in symptom_trends[symptom]:
                symptom_trends[symptom][date_str] = 0
            
            symptom_trends[symptom][date_str] += 1
    
    # Sort dates
    date_list.sort()
    
    # Find most common symptoms
    symptom_totals = Counter()
    for symptom, dates in symptom_trends.items():
        symptom_totals[symptom] = sum(dates.values())
    
    # Display top symptoms over time
    print("\n📊 Symptom Frequency Over Time:")
    
    for symptom, _ in symptom_totals.most_common(5):
        print(f"\n{symptom.capitalize()}:")
        
        # Create simple bar chart
        for date in date_list:
            count = symptom_trends[symptom].get(date, 0)
            bar = "█" * count if count > 0 else "."
            print(f"{date}: {bar} ({count})")
    
    print("\nLegend: Each █ represents one occurrence of the symptom on that date")

def manage_medications(user_profile):
    """Manage medications for the current user"""
    patient_id = user_profile["patient_number"]
    
    # Load existing medications data
    all_medications = load_medications()
    
    # Initialize user's medications if not exists
    if patient_id not in all_medications:
        all_medications[patient_id] = []
    
    user_medications = all_medications[patient_id]
    
    print_header("💊 Medication Management")
    
    while True:
        print("\n1. View my medications")
        print("2. Add a new medication")
        print("3. Remove a medication")
        print("4. Set medication reminders")
        print("5. Back to main menu")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            if not user_medications:
                print(colorize("\n❌ You don't have any medications saved.", color="yellow"))
            else:
                print(colorize("\n📋 Your Medications:", color="green"))
                for i, med in enumerate(user_medications, 1):
                    print(f"{i}. {med['name']} - {med['dosage']} - {med['frequency']}")
                    if 'reminders' in med and med['reminders']:
                        print(f"   🔔 Reminders: {', '.join(med['reminders'])}")
        
        elif choice == "2":
            med_name = input("Enter medication name: ").strip()
            med_dosage = input("Enter dosage (e.g., 500mg): ").strip()
            med_frequency = input("Enter frequency (e.g., twice daily): ").strip()
            med_instructions = input("Enter special instructions (optional): ").strip()
            
            new_med = {
                "name": med_name,
                "dosage": med_dosage,
                "frequency": med_frequency,
                "instructions": med_instructions,
                "start_date": datetime.now().strftime("%Y-%m-%d"),
                "reminders": []
            }
            
            user_medications.append(new_med)
            save_medications(all_medications)
            print(colorize("\n✅ Medication added successfully!", color="green"))
        
        elif choice == "3":
            if not user_medications:
                print(colorize("\n❌ You don't have any medications to remove.", color="yellow"))
            else:
                print(colorize("\n📋 Your Medications:", color="green"))
                for i, med in enumerate(user_medications, 1):
                    print(f"{i}. {med['name']} - {med['dosage']}")
                
                try:
                    med_index = int(input("\nEnter the number of the medication to remove (or 0 to cancel): ").strip())
                    if 1 <= med_index <= len(user_medications):
                        removed = user_medications.pop(med_index - 1)
                        save_medications(all_medications)
                        print(colorize(f"\n✅ Removed {removed['name']} from your medications.", color="green"))
                    elif med_index != 0:
                        print(colorize("\n❌ Invalid selection.", color="red"))
                except ValueError:
                    print(colorize("\n❌ Please enter a valid number.", color="red"))
        
        elif choice == "4":
            if not user_medications:
                print(colorize("\n❌ You don't have any medications to set reminders for.", color="yellow"))
            else:
                print(colorize("\n📋 Your Medications:", color="green"))
                for i, med in enumerate(user_medications, 1):
                    print(f"{i}. {med['name']} - {med['dosage']}")
                
                try:
                    med_index = int(input("\nEnter the number of the medication to set reminders for (or 0 to cancel): ").strip())
                    if 1 <= med_index <= len(user_medications):
                        selected_med = user_medications[med_index - 1]
                        
                        print(f"\nSetting reminders for {selected_med['name']}")
                        print("Enter times in 24-hour format (HH:MM), separated by commas.")
                        print("Example: 08:00, 14:00, 20:00")
                        
                        times = input("\nEnter reminder times: ").strip()
                        if times:
                            selected_med['reminders'] = [t.strip() for t in times.split(',')]
                            save_medications(all_medications)
                            print(colorize("\n✅ Reminders set successfully!", color="green"))
                        else:
                            print(colorize("\n❌ No reminder times provided.", color="yellow"))
                    elif med_index != 0:
                        print(colorize("\n❌ Invalid selection.", color="red"))
                except ValueError:
                    print(colorize("\n❌ Please enter a valid number.", color="red"))
        
        elif choice == "5":
            break
        
        else:
            print(colorize("\n❌ Invalid choice. Please enter a number between 1 and 5.", color="red"))

def check_medication_reminders(user_profile):
    """Check and display medication reminders"""
    patient_id = user_profile["patient_number"]
    
    # Load existing medications data
    all_medications = load_medications()
    
    if patient_id not in all_medications:
        return
    
    user_medications = all_medications[patient_id]
    current_time = datetime.now().strftime("%H:%M")
    current_hour = int(current_time.split(':')[0])
    current_minute = int(current_time.split(':')[1])
    
    due_medications = []
    
    for med in user_medications:
        if 'reminders' in med and med['reminders']:
            for reminder in med['reminders']:
                try:
                    reminder_hour = int(reminder.split(':')[0])
                    reminder_minute = int(reminder.split(':')[1])
                    
                    # Check if reminder is due (within the last hour)
                    time_diff = (current_hour - reminder_hour) * 60 + (current_minute - reminder_minute)
                    
                    if 0 <= time_diff < 60:  # Reminder is due within the last hour
                        due_medications.append(med)
                        break
                except (ValueError, IndexError):
                    continue
    
    if due_medications:
        print_header("🔔 MEDICATION REMINDERS")
        print(colorize("The following medications are due:", color="yellow"))
        
        for med in due_medications:
            print(f"- {med['name']} ({med['dosage']}): {med['frequency']}")
            if med['instructions']:
                print(f"  Instructions: {med['instructions']}")
        
        print("\nPlease take your medications on time!")

# Run the main function to start the program
if __name__ == "__main__":
    main()