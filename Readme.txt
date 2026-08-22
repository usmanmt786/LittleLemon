Little Lemon API Paths
=======================

Base URL: http://127.0.0.1:8000

HTML home page:
- GET /restaurant/

Menu API:
- GET, POST /restaurant/menu-items/
- GET, PUT, DELETE /restaurant/menu-items/<id>/

Table booking API:
- GET, POST /restaurant/booking/tables/
- GET, PUT, PATCH, DELETE /restaurant/booking/tables/<id>/

Authentication:
- POST /restaurant/api-token-auth/
- POST /auth/users/
- POST /auth/token/login/
- POST /auth/token/logout/

Protected endpoint:
- GET /restaurant/message/

User API:
- GET, POST /restaurant/users/
- GET, PUT, PATCH, DELETE /restaurant/users/<id>/

Send the token in the Authorization header when testing protected endpoints:
Authorization: Token <token>
