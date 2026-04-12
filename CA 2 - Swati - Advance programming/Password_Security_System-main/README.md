# Password Security & Breach Detection System

## Project Overview
The Password Security & Breach Detection System is a cybersecurity-focused web application developed using Python and Flask. The system helps users create secure passwords, analyze password strength, detect compromised credentials, and prevent unsafe password practices.

This project was developed as part of the **Advanced Programming Techniques** module and demonstrates secure software development, API integration, authentication, testing, and modular system architecture.

---

## Problem Statement
Many users rely on weak or reused passwords, which exposes them to security breaches and credential theft. This system addresses the problem by:

- Evaluating password strength
- Detecting breached passwords
- Preventing password reuse
- Providing password generation tools
- Maintaining security logs

---

## Features

### Authentication System
- User registration
- Secure login system
- Session-based authentication
- Logout functionality

### Password Analysis
- Password strength evaluation
- Entropy calculation
- Pattern detection
- Password reuse detection

### Breach Detection
- Checks if a password appears in known breaches using a secure API-based method

### Password Generator
- Automatically generates secure passwords

### Logging & Monitoring
- Tracks user password checks
- Security logs dashboard

---

## System Architecture
The system follows a **Layered Architecture**:
Presentation Layer → HTML Templates
Business Logic → Python Modules
Data Layer → SQLite Database
External Services → Breach API

---

## Technologies Used
- Python
- Flask (Web Framework)
- SQLite (Database)
- HTML / CSS (Frontend)
- bcrypt (Password Hashing)
- Requests (API Communication)

---

## Project Structure
password-security-system/
│
├── app.py
├── requirements.txt
├── README.md
├── database.py
├── database.db
├── auth.py
│
├── password_checker.py
├── breach_checker.py
├── password_generator.py
├── entropy_calculator.py
├── pattern_checker.py
│
├── history.py
├── logger.py
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── logs.html
│
├── static/
│ └── style.css
│
├── tests/
│ ├── test_password.py
│ ├── test_breach.py
│ ├── test_generator.py
│ ├── test_entropy.py
│ ├── test_pattern.py
│ ├── test_auth.py
│ ├── test_history.py
│ ├── test_database.py
│ ├── test_logs.py

