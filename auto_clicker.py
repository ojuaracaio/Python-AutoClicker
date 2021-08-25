import tkinter as tk
import pyautogui as py
import time

def botao():
	time.sleep(int(entry_tempo.get()))
	for i in range(int(entry_quantia.get())):
		py.click()
		time.sleep(1/int(entry_velocidade.get()))


root = tk.Tk()
#título
root.title('Super Auto Clicker Boladíssimo')

#corpo

label_tempo = tk.Label(root, text='Tempo de espera (s)')
label_quantia = tk.Label(root, text='Nº de cliques')
label_velocidade = tk.Label(root, text='Velocidade dos cliques')

label_tempo.grid(row=0, column=0)
label_velocidade.grid(row=1, column=0)
label_quantia.grid(row=2,column=0)

entry_tempo = tk.Entry(root)
entry_quantia = tk.Entry(root)
entry_velocidade = tk.Entry(root)

entry_tempo.grid(row=0,column=1)
entry_velocidade.grid(row=1, column=1)
entry_quantia.grid(row=2,column=1)

botao_inicio = tk.Button(root, text='Iniciar', command=botao)
botao_inicio.grid(row=4, column=0, columnspan=2)

root.mainloop()
