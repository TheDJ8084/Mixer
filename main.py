from tkinter import *
from tkinter import ttk
from tkdial import Jogwheel

root = Tk()
root.title("Mixer")
mainframe = ttk.Frame(root)
mainframe.columnconfigure(8, weight=1)
mainframe.rowconfigure(0, weight=1)
s = ttk.Style()
s.theme_use('classic')

s.configure('Vertical.Tscale')

ch01 = ttk.Frame(mainframe)
ch01.columnconfigure(10, weight=1)
ch01.rowconfigure(0, weight=1)
ch01high = Jogwheel(ch01, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch01high.set(value=0)
ch01mid = Jogwheel(ch01, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch01mid.set(value=0)
ch01freq = Jogwheel(ch01, text="Hz", start=5000, end=200, radius=90, button_radius=5, scroll_steps=50)
ch01freq.set(value=2600)
ch01low = Jogwheel(ch01, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch01low.set(value=0)
ch01pan = Jogwheel(ch01, start=100, end=-100, radius=90, button_radius=5, scroll_steps=10)
ch01pan.set(value=0)
ch01mute = ttk.Button(ch01, text='Mute', command="ch01mute")
ch01solo = ttk.Button(ch01, text='Solo', command="ch01solo")
ch01fader = ttk.Scale(ch01, orient=VERTICAL, length=140, from_=100, to=0)
ch01name = ttk.Label(ch01, text='CH01')
ch01sends = ttk.Button(ch01, text='Sends', command="ch01sends")

ch02 = ttk.Frame(mainframe)
ch02.columnconfigure(0, weight=1)
ch02.rowconfigure(10, weight=1)
ch02high = Jogwheel(ch02, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch02high.set(value=0)
ch02mid = Jogwheel(ch02, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch02mid.set(value=0)
ch02freq = Jogwheel(ch02, text="Hz", start=5000, end=200, radius=90, button_radius=5, scroll_steps=50)
ch02freq.set(value=2600)
ch02low = Jogwheel(ch02, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch02low.set(value=0)
ch02pan = Jogwheel(ch02, start=100, end=-100, radius=90, button_radius=5, scroll_steps=10)
ch02pan.set(value=0)
ch02mute = ttk.Button(ch02, text='Mute', command="ch02mute")
ch02solo = ttk.Button(ch02, text='Solo', command="ch02solo")
ch02fader = ttk.Scale(ch02, orient=VERTICAL, length=140, from_=100, to=0)
ch02name = ttk.Label(ch02, text='CH02')
ch02sends = ttk.Button(ch02, text='Sends', command="ch02sends")

ch03 = ttk.Frame(mainframe)
ch03.columnconfigure(0, weight=1)
ch03.rowconfigure(10, weight=1)
ch03high = Jogwheel(ch03, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch03high.set(value=0)
ch03mid = Jogwheel(ch03, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch03mid.set(value=0)
ch03freq = Jogwheel(ch03, text="Hz", start=5000, end=200, radius=90, button_radius=5, scroll_steps=50)
ch03freq.set(value=2600)
ch03low = Jogwheel(ch03, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch03low.set(value=0)
ch03pan = Jogwheel(ch03, start=100, end=-100, radius=90, button_radius=5, scroll_steps=10)
ch03pan.set(value=0)
ch03mute = ttk.Button(ch03, text='Mute', command="ch03mute")
ch03solo = ttk.Button(ch03, text='Solo', command="ch03solo")
ch03fader = ttk.Scale(ch03, orient=VERTICAL, length=140, from_=100, to=0)
ch03name = ttk.Label(ch03, text='CH03')
ch03sends = ttk.Button(ch03, text='Sends', command="ch03sends")

ch04 = ttk.Frame(mainframe)
ch04.columnconfigure(0, weight=1)
ch04.rowconfigure(10, weight=1)
ch04high = Jogwheel(ch04, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch04high.set(value=0)
ch04mid = Jogwheel(ch04, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch04mid.set(value=0)
ch04freq = Jogwheel(ch04, text="Hz", start=5000, end=200, radius=90, button_radius=5, scroll_steps=50)
ch04freq.set(value=2600)
ch04low = Jogwheel(ch04, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch04low.set(value=0)
ch04pan = Jogwheel(ch04, start=100, end=-100, radius=90, button_radius=5, scroll_steps=10)
ch04pan.set(value=0)
ch04mute = ttk.Button(ch04, text='Mute', command="ch04mute")
ch04solo = ttk.Button(ch04, text='Solo', command="ch04solo")
ch04fader = ttk.Scale(ch04, orient=VERTICAL, length=140, from_=100, to=0)
ch04name = ttk.Label(ch04, text='CH04')
ch04sends = ttk.Button(ch04, text='Sends', command="ch04sends")

ch05 = ttk.Frame(mainframe)
ch05.columnconfigure(0, weight=1)
ch05.rowconfigure(10, weight=1)
ch05high = Jogwheel(ch05, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch05high.set(value=0)
ch05mid = Jogwheel(ch05, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch05mid.set(value=0)
ch05freq = Jogwheel(ch05, text="Hz", start=5000, end=200, radius=90, button_radius=5, scroll_steps=50)
ch05freq.set(value=2600)
ch05low = Jogwheel(ch05, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch05low.set(value=0)
ch05pan = Jogwheel(ch05, start=100, end=-100, radius=90, button_radius=5, scroll_steps=10)
ch05pan.set(value=0)
ch05mute = ttk.Button(ch05, text='Mute', command="ch05mute")
ch05solo = ttk.Button(ch05, text='Solo', command="ch05solo")
ch05fader = ttk.Scale(ch05, orient=VERTICAL, length=140, from_=100, to=0)
ch05name = ttk.Label(ch05, text='CH05')
ch05sends = ttk.Button(ch05, text='Sends', command="ch05sends")

ch06 = ttk.Frame(mainframe)
ch06.columnconfigure(0, weight=1)
ch06.rowconfigure(10, weight=1)
ch06high = Jogwheel(ch06, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch06high.set(value=0)
ch06mid = Jogwheel(ch06, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch06mid.set(value=0)
ch06freq = Jogwheel(ch06, text="Hz", start=5000, end=200, radius=90, button_radius=5, scroll_steps=50)
ch06freq.set(value=2600)
ch06low = Jogwheel(ch06, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch06low.set(value=0)
ch06pan = Jogwheel(ch06, start=100, end=-100, radius=90, button_radius=5, scroll_steps=10)
ch06pan.set(value=0)
ch06mute = ttk.Button(ch06, text='Mute', command="ch06mute")
ch06solo = ttk.Button(ch06, text='Solo', command="ch06solo")
ch06fader = ttk.Scale(ch06, orient=VERTICAL, length=140, from_=100, to=0)
ch06name = ttk.Label(ch06, text='CH06')
ch06sends = ttk.Button(ch06, text='Sends', command="ch06sends")

ch07 = ttk.Frame(mainframe)
ch07.columnconfigure(0, weight=1)
ch07.rowconfigure(10, weight=1)
ch07high = Jogwheel(ch07, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch07high.set(value=0)
ch07mid = Jogwheel(ch07, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch07mid.set(value=0)
ch07freq = Jogwheel(ch07, text="Hz", start=5000, end=200, radius=90, button_radius=5, scroll_steps=50)
ch07freq.set(value=2600)
ch07low = Jogwheel(ch07, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch07low.set(value=0)
ch07pan = Jogwheel(ch07, start=100, end=-100, radius=90, button_radius=5, scroll_steps=10)
ch07pan.set(value=0)
ch07mute = ttk.Button(ch07, text='Mute', command="ch07mute")
ch07solo = ttk.Button(ch07, text='Solo', command="ch07solo")
ch07fader = ttk.Scale(ch07, orient=VERTICAL, length=140, from_=100, to=0)
ch07name = ttk.Label(ch07, text='CH07')
ch07sends = ttk.Button(ch07, text='Sends', command="ch07sends")

ch08 = ttk.Frame(mainframe)
ch08.columnconfigure(0, weight=1)
ch08.rowconfigure(10, weight=1)
ch08high = Jogwheel(ch08, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch08high.set(value=0)
ch08mid = Jogwheel(ch08, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch08mid.set(value=0)
ch08freq = Jogwheel(ch08, text="Hz", start=5000, end=200, radius=90, button_radius=5, scroll_steps=50)
ch08freq.set(value=2600)
ch08low = Jogwheel(ch08, text="dB", start=15, end=-15, radius=90, button_radius=5, scroll_steps=1)
ch08low.set(value=0)
ch08pan = Jogwheel(ch08, start=100, end=-100, radius=90, button_radius=5, scroll_steps=10)
ch08pan.set(value=0)
ch08mute = ttk.Button(ch08, text='Mute', command="ch08mute")
ch08solo = ttk.Button(ch08, text='Solo', command="ch08solo")
ch08fader = ttk.Scale(ch08, orient=VERTICAL, length=140, from_=100, to=0)
ch08name = ttk.Label(ch08, text='CH08')
ch08sends = ttk.Button(ch08, text='Sends', command="ch08sends")


def render():
    mainframe.grid(column=0, row=0)

    ch01.grid(column=0, row=0)
    ch01high.grid(column=0, row=1)
    ch01mid.grid(column=0, row=2)
    ch01freq.grid(column=0, row=3)
    ch01low.grid(column=0, row=4)
    ch01pan.grid(column=0, row=5)
    ch01mute.grid(column=0, row=6)
    ch01solo.grid(column=0, row=7)
    ch01fader.grid(column=0, row=8)
    ch01name.grid(column=0, row=9)
    ch01sends.grid(column=0, row=10)

    ch02.grid(column=1, row=0)
    ch02high.grid(column=0, row=1)
    ch02mid.grid(column=0, row=2)
    ch02freq.grid(column=0, row=3)
    ch02low.grid(column=0, row=4)
    ch02pan.grid(column=0, row=5)
    ch02mute.grid(column=0, row=6)
    ch02solo.grid(column=0, row=7)
    ch02fader.grid(column=0, row=8)
    ch02name.grid(column=0, row=9)
    ch02sends.grid(column=0, row=10)

    ch03.grid(column=2, row=0)
    ch03high.grid(column=0, row=1)
    ch03mid.grid(column=0, row=2)
    ch03freq.grid(column=0, row=3)
    ch03low.grid(column=0, row=4)
    ch03pan.grid(column=0, row=5)
    ch03mute.grid(column=0, row=6)
    ch03solo.grid(column=0, row=7)
    ch03fader.grid(column=0, row=8)
    ch03name.grid(column=0, row=9)
    ch03sends.grid(column=0, row=10)

    ch04.grid(column=3, row=0)
    ch04high.grid(column=0, row=1)
    ch04mid.grid(column=0, row=2)
    ch04freq.grid(column=0, row=3)
    ch04low.grid(column=0, row=4)
    ch04pan.grid(column=0, row=5)
    ch04mute.grid(column=0, row=6)
    ch04solo.grid(column=0, row=7)
    ch04fader.grid(column=0, row=8)
    ch04name.grid(column=0, row=9)
    ch04sends.grid(column=0, row=10)

    ch05.grid(column=4, row=0)
    ch05high.grid(column=0, row=1)
    ch05mid.grid(column=0, row=2)
    ch05freq.grid(column=0, row=3)
    ch05low.grid(column=0, row=4)
    ch05pan.grid(column=0, row=5)
    ch05mute.grid(column=0, row=6)
    ch05solo.grid(column=0, row=7)
    ch05fader.grid(column=0, row=8)
    ch05name.grid(column=0, row=9)
    ch05sends.grid(column=0, row=10)

    ch06.grid(column=5, row=0)
    ch06high.grid(column=0, row=1)
    ch06mid.grid(column=0, row=2)
    ch06freq.grid(column=0, row=3)
    ch06low.grid(column=0, row=4)
    ch06pan.grid(column=0, row=5)
    ch06mute.grid(column=0, row=6)
    ch06solo.grid(column=0, row=7)
    ch06fader.grid(column=0, row=8)
    ch06name.grid(column=0, row=9)
    ch06sends.grid(column=0, row=10)

    ch07.grid(column=6, row=0)
    ch07high.grid(column=0, row=1)
    ch07mid.grid(column=0, row=2)
    ch07freq.grid(column=0, row=3)
    ch07low.grid(column=0, row=4)
    ch07pan.grid(column=0, row=5)
    ch07mute.grid(column=0, row=6)
    ch07solo.grid(column=0, row=7)
    ch07fader.grid(column=0, row=8)
    ch07name.grid(column=0, row=9)
    ch07sends.grid(column=0, row=10)

    ch08.grid(column=7, row=0)
    ch08high.grid(column=0, row=1)
    ch08mid.grid(column=0, row=2)
    ch08freq.grid(column=0, row=3)
    ch08low.grid(column=0, row=4)
    ch08pan.grid(column=0, row=5)
    ch08mute.grid(column=0, row=6)
    ch08solo.grid(column=0, row=7)
    ch08fader.grid(column=0, row=8)
    ch08name.grid(column=0, row=9)
    ch08sends.grid(column=0, row=10)


render()
root.mainloop()
