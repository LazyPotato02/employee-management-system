# softuni-final-project

RUN IN PRODUCTION STATE
- docker-compose -f docker-compose.prod.yml up -d --build
- docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
- docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

RUN IN DEVELOPMENT STATE:
- docker compose up -d
- docker-compose exec web python manage.py migrate
- docker-compose exec web python manage.py createsuperuser


Setting up groups for properly user experience
```
To make the app function properly you need to log into the admin panel and add 2 groups viewer and editor:

    STEP #1: Set up groups and permissions 
        
    Log into django admin panel with the admin credentials and create 2 groups:

        - Editor:
            should have all permissions for cells,employees,materials,orders
        - Viewer:
            should have only Can view permission for cells,employees,materials,orders


    - EVERY NEW USER HAS Viewer GROUP(If you want a user with Viewer group to log in into the admin panel
    you need to give him the staff status with the superuser account you created first)
        -You can do this step for the Editor group too

    


    
TO MAKE THE APP FUNCTION PROPERLY YOU NEED TO LOG INTO THE ADMIN PANEL
```

REBUILDING DOCKER:
docker-compose -f docker-compose.prod.yml down -v

docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear