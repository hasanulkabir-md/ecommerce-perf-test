# 🛒 E-commerce Checkout API Performance Testing

## 📌 Overview
This project demonstrates **performance testing of a simple E-commerce Checkout API** using **FastAPI (Python)** as the backend and **Locust** for load testing.  

The goal is to evaluate how the checkout process (browse → add to cart → checkout) performs under increasing user load, identify bottlenecks, and suggest improvements.  

---

## ⚙️ Tech Stack
- **FastAPI** → lightweight Python web framework for the API  
- **Uvicorn** → ASGI server for running FastAPI  
- **Locust** → Python-based load testing tool  
- **Linux + VS Code** → development environment  

---

## 🚀 Features
- REST API with 3 endpoints:
  - `GET /products` → fetch product list  
  - `POST /cart` → add item to cart  
  - `POST /checkout` → simulate order creation  
- Load test simulation of real-world user flows:
  - Browsing products  
  - Adding items to cart  
  - Completing checkout  
- Performance metrics collected:
  - Response times (avg, 90th/95th percentile)  
  - Throughput (requests/sec)  
  - Error rates under load  

---

## 📂 Project Structure
```

ecommerce-perf-test/
├── api/              # FastAPI backend
│   └── main.py
├── tests/            # Locust performance tests
│   └── locustfile.py
├── results/          # Exported reports (CSV/screenshots)
├── practice-docs/ # ✅ Extra QA documentation (test cases, bug reports, graphs)
└── README.md

````

---

## 🛠️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/hasanukabir-md/ecommerce-perf-test.git
cd ecommerce-perf-test
````

### 2. Install dependencies

```bash
pip install fastapi uvicorn locust
```

### 3. Run the API

```bash
uvicorn api.main:app --reload --host 127.0.0.1 --port 8000
```

API available at:

* [http://127.0.0.1:8000/products](http://127.0.0.1:8000/products)
* Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 4. Run Locust

Open a new terminal:

```bash
cd tests
locust -f locustfile.py --host=http://127.0.0.1:8000
```

Then open: [http://localhost:8089](http://localhost:8089)

---

## 📊 Results
### FastAPI Swagger UI
![FastAPI Swagger](screenshots/fastapi_swagger.png)

### Locust Dashboard

![Locust Dashboard](screenshots/locust_dashboard.png)

### Response Time Distribution

![Performance Graph](screenshots/locust_chart.png)

**Findings:**

* API handled up to **300 concurrent users** with avg response time < 500ms.
* Beyond 500 users, checkout endpoint slowed significantly (> 1.5s avg).
* Bottleneck: in-memory cart implementation → no caching/DB optimizations.

---

## ✅ Recommendations

* Implement database indexing for faster cart operations.
* Add caching layer (Redis) for frequently requested products.
* Optimize checkout logic with async I/O.
* Run tests in CI/CD (GitHub Actions) with pass/fail thresholds.

---
## 📑 Extra QA Documentation (Practice Project)

For recruiters:
👉 Check the dedicated QA documentation with **test cases, bug reports, and performance analysis** here:
➡️ [practice-docs/](./practice-docs)

Contents include:

* [QA\_TestCases.xlsx](./practice-docs/QA_TestCases.xlsx) → Detailed functional & performance test cases
* [QA\_BugReports.xlsx](./practice-docs/QA_BugReports.xlsx) → Logged bugs with severity & repro steps
* [Performance Graphs](./practice-docs/docs) → Response time, failure rate, and CSV summary

---

## 🎯 Impact

This project highlights:

* Ability to design & test APIs for scalability.
* Skill with **performance testing tools (Locust)**.
* Understanding of **bottlenecks, metrics, and optimizations**.
* CI/CD-ready performance testing approach.

---

👨‍💻 **Author**: Md. Hasanul Kabir
🔗 [LinkedIn](https://linkedin.com/in/hasanulkabir_md) | [Portfolio](https://your-portfolio.com)

---








