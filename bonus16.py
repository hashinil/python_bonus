import PySimpleGUI as sg
import zip_creater16

label1 = sg.Text("Select files to compress:  ")
input1 = sg.Input()
choose1 = sg.FilesBrowse("Choose", key='file_path')

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose2 = sg.FolderBrowse("Choose", key='folder_path')

compressed = sg.Button("Compress")
compressed_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose1],
                           [label2, input2, choose2],
                           [compressed, compressed_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepath = values["file_path"].split(";")
    folder = values["folder_path"]
    zip_creater16.make_archive(filepath, folder)
    window["output"].update(value="Completed!")

    print(filepath)
    print(folder)
window.close()