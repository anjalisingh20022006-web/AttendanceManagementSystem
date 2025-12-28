# Attendance Data Analytics Code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Load CSV File
df = pd.read_csv("attendance.csv")
print("\n--- Attendance Data ---\n")
print(df)
#Basic Data Analysis
print("\n--- Data Info ---")
print(df.info())
print("\n--- Missing Values ---")
print(df.isnull().sum())
#Attendance Calculation
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

df['Total Present'] = df[days].sum(axis=1)
df['Total Absent'] = len(days) - df['Total Present']
df['Attendance %'] = (df['Total Present'] / len(days)) * 100
#Attendance Status
df['Status'] = df['Attendance %'].apply(
    lambda x: 'Defaulter' if x < 75 else 'Regular')
print("\n--- Attendance Summary ---\n")
print(df[['Roll No', 'Name', 'Total Present', 'Total Absent', 'Attendance %', 'Status']])
#Descriptive Statistics
print("\n--- Descriptive Statistics ---\n")
print(df[days].describe())
#Students Below 75% Attendance
low_attendance = df[df['Attendance %'] < 75]
print("\n--- Students Below 75% Attendance ---\n")
print(low_attendance[['Roll No', 'Name', 'Attendance %']])
#Daily Attendance Status
status_df = df.copy()
for day in days:
    status_df[day] = status_df[day].map({1: 'Present', 0: 'Absent'})

print("\n--- Daily Attendance Status ---\n")
print(status_df[['Roll No', 'Name'] + days])
#Data Visualization

# Graph 1: Attendance Percentage of Students
plt.figure()
plt.bar(df['Name'], df['Attendance %'])
plt.xlabel("Students")
plt.ylabel("Attendance Percentage")
plt.title("Student Attendance Percentage")
plt.xticks(rotation=45)
plt.show()

# Graph 2: Total Present Days
plt.figure()
plt.bar(df['Name'], df['Total Present'])
plt.xlabel("Students")
plt.ylabel("Days Present")
plt.title("Total Present Days (Weekly)")
plt.xticks(rotation=45)
plt.show()
#Save Processed Data
df.to_csv("attendance_analysis_output.csv", index=False)
print("\nProcessed data saved as attendance_analysis_output.csv")
