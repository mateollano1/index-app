import PySimpleGUI as sg


class PronosticoView():
    def __init__(self) -> None:
        BACKGROUND_COLOR = "#f3f3f2"
        PRIMARY_TEXT_COLOR = "#59595b"
        super().__init__()
        selection = {
            "Costos Variables": "-IPC",
            "Costo Marginal   ": "-IPC",
            "Precio CXC       ": "-IPC",
            "Otros Ingresos   ": "-IPC",
        }
        selection_conf = {
            "Año_Inicial        ": "",
            "Año_Final          ": "",
            "Despacho_central   ": False,
            "Impuesto_de_renta  ":"",
            "Días_por_cobrar    ":"",
            "Días_por_pagar     ":"",
        }

        cols = ["Costos Variables", "Costo Marginal   ", "Precio CXC       ",
                "Otros Ingresos   "]
        summary_viewer = [
            [sg.Text("Resumen", background_color=BACKGROUND_COLOR,
                     text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 16), pad=((250, 0), (0, 0)))],
            [sg.Text("Directorio Seleccionado:", key="folder_name", background_color=BACKGROUND_COLOR, pad=((30, 0), (10, 0)),
                     text_color=PRIMARY_TEXT_COLOR)],
            [sg.Text("Indexadores", pad=((150, 100), (30, 0))),
             sg.Text("Variables adicionales", pad=((10, 0), (30, 0))), ],
            [
                sg.Text('\n\n  Costos Variables                IPC\n\n  Costo Marginal                   IPC\n\n  Precio CXC                       IPC\n\n  Otros Ingresos                   IPC', key="selected_index", pad=((80, 20), (0, 0)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.VSeperator(),
                sg.Text("\n\n  Año Inicial                  \n\n  Año Final                    \n\n  Despacho central             False\n\n  Impuesto de renta            \n\n  Días por cobrar              \n\n  Días por pagar               ", key="selected_conf", pad=((10, 10), (0, 0)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR)],
        ]
        indexadores_viewer = [
            [sg.Text(f'{i}', pad=((0, 0), (12, 12)), background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=True, pad=((80, 0), (12, 12)),
                      enable_events=True, key=f"-IPC&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("        ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False, pad=((30, 0), (12, 12)),
                      enable_events=True, key=f"-IPP&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("           ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False, pad=((30, 0), (12, 12)),
                      enable_events=True, key=f"-PPI&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("        ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False, pad=((30, 0), (12, 12)),
                      enable_events=True, key=f"-CPI&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
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
                sg.Text(" IPC", pad=((200, 0), (20, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Text(" IPP", pad=((75, 0), (20, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Text(" PPI", pad=((83, 0), (20, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Text(" CPI", pad=((75, 0), (20, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
            ],
            [
                sg.Column(indexadores_viewer, size=(
                    650, 250),  vertical_scroll_only=True, background_color=BACKGROUND_COLOR),
            ],
        ]
        second_file_list_column = [
            [
                sg.Text("Configuración", pad=((0, 0), (0, 0)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 14)),
            ],
            [sg.HSeparator()],
            [
                sg.Text('Año Inicial', size=(15, 1), pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(size=(15, 1), pad=(
                    (10, 0), (10, 5)), key="-conf&Año_Inicial        ", enable_events=True,),
                sg.Text('Año Final', size=(15, 1), pad=((60, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(size=(15, 1), pad=(
                    (10, 100), (10, 5)), key="-conf&Año_Final          ", enable_events=True,),
            ],
            [
                sg.Text('Despacho Central', pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Checkbox(
                    '',
                    enable_events=True,
                    background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, key="-conf&Despacho_central   ")
            ],
            [
                sg.Text('Impuesto de renta', size=(15, 1), pad=(
                    (10, 0), (10, 5)), background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(size=(15, 1), pad=(
                    (10, 0), (10, 5)), key="-conf&Impuesto_de_renta  ", enable_events=True)
            ],
            [
                sg.Text('Días por cobrar', size=(15, 1), pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(
                    size=(15, 1), pad=((10, 0), (10, 5)), key="-conf&Días_por_cobrar    ", enable_events=True)
            ],
            [
                sg.Text('Días por pagar', size=(15, 1), pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(
                    size=(15, 1), pad=((10, 0), (10, 5)), key="-conf&Días_por_pagar     ", enable_events=True)
            ],
            [sg.Column(summary_viewer, size=(550, 330), pad=((0, 0), (50, 0)),
                       background_color=BACKGROUND_COLOR), ],
            [sg.Button('Calcular',  visible=True, font=(
                'Helvetica', 11), key='go', border_width=0,
                button_color="#454851", pad=((200, 0), (0, 50))
            ),
                sg.Button('Reiniciar Valores',  visible=True, font=(
                    'Helvetica', 11), key='go', border_width=0,
                button_color="#454851", pad=((20, 0), (0, 50))
            )]
        ]

        layout = [

            [
                sg.Column(file_list_column, background_color=BACKGROUND_COLOR),
                sg.VSeperator(),
                sg.Column(second_file_list_column,
                          background_color=BACKGROUND_COLOR),
                # sg.Column(summary_viewer, size=(
                #     450, 650), background_color=BACKGROUND_COLOR),
                # sg.Column([[sg.Button('Calcular', size=(0, 0), visible=True, font=(
                #     'Helvetica', 11), key='go', border_width=0,
                #     button_color="#454851"
                #     )]], element_justification='', expand_x=True, background_color=BACKGROUND_COLOR
                #     ),
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
                continue
            if "-IPC&" in event or "-IPP&" in event or "-PPI&" in event or "-CPI&" in event:
                value, key = event.split("&")
                selection[key] = value
                summary = ""
                for selected in selection:
                    data = []
                    data.append(sg.Text(""))
                    summary = f"{summary}\n\n  {selected}                {selection[selected][1:]}"
                window["selected_index"].update(summary)
                continue
            if "-conf&" in event:
                value, key = event.split("&")
                input_value = values[event]
                selection_conf[key] = input_value
                conf_summary = ""
                # conf_summary = f"""\n\n  Año Inicial:  {selection_conf['Año_Inicial']}        Año Final:  {selection_conf['Año_Final']} \n\n
                # Despacho central:  {selection_conf['Despacho_central']}"""
                for selected in selection_conf:
                    conf_summary = f"{conf_summary}\n\n  {selected.replace('_',' ')}          {selection_conf[selected]}"
                window["selected_conf"].update(conf_summary)
            # if "-restore-" in event:
            #     selection = {}
            #     event["-IPC1"] = False
            #     window["selected_index"].update("")
        try:
            window.close()
        except SystemExit:
            print("Closing Window")


if __name__ == '__main__':
    pronosticos_view = PronosticoView()
