import PySimpleGUI as sg


class PronosticoView():
    def __init__(self) -> None:
        BACKGROUND_COLOR = "#f3f3f2"
        PRIMARY_TEXT_COLOR = "#59595b"
        super().__init__()
        selection = {}
        cols = ["indexador a", "indexador b", "indexador c",
                "indexador d", "indexador e", "indexador f", "indexador g"]
        summary_viewer = [
            [sg.Text("Resumen:", background_color=BACKGROUND_COLOR,
                     text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 18))],
            [sg.Text("", key="folder_name", background_color=BACKGROUND_COLOR,
                     text_color=PRIMARY_TEXT_COLOR)],
            [sg.Text("", key="selected_index",
                     background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR)],
        ]
        indexadores_viewer = [
            [sg.Text(f'{i}', pad=((0, 0), (12, 12)), background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("               ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False,
                      enable_events=True, key=f"-a&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("               ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False,
                      enable_events=True, key=f"-b&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("               ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False,
                      enable_events=True, key=f"-c&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("               ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False,
                      enable_events=True, key=f"-d&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             ] for i in cols
        ]

        file_list_column = [
            [
                sg.Image(source="imgs/img2.png", pad=((70, 200), (10, 15)),
                         size=(160, 160), background_color=BACKGROUND_COLOR),
                sg.Image(source="imgs/img2.png", pad=((0, 0), (10, 15)),  size=(
                    160, 160), background_color=BACKGROUND_COLOR),
            ],
            [sg.Text("Titulo de la app", pad=((220, 0), (10, 15)),
                     background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, font=("Lohit", 22))],
            [
                sg.Text("Directorio de Trabajo",
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.In(size=(60, 20), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse(font=(
                    'Helvetica', 10)),

            ],
            [
                sg.Text("Indexadores", pad=((0, 0), (50, 0)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 14)),
                sg.Button(image_source="imgs/reload.png", image_size=(15, 15), pad=((5, 0), (45, 0)),
                          button_color=BACKGROUND_COLOR, border_width=0,
                          tooltip="Reiniciar valores", enable_events=True, key="-restore-")
            ],
            [sg.HSeparator()],
            [
                sg.Text(" Opción A", pad=((140, 0), (10, 10)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Text(" Opción B", pad=((40, 0), (10, 10)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Text(" Opción C", pad=((50, 0), (10, 10)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Text(" Opción D", pad=((50, 0), (10, 10)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
            ],
            [
                sg.Column(indexadores_viewer, scrollable=True, size=(
                    650, 250),  vertical_scroll_only=True, background_color=BACKGROUND_COLOR),
            ],
        ]

        layout = [
            [
                sg.Column(file_list_column, background_color=BACKGROUND_COLOR),
                sg.VSeperator(),

                sg.Column(summary_viewer, size=(
                    450, 650), background_color=BACKGROUND_COLOR),
                sg.Column([[sg.Button('Calcular', size=(0, 0), visible=True, font=(
                    'Helvetica', 11), key='go')]], element_justification='', expand_x=True, background_color=BACKGROUND_COLOR),
            ]
        ]

        window = sg.Window("Name of app", layout,
                           background_color=BACKGROUND_COLOR)
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "-FOLDER-":
                folder = values["-FOLDER-"]
                window["folder_name"].update(
                    f"  Directorio seleccionado: {folder}")
            if "-a&" in event or "-b&" in event or "-c&" in event or "-d&" in event:
                value, key = event.split("&")
                selection[key] = value
                summary = ""
                for selected in selection:
                    data = []
                    data.append(sg.Text(""))
                    summary = f"{summary}\n\n  {selected} {selection[selected]}"
                window["selected_index"].update(summary)
            # if "-restore-" in event:
            #     selection = {}
            #     event["-a&1"] = False
            #     window["selected_index"].update("")
        try:
            window.close()
        except SystemExit:
            print("Closing Window")


if __name__ == '__main__':
    pronosticos_view = PronosticoView()
