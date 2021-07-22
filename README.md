# django-stock-app
Application for storing and displaying data about different stocks. Stocks data will be gathering from the web and displaying after logging into the app.

DjangoStockApp which scrapes informations about stock prices from last month. Website uses Celery and allows to easy set datarange for displaying prices.
All app is based on Django and djangorestframework. It uses two databases one for users and second for companies and their stocks prices. App has log in and logout system to authenticate users. It also ensures small API to receive data from databases. Celery scrapes data every day at midnight.


Link to heroku: https://drf-stock-app.herokuapp.com/
testing account: username:test password:test
