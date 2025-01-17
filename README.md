
# Instagram Phishing Webpage Documentation

## 1. Project Overview
This project is a phishing simulation webpage designed for educational purposes and cybersecurity awareness. It mimics the Instagram login interface, capturing user credentials and storing them in a PostgreSQL database hosted on Render.com. The project aims to demonstrate the dangers of phishing attacks and educate users about preventive measures.

![alt text](result-page.jpeg)
---

## 2. Features
- A realistic Instagram login page interface.
- Secure storage of credentials using PostgreSQL.
- Environment variable management for sensitive information.
- Hosted live on Render.com for easy accessibility.
- Demonstrates the effectiveness of deceptive domain names in phishing scenarios.

---

## 3. Domain Name Selection
Choosing an effective domain name is a critical aspect of phishing awareness demonstrations. Some techniques to simulate deception include:

- Replacing letters with similar-looking characters (e.g., using “l” (lowercase L) in place of “i” to create URLs like `instalgram.com` instead of `instagram.com`).
- Adding slight variations to the domain, such as prefixes, suffixes, or hyphens (e.g., `secure-instagram.com`).
- Using alternate top-level domains (TLDs) like `.net`, `.org`, or `.info`.

These methods exploit user trust in familiar URLs. However, it’s crucial to emphasize that this project is for awareness and educational purposes only. Misuse of such techniques is illegal and unethical.

---

## 4. Database Configuration

### 4.1 PostgreSQL Setup on Render.com
1. Log in to Render.com and create a new **PostgreSQL** database.
2. Copy the **Database URL** provided. This will serve as the connection string for your application.

### 4.2 Managing the Database Locally
To edit tables and manage data effectively, download a PostgreSQL GUI tool like **pgAdmin** or **Workbench**:

1. **Download pgAdmin**: Install pgAdmin from the official website (https://www.pgadmin.org/).
2. **Connect to the Database**:
   - Use the Database URL provided by Render.com to connect.
   - Edit tables, view data, and manage schema conveniently.

### 4.3 Database Schema
The database schema should be created manually using your preferred database management tool. This ensures consistency and avoids potential deployment issues.

---

## 5. Environment Variables
Sensitive credentials and configuration details are managed using a `.env` file to ensure security. The following keys should be included:

- `DATABASE_URL`: The connection string provided by Render.com. databse url
- `USER`: The user name provided
- `PASSWORD`: simply password
- `HOST`: host
- `DATABASE`: table name

Ensure that the `.env` file is included in the `.gitignore` file to prevent accidental exposure.

---

## 6. Deployment Steps

### 6.1 Preparing for Deployment
1. Push the project code to a GitHub repository.
2. Ensure all dependencies are listed in `requirements.txt`.
3. Verify that the `Procfile` is correctly configured.

### 6.2 Deploying on Render.com
1. Create a new **Web Service** on Render.com.
2. Link the GitHub repository containing your code.
3. Set the **Build Command**:
   ```plaintext
   pip install -r requirements.txt
   ```
4. Set the **Start Command**:
   ```plaintext
   gunicorn app:app
   ```
5. Add environment variables in the Render.com dashboard.

---

## 7. Testing

### 7.1 Local Testing
1. Run the application locally to ensure functionality.
2. Test the database connection using sample credentials.

### 7.2 Live Testing
1. Access the deployed URL provided by Render.com.
2. Submit test credentials and verify that they are stored correctly in the PostgreSQL database.

---

## 8. Security Considerations
- Use HTTPS to secure communication between the client and server.
- Sanitize database inputs to prevent SQL injection.
- Educate users about recognizing phishing attempts through subtle URL and domain discrepancies.
- Clearly state that this project is for ethical and educational purposes only.

---

## 9. Conclusion
This project serves as a practical demonstration of phishing attack mechanisms and aims to raise awareness about cybersecurity vulnerabilities. It should only be used in controlled environments and for ethical purposes.

