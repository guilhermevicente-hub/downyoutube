import PySimpleGUI as sg 
from pytube import YouTube

sg.theme("Dark Blue 16")

interface = [
    
    [sg.Titlebar("Youtube Download", None, "red", "white")],
    [sg.Text("URL")],
    [sg.Input(size=(50,1), key="url")],
    [sg.Button("download")]    
]


janela = sg.Window("window", interface)

while True:
    evento, valor = janela.read()
    
    if valor == sg.WIN_CLOSED:
        break
    
    if evento == "download":
        link = janela["url"].get()
        video = YouTube(link)
        stream = video.streams.get_highest_resolution().download()
    print("Download completado")
janela.close()
exit()