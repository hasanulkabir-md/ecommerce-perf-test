
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
[
## 📊 Performance Results

![Response Time](https://github.com/hasanulkabir-md/ecommerce-perf-test/blob/main/practice-docs/docs/users_vs_response_detailed.png?raw=true)
![Failures](https://github.com/hasanulkabir-md/ecommerce-perf-test/blob/main/practice-docs/docs/users_vs_failures.png?raw=true)
![Users vs Response](https://github.com/hasanulkabir-md/ecommerce-perf-test/blob/main/practice-docs/docs/users_vs_response.png?raw=true)
[Download Summary CSV](https://github.com/hasanulkabir-md/ecommerce-perf-test/blob/main/practice-docs/docs/summary.csv)](https://github.com/hasanulkabir-md/ecommerce-perf-test/blob/main/practice-docs/docs/users_vs_response_detailed.png?raw=true)


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





