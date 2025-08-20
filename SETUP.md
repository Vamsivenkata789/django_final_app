
## 📁 Project Structure

```
module_registration_1/
├── module_registration/          # Main project directory
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   └── wsgi.py                  # WSGI configuration
├── core/                        # Core app (home, about, contact)
│   ├── management/commands/     # Custom management commands
│   ├── views.py                # Core views
│   └── urls.py                 # Core URLs
├── students/                    # Student management app
│   ├── models.py               # Student, EmailVerification, PasswordResetOTP
│   ├── views.py                # Authentication and profile views
│   ├── admin.py                # Custom admin configuration
│   └── urls.py                 # Student URLs
├── modules/                     # Module management app
│   ├── models.py               # Module and Registration models
│   ├── views.py                # Module listing and registration views
│   ├── admin.py                # Module admin configuration
│   └── urls.py                 # Module URLs
├── api/                         # REST API app
│   ├── views.py                # API viewsets and serializers
│   └── urls.py                 # API URLs
├── templates/                   # Template files
│   ├── base/                   # Base templates
│   ├── core/                   # Core app templates
│   ├── modules/                # Module app templates
│   └── students/               # Student app templates
├── static/                      # Static files
│   ├── css/                    # Custom CSS
│   └── js/                     # Custom JavaScript
├── media/                       # Media files (uploads)
├── requirements.txt             # Python dependencies
└── manage.py                   # Django management script
```

## 🚀 Running the Application

### Prerequisites
- Python 3.11+
- Virtual environment activated

### Setup Commands
```bash
# Navigate to project directory
cd d:\django\module_registration_1

# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run migrations
python3.11 manage.py migrate

# Create superuser (if needed)
python3.11 manage.py createsuperuser

# Populate sample data
python3.11 manage.py populate_sample_data

# Start development server
python3.11 manage.py runserver
```

### Access Points
- **Main Application**: http://127.0.0.1:8000/
- **Admin Interface**: http://127.0.0.1:8000/admin/
- **API Root**: http://127.0.0.1:8000/api/
- **API Token**: http://127.0.0.1:8000/api/auth/token/

## 📊 Sample Data

### Sample Students (Login Credentials)
- **Username**: `john_doe` | **Password**: `password123`
- **Username**: `jane_smith` | **Password**: `password123`
- **Username**: `bob_wilson` | **Password**: `password123`
- **Username**: `alice_brown` | **Password**: `password123`
- **Username**: `charlie_davis` | **Password**: `password123`

### Sample Modules
- CS101 - Introduction to Computer Science (3 credits)
- CS201 - Database Management Systems (4 credits)
- CS301 - Web Development (3 credits)
- DA101 - Data Analytics (3 credits)
- ML201 - Machine Learning (4 credits)
- SE301 - Software Engineering (3 credits)
- MAD201 - Mobile App Development (3 credits)
- CYB101 - Cybersecurity Fundamentals (3 credits)
- MKT201 - Digital Marketing (2 credits)
- PM101 - Project Management (2 credits)


## Database Configuration
For local development, use the following MySQL configuration:
```ini
[mysql]
user = root
password = 
database = universityportal
host = localhost
```