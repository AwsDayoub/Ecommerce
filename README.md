### Ecommerce Project 
Welcome to the Ecommerce project! This project is built using Django and React, providing a robust ecommerce website with features such as user registration, product catalog, shopping cart, adding products, and viewing orders.

## Getting Started
To get started with the Ecommerce project, follow the instructions below:

# Prerequisites:
- Python (version 3.7 or above)
- Node.js (version 12 or above)
- npm (Node Package Manager)

# Installation

1. Clone the project repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/ecommerce-project.git```

2. Change into the project directory:

   ```shell
   cd Ecommerce
   ```
3. Set up the backend:
   - create virtual environment:
     ```shell
     cd Ecommerce-backend-
     ```
  - activate virtual environment:
      - for windows:
        ```shell
          venv\Scripts\activate
        ```
      - for mac and linux:
          ```shell
              source venv/bin/activate
          ```
  - install the backend depandicies:
      ```shell
        pip install -r requirements.txt
      ```
  - apply database migrations:
    ```shell
        python manage.py migrate
    ```
  - start the django development server:
      ```shell
        python manage.py runserver
      ```
    The backend server will be accessible at http://localhost:8000.

4. Set up the frontend:
   - Change into the frontend directory:
       ```shell
         cd Ecommerce-frontend-
       ```
   - Install the frontend dependencies:
       ```shell
         npm install
       ```
   - Start the React development server:
       ```shell
           npm start
         ```
    The frontend server will be accessible at http://localhost:3000.
   
## Features

The Ecommerce project includes the following main features:

  - Registration: Users can create accounts and log in to the website.
  - Product catalog: Users can browse and search for products.
  - Shopping cart: Users can add products to their shopping cart and proceed to checkout.
  - Add product: Admin users can add new products to the catalog.
  - View orders: Admin users can view and manage orders placed by customers.
      
   
