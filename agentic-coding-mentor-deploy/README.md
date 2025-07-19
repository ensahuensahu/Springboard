# Agentic Coding Mentor: Production Deployment

## 🚀 How to Run

1. **Build Docker Image**
   ```
   docker build -t agentic-api .
   ```

2. **Run the Container**
   ```
   docker run -p 8080:8080 agentic-api
   ```

3. **Test the API**
   Run `notebook/api_demo.py` or visit Swagger UI at `http://localhost:8080/docs`

## 📘 API Endpoint

| Method | Endpoint    | Input Format       | Description            |
|--------|-------------|--------------------|------------------------|
| POST   | /feedback   | {"code": string}   | Returns code feedback  |
