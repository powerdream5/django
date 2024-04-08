## Overview

This repository contains the source code for a compact team member management application built with the Django framework. It demonstrates the utilization of Django's features, including model forms and generic class-based views like ListView, CreateView, and UpdateView.

## Starting the Application
Once you have cloned the repository, navigate to the root directory. Ensure Docker and Docker Compose are installed on your system. You can then start the application with the following command:
```bash
docker-compose up --build
```

After the application has successfully started, access it by opening [http://localhost:3000](http://localhost:8000) in your web browser.
<br/>

## Unit Testing
To conduct unit testing for this project, first ensure `pipenv` is installed on your system. Activate the virtual environment from the root directory using:
```bash
pipenv shell
```

Next, run the following command:
```bash
python manage.py test --setting=instawork.settings_test team/tests
```
