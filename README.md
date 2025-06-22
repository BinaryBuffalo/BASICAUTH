Login Interface
This application provides a simple and secure login and registration interface built with Django. It's designed to be sleek and user-friendly, supporting both mobile and desktop browsers across all modern web browsers (Chrome, Brave, Edge, Safari, etc.).

Features
Captcha Security: Integrates django-simple-captcha for enhanced security.

User Authentication: Includes dedicated login and registration interfaces.

Input Fields: Provides fields for email and username input.

Input Validation: Robust validation for all input fields.

Redirection: Automatic redirection after successful login and registration.

Auto-Login: Users are automatically logged in after registration.

Credential Saving: Persists user credentials across page refreshes.

Responsive Design: Fully supports mobile and desktop browsers.

Cross-Browser Compatibility: Works seamlessly across modern web browsers.

Important Note
WARNING: This application is currently configured for development use only (DEBUG mode is enabled). It is not suitable for production environments. For production deployment, please use a WSGI or ASGI server. Refer to the official Django documentation for more information on deployment: https://docs.djangoproject.com/en/5.2/howto/deployment/

Setup
Follow these steps to get the application running on your local machine:

Install Dependencies:

pip install django-simple-captcha
pip install django
# If there are other specific dependencies, add them here
# pip install your-other-dependency

Run Migrations:

python manage.py migrate

Collect Static Files:

python manage.py collectstatic

Start the Development Server:

python manage.py runserver

Endpoints
Once the server is running, you can access the following endpoints:

Registration: http://localhost:8000/users/register/

Login: http://localhost:8000/users/login_view/

(Note: The default port for Django's development server is 8000. If you are using a different port, adjust 8000 accordingly.)

This application aims to provide a simple, sleek, and secure foundation for user authentication if implemented properly!
