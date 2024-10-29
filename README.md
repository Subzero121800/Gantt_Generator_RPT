# Gantt Chart Generator

A Python-based Gantt chart generator with two versions: a tkinter GUI and a basic script. Users can input tasks, set durations, and define dependencies to create customizable Gantt charts for project timeline visualization.

## Table of Contents

***None Yet***

## Features

- GUI Version:
  - User-Friendly Interface: Easy-to-use GUI for inputting tasks, durations, and dependencies.
  - Automated Dependency Handling: Adjusts task start dates based on dependencies.
  - Customizable Chart: Set custom title and year for each chart.
  - Scrollable Task List: Add multiple tasks in an organized layout.
  - Save Chart: Export Gantt charts as .png or .jpg files.

- Basic Script Version:
  - Quick Chart Generation: Create Gantt charts without a GUI.
  - Random Color Assignment: Automatically assigns colors to tasks.
  - Customizable via Code: Easily modify task data in the script.

## Installation

### Prerequisites

- Python 3.x
- Required Libraries: tkinter (included with Python), matplotlib

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gantt-chart-generator.git
   ```

2. Navigate to the project directory:
   ```
   cd gantt-chart-generator
   ```

3. Install dependencies:
   ```
   pip install matplotlib
   ```

## Usage

### GUI Version

1. Run the Program:
   ```
   python gantt_chart_generator_gui.py
   ```

2. Enter Chart Details:
   - Set the Chart Title and Year in the input fields.

3. Add Tasks:
   - Enter task name, start date (MMDD format), duration (days), and dependencies.

4. Generate and Save:
   - Click "Generate Chart" to view the chart.
   - Click "Save Chart" to export as an image file.

### Basic Script Version

1. Edit the tasks list in `joes_gantt_generator_noai.py` with your project data.

2. Run the script:
   ```
   python joes_gantt_generator_noai.py
   ```

3. The Gantt chart will be displayed with random colors for each task.

## Screenshots

[Add screenshots of GUI and generated charts here]

## Basic Script (No GUI)

The basic script (`joes_gantt_generator_noai.py`) offers a minimal version without a GUI. It uses random colors and generates a Gantt chart based on pre-defined tasks in the script.

For detailed instructions, refer to the included PDF guide: [Joes_Chart_Generator_NoGUI.pdf](path/to/Joes_Chart_Generator_NoGUI.pdf).

## Contributing

1. Fork the repository
2. Create a feature branch:
   ```
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch:
   ```
   git push origin feature/AmazingFeature
   ```
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
