import tkinter.messagebox
import threading
from timmer import timmer

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

t = timmer()    # 计时器
def run_timmer():
    def monitoring_state(): # 监视函数
        while t.running:    # 运行状态下，会一直阻塞 ’停止提示‘ 的发生
            continue
        state.config(text='Stopped')
        tkinter.messagebox.showinfo(title='Over', message='STOP！！！')

    hour = hours.get()
    minute = minutes.get()
    t.hour = hour   # 给计时器设置参数
    t.minute = minute
    # 验证输入参数的合法性
    if (hour == '' or '0' <= hour < 'inf') \
            and (minute == '' or '0' <= minute < '60') \
            and (hour != '0' or minute != '0') \
            and (hour != '' or minute != '') \
            and not t.running:
        state.config(text='Running')
        if hour == '':  # 如果没有输入，默认是 0
            hours.insert(0, 0)
            t.hour = '0'
        if minute == '':
            minutes.insert(0, 0)
            t.minute = '0'

        run = threading.Thread(target=t.run)    # 开辟一个计时线程
        run.setDaemon(True)
        run.start()
        monitor = threading.Thread(target=monitoring_state) # 监听状态线程
        monitor.setDaemon(True)
        monitor.start()
    else:
        tkinter.messagebox.showerror(title='Ops!', message='Are you fool?')

def stop_timmer():
    if t.running:   # 只有运行状态下可以中止
        stop = threading.Thread(target=t.stop)  # 中止线程
        stop.setDaemon(True)
        stop.start()
        # 跟新GUI的状态
        state.config(text='Stopped')
        hours.delete(0, tkinter.END)
        minutes.delete(0, tkinter.END)

tkinter.Button(frame_b, text='开始', command=run_timmer).pack(side='left')
tkinter.Button(frame_b, text='中止', command=stop_timmer).pack(side='right')
window.mainloop()
