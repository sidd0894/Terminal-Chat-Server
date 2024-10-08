# Terminal Chat Server
This is a terminal based chat where multiple users can connect to the server and communicate with each other.

## About this Project
The Python project is made using `socket` module for real-time communication between clients (users) and a server and `threading` module for managing multiple concurrent connections and ensuring that the server can handle communication with multiple clients simultaneously.

## How to run this project?
To run this follow the steps given below-
1. **Install python**: <br>
Get python from [python.org](https://www.python.org/downloads/) if you don't have it yet. This project is compatible with Python 3.x.

2. **Download or Clone the Repository**: <br>
Download the zip of this repository  from the green 'Code' button on top or you can clone this repository using the following command:
   ```
   git clone <repository-url>
   ```

3. **Navigate to the directory** where the repository is saved in your system, then go into the directory named `main` and open terminal in that directory.

4. Now run the command in the terminal accordingly:

    If you want to start a server:
    ```
    python server.py
    ```
    Or
    
    If you want to connect to a server as a client:
    ```
    python client.py
    ```

# Disclaimer

This chat application is designed for educational purposes and may not be suitable for production use. It currently lacks robust encryption and authentication features, so communications are sent in plaintext and could be intercepted by third parties. 

**Security Warning:**
- **Encryption:** This application does not use encryption for communications. Any data exchanged between clients can be intercepted.
- **Authentication:** The application does not include authentication mechanisms to verify user identity.

**Usage Recommendations:**
- Use this application only in a controlled, secure environment.
- Do not use it for sensitive or confidential communications.

**Dependencies:**
- This project depends on [socket](https://docs.python.org/3/library/socket.html) and [threading](https://docs.python.org/3/library/threading.html). Ensure these libraries are up to date to avoid known vulnerabilities.

By using this project, you acknowledge that you understand these limitations and risks.
