#----------------------------------------------------------
# ======= ACADEMIC PERFORMANCE ANALYSIS OF STUDENTS =======
#----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("students_10.csv")

# Handle missing values
subjects = ["Math", "Science", "English", "Computer", "Social"]
df[subjects] = df[subjects].fillna(df[subjects].mean())

# Calculate Total, Average, Grade, Rank
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

def grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    else: return "F"

df["Grade"] = df["Average"].apply(grade)
df["Rank"] = df["Average"].rank(ascending=False).astype(int)

# Summary
print("Class Average:", round(df["Average"].mean(), 2))
print("Topper:", df.loc[df["Average"].idxmax(), "Name"])
print("Failure Rate:", round((df["Grade"] == "F").mean() * 100, 2), "%")
print("\nCity-wise Average\n", df.groupby("City")["Average"].mean())

# Save Files
df.to_csv("cleaned_students.csv", index=False)
df[["Name", "Average", "Grade", "Rank"]].to_csv("summary_report.csv", index=False)

# Charts

# Bar Chart
df.groupby("City")["Average"].mean().plot(kind="bar", title="City Average")
plt.show()

# Pie Chart
df["Grade"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.show()

# Scatter Plot
plt.scatter(df["StudyHours"], df["Average"])
plt.xlabel("Study Hours")
plt.ylabel("Average")
plt.show()

# Line Chart
x = df.sort_values("Rank")
plt.plot(x["Rank"], x["Average"], marker="o")
plt.show()

# Heatmap
sns.heatmap(df[subjects].corr(), annot=True)
plt.show()

print("Project Completed Successfully!")