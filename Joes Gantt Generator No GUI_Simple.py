import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

# Base start date for the project
project_start = datetime(2024, 1, 1)

# Tasks based on River Point Technology's services
tasks = [
    {"name": "Digital Transformation Consultation", "start": datetime(2024, 1, 5), "end": datetime(2024, 2, 20)},
    {"name": "Cloud Management Strategy Development", "start": datetime(2024, 2, 21), "end": datetime(2024, 4, 10)},
    {"name": "Agile DevOps Training and Workshops", "start": datetime(2024, 4, 11), "end": datetime(2024, 6, 5)},
    {"name": "Application Modernization & Testing", "start": datetime(2024, 6, 6), "end": datetime(2024, 8, 25)},
    {"name": "RPT Accelerator: Day 2 Optimization", "start": datetime(2024, 8, 26), "end": datetime(2024, 10, 15)},
    {"name": "Final Review & CI/CD Implementation", "start": datetime(2024, 10, 16), "end": datetime(2024, 12, 1)},
    {"name": "Onboarding and Handover Process", "start": datetime(2024, 12, 2), "end": datetime(2024, 12, 22)},
    {"name": "Potential Hiring as Next Steps", "start": datetime(2024, 12, 23), "end": datetime(2024, 12, 24)},  # Hypothetical hire date: Monday or Tuesday
]

# Plotting the Gantt chart with specific tasks
fig, ax = plt.subplots(figsize=(18, 14))  # Adjusted figure size for better readability

colors = plt.cm.tab20(np.linspace(0, 1, len(tasks)))

for i, task in enumerate(tasks):
    start = mdates.date2num(task["start"])
    end = mdates.date2num(task["end"])
    ax.barh(i, end - start, left=start, height=0.4, align='center', color=colors[i], edgecolor='grey')

# Key project milestones
staffing_ramp_up_start_date_num = mdates.date2num(tasks[0]["start"])  # Digital Transformation Start
final_milestone_date_num = mdates.date2num(tasks[-1]["end"])  # Hypothetical hiring date

ax.axvline(x=staffing_ramp_up_start_date_num, color="blue", linestyle="--", label="Project Start")
ax.axvline(x=final_milestone_date_num, color="green", linestyle="--", label="Potential Hiring Date")

# X-axis formatting options
ax.set_xlabel("Date", fontsize=16, fontweight='bold')
ax.set_ylabel("Tasks", fontsize=16, fontweight='bold')
ax.set_title("River Point Technology Project Timeline", fontsize=16, fontweight='bold')

# Show months on x-axis
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Y-axis
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task["name"] for task in tasks], fontsize=12, fontweight='bold')

# Grid and legend
plt.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12, title_fontsize='large')
for text in plt.legend().get_texts():
    text.set_weight('bold')

# Adjust layout
plt.tight_layout()
plt.show()