# Tasks Overview

This repository contains the implementation of a web application with a responsive frontend and a Django chat application, along with AWS Lambda functions.

## Frontend Development

The frontend of this project consists of a responsive webpage with the following features:

1. **Navbar**  
   A fixed navbar at the top of the page that does not move when scrolling.

2. **Three Sections**  
   - **Left Menu**: A collapsible menu on the left side.
   - **Main Content Area**: The center area where the primary content is displayed.
   - **Right-Side Panel**: A panel on the right side for additional information or widgets.

3. **Footer**  
   A footer section at the bottom of the page.

4. **Responsive Shrinking**  
   A JavaScript function that dynamically adjusts the page width based on the screen size. The following width adjustments are implemented:
   - Screen width between 992px and 1600px: Shrink the page by 90%.
   - Screen width between 700px and 767px: Shrink the page by 80%.
   - Screen width between 600px and 700px: Shrink the page by 75%.
   - Screen width less than or equal to 600px: Shrink the width to 50%.

## Django Chat Application

The Django chat application includes the following features:

1. **User Authentication**  
   Users can sign up, log in, and access the chat application.

2. **User List**  
   A collapsible left menu displays all registered users.

3. **Initiate Chat**  
   The logged-in user can select any user from the left menu and initiate a chat with them.

4. **Message Storage**  
   All user data and chat messages are stored in the database.

5. **Retrieve Old Messages**  
   Old messages are retrieved and displayed in the chat interface.

6. **Real-time Chat**  
   WebSocket is used for real-time messaging in the chat application.

7. **User-Friendly Interface**  
   The chat interface is designed to be intuitive and easy to use.

## AWS Lambda Functions

1. **Add Two Numbers**  
   An AWS Lambda function that adds two numbers and returns the result.

2. **Store File in S3**  
   An AWS Lambda function that stores a document or PDF file in an S3 bucket.

## How to Run the Project

1. **Clone the Repository**  
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/your-username/repository-name.git
## To run Frontend
    Change the directory to Task 1. Responsive_website, "cd Task 1. Responsive_website"
    Either use VS Code extension "Go live"
    Or use directly "localhost:8000"
    Note: Do not forget to uncomment the lines(72, 73), to see the shrik function execution
## To run Django Project
    Change the directory to Task 2. django-project/chat, "cd Task 2. django-project/chat"
    Install "django", "pip install django"
    Run, "python manage.py runserver"
    Note: While testing the chat messages I have made it simple, so we have  to refresh the application to see communication. (Time begin I have not made it realtime chat app).
## AWS Tasks are in the file. Self Explanatory
    The Sample events(tested) and outputs are in the file.

## Samples of Chat app
    Note: While testing the chat messages I have made it simple, so we have  to refresh the application to see communication. (Time begin I have not made it realtime chat app).

![Screenshot 2025-01-18 130412](https://github.com/user-attachments/assets/634e3f93-b42f-44b8-852b-344b4ba258ae)
![Screenshot_2025-01-18-13-04-13-27_3aea4af51f236e4932235fdada7d1643](https://github.com/user-attachments/assets/c91c0ec8-c21a-480f-aa23-0ecb1b28ae9c)
Note: While testing the chat messages I have made it simple, so we have  to refresh the application to see communication. (Time begin I have not made it realtime chat app).

# Thank You!
