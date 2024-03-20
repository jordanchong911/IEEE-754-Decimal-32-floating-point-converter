import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk  # Import the ttk module for combobox
from functools import partial

# Import the conversion function correctly
from logic.densely_packed_BCD import convert_to_dpd
from logic.densely_packed_BCD import write_to_file  # Import the write_to_file function

def convert_and_display(num_entry, power_entry, rounding_combobox, result_text):
    num = num_entry.get()
    power = power_entry.get()
    rounding_method = rounding_combobox.get()  # Get the selected rounding method from the combobox

    # Validate if num and power are numeric values
    if not (num.replace('.', '', 1).isdigit() or num.lstrip('-').replace('.', '', 1).isdigit()):
        messagebox.showerror("Error", "Please enter a valid number.")
        return
    if not (power.isdigit() or power.lstrip('-').isdigit()):
        messagebox.showerror("Error", "Please enter a valid power.")
        return

    if (rounding_method == "Truncate"):
        rounding = "truncate"
    elif (rounding_method == "Round Up"):
        rounding = "round_up"
    elif (rounding_method == "Round Down"):
        rounding = "round_down"
    elif (rounding_method == "Round, Ties to Even"):
        rounding = "nearest_even"
    elif (rounding_method == "Round, Ties Away Zero"):
        rounding = "nearest_zero"

    try:
        # Perform conversion
        binary, hexadecimal = convert_to_dpd(num, int(power), rounding)
        # Display results
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"DPD result:\nBinary: {binary}\nHexadecimal: {hexadecimal}")
        # Return binary and hexadecimal values for export
        return binary, hexadecimal
    except Exception as e:
        messagebox.showerror("Error", str(e))

def export_to_text(binary, hexadecimal):
    # Call the write_to_file function with binary and hexadecimal values
    write_to_file(binary, hexadecimal)

def create_gui():
    root = tk.Tk()
    root.title("IEEE-754 Decimal-64 Floating-Point Converter")

    # Create entry fields
    num_label = tk.Label(root, text="Number:")
    num_label.grid(row=0, column=0, padx=5, pady=5)
    num_entry = tk.Entry(root, width=30)
    num_entry.grid(row=0, column=1, padx=5, pady=5)

    power_label = tk.Label(root, text="Power:")
    power_label.grid(row=1, column=0, padx=5, pady=5)
    power_entry = tk.Entry(root, width=30)
    power_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create combobox for rounding method selection
    rounding_label = tk.Label(root, text="Rounding Method:")
    rounding_label.grid(row=2, column=0, padx=5, pady=5)
    rounding_combobox = ttk.Combobox(root, values=["Truncate", "Round Up", "Round Down", "Round, Ties to Even", "Round, Ties Away Zero"])
    rounding_combobox.current(0)  # Set default value to the first option
    rounding_combobox.grid(row=2, column=1, padx=5, pady=5)

    # Create buttons
    result_text = scrolledtext.ScrolledText(root, width=50, height=8, wrap=tk.WORD)
    result_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def display_results():
        convert_and_display(num_entry, power_entry, rounding_combobox, result_text)

    convert_btn = tk.Button(root, text="Submit", command=display_results)
    convert_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def export_results():
        binary, hexadecimal = convert_and_display(num_entry, power_entry, rounding_combobox, result_text)
        if binary and hexadecimal:
            # Export to text file
            export_to_text(binary, hexadecimal)
            # Display export success message
            messagebox.showinfo("Export Successful", "Results exported to 'dpd_results.txt'")

    export_btn = tk.Button(root, text="Export to Text", command=export_results)
    export_btn.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

# Call the function to create GUI
create_gui()
