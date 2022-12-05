# Django + Vue.js CRUD app example
## Installation
Backend is dockerized, so build up and serve the containers, then run Django migrations

```bash
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
```