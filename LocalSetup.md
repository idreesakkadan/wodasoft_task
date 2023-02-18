### Setting up in local machine
- Clone from the repository.
- Install Postgres if Not installed already 
- Create database and user based on the settings
- Grant all permissions for that user on that database
- Run the application 


##### Setting up virtual environemnt 
- Make sure to install python3.10
- Run the command : virtualenv .venv --python=python3.10

##### Creating local database
- Create database using the command, CREATE DATABASE database_name;
- Create database user using the command ,CREATE USER database_user  WITH PASSWORD 'password';
- ALTER ROLE database_user SET client_encoding TO 'utf8';
- ALTER ROLE database_user SET default_transaction_isolation TO 'read committed';
- ALTER ROLE database_user SET timezone TO 'UTC';
- GRANT ALL PRIVILEGES ON DATABASE database_name TO database_user;
- GRANT CREATE ON DATABASE database_name TO database_user ;


##### Setting up initial migrations 
- Before running the application, make sure we set up the migrations.
- RUN python manage.py migrate command!
- Now to create a super user, run the command: python manage.py createsuperuser
- After that, enter the user details.