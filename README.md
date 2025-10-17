# Dynamic Profile API

Backend Wizards Stage 0 Task - A dynamic profile endpoint with Cat Facts API integration.

## Features

- GET `/me` endpoint returns profile information in JSON format
- Dynamic cat facts from external Cat Facts API
- Real-time UTC timestamps in ISO 8601 format
- Proper error handling and fallback mechanisms
- Deployed on Railway

## API Response Format

```json
{
  "status": "success",
  "user": {
    "email": "ameeahmedy@gmail.com",
    "name": "Ahmed Anwar",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-17T13:11:34.293071+00:00",
  "fact": "In ancient Egypt, mummies were made of cats, and embalmed mice were placed with them in their tombs. In one ancient city, over 300,000 cat mummies were found."
}
```
## Local Development

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation & Setup

1. **Clone the repository**
2. **Create and activate virtual environment**
3. **Install dependencies**
4. **Set up environment variables**
5. **Run the development server**
6. **Test your API**

## Dependencies
Django==4.2.7
djangorestframework==3.14.0
requests==2.31.0
python-dotenv==1.0.0
gunicorn==21.2.0

## Environment Variables
PROFILE_EMAIL=your.email@example.com
PROFILE_NAME=Your Full Name  
PROFILE_STACK=Your Backend Stack
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1