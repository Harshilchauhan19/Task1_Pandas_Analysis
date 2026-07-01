
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_data.csv")


print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())


print("\nStatistics:")
print(df.describe())


print("\nAverage Final Marks (G3):")
print(df["G3"].mean())

print("\nHighest Final Marks:")
print(df["G3"].max())

print("\nLowest Final Marks:")
print(df["G3"].min())


gender_marks = df.groupby("sex")["G3"].mean()

plt.figure(figsize=(5,5))
plt.bar(gender_marks.index, gender_marks.values)

plt.title("Average Final Marks by Gender")
plt.xlabel("Gender")
plt.ylabel("Average G3 Marks")

plt.show()

plt.figure(figsize=(6,5))

plt.scatter(df["studytime"], df["G3"])

plt.title("Study Time vs Final Marks")

plt.xlabel("Study Time")

plt.ylabel("Final Marks (G3)")

plt.show()


plt.figure(figsize=(12,8))

sns.heatmap(df.corr(numeric_only=True),annot=True)

plt.title("Correlation Heatmap")

plt.show()