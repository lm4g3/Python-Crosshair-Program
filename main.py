














##################################################################

#█▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀ █░░█ █▀▀█ ░▀░ █▀▀█   ▀▀█▀▀ █▀▀█ █▀▀█ █░░
#█░░ █▄▄▀ █░░█ ▀▀█ ▀▀█ █▀▀█ █▄▄█ ▀█▀ █▄▄▀   ░░█░░ █░░█ █░░█ █░░
#▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀ ▀░▀▀   ░░▀░░ ▀▀▀▀ ▀▀▀▀ ▀▀▀

##########################SETTING#################################
hud = True
hud_time = True
hud_rainbow = False
hud_color = "white"

circle = False
circle_rainbow = False
circle_color = "white"
circle_size = 150
cricle_width = 1.5

cross = True
cross_rainbow = True
cross_color = "white"
cross_size = 15
cross_thickness = 1.5

##################################################################














import tkinter as tk
import time
import colorsys
def rainbow_text():
    global current_color_index
    hue = current_color_index / 60.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color_code = "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))
    if hud_rainbow == True:
        label.config(fg=color_code)
    else:
        label.config(fg=hud_color)
    current_color_index = (current_color_index + 1) % 360
    rainbow_color_for_circle = rainbow_color(current_color_index / 60.0)
    rainbow_color_for_cross = rainbow_color(current_color_index / 60.0)
    if circle == True and circle_rainbow == True:
        draw_centered_circle(canvas, 150, 150, 70, rainbow_color_for_circle, cricle_width)
    elif circle == True and circle_rainbow == False:
        draw_centered_circle(canvas, 150, 150, circle_size, circle_color, cricle_width)

    if cross == True and cross_rainbow == True:
        draw_cross(canvas, 150, 150, 6, cross_thickness, rainbow_color_for_cross)
    elif cross == True and cross_rainbow == False:
        draw_cross(canvas, 150, 150, cross_size, cross_thickness, cross_color)
    root.after(20, rainbow_text)  # 실행 간격을 20ms로 변경
def update_time():
    current_time = time.strftime("%I:%M:%p")
    text = ""
    if hud == True:
        text = f"Crosshair"
        if hud_time == True:
            text = text + f" [{current_time}]"
        if circle == True:
            text = text + "\n| Circle"
        if circle_rainbow == True:
            text = text + " (rainbow)"
        if cross == True:
            text = text + "\n| Cross"
        if cross_rainbow == True:
            text = text + " (rainbow)"
    label.config(text=text)
    root.after(1000, update_time)
def rainbow_color(hue):
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))
def draw_centered_circle(canvas, x, y, radius, color, width):
    x0 = x - radius
    y0 = y - radius
    x1 = x + radius
    y1 = y + radius
    return canvas.create_oval(x0, y0, x1, y1, outline=color, width=width)
def draw_cross(canvas, x, y, size, thickness, color):
    half_thickness = thickness // 2
    canvas.create_line(x, y - size, x, y + size, fill=color, width=thickness)  # 세로선
    canvas.create_line(x - size, y, x + size, y, fill=color, width=thickness)  # 가로선
root = tk.Tk()
root.geometry('1920x1080')
root.overrideredirect(True)
root.config(bg='#000000')
root.attributes("-alpha", 1)
root.wm_attributes("-topmost", 1)
root.attributes('-transparentcolor', '#000000', '-topmost', 1)
root.resizable(False, False)
label = tk.Label(root, text="", bg="black", fg="#FFFFFF", font=("Arial", 20), bd=0, justify='left')
label.place(x=0, y=0)
canvas = tk.Canvas(root, width=300, height=300, bg="black", highlightthickness=0)
canvas.place(x=(root.winfo_screenwidth() - 300) // 2, y=(root.winfo_screenheight() - 300) // 2)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = screen_width // 2
center_y = screen_height // 2
current_color_index = 0
rainbow_text()
update_time()
root.mainloop()
