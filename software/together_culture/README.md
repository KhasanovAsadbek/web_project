# Together Culture

Together Culture is a Community Interest Company that gathers a membership community united in their desire to help create a more equitable and ecological creative economy. This Django project provides facilities, creative leadership, and entrepreneurial skills development, momentum, structure, and resources for people to come together and make change happen.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/together_culture.git
   cd together_culture
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Insert initial data into the database:
   ```bash
   python manage.py insert_initial_data
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application:
   Open your web browser and go to `http://127.0.0.1:8000/`

## Usage

- Home Page: Provides an overview of Together Culture.
- Search Members: Allows you to search for members by name.
- Search Events: Allows you to search for events by name.
- Add Member: Allows you to add a new member to the database.