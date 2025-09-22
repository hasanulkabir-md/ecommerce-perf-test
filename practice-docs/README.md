
```markdown
# 🧪 QA Practice Documentation – E-commerce Checkout API

## 📌 Overview
This folder contains **QA documentation and performance testing results** for the `ecommerce-perf-test` project.  
It demonstrates structured **test case design, bug reporting, and load testing analysis** — valuable skills for a QA / Software Test Engineer role.  

---

## 📑 Contents
- **QA_TestCases.xlsx** → Functional, negative, and performance test cases.  
- **QA_BugReports.xlsx** → Logged bugs with severity, priority, and repro steps.  
- **docs/** → Graphs, summary reports (CSV, PNG).  
- **scripts/** → Utility scripts (`plot_results.py` for generating graphs, `generate_xlsx.py` for creating Excel docs).  
- **README.md** → This documentation.  

---

## 📝 Test Cases
See [QA_TestCases.xlsx](./QA_TestCases.xlsx).  
Examples include:
- Fetch product list (`GET /products`)  
- Add valid/invalid items to cart (`POST /cart`)  
- Checkout scenarios (`POST /checkout`)  
- Negative tests (empty cart, invalid payload)  
- Performance tests (50, 100, 500 concurrent users)  

---

## 🐞 Bug Reports
See [QA_BugReports.xlsx](./QA_BugReports.xlsx).  
Examples:
- **BUG-001** → Checkout allows empty cart (High severity).  
- **BUG-002** → Performance degradation at 500 users (High severity).  
- **BUG-003** → Cart not persistent after API restart (Medium severity).  

---
## 📊 Performance Results

### Response Times (Avg, 90%, 95%)
![Response Time](https://raw.githubusercontent.com/hasanulkabir-md/ecommerce-perf-test/main/practice-docs/docs/users_vs_response_detailed.png)

### Failures
![Failures](https://raw.githubusercontent.com/hasanulkabir-md/ecommerce-perf-test/main/practice-docs/docs/users_vs_failures.png)

### Additional Graph
![Users vs Response](https://raw.githubusercontent.com/hasanulkabir-md/ecommerce-perf-test/main/practice-docs/docs/users_vs_response.png)

### Summary (from [summary.csv](https://raw.githubusercontent.com/hasanulkabir-md/ecommerce-perf-test/main/practice-docs/docs/summary.csv))

### Failures
![Failures](https://raw.githubusercontent.com/hasanulkabir-md/ecommerce-perf-test/main/practice-docs/docs/users_vs_failures.png)

### Additional Graph
![Users vs Response](https://raw.githubusercontent.com/hasanulkabir-md/ecommerce-perf-test/main/practice-docs/docs/users_vs_response.png)

### Summary (from [summary.csv](https://raw.githubusercontent.com/hasanulkabir-md/ecommerce-perf-test/main/practice-docs/docs/summary.csv))


---

## 🎯 Key Learnings
- Writing **clear test cases** improves coverage & repeatability.  
- Logging **structured bug reports** helps prioritize fixes.  
- Performance bottlenecks appear after **100+ concurrent users**.  
- Graphs & reports make results easy to present to non-technical stakeholders.  

---

👨‍💻 **Author**: Md Hasanul Kabir  
📌 MSc Computer Science & Technology  
📍 Based in Feni / Nanjing  
```

---








