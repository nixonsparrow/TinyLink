# TinyLink
Shorten your urls, make your links user-friendly

## Tests

To run tests, call:

```
$ python manage.py test
```

## Functionality

To run project, call:

```
$ python manage.py runserver
```

Endpoints
```
/           # GET, POST
/<code>     # GET
```

To create a shortened link just make POST request:
```
POST ENDPOINT: /
CONTENT:
{
    "original": "YOUR LINK TO SHORTEN"
}
```

To list all shortened links just make GET request:
```
GET ENDPOINT: /
EXAMPLE CONTENT:
[
    {
        "id": 1,
        "original": "http://google.com",
        "short": "anowlx",
        "created_at": "2023-05-12T12:30:00.683869Z"
    },
    {
        "id": 2,
        "original": "http://postman.com",
        "short": "juwplf",
        "created_at": "2023-05-12T12:30:29.728659Z"
    }
]
```

To get redirection link use short attribute of created link:

```
EXAMPLE GET ENDPOINT: /anowlx/
```
And you will be redirected to the original link provided 
for the object with exact short code (or 404 if not existing).