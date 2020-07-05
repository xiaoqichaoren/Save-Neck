import tkinter.messagebox
import threading
import time

class timmer(threading.Thread):
    def __init__(self):
        super(timmer, self).__init__()
        self._running = False

    def stop(self):
        self._running = False
        state.config(text='Stopped')
        hours.delete(0, tkinter.END)
        minutes.delete(0, tkinter.END)

    def run(self) -> None:
        h_value = hours.get()
        m_value = minutes.get()
        if (h_value == '' or '0' <= h_value < 'inf') \
                and (m_value == '' or '0' <= m_value < '60') \
                and (not h_value == '0' or not m_value == '0') \
                and (not h_value == '' or not m_value == ''):
            if h_value == '':
                hours.insert(0, 0)
                h_value = 0
            if m_value == '':
                minutes.insert(0, 0)
                m_value = 0

            self._running = True
            state.config(text='Running')
            s = int(h_value) * 3600 + int(m_value) * 60
            while self._running and s != 0:
                time.sleep(1)
                s -= 1
            tkinter.messagebox.showinfo(title='Over', message='Time`s up')
        else:
            tkinter.messagebox.showerror(title='Ops!', message='Are you fool?')


if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('250x125')
    window.title('Save Neck')

    state = tkinter.Label(window, text='Stopped')
    state.pack()

    frame = tkinter.Frame(window)
    frame.pack()
    frame_l = tkinter.Frame(frame)
    frame_r = tkinter.Frame(frame)
    frame_b = tkinter.Frame(window)
    frame_l.pack(side='left')
    frame_r.pack(side='right')
    frame_b.pack()

    tkinter.Label(frame_r, text='小时').pack()
    tkinter.Label(frame_r, text='分钟').pack()
    hours = tkinter.Entry(frame_l, width=3)
    minutes = tkinter.Entry(frame_l, width=3)
    hours.pack()
    minutes.pack()

    t = timmer()
    def run_timmer():
        run = threading.Thread(target=t.run)
        run.setDaemon(True)
        run.start()
    def stop_timmer():
        stop = threading.Thread(target=t.stop)
        stop.setDaemon(True)
        stop.start()

    tkinter.Button(frame_b, text='开始', command=run_timmer).pack(side='left')
    tkinter.Button(frame_b, text='中止', command=stop_timmer).pack(side='right')
    window.mainloop()
