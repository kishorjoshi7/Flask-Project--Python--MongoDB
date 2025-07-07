# Flask Project: REST API with Python & MongoDB

A lightweight RESTful API built using **Flask** and **MongoDB**, designed to demonstrate CRUD operations and backend integration using Python. This project is ideal for learning how to connect Flask applications with NoSQL databases and structure scalable APIs.

## 🚀 Features

- RESTful API endpoints for data manipulation
- MongoDB integration using `pymongo`
- JSON-based request and response handling
- Modular Flask app structure
- Environment-based configuration support

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: MongoDB
- **Tools**: pymongo, Flask extensions

## 📁 Project Structure

```
Flask-Project--Python--MongoDB/
├── app.py               # Main application entry point
├── config.py            # Configuration settings
├── routes/              # API route definitions
├── models/              # MongoDB data models
├── utils/               # Helper functions
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/kishorjoshi7/Flask-Project--Python--MongoDB.git
   cd Flask-Project--Python--MongoDB
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file and add your MongoDB URI:
     ```
     MONGO_URI=mongodb://localhost:27017/your-db-name
     ```

5. **Run the application**
   ```bash
   flask run
   ```

## 📬 API Endpoints

| Method | Endpoint        | Description          |
|--------|------------------|----------------------|
| GET    | `/items`         | Fetch all items      |
| POST   | `/items`         | Create a new item    |
| GET    | `/items/<id>`    | Fetch item by ID     |
| PUT    | `/items/<id>`    | Update item by ID    |
| DELETE | `/items/<id>`    | Delete item by ID    |

## 🧪 Testing

Use tools like **Postman** or **cURL** to test the API endpoints.

## 📌 Future Enhancements

- Add JWT-based authentication
- Implement pagination and filtering
- Dockerize the application
- Add Swagger/OpenAPI documentation

## 🙌 Acknowledgements

Built with ❤️ by [Kishor Joshi](https://github.com/kishorjoshi7)  
Inspired by real-world backend architecture and MongoDB integration patterns.

---

> _“Code is like a cocktail—balanced, layered, and best served with clarity.”_
