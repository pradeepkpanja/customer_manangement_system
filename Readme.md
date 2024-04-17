# Contact Management System Web Application 📇

Welcome to our **Contact Management System** web application! This powerful tool allows users to efficiently manage their contacts with various functionalities. Let's get started! 🚀

Developed By: Pradeep Panja c0864407 and Aishwinder Singh - c0866875

## Getting Started

To run this application locally on your PC, follow these steps:

1. **Clone the Repository**:
   - Clone this repository to your local machine using the following command:
     ```bash
     git clone https://github.com/pradeepkpanja/customer_manangement_system.git
     ```

2. **Navigate to the Project Directory**:
   - Move into the project directory using the `cd` command:
     ```bash
     cd contact_manager_project
     ```

3. **Set Up Virtual Environment (Optional but Recommended)**:
   - It's recommended to create a virtual environment to isolate dependencies. Use the following command to create a virtual environment (assuming you have Python installed):
     ```bash
     python -m venv venv
     ```

4. **Activate the Virtual Environment**:
   - Activate the virtual environment. The command varies based on your operating system:
     - For Windows:
       ```bash
       venv\Scripts\activate
       ```
     - For Unix/Linux:
       ```bash
       source venv/bin/activate
       ```

5. **Install Dependencies**:
   - Use `pip` to install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

6. **Set Up the Database**:
   - Run the database migrations to set up the initial database schema:
     ```bash
     python manage.py migrate
     ```

7. **Run the Development Server**:
   - Start the development server with the following command:
     ```bash
     python manage.py runserver
     ```

8. **Access the Application**:
   - Once the server is running, open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 

9. **Register and Log In**:
   - You'll need to register as a new user and then log in to start managing your contacts.

Enjoy organizing your contacts efficiently! 📞📧👥

For more detailed tutorials and examples, explore resources like [PythonTutorial.net's Django Tutorial](https://www.pythontutorial.net/django-tutorial/) and [Real Python's Get Started With Django](https://realpython.com/get-started-with-django-1/). 📚🌐
