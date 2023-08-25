# Basic news site 


## Initial setup

```py
python manage.py migrate
python manage.py createsuperuser
```

Fire it up:
```py
python manage.py runserver
```

## Set up sections

The home page template starts with three sections:
- Hero slot
- Top News
- Latest News

To populate these sections on the home page, in admin, go to 'Homepage sections' and add these sections:
- hero
- top_news
- latest

*(These names are hard coded in the template.)*
