import tkinter as tk
from tkinter import filedialog, ttk
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Define a single theme with a creamy white background
THEME = {
    "bg_color": "#f5f5dc",  # Creamy white background
    "fg_color": "#000000",
    "input_bg": "#ffffff",
    "button_bg": "#cccccc",
    "button_fg": "#000000",
    "frame_bg": "#f5f5dc",
    "button_active_bg": "#bbbbbb",
    "highlight_bg": "#cccccc"
}

# Initialize the root window
root = tk.Tk()
root.title("Gantt Chart Generator")
root.configure(bg=THEME["bg_color"])

# Global list to hold task inputs
task_rows = []

# Chart title entry
title_label = tk.Label(root, text="Chart Title:", bg=THEME["bg_color"], fg=THEME["fg_color"])
title_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

title_entry = tk.Entry(root, bg=THEME["input_bg"], fg=THEME["fg_color"])
title_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew", columnspan=2)

# Year input field
year_label = tk.Label(root, text="Year:", bg=THEME["bg_color"], fg=THEME["fg_color"])
year_label.grid(row=0, column=3, padx=10, pady=5, sticky="w")

year_entry = tk.Entry(root, bg=THEME["input_bg"], fg=THEME["fg_color"])
year_entry.grid(row=0, column=4, padx=10, pady=5, sticky="ew")
year_entry.insert(0, datetime.now().year)

