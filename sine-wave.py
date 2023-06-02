import tkinter as tk 
import numpy as np 
import matplotlib.pyplot as plt 

class SineWaveGUI: 
    def __init__(self, master): 
        self.master = master 
        master.title("Sine Wave Simulator") 
 
        # Default values 
        self.amplitude = tk.DoubleVar(value=0.0) 
        self.frequency = tk.DoubleVar(value=0.0) 
        self.phase = tk.DoubleVar(value=0.0) 
 
        # Widgets 
        self.amplitude_label = tk.Label(master, text="Amplitude:") 
        self.amplitude_entry = tk.Entry(master, textvariable=self.amplitude)
        self.amplitude_note = tk.Label(master, text="Note: Amplitude cannot be in negative.")
        self.frequency_label = tk.Label(master, text="Frequency:") 
        self.frequency_entry = tk.Entry(master, textvariable=self.frequency) 
        self.frequency_note = tk.Label(master, text="Note: Frequency cannot be in negative.")
        self.phase_label = tk.Label(master, text="Phase:") 
        self.phase_entry = tk.Entry(master, textvariable=self.phase)
        self.phase_note = tk.Label(master, text="Note: Phase cannot be greater than 360 or in negative.") 
        self.generate_button = tk.Button(master, text="Generate Sinewave", command=self.execute) 
 
        # Grid layout 
        self.amplitude_label.grid(row=0, column=0) 
        self.amplitude_entry.grid(row=0, column=1) 
        self.amplitude_note.grid(row=0, column=2) 
        self.frequency_label.grid(row=1, column=0) 
        self.frequency_entry.grid(row=1, column=1)
        self.frequency_note.grid(row=1, column=2)  
        self.phase_label.grid(row=2, column=0) 
        self.phase_entry.grid(row=2, column=1) 
        self.phase_note.grid(row=2, column=2)  
        self.generate_button.grid(row=3, column=0, columnspan=2) 

    def execute(self): 
        t = np.linspace(0, 10, 1000) 
        y = self.amplitude.get() * np.sin(2 * np.pi * self.frequency.get() * t - self.phase.get()) 
        plt.figure(figsize=(10,4))
        plt.plot(t, y) 
        plt.title("Sine wave")
        plt.xlabel("Time(s)") 
        plt.ylabel("Amplitude")
        plt.show() 
        
# Create and run the GUI 
root = tk.Tk() 
app = SineWaveGUI(root)
root.mainloop()
