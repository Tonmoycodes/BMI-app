# 🩺 Health Monitor App

**Developed by:** **Tonmoy Buragohain**

## Overview

Health Monitor App is a simple Python command-line application that helps users calculate and interpret two important health metrics:

* **Body Mass Index (BMI)**
* **Blood Pressure (BP)**

The application provides instant results along with basic health recommendations based on standard medical guidelines. It is designed for educational purposes and can serve as a beginner-friendly healthcare utility.

---

## Features

### 1. BMI Calculator

The BMI module allows users to:

* Calculate Body Mass Index (BMI)
* Determine BMI category
* Estimate healthy body weight using the Devine Formula
* Suggest whether the user should gain or lose weight

### BMI Categories

| BMI            | Category          |
| -------------- | ----------------- |
| Below 18.5     | Underweight       |
| 18.5 – 24.9    | Normal Weight     |
| 25.0 – 29.9    | Overweight        |
| 30.0 – 34.9    | Obesity Class I   |
| 35.0 – 39.9    | Obesity Class II  |
| 40.0 and above | Obesity Class III |

---

### 2. Blood Pressure Monitor

The Blood Pressure module provides:

* Mean Arterial Pressure (MAP)
* Pulse Pressure (PP)
* Blood Pressure Category
* Lifestyle suggestions based on the result

### Blood Pressure Categories

| Category             | Systolic (mmHg) | Diastolic (mmHg) |
| -------------------- | --------------- | ---------------- |
| Normal               | <120            | and <80          |
| Elevated             | 120–129         | and <80          |
| Hypertension Stage 1 | 130–139         | or 80–89         |
| Hypertension Stage 2 | ≥140            | or ≥90           |
| Hypertensive Crisis  | ≥180            | or ≥120          |

---

## Technologies Used

* Python 3
* Functions
* Conditional Statements
* User Input
* Basic Mathematical Calculations

---

## How to Run

1. Make sure Python 3 is installed.
2. Save the source code as `health_monitor.py`.
3. Open a terminal or command prompt.
4. Run the program:

```bash
python health_monitor.py
```

5. When prompted, enter the report you want:

```text
BMI
```

or

```text
BP
```

6. Enter the requested values to receive your health report.

---

## Example

### BMI

```text
Enter what report you want: BMI
Enter your weight in kgs: 70
Enter your height in m: 1.75
Enter your gender: Male

Your BMI is 22.86
You have a Normal weight
Your healthy weight is 70.46 Kgs
No bulking or cutting needed
```

### Blood Pressure

```text
Enter what report you want: BP
Enter your systolic: 120
Enter your diastolic: 80

Your Mean Arterial Pressure is 93.33 mmHg
Your Pulse Pressure is 40 mmHg
You have Hypertension Stage 1
```

---

## Medical Disclaimer

This application is intended **for educational and informational purposes only**.

* It is **not** a medical device.
* It does **not** diagnose medical conditions.
* BMI and Blood Pressure classifications are based on generally accepted clinical guidelines.
* Always consult a qualified healthcare professional for medical advice, diagnosis, or treatment.
* If you experience symptoms such as chest pain, severe headache, difficulty breathing, confusion, weakness, or vision changes, seek emergency medical care immediately.

---

## Future Improvements

* Streamlit Web Interface
* Graphical Health Dashboard
* Data Storage and History
* Blood Sugar Monitoring
* Heart Rate Analysis
* Health Report Export (PDF)
* User Authentication
* Interactive Charts

---

## Author

**Tonmoy Buragohain**

Thank you for checking out this project. Feedback and suggestions are always welcome!
