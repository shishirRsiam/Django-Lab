# Setting Up Django + PostgreSQL Connection

## Prerequisites

- **Python Installed**: Ensure Python is installed on your system.
- **Django Installed**: Ensure Django is installed on your system. You can install it using pip:
  ``` bash
  pip install django
  ```
- **PostgreSQL Installed**: Ensure PostgreSQL is installed on your system. You can download it [here](https://www.postgresql.org/download/).

## Steps

- **Database Created**: Open PgAdmin and create a database. For this example, we will use `SiamDB` as the database name.

- **Create Your Django Project**: Use the following command to create your Django project. You can use any name you like:
  ```bash
  django-admin startproject postgreSQLConnection
  ```

## Connection Settings

- Open your project directory and navigate to the `postgreSQLConnection/settings.py` file.

- Make sure to **remove the old SQLite database code**:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

- Replace it with the following code to connect to the PostgreSQL database:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'SiamDB',       # Your database name
            'USER': 'postgres',      # Your PostgreSQL username
            'PASSWORD': '123456',    # Your PostgreSQL password
            'HOST': 'localhost',     # Set to 'localhost' if running locally
            'PORT': '5432',          # Default PostgreSQL port
        }
    }
    ```

This code establishes a connection to the PostgreSQL database named `SiamDB` using the specified username and password. Adjust the values as necessary for your setup.


## Additional Steps

1. **Install psycopg or psycopg2**: Django requires `psycopg` or `psycopg2` to connect to PostgreSQL. Install it using pip:
   ```bash
   pip install psycopg
   pip install psycopg2
   ```

2. **Apply Migrations**: After configuring the database, apply migrations to set up the initial database structure:
   ```bash
   python manage.py migrate
   ```

3. **Run the Development Server**: Start the Django development server to verify the connection:
   ```bash
   python manage.py runserver
   ```

   If everything is set up correctly, you should see no database-related errors in the terminal, indicating a successful connection to PostgreSQL.

## Common Troubleshooting Tips

- **Connection Refused**: Ensure PostgreSQL is running and that the `HOST` and `PORT` settings are correct.
- **Authentication Error**: Verify the `USER` and `PASSWORD` values in `settings.py` match your PostgreSQL credentials.
- **Firewall and Network Access**: If you're connecting to a remote PostgreSQL server, ensure firewall settings allow access to the database server and adjust configurations in `pg_hba.conf` if necessary.

---

This guide provides a complete setup for integrating Django with PostgreSQL in your project.