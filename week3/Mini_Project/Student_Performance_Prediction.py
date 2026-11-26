import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("Dataset.csv")

print("Student Performance Dataset")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna()

X = df[[
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Score"
]]

le = LabelEncoder()
y = le.fit_transform(df["Result"])

print("\nFeatures and Target Selected Successfully!")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

y_pred = model.predict(X_test)

print("\nActual Results:")
print(le.inverse_transform(y_test))

print("\nPredicted Results:")
print(le.inverse_transform(y_pred))

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=le.inverse_transform([0, 1]),
    zero_division=0
))

new_students = pd.DataFrame({
    "Study_Hours": [6, 2, 8],
    "Attendance": [85, 55, 95],
    "Previous_Marks": [72, 35, 90],
    "Assignment_Score": [80, 40, 95]
})

predictions = model.predict(new_students)

new_students["Prediction"] = le.inverse_transform(predictions)

print("\nNEW STUDENT PERFORMANCE PREDICTIONS")
print(new_students.to_string(index=False))

for i in range(len(new_students)):
    print("\nStudent", i + 1)
    print("Study Hours:", new_students.iloc[i]["Study_Hours"])
    print("Attendance:", new_students.iloc[i]["Attendance"], "%")
    print("Previous Marks:", new_students.iloc[i]["Previous_Marks"])
    print("Assignment Score:", new_students.iloc[i]["Assignment_Score"])
    print("Prediction:", new_students.iloc[i]["Prediction"].upper())

new_students.to_csv("Student_Performance_Predictions.csv", index=False)

print("\nPredictions saved successfully!")
