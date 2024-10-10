# Data Visualizer

This Data Visualizer project is a GUI-based application built using Tkinter that allows users to load an Excel or CSV file and create customized visualizations based on the selected columns. The project uses Pandas for data handling and Matplotlib for generating the graphs. It's an easy-to-use tool for visually exploring relationships within your dataset.

## Features

- GUI Interface: Built using Tkinter, providing an intuitive and user-friendly interface.

- File Upload: Users can import data files in Excel (.xlsx) or CSV (.csv) format through a file dialog.
  
- Data Handling with Pandas: Efficiently read and manipulate data using Pandas, allowing for flexible data selection.
  
- Custom Visualization: Users can select two columns of data (e.g., temperature vs. humidity) and generate visualizations like scatter plots, line graphs, or bar charts.
  
- Graph Display: Graphs are rendered within the GUI using Matplotlib, and interactive controls allow users to update the graph dynamically.

- Save Option: Users can save the generated graphs as images directly from the interface.


## Libraries Used
- Tkinter: For the graphical user interface (GUI).

- Pandas: For reading and handling Excel/CSV files.

- Matplotlib: For plotting graphs and visualizations.

- Tkinter.ttk: For enhanced widget styling and components.

- Tkinter.filedialog: For file selection dialogs.

- Tkinter.messagebox: For displaying alerts and messages.

## Installation

To run this project locally, you need to install the following libraries:

```bash
pip install tkinter
pip install pandas
pip install matplotlib
```
    
## How to Run
1) Clone the repository:

```bash
git clone https://github.com/ShubhamBabar3001/Data-Visualizer.git
```
```bash
cd Data-Visualizer
```
2) Install the dependencies listed above.
3. Run the Python script:
```bash
python dataVisualizer.py
```
## How It Works:

- Upload Dataset: The user can upload an Excel or CSV file using a file dialog.
  
- Select Columns: Two columns from the dataset can be selected from dropdown menus for comparison or visualization.

- Create Graph: Choose the type of graph (scatter plot, line chart, etc.) from the dropdown, and click "Create Graph" to generate the visualization.

- Save Graph: The generated graph can be saved as an image file.


## Screenshots
![image](https://github.com/user-attachments/assets/5393ea96-3003-453a-b864-0cc13ccd962b)



## Contributing

Feel free to contribute by opening issues or submitting pull requests. All contributions are welcome!
