# BMI Calculator

The BMI Calculator project is a web-based application developed using the Django framework, which leverages Python for backend logic and data management. The project uses MySQL as the database management system to store user data, including name, age, weight, and height, ensuring robust and scalable data handling. HTML and CSS are employed for creating the user interface, with specific emphasis on designing responsive and visually appealing layouts. Static files, including images, are managed efficiently to enhance user experience. The core functionality of the application includes calculating the Body Mass Index (BMI) based on user inputs and providing tailored health suggestions based on BMI classifications. The project's frontend employs modern CSS techniques for styling, ensuring that elements are well-aligned and images are appropriately placed to complement the textual content. The integration of static files and the Django templating system allows for dynamic content rendering, making the application both functional and aesthetically pleasing.

## Getting Started

To run the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Avinep123/bmi_calculator.git
    cd bmi_calculator
    ```

2. **Create a database in MySQL:**

    ```sql
    CREATE DATABASE bmi;
    USE bmi;
    ```

3. **Configure the database settings:**

    Open `bmi_calculator/settings.py` and update the database configuration with your MySQL credentials user,password,port,host:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bmi',
            'USER': 'root',
            'PASSWORD': 'your_password',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

Your application should now be running at `http://127.0.0.1:8000/`.

## Usage

Visit the web application in your browser to use the BMI Calculator. Enter your details to calculate your BMI and receive health suggestions based on your BMI classification.


