import pandas as pd

# --- Test Cases Data ---
test_cases_data = [
    {"Test Case ID": "TC01", "Title": "Fetch product list", "Steps": "GET /products", "Expected Result": "Return products"},
    {"Test Case ID": "TC02", "Title": "Add valid item to cart", "Steps": "POST /cart {id:1, qty:1}", "Expected Result": "Item added"},
    {"Test Case ID": "TC03", "Title": "Checkout empty cart", "Steps": "POST /checkout", "Expected Result": "Error: Cart empty"},
    {"Test Case ID": "TC04", "Title": "Invalid product ID", "Steps": "POST /cart {id:99, qty:1}", "Expected Result": "Error: Product not found"},
    {"Test Case ID": "TC05", "Title": "Stress Test 500 users", "Steps": "Run Locust with 500 users", "Expected Result": "< 2s avg, < 5% failures"},
]

df_cases = pd.DataFrame(test_cases_data)
df_cases.to_excel("practice-docs/QA_TestCases.xlsx", index=False)

# --- Bug Reports Data ---
bug_reports_data = [
    {"Bug ID": "BUG-001", "Title": "Checkout allows empty cart", "Severity": "High", "Steps": "POST /checkout with empty cart", "Expected": "Error: Cart empty", "Actual": "Order placed, total=0"},
    {"Bug ID": "BUG-002", "Title": "Performance degradation at 500 users", "Severity": "High", "Steps": "Run Locust with 500 users", "Expected": "95% < 1s", "Actual": "95% ~2.5s, 5% failures"},
    {"Bug ID": "BUG-003", "Title": "Cart not persistent after restart", "Severity": "Medium", "Steps": "Add item, restart API, check cart", "Expected": "Cart persists", "Actual": "Cart empty"},
]

df_bugs = pd.DataFrame(bug_reports_data)
df_bugs.to_excel("practice-docs/QA_BugReports.xlsx", index=False)

print("✅ Excel files created: QA_TestCases.xlsx and QA_BugReports.xlsx inside practice-docs/")
