# Django App with API


Designing and implementing a Django application with a RESTful API to manage several entities: Profession, Skill, and Topic. 


## Features

* Documentation at /api/doc/swagger/
* CRUD operations for Professions
* CRUD operations for Skills
* CRUD operations for Topics


## How to run with Docker

Docker should be installed.


Create `.env` file with your variables (look at `.env.sample`
file, don't change `POSTGRES_DB` and `POSTGRES_HOST`).


```shell
docker-compose build
docker-compose up
```


###    Use the following command in docker desktop backend_task-app-1 terminal to load prepared data from fixture:
```
    python manage.py loaddata sample_data1.json
```