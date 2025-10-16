import pandas as pd
import matplotlib.pyplot as plt
import random

names = [f"Student_{i}" for i in range(1, 11)]
marks = [random.randint(40, 100) for _ in names]

df = pd.DataFrame({"Name": names, "Marks": marks})
print(df)

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Visualization 📊")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
