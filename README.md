# SnapClass — AI Attendance System

SnapClass is a smart classroom attendance app that uses facial recognition and voice recognition to automatically mark student attendance, removing the need for manual roll calls.

## Features
- Teacher and student login/registration
- Face enrollment and recognition-based attendance
- Voice enrollment and recognition-based attendance
- Subject/class management for teachers
- QR-based enrollment sharing
- Attendance logs and history per subject

## Tech Stack
- **Frontend/App**: Streamlit
- **Backend/Database**: Supabase (PostgreSQL)
- **Face Recognition**: `face_recognition`, `dlib`
- **Voice Recognition**: `resemblyzer`, `librosa`

## Setup

1. Clone the repo and install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a Supabase project and set up the required tables (see `src/database/db.py` for schema).

3. Add your credentials to `.streamlit/secrets.toml`:
   ```toml
   SUPABASE_URL = "your-project-url"
   SUPABASE_PUBLISHABLE_KEY = "your-publishable-key"
   ```

4. Run the app:
   ```
   streamlit run app.py
   ```
