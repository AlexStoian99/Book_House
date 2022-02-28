# BookHouse
BookHouse is an application developed for libraries, it contains a SQLite database, the main technologies are Python, Django, HTML, CSS, JavaScript, jQuery, Ajax.
## Dependencies
 Dependencies for the project are handled using Pipenv. Use `pip install --user --upgrade pipenv pip` to update your **pip** and **pipenv** packages. 
 Afterwards use `pipenv install --dev --deploy --ignore-pipfile` to create the Python virtual environment with all the project's dependencies.
 You can use `pipenv shell` to start a shell in the new venv, or use `pipenv run <command>` for running commands inside the venv.

 If additional dependencies are required during development, use `pipenv install <package>` (for packages required in production) or 
 `pipenv install --dev <package>` (for development tasks) to install the package, include it in the Pipfile and update the Pipfile.lock.

 ## Style formatting
 This project contains several tools used to adapt styling to PEP8 conventions, organize imports and check for poor code design.

 For code formatting use `isort polls` and `autopep8 --in-place --recursive polls`.
 For running static checks use `isort -c polls`, `flake8 polls` and `pylint polls`.
 
 ## About the project 
 The main functionalities:
  - crud operations
  - login and register
  - access restrictions for users
  - notifications
 The following images represent the functionality of the application
 
 <img width="1440" alt="Screenshot 2022-02-28 at 09 21 01" src="https://user-images.githubusercontent.com/75396991/155949820-7bca180f-85f7-4af8-b1fa-343d7381b397.png">
 <img width="1440" alt="Screenshot 2022-02-28 at 10 36 03" src="https://user-images.githubusercontent.com/75396991/155951107-a2edfe46-5c93-4993-87c0-e187569a92bc.png">
 <img width="1440" alt="Screenshot 2022-02-28 at 09 21 49" src="https://user-images.githubusercontent.com/75396991/155949857-4a268715-dd0e-4a82-81c3-8b0a29e433ea.png">
 <img width="1438" alt="Screenshot 2022-02-28 at 09 20 44" src="https://user-images.githubusercontent.com/75396991/155949740-c5920fbe-0a65-43e0-823c-cb56134882bd.png">
<img width="1440" alt="Screenshot 2022-02-28 at 09 21 16" src="https://user-images.githubusercontent.com/75396991/155949850-7c38f08a-b4e7-42b0-b0a7-03f4f024442f.png">
<img width="1440" alt="Screenshot 2022-02-28 at 09 22 05" src="https://user-images.githubusercontent.com/75396991/155949865-de0d6417-f281-4d75-9ed9-80f0eee4654a.png">
<img width="1440" alt="Screenshot 2022-02-28 at 09 22 27" src="https://user-images.githubusercontent.com/75396991/155949871-a08c7461-9410-4139-8965-00968502c001.png">
