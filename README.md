# Ecommerce Project API

This project is an ecommerce API with various features for admins, managers, delivery crew, and customers.

## Installation

### Install Pipenv

Pipenv is a tool that aims to bring the best of all packaging worlds to the Python world. It harnesses Pipfile, pip, and virtualenv into one single command. Here's how you can install it:

```bash
pip install pipenv
```

### Activate virtual environment
```bash
pipenv shell
```

### Install Django and Django Rest Framework
With your Pipenv environment activated, you can install Django and Django Rest Framework:
```bash
pipenv install django djangorestframework
```

## API Endpoints
```bash
/api/categories/ #(GET, POST): Endpoint for retrieving and creating categories.
/api/Menu-Items/ #(GET, POST): Endpoint for retrieving and creating menu items.
/api/MenuItem/<int:pk>/ #(GET, PUT, DELETE): Endpoint for retrieving, updating, and deleting a specific menu item.
/api/Cart/ #(GET, POST): Endpoint for retrieving and creating items in the cart.
/api/Orders/ #(GET, POST): Endpoint for retrieving and creating orders.
/api/Order/<int:pk>/ #(GET, PUT, DELETE): Endpoint for retrieving, updating, and deleting a specific order.
/api/groups/manager/users #(GET, POST, DELETE): Endpoint for listing, creating, and deleting users in the manager group.
/api/groups/delivery-crew/users #(GET, POST, DELETE): Endpoint for listing, creating, and deleting users in the delivery crew group.
```

## Features
### Admin Features
1. Assign users to the manager group.
2. Add menu items.
3. Add categories.

### Manager Features
1. Log in.
2. Update the item of the day.
3. Assign users to the delivery crew.
4. Assign orders to the delivery crew.

### Delivery Crew Features
1. Access orders assigned to them.
2. Update an order as delivered.

### Customer Features
1. mRegister.
2. Log in using their username and password and get access tokens.
3. Browse all categories.
4. Browse all the menu items at once.
5. Browse menu items by category.
6. Paginate menu items.
7. Sort menu items by price.
8. Add menu items to the cart.
9. Access previously added items in the cart.
10. Place orders.
11. Browse their own orders.


## Insomnia Testing
Here are the screenshots of the API endpoints tested in Insomnia and in Browser:

#### Creating category using Admin token
![alt text](Screen shots/image.png)

#### Creating category using non-admin or non-staff token
![alt text](Screen shots/image-1.png)

#### Listing menu items -> GET method
![alt text](Screen shots/image-2.png)

#### Creating menu-items using admin token -> POST method
![alt text](Screen shots/image-3.png)

#### Retriving single order
![alt text](Screen shots/image-4.png)

#### Listing all orders
![alt text](Screen shots/image-5.png)