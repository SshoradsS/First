import tkinter as tk
from tkinter import messagebox
import webbrowser

def bye():
    root.destroy()

def amozesh():
    messagebox.showinfo("آموزش نصب بازی", "برای نصب بازی، بازی را از سایت زیر دانلود کنید.")
    result = messagebox.askquestion("GoldTeam", "آیا می‌خواهی سایت را باز کنی؟")
    if result == 'yes':
        webbrowser.open("https://gold-team.org/")
    else:
        root.destroy()

# ساخت پنجره
root = tk.Tk()
root.title("برنامه نصب بازی")
root.geometry("600x400")

# رنگ‌های RGB برای افکت گیمینگ
colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8F00FF"]
color_index = 0

# تغییر رنگ پس‌زمینه و رنگ نوشته
def change_bg():
    global color_index
    # تغییر پس‌زمینه پنجره و نوشته‌های دیگر
    root.configure(bg=colors[color_index])
    
    color_index = (color_index + 1) % len(colors)  # تغییر رنگ بعدی
    root.after(200, change_bg)  # هر 200 میلی‌ثانیه یکبار رنگ تغییر می‌کنه

# شروع انیمیشن تغییر رنگ
change_bg()

# عنوان خوش‌آمدگویی
welcome = tk.Label(root, text="🎮 به برنامه آموزش نصب بازی خوش آمدید 🎮", font=("B Nazanin", 18, "bold"), fg="white", bg=colors[0])
welcome.pack(pady=20)

# دکمه آموزش
amozesh_btn = tk.Button(root, text="آموزش نصب", font=("B Nazanin", 16), bg="#1e3d59", fg="white", width=15, command=amozesh, cursor="hand2")
amozesh_btn.pack(pady=10)

# دکمه خروج
exit_btn = tk.Button(root, text="خروج", font=("B Nazanin", 14), bg="#c0392b", fg="white", width=10, command=bye, cursor="hand2")
exit_btn.pack(pady=10)

# اجرای برنامه
root.mainloop()

print('end')