# Scrollable frame for task rows
task_frame_container = tk.Frame(root, bg=THEME["frame_bg"])
task_frame_container.grid(row=1, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

# Canvas and scrollbar for the scrollable task frame
task_canvas = tk.Canvas(task_frame_container, bg=THEME["frame_bg"], highlightthickness=0)
task_canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(task_frame_container, orient="vertical", command=task_canvas.yview)
scrollbar.pack(side="right", fill="y")
task_canvas.configure(yscrollcommand=scrollbar.set)

# Frame inside the canvas for tasks
task_frame = tk.Frame(task_canvas, bg=THEME["frame_bg"])
task_canvas.create_window((0, 0), window=task_frame, anchor="nw")


# Function to update the scroll region for dynamic resizing
def update_scroll_region(event):
    task_canvas.configure(scrollregion=task_canvas.bbox("all"))


task_frame.bind("<Configure>", update_scroll_region)

# Column headers for task rows
tk.Label(task_frame, text="Task Name", bg=THEME["frame_bg"], fg=THEME["fg_color"]).grid(row=0, column=0, padx=5, pady=5)
tk.Label(task_frame, text="Start Date (MMDD)", bg=THEME["frame_bg"], fg=THEME["fg_color"]).grid(row=0, column=1, padx=5,
                                                                                                pady=5)
tk.Label(task_frame, text="Duration (days)", bg=THEME["frame_bg"], fg=THEME["fg_color"]).grid(row=0, column=2, padx=5,
                                                                                              pady=5)
tk.Label(task_frame, text="Dependency", bg=THEME["frame_bg"], fg=THEME["fg_color"]).grid(row=0, column=3, padx=5,
                                                                                         pady=5)


# Function to add a new task row
def add_task_row():
    row_idx = len(task_rows) + 1
    task_name_entry = tk.Entry(task_frame, bg=THEME["input_bg"], fg=THEME["fg_color"])
    task_name_entry.grid(row=row_idx, column=0, padx=5, pady=2)
    task_name_entry.insert(0, f"Task {row_idx}")

    start_entry = tk.Entry(task_frame, bg=THEME["input_bg"], fg=THEME["fg_color"])
    start_entry.grid(row=row_idx, column=1, padx=5, pady=2)
    start_entry.insert(0, (datetime.now() + timedelta(days=row_idx)).strftime("%m%d"))

    days_entry = tk.Entry(task_frame, bg=THEME["input_bg"], fg=THEME["fg_color"])
    days_entry.grid(row=row_idx, column=2, padx=5, pady=2)
    days_entry.insert(0, "5")

    dependency_var = tk.StringVar()
    dependency_dropdown = ttk.Combobox(task_frame, textvariable=dependency_var,
                                       values=[None] + [t["name"].get() for t in task_rows], state="readonly")
    dependency_dropdown.grid(row=row_idx, column=3, padx=5, pady=2)

    remove_button = tk.Button(task_frame, text="Remove", command=lambda: remove_task_row(task_row),
                              bg=THEME["button_bg"], fg=THEME["button_fg"], activebackground=THEME["button_active_bg"],
                              highlightbackground=THEME["highlight_bg"])
    remove_button.grid(row=row_idx, column=4, padx=5, pady=2)

    task_row = {"name": task_name_entry, "start": start_entry, "days": days_entry, "dependency": dependency_dropdown,
                "remove_button": remove_button}
    task_rows.append(task_row)


# Function to remove a task row
def remove_task_row(task_row):
    for widget in task_row.values():
        widget.grid_forget()
    task_rows.remove(task_row)


# Automatically add one default task at start
add_task_row()


# Handle dependencies
def resolve_dependencies():
    for task in task_rows:
        dependency_name = task["dependency"].get()
        if dependency_name and dependency_name != "None":
            for dep_task in task_rows:
                if dep_task["name"].get() == dependency_name:
                    dep_end_date = datetime.strptime(dep_task["start"].get(), "%m%d") + timedelta(
                        days=int(dep_task["days"].get()))
                    task["start"].delete(0, tk.END)
                    task["start"].insert(0, dep_end_date.strftime("%m%d"))


# Generate and display Gantt chart
def generate_chart():
    resolve_dependencies()
    tasks, start_dates, durations = [], [], []
    for task in task_rows:
        tasks.append(task["name"].get())
        start_dates.append(datetime.strptime(task["start"].get(), "%m%d"))
        durations.append(int(task["days"].get()))

    fig, ax = plt.subplots()
    ax.barh(tasks, durations, left=start_dates)
    plt.title(title_entry.get())
    plt.xlabel("Date")
    plt.ylabel("Tasks")

    # Format the date on x-axis
    ax.xaxis.set_major_formatter(DateFormatter('%m-%d'))
    plt.show()


# Save the chart to a file
def save_chart():
    resolve_dependencies()
    tasks, start_dates, durations = [], [], []
    for task in task_rows:
        tasks.append(task["name"].get())
        start_dates.append(datetime.strptime(task["start"].get(), "%m%d"))
        durations.append(int(task["days"].get()))

    fig, ax = plt.subplots()
    ax.barh(tasks, durations, left=start_dates)
    plt.title(title_entry.get())
    plt.xlabel("Date")
    plt.ylabel("Tasks")
    ax.xaxis.set_major_formatter(DateFormatter('%m-%d'))

    # File dialog for saving
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                                                        ("All Files", "*.*")])
    if file_path:
        plt.savefig(file_path)


# Buttons
button_frame = tk.Frame(root, bg=THEME["bg_color"])
button_frame.grid(row=2, column=0, columnspan=5, padx=10, pady=5, sticky="ew")

add_row_button = tk.Button(button_frame, text="Add Task", command=add_task_row, bg=THEME["button_bg"],
                           fg=THEME["button_fg"])
add_row_button.pack(side="left", padx=5, pady=5)

generate_button = tk.Button(button_frame, text="Generate Chart", command=generate_chart, bg=THEME["button_bg"],
                            fg=THEME["button_fg"])
generate_button.pack(side="left", padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save Chart", command=save_chart, bg=THEME["button_bg"],
                        fg=THEME["button_fg"])
save_button.pack(side="left", padx=5, pady=5)

quit_button = tk.Button(button_frame, text="Quit", command=root.quit, bg=THEME["button_bg"], fg=THEME["button_fg"])
quit_button.pack(side="left", padx=5, pady=5)

# Configure dynamic resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()
