
# Employee Management System




## Demo

[Deployed demo](http://homeserver3995.tplinkdns.com/)


## Deployment



> Edit .env file and settings.py to match you credentials
**You can edit the database credentials in the docker-compose files**

**Step - 1** 
```bash
  docker-compose -f docker-compose.prod.yml up -d --build
```
**Step - 2** 

```bash
  docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
**Step - 3** 

```bash
  docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```
**Step - 4** 
* You will be propted to enter first superuser account credentials

```bash
  docker-compose exec web python manage.py createsuperuser
```

**Deleting**
```bash
  docker-compose -f docker-compose.prod.yml down -v
```
## License

[MIT](https://choosealicense.com/licenses/mit/)

