import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global variable to store the current figure
current_figure = None

def open_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
    if file_path:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path, encoding='latin1')  # Specify the encoding
        else:
            df = pd.read_excel(file_path)
        
        text_area.config(state='normal')  # Make the text area editable
        text_area.delete(1.0, tk.END)  # Clear the text area
        
        # Display the dataframe in the text area
        text_area.insert(tk.END, df.to_string(index=False))
        text_area.config(state='disabled')  # Make the text area non-editable again
        
        # Get the column names and set them in the dropdowns
        columns = df.columns.tolist()
        dropdown1['values'] = columns
        dropdown2['values'] = columns

def create_graph():
    global current_figure
    x_column = dropdown1.get()
    y_column = dropdown2.get()
    graph_type = dropdown3.get()
    
    if not x_column or not y_column or not graph_type:
        messagebox.showwarning("Warning", "You have not passed the required parameters.")
        return  # Do nothing if any dropdown is not selected
    
    fig, ax = plt.subplots()
    
    try:
        if graph_type == "Line Plot":
            df.plot(x=x_column, y=y_column, kind='line', ax=ax)
        elif graph_type == "Bar Plot":
            df.plot(x=x_column, y=y_column, kind='bar', ax=ax)
        elif graph_type == "Scatter Plot":
            df.plot(x=x_column, y=y_column, kind='scatter', ax=ax)
        elif graph_type == "Histogram":
            df[y_column].plot(kind='hist', ax=ax)
        elif graph_type == "Box Plot":
            df[[x_column, y_column]].plot(kind='box', ax=ax)
        elif graph_type == "Pie Chart":
            df[y_column].value_counts().plot(kind='pie', ax=ax)
    except:
        messagebox.showwarning("Warning", "You have not passed the required parameters.")
        return
    
    ax.set_title(f"{graph_type} of {y_column} vs {x_column}")
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    
    # Clear the previous graph
    for widget in graph_space.winfo_children():
        widget.destroy()
    
    # Display the new graph
    canvas = FigureCanvasTkAgg(fig, master=graph_space)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
    
    # Store the current figure
    current_figure = fig

def save_graph():
    if current_figure is None:
        messagebox.showwarning("Warning", "No graph available to save.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        current_figure.savefig(file_path)
        messagebox.showinfo("Success", f"Graph saved successfully at {file_path}")

# Create the main window
root = tk.Tk()
root.title("Data Visualizer")
root.configure(bg='#1a1a1a')  # Set background color to dark gray

# Set the size of the main window
root.geometry("1100x600")  

# Create a frame for the heading
header_frame = tk.Frame(root, bg='#1a1a1a')
header_frame.pack(fill='x', pady=10)

# Create the heading label
heading_label = tk.Label(
    header_frame, 
    text="Data Visualizer", 
    font=("Helvetica", 20, "bold"), 
    bg='#1a1a1a', 
    fg='white'
)
heading_label.pack(pady=10)

# Create a frame for the content below the heading
content_frame = tk.Frame(root, bg='#ffffff')
content_frame.pack(fill='both', expand=True, padx=10, pady=10)

# Create the left frame
left_frame = tk.Frame(content_frame, bg='#ffffff', width=550)
left_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)

# Create the right frame
right_frame = tk.Frame(content_frame, bg='#ffffff', width=550)
right_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)

# Create a Text widget in the left frame
# Create a Text widget in the left frame
text_area = tk.Text(left_frame, wrap='none', bg='#f0f0f0', fg='#000000', state='normal')
text_area.place(relwidth=1, relheight=0.7)  # Occupy 70% of the height

# Create vertical scrollbar
v_scrollbar = tk.Scrollbar(left_frame, orient='vertical', command=text_area.yview)
v_scrollbar.place(relx=0.98, rely=0, relheight=0.7)

# Create horizontal scrollbar
h_scrollbar = tk.Scrollbar(left_frame, orient='horizontal', command=text_area.xview)
h_scrollbar.place(relx=0, rely=0.7, relwidth=0.98, height=20)

# Link scrollbars to the text widget
text_area.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

# Bind the text area to open the file chooser on click
text_area.bind("<Button-1>", lambda event: open_file())

# Create a frame below the text area for the labels and dropdowns
dropdown_frame = tk.Frame(left_frame, bg='#ffffff')
dropdown_frame.place(rely=0.7, relwidth=1, relheight=0.3)

# Create the first label and dropdown
label1 = tk.Label(dropdown_frame, text="Select column 1", bg='#ffffff', fg='#000000')
label1.grid(row=0, column=0, padx=10, pady=5, sticky='w')
dropdown1 = ttk.Combobox(dropdown_frame)
dropdown1.grid(row=1, column=0, padx=10, pady=5, sticky='w')

# Create the second label and dropdown
label2 = tk.Label(dropdown_frame, text="Select column 2", bg='#ffffff', fg='#000000')
label2.grid(row=0, column=1, padx=10, pady=5, sticky='w')
dropdown2 = ttk.Combobox(dropdown_frame)
dropdown2.grid(row=1, column=1, padx=10, pady=5, sticky='w')

# Create the third label and dropdown for "Select Graph"
label3 = tk.Label(dropdown_frame, text="Select Graph", bg='#ffffff', fg='#000000')
label3.grid(row=0, column=2, padx=10, pady=5, sticky='w')
dropdown3 = ttk.Combobox(dropdown_frame, values=["Line Plot", "Bar Plot", "Scatter Plot", "Histogram", "Box Plot", "Pie Chart"])
dropdown3.grid(row=1, column=2, padx=10, pady=5, sticky='w')

# Create a button below the dropdowns
button = tk.Button(dropdown_frame, text="Create Graph", bg='#000000', fg='#ffffff', font=("Helvetica", 12, "bold"), width=20, height=2, command=create_graph)
button.grid(row=2, column=0, columnspan=3, pady=20)

# Add a label "Graph" at the upper left corner of the right frame
graph_label = tk.Label(right_frame, text="Graph", bg='#ffffff', fg='#000000', font=("Helvetica", 16, "bold"))
graph_label.pack(anchor='nw', padx=10, pady=10)

# Add a frame for the graph selection space
graph_space = tk.Frame(right_frame, bg='#f0f0f0', width=550, height=400)
graph_space.pack(fill='both', expand=True, padx=10, pady=10)

# Add a "Save" button at the bottom of the right frame
save_button = tk.Button(right_frame, text="Save", bg='#000000', fg='#ffffff', font=("Helvetica", 12, "bold"), width=20, height=2, command=save_graph)
save_button.pack(side='bottom', pady=20)

# Run the application
root.mainloop()