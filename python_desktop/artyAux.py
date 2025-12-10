import tkinter as tk
from tkinter import ttk
import sys

trasparency = 0.5
locked = False
def calculate(*args):
    try:
        ang200 = float(entry_ang200.get())
        ang600 = float(entry_ang600.get())
        dist = float(entry_dist.get())
        comp = float(entry_comp.get())

        proportion = (ang600 - ang200) / 400
        final_angle = (ang200 + proportion * (dist - 200)) + comp

        result_label.config(text=f"Angle: {final_angle:.2f}")

    except:
        result_label.config(text="Angle: ---")


def trasparencyModeMinus():
    global trasparency
    value = trasparency-0.1 
    if (value >= 0.1 and value <= 1.0):
        root.attributes('-alpha',value)
        trasparency = value

def trasparencyModePlus():
    global trasparency
    value = trasparency+0.1
    if (value >= 0.1 and value <= 1.0):
        root.attributes('-alpha',value)
        trasparency = value

def close_window(): 
    root.destroy()

def lock_window(): 
    global locked
    locked = not (locked)
    root.resizable(not locked, not locked)
    root.overrideredirect(locked)


def set_values(art_type): 
    if(art_type == 'Ally'):
        entry_ang200.delete(0,tk.END)
        entry_ang200.insert(0,'954')
        
        entry_ang600.delete(0,tk.END)
        entry_ang600.insert(0,'859')

        entry_comp.delete(0,tk.END)
        entry_comp.insert(0,'0')
    elif(art_type == 'USSR'):
        entry_ang200.delete(0,tk.END)
        entry_ang200.insert(0,'1099')
        
        entry_ang600.delete(0,tk.END)
        entry_ang600.insert(0,'1014')

        entry_comp.delete(0,tk.END)
        entry_comp.insert(0,'0')
    elif(art_type == 'Brit'):
        entry_ang200.delete(0,tk.END)
        entry_ang200.insert(0,'515')
        
        entry_ang600.delete(0,tk.END)
        entry_ang600.insert(0,'444')

        entry_comp.delete(0,tk.END)
        entry_comp.insert(0,'0')
    elif(art_type == 'Mob'):
        entry_ang200.delete(0,tk.END)
        entry_ang200.insert(0,'533')
        
        entry_ang600.delete(0,tk.END)
        entry_ang600.insert(0,'267')

        entry_comp.delete(0,tk.END)
        entry_comp.insert(0,'0')
        
    

# -------------------------
#  Window configuration
# -------------------------


root = tk.Tk()
root.title("HLL Artillery Calculator")

# Window size
root.geometry("300x300")

# Always on top
root.attributes("-topmost", True)

# Prevent window from taking focus when clicking
if sys.platform.startswith("win"):
    try:
        root.attributes("-toolwindow", True)
    except tk.TclError:
        pass
root.attributes('-alpha',trasparency)
root.resizable(not locked, not locked)
root.overrideredirect(locked)

#root.iconbitmap("icon.ico") 
# Background style
root.configure(bg="#3b3b3b")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#3b3b3b", foreground="#e0e0c0", font=("Courier New", 11))
style.configure("TEntry", fieldbackground="#555", foreground="white", insertcolor="white")
style.configure("TFrame", background="#3b3b3b")
style.configure("TButton", background="#3b3b3b",foreground="#e0e0c0", font=("Courier New", 11))



# -------------------------
#   Window Control
# -------------------------

w_control = ttk.Frame(root)
w_control.pack(padx=0, pady=0, fill="both", expand=True)

close = ttk.Button(w_control, text="x",command=close_window, style = 'TButton',width=2).pack(side=tk.RIGHT)

lock = ttk.Button(w_control, text="🔒",command=lock_window, style = 'TButton',width=2).pack(side=tk.RIGHT)

vis_up = ttk.Button(w_control, text="+",command=trasparencyModePlus, style = 'TButton',width=2).pack(side=tk.RIGHT)

vis_down = ttk.Button(w_control, text="-",command=trasparencyModeMinus, style = 'TButton',width=2).pack(side=tk.RIGHT)



# -------------------------
#   Standart Values
# -------------------------

sv_control = ttk.Frame(root)
sv_control.pack(padx=10, pady=0, fill="both", expand=True)

close = ttk.Button(sv_control, text="Al/Ax",command=lambda:set_values("Ally"), style = 'TButton',width=5).pack(side=tk.LEFT)

lock = ttk.Button(sv_control, text="USSR",command=lambda:set_values("USSR"), style = 'TButton',width=5).pack(side=tk.LEFT)

vis_up = ttk.Button(sv_control, text="Brit",command=lambda:set_values("Brit"), style = 'TButton',width=5).pack(side=tk.LEFT)

vis_down = ttk.Button(sv_control, text="Mob",command=lambda:set_values("Mob"), style = 'TButton',width=5).pack(side=tk.LEFT)




# -------------------------
#   Input fields
# -------------------------

frame = ttk.Frame(root)
frame.pack(padx=5, pady=5, fill="both", expand=True)

ttk.Label(frame, text="Angle @ 200m").pack(anchor="w")

entry_ang200 = ttk.Entry(frame)
entry_ang200.pack(fill="x")

ttk.Label(frame, text="Angle @ 600m").pack(anchor="w")
entry_ang600 = ttk.Entry(frame)
entry_ang600.pack(fill="x")

ttk.Label(frame, text="Compensation (angle)").pack(anchor="w")
entry_comp = ttk.Entry(frame)
entry_comp.pack(fill="x")

ttk.Label(frame, text="Target Distance (m)").pack(anchor="w")
entry_dist = ttk.Entry(frame)
entry_dist.pack(fill="x")



# -------------------------
#   Result label
# -------------------------
result_label = ttk.Label(frame, text="Angle: ---", font=("Courier New", 13, "bold"))
result_label.pack(pady=10)

# Calculate automatically on typing
entry_ang200.bind("<KeyRelease>", calculate)
entry_ang600.bind("<KeyRelease>", calculate)
entry_dist.bind("<KeyRelease>", calculate)
entry_comp.bind("<KeyRelease>", calculate)

root.mainloop()
