import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import moviepy.editor
from PIL import Image, ImageTk

root = tkinter.Tk()
root.iconbitmap('Mp3.ico.jpg')
root.title('MP4 TO MP3')
root.grid_columnconfigure(0, weight=1)  # set column 0 to expand
root.grid_rowconfigure(1, weight=1)  # set row 1 to expand
# giving the label to screen
c = tkinter.Canvas(root, width=150, height=100)
c.grid(columnspan=3)

# adding the image
img = Image.open('Test1.png')
logo = ImageTk.PhotoImage(img)
lo = tkinter.Label(image=logo)
lo.image = logo
lo.grid(columnspan=3, pady=2)

# Now adding the label to canvas
la = tkinter.Label(root, text='CONVERT MP4 TO MP3', background='cyan', font='RAILWAY')
la.grid(columnspan=3, pady=3)  # added pady to move label upward

# adding the function
def start():
    # condition to see the weather the conversion get completed or not
    but.grid_remove()
    la.grid(columnspan=3, pady=50)
    la.config(text='CONVERTING...', fg='red', border=4)
    # here the file conversion used
    file = askopenfilename()
    vid = moviepy.editor.VideoFileClip(file)
    aud = vid.audio
    output_path = asksaveasfilename(defaultextension='.mp3', filetypes=[('MP3 file', '*.mp3')], initialfile='Demo.mp3')
    aud.write_audiofile(output_path)
    la.config(text='CONVERTED', fg='red', border=4)
    # this destroy the window after the 3000 sec
    la.after(3000, root.destroy())


# Now add the button
but = tkinter.Button(root, text='CONVERT', command=lambda: start(), border=4, background='red', font='Elephant')
but.grid(columnspan=3, pady=50)  # added pady to move button upward

root.mainloop()
