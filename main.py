import tkinter as tk

class LoadingSpinner:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Loading Spinner")
        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas.pack()
        self.draw_circle()

    def draw_circle(self):
        self.canvas.delete("all")
        self.canvas.create_oval(50, 50, 150, 150, fill="#fff")
        self.canvas.create_oval(70, 70, 130, 130, fill="#000")
        self.canvas.create_oval(90, 90, 110, 110, fill="#fff")
        self.root.after(500, self.animate)

    def animate(self):
        self.canvas.delete("all")
        self.canvas.create_oval(50, 50, 150, 150, fill="#fff")
        self.canvas.create_oval(70, 70, 130, 130, fill="#000")
        self.canvas.create_oval(90, 90, 110, 110, fill="#fff")
        self.root.after(500, self.animate)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    spinner = LoadingSpinner()
    spinner.run()
