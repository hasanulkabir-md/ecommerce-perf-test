import pandas as pd
import matplotlib.pyplot as plt
import os

# Folders
results_folder = "results/"
docs_folder = "docs/"
os.makedirs(docs_folder, exist_ok=True)

summary = []

for users in [50, 100, 500]:
    file = os.path.join(results_folder, f"test_{users}_stats.csv")
    if os.path.exists(file):
        df = pd.read_csv(file)
        total = df[df['Name'] == 'Aggregated']
        if not total.empty:
            avg_response = total["Average Response Time"].values[0]
            failures = total["Failure Count"].values[0]
            p90 = total["90%"].values[0]
            p95 = total["95%"].values[0]
            summary.append((users, avg_response, p90, p95, failures))

summary_df = pd.DataFrame(
    summary,
    columns=["Users", "AvgResponseTime(ms)", "P90(ms)", "P95(ms)", "Failures"]
)

# Save summary CSV
summary_df.to_csv(os.path.join(docs_folder, "summary.csv"), index=False)

# Plot Avg + Percentiles
plt.figure(figsize=(8,5))
plt.plot(summary_df["Users"], summary_df["AvgResponseTime(ms)"], marker="o", label="Average")
plt.plot(summary_df["Users"], summary_df["P90(ms)"], marker="s", label="90th Percentile")
plt.plot(summary_df["Users"], summary_df["P95(ms)"], marker="^", label="95th Percentile")
plt.title("Users vs Response Time")
plt.xlabel("Number of Users")
plt.ylabel("Response Time (ms)")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(docs_folder, "users_vs_response_detailed.png"))
plt.close()

# Plot Failures
plt.figure(figsize=(8,5))
plt.plot(summary_df["Users"], summary_df["Failures"], marker="o", color="red")
plt.title("Users vs Failures")
plt.xlabel("Number of Users")
plt.ylabel("Failures")
plt.grid(True)
plt.savefig(os.path.join(docs_folder, "users_vs_failures.png"))
plt.close()

print("✅ Done: Summary saved in docs/summary.csv, graphs saved in docs/")
