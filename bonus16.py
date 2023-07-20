import PySimpleGUI as sg

label1 = sg.Text("Select files to compress:  ")
input1 = sg.Input()
choose1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose2 = sg.FilesBrowse("Choose")

compressed = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose1],
                           [label2, input2, choose2],
                           [compressed]])

window.read()
window.close()