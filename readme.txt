Django Project inside littlelemon-capstone folder

APIs paths to Test:

Login:
/auth/token/login/

Logout:
/auth/token/logout/

Restaurant homepage:
/restaurant/

Menu/Menu Items Endpoints:
/restaurant/menu-items/ or /restaurant/menu/
/api/menu-items or /api/menu

Single Menu Item Endpoints
/restaurant/menu-items/<int:pk> or /restaurant/menu/<int:pk>
/api/menu-items/<int:pk> or /api/menu/<int:pk>

GET or POST: /restaurant/booking/tables/
GET, PUT, or DELETE: /restaurant/booking/tables/<int:pk> 

Api Root Endpoint
/auth/

User List
/auth/users/

User List
/auth/users/<username>