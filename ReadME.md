# Facebook Login

This project implements a simple Django application to simulate a Facebook-like login page. It stores login attempts (including username and password) in a database and redirects users to a specific link upon form submission.

---

## Features

- **Custom Login Page:** A styled HTML login form inspired by Facebook's interface.
- **Database Logging:** Captures and stores username, password, and timestamp for every login attempt.
- **Redirection:** Redirects users to a predefined URL upon form submission.
- **Responsive Design:** Ensures the login page works seamlessly across devices.

---

## Project Structure

1. **Models:** Defines a `LoginAttempt` model to log login attempts, including username, password, and the timestamp of each attempt.
2. **Views:** Handles rendering of the login form and processes form submissions by saving login attempts to the database and redirecting users to a predefined URL.
3. **URL Configuration:** Maps the root URL to the login view for serving the login page.
4. **Templates:** Includes a styled HTML login form inspired by Facebook's login interface, designed for responsiveness.

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/TewodrosAdimas/fb.git
   cd fb
   ```

2. **Install Dependencies:**
   Ensure you have Django installed. If not, install it:
   ```bash
   pip install django
   ```

3. **Run Migrations:**
   Set up the database by applying migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Server:**
   Start the development server:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## License

This project is for educational purposes only and should not be used in production without significant modifications to ensure data security. 

---

