# Application of Translation between French and Vietnamese - Request API, Deploy Application

![Project Image](https://img.freepik.com/premium-photo/flags-france-vietnam-divided-diagonally_698953-12872.jpg)

## 🚀 Introduction

This project aims to connect to the Azure Translator API and execute a request to translate the entered text from French to Vietnamese. The goal will then be to deploy a mini-application via Heroku.

## 🎮 Prerequisites

- **Python 3.11**
- **Flask 2.2.3**
- **Requests 2.31.0**
- **Gunicorn 20.1.0**
- **Werkzeug 2.2.2**

## 🛠️ Technos Used

- **Microsoft Azure**
- **Heroku**
- **Python**

## 🇲🇫➡️🇻🇳 Output 

Test the application here:
https://cryptic-beach-96708-dc6294d8f009.herokuapp.com/translate

## 🛠️ Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/StanEM75/API_Cloud-Translator_French_Vietnamese.git
    cd API_Cloud-Translator_French_Vietnamese
    ```

2. **Create and activate a virtual environment:**
The goal is to avoid conflicts between packages.

    ```bash
    python -m venv myenv
    source myenv/bin/activate
    ```

3. **Install dependencies:**
We need these packages to have a working project.

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
Need to set environment variables for the Azure Translator API. The `.env` file in the project directory will store the actual values:

    ```plaintext
    SUBSCRIPTION_KEY=your_subscription_key
    ENDPOINT=your_endpoint_url
    LOCATION=your_location
    ```

5. **Run the application:**
It creates a local application on the computer.

    ```bash
    python app.py
    ```

6. **Login on Heroku for the deployment:**

    ```bash
    heroku login
    ```

7. **Create a Heroku app:**

    ```bash
    heroku create
    ```

8. **Push the files to the Heroku project:**

    ```bash
    git add .
    git commit -m "Initial commit"
    git push heroku master
    ```

9. **Set the environment variables**

    ```bash
    heroku config:set SUBSCRIPTION_KEY=your_subscription_key --app <app>
    heroku config:set ENDPOINT=your_endpoint --app <app>
    heroku config:set LOCATION=your_location --app <app>
    ```

10. **Launch the application**

    ```bash
    heroku open
    ```




