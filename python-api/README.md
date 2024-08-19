# Encrypt Decrypt API

A simple Python API application to encrypt and decrypt messages using the Fernet symmetric encryption method.

## Requirements

- Python 3.7+
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/belpamulle/boowalla.git
   cd boowalla/python-api


2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

3. Install the required dependencies:

```pip install -r requirements.txt
```

## Running the Application
1. Set the AUTH_TOKEN and ENABLE_AUTH as needed in the app.py file.
2. Run the application:
`python app.py
   `
   The API will be accessible at http://localhost:5000.

## API Endpoints

### Encrypt Message
URL: `/api/encrypt`
Method: POST
Request Body:
```
{
    "data": "Your message",
    "key": "Your key"
}

```

### Decrypt Message
URL: `/api/decrypt`
Method: POST
Request Body:
```
{
    "data": "Encrypted message",
    "key": "Your key"
}

```
