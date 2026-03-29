# 1CIA FirstProject

This is a Django project containing multiple applications: `firstApp`, `userApp`, `sessionApp`, and `conferenceApp`.

## Prerequisites

- Python 3.10+
- Git

## Clone the Repository

```bash
git clone https://github.com/LindaOuer/PFW_1CIA_2526.git
cd PFW_1CIA_2526
```

## Setup and Testing Instructions

You can set up and run this project using either standard `pip` or `uv` (a extremely fast Python package and project manager).

### Option 1: Using `uv` (Recommended for speed)

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   *(For Windows or other methods, see the [uv documentation](https://docs.astral.sh/uv/))*

2. **Create a virtual environment**:
   ```bash
   uv venv
   ```

3. **Activate the virtual environment**:
   - On Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install dependencies**:

   **Option A: Using `requirements.txt`:**
   ```bash
   uv pip install -r requirements.txt
   ```
   
   **Option B: Install Django separately:**
   ```bash
   uv pip install django=="5.2.*"
   ```

5. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

### Option 2: Using standard `pip`

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies**:

   **Option A: Using `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```
   
   **Option B: Install Django separately:**
   ```bash
   pip install django=="5.2.*"
   ```

4. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
