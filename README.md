# Django + Vue.js app example
## Installation
Backend is dockerized, so build up and serve the containers, then run Django migrations

```bash
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
```
Done. API is served at http://localhost:8000/

Now serve the client
```bash
cd client
yarn install
yarn serve
```
Enjoy, app is ready to play with, client is served at http://localhost:8080/
