import PySimpleGUI as sg
from zip_extractor18 import extract_archive

sg.theme("Black")

zip_lbl = sg.Text("Select Folder: ")
zip_input = sg.Input()
zip_btn = sg.FileBrowse("Choose", key='archive')

des_lbl = sg.Text("Select Destination Folder: ")
des_input = sg.Input()
des_btn = sg.FolderBrowse("Choose", key='destin')

extract_btn = sg.Button("Extract")
out_lbl = sg.Text(key='output', text_color='blue')

window = sg.Window("Archive Extractor",
                   [[zip_lbl, zip_input, zip_btn],
                    [des_lbl, des_input, des_btn],
                    [extract_btn, out_lbl]])
while True:
    event, values = window.read()
    archive_path = values["archive"]
    des_path = values["destin"]
    extract_archive(archive_path, des_path)
    window['output'].update(value="Completed!")
window.close()
