import tkinter as tk
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("珠海天气")
        self.root.geometry("430x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#dfeeff")

        # 主卡片
        self.card = tk.Frame(
            root,
            width=390,
            height=360,
            bg="#ffffff",
            padx=20,
            pady=18,
            bd=0
        )
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        # 顶部
        top = tk.Frame(self.card, bg="#ffffff")
        top.pack(fill="x")

        left = tk.Frame(top, bg="#ffffff")
        left.pack(side="left")

        city = tk.Label(
            left,
            text="珠海",
            font=("Microsoft YaHei", 26, "bold"),
            bg="#ffffff",
            fg="#1f3a5f"
        )
        city.pack(anchor="w")

        date_text = datetime.now().strftime("%Y-%m-%d")
        date_label = tk.Label(
            left,
            text=date_text,
            font=("Microsoft YaHei", 12),
            bg="#ffffff",
            fg="#6d7d97"
        )
        date_label.pack(anchor="w", pady=(4, 0))

        icon = tk.Label(
            top,
            text="☀️",
            font=("Microsoft YaHei", 28),
            bg="#ffffff",
            fg="#f8b400"
        )
        icon.pack(side="right")

        # 温度
        temp = tk.Label(
            self.card,
            text="27°",
            font=("Microsoft YaHei", 42, "bold"),
            bg="#ffffff",
            fg="#1c2d4d"
        )
        temp.pack(anchor="w", pady=(20, 0))

        condition = tk.Label(
            self.card,
            text="晴",
            font=("Microsoft YaHei", 18),
            bg="#ffffff",
            fg="#4e6282"
        )
        condition.pack(anchor="w")

        # 信息框
        info = tk.Frame(self.card, bg="#ffffff")
        info.pack(fill="x", pady=(22, 0))

        box1 = tk.Frame(info, bg="#f3f8ff", width=100, height=80)
        box1.grid(row=0, column=0, padx=(0, 10), sticky="nsew")
        box2 = tk.Frame(info, bg="#f3f8ff", width=100, height=80)
        box2.grid(row=0, column=1, padx=10, sticky="nsew")
        box3 = tk.Frame(info, bg="#f3f8ff", width=100, height=80)
        box3.grid(row=0, column=2, padx=(10, 0), sticky="nsew")

        info.grid_columnconfigure(0, weight=1)
        info.grid_columnconfigure(1, weight=1)
        info.grid_columnconfigure(2, weight=1)

        tk.Label(box1, text="湿度", bg="#f3f8ff", fg="#7a8aa3", font=("Microsoft YaHei", 11)).place(relx=0.5, rely=0.25, anchor="center")
        tk.Label(box1, text="68%", bg="#f3f8ff", fg="#2c4365", font=("Microsoft YaHei", 18, "bold")).place(relx=0.5, rely=0.68, anchor="center")

        tk.Label(box2, text="风速", bg="#f3f8ff", fg="#7a8aa3", font=("Microsoft YaHei", 11)).place(relx=0.5, rely=0.25, anchor="center")
        tk.Label(box2, text="8 km/h", bg="#f3f8ff", fg="#2c4365", font=("Microsoft YaHei", 16, "bold")).place(relx=0.5, rely=0.68, anchor="center")

        tk.Label(box3, text="空气", bg="#f3f8ff", fg="#7a8aa3", font=("Microsoft YaHei", 11)).place(relx=0.5, rely=0.25, anchor="center")
        tk.Label(box3, text="良", bg="#f3f8ff", fg="#2c4365", font=("Microsoft YaHei", 18, "bold")).place(relx=0.5, rely=0.68, anchor="center")

def main():
    root = tk.Tk()
    WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


