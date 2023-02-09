import PySimpleGUI as sg
from pch_evaluator import *
import traceback

from numpy import size


class PronosticoView():
    def __init__(self) -> None:
        BACKGROUND_COLOR = "#f3f3f2"
        PRIMARY_TEXT_COLOR = "#59595b"
        DEFAULT_SELECTED_INDEX = "\n\n  Costo Marginal                   IPC\n\n  Precio CXC                       IPC\n\n  Otros Ingresos                   IPC\n\n  CERE                               IPC\n\n  FAZNI                               IPC\n\n  Ley 99                               IPC\n\n  AGC                                 IPC"
        DEFAULT_SELECTED_CONF = "\n\n  Año Inicial                     \n\n  Año Final                       \n\n  Despacho central           False\n\n  Año Evaluación              \n\n  Impuesto de renta           \n\n  costo patrimonio             \n\n  Días por cobrar               \n\n  Días por pagar                \n\n  Aumento ampliación        \n\n  Costo ampliación          \n\n  Año ampliación            \n\n  Años a diferir                   "
        METHOD_VALUES = {
            "Año_Inicial             ": "init_year",
            "Año_Final               ": "end_year",
            "Despacho_central   ": "central_dispatched",
            "Días_por_cobrar       ": "dias_cobrar",
            "Días_por_pagar        ": "dias_pagar",
            "Aumento_ampliación": "flow_increase",
            "Costo_ampliación     ": "increase_cost",
            "Año_ampliación        ": "year_increase",
            "costo_patrimonio     ": "costo_patrimonio",
            "Años_a_diferir           ": "differ_option_period",
            "Capacidad_ENFICC": "enficc_capacity",
            "Año_disponibilidad_ENFICC": "enficc_available_year"
        }
        INDEX_VALUES = {
            "Costo Marginal   ": "marginal cost",
            "Precio CXC       ": "confiability prices",
            "Otros Ingresos   ": "other incomes",
            "CERE               ": "CERE",
            "FAZNI               ": "fazni",
            "Ley 99               ": "Ley 99",
            "AGC                 ": "Agc",
            "Precios contratos   ": "contract prices",
            "Delta I": "Delta I"
        }
        DEFAULT_INDEX_SELECTION = {
            "Costo Marginal   ": "-IPC",
            "Precio CXC       ": "-IPC",
            "Otros Ingresos   ": "-IPC",
            "CERE               ": "-IPC",
            "FAZNI               ": "-IPC",
            "Ley 99               ": "-IPC",
            "AGC                 ": "-IPC",
            "Precios contratos   ": "-IPC",
            "Delta I": "-IPC",

        }
        DEFAULT_SELECTION_CONF = {
            "Año_Inicial             ": "",
            "Año_Final               ": "",
            "Despacho_central   ": False,
            "Año_Evaluación      ": "",
            "costo_patrimonio     ": "",
            "Días_por_cobrar       ": "",
            "Días_por_pagar        ": "",
            "Aumento_ampliación": "",
            "Costo_ampliación     ": "",
            "Año_ampliación        ": "",
            "Años_a_diferir           ": "",
            "Capacidad_ENFICC": "",
            "Año_disponibilidad_ENFICC": ""
        }
        super().__init__()
        selection = DEFAULT_INDEX_SELECTION.copy()
        selection_conf = DEFAULT_SELECTION_CONF.copy()
        folder = ""
        deva = [
            [sg.Text(DEFAULT_SELECTED_INDEX, key="selected_index", pad=((80, 20), (0, 75)),
                     background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.VSeperator(),
             sg.Text(DEFAULT_SELECTED_CONF, key="selected_conf", pad=((10, 10), (0, 0)),
                     background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR)]]
        summary_viewer = [
            [sg.Text("Resumen", background_color=BACKGROUND_COLOR,
                     text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 14), pad=((270, 0), (0, 0)))],
            [sg.Text("Directorio Seleccionado:", key="folder_name", background_color=BACKGROUND_COLOR, pad=((30, 0), (10, 0)),
                     text_color=PRIMARY_TEXT_COLOR)],
            [sg.Text("Indexadores", pad=((150, 100), (20, 0))),
             sg.Text("Variables adicionales", pad=((60, 0), (20, 0))), ],
            [
                sg.Column(deva, pad=((0, 0), (0, 15)), size=(570, 200),
                          vertical_scroll_only=True, background_color=BACKGROUND_COLOR, scrollable=True),
            ],
        ]
        indexadores_viewer = [
            [sg.Text(f'{i}', pad=((0, 0), (8, 8)), size=(13, 1), background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=True, pad=((60, 0), (8, 8)),
                      enable_events=True, key=f"-IPC&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("        ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False, pad=((25, 0), (8, 8)),
                      enable_events=True, key=f"-IPP&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("           ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False, pad=((25, 0), (8, 8)),
                      enable_events=True, key=f"-PPI&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             sg.T("        ", background_color=BACKGROUND_COLOR),
             sg.Radio(f"", f"RADIO{i}", default=False, pad=((25, 55), (8, 8)),
                      enable_events=True, key=f"-CPI&{i}", background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
             ] for i in DEFAULT_INDEX_SELECTION
        ]

        file_list_column = [
            [
                sg.Image(source="imgs/hidro5.png", pad=((20, 20), (30, 30)),
                         size=(237, 120), background_color=BACKGROUND_COLOR),
                sg.Image(source="imgs/idea1.png", pad=((0, 50), (30, 30)),  size=(
                    120, 120), background_color=BACKGROUND_COLOR),
                sg.Image(source="imgs/gen.png", pad=((0, 0), (30, 30)),  size=(
                    120, 120), background_color=BACKGROUND_COLOR),
            ],
            [sg.Text("Evaluación Económica", pad=((190, 0), (0, 0)),
                     background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 22))],
            [sg.Text("Proyectos Hidroeléctricos", pad=((220, 0), (0, 15)),
                     background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 14))],
            [
                sg.Text("Directorio de Trabajo",
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.In(size=(54, 20), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse(font=(
                    'Helvetica', 10)),

            ],
            [
                sg.Text("Indexadores", pad=((0, 0), (20, 0)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 14)),
                sg.Button(image_source="imgs/reload.png", image_size=(15, 15), pad=((5, 0), (15, 0)),
                          button_color=BACKGROUND_COLOR, border_width=0,
                          tooltip="Reiniciar valores", enable_events=True, key="-restore-")
            ],
            [sg.HSeparator()],
            [
                sg.Text(" IPC", pad=((200, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Text(" IPP", pad=((64, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Text(" PPI", pad=((77, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Text(" CPI", pad=((72, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
            ],
            [
                sg.Column(indexadores_viewer, pad=((30, 0), (0, 15)), scrollable=True,
                          vertical_scroll_only=True, background_color=BACKGROUND_COLOR),
            ],
        ]
        second_file_list_column = [
            [
                sg.Text("Configuración", pad=((0, 0), (0, 0)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 14)),
            ],
            [sg.HSeparator()],
            [
                sg.Text('Año Inicial', size=(17, 1), pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(size=(15, 1), pad=(
                    (10, 0), (10, 5)), key="-conf&Año_Inicial             ", enable_events=True,),
                sg.Text('Año Final', size=(15, 1), pad=((60, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(size=(15, 1), pad=(
                    (10, 100), (10, 5)), key="-conf&Año_Final               ", enable_events=True,),
            ],
            [
                sg.Text('Despacho Central', size=(17, 1), pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.Checkbox(
                    '',
                    pad=((5, 90), (0, 0)),
                    enable_events=True,
                    background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, key="-conf&Despacho_central   "),
                sg.Text('Año Evaluación', size=(15, 1), pad=((60, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(size=(15, 1), pad=(
                    (10, 100), (10, 5)), key="-conf&Año_Evaluación      ", enable_events=True,),
            ],
            [
                sg.Text('Capacidad ENFICC', size=(17, 1), pad=(
                    (10, 0), (10, 5)), background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(size=(15, 1), pad=(
                    (10, 0), (10, 5)), key="-conf&Capacidad_ENFICC", enable_events=True),
                sg.Text('Costo patrimonio', size=(15, 1), pad=((60, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(
                    size=(15, 1), pad=((10, 0), (10, 5)), key="-conf&costo_patrimonio     ", enable_events=True)

            ],
            [
                sg.Text('Días por cobrar', size=(17, 1), pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(
                    size=(15, 1), pad=((10, 0), (10, 5)), key="-conf&Días_por_cobrar       ", enable_events=True),
                sg.Text('Días por pagar', size=(15, 1), pad=((60, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(
                    size=(15, 1), pad=((10, 0), (10, 5)), key="-conf&Días_por_pagar        ", enable_events=True)
            ],
            [
                sg.Text('Año ini. ENFICC', size=(17, 1), pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(
                    size=(15, 1), pad=((10, 0), (10, 5)), key="-conf&Año_disponibilidad_ENFICC", enable_events=True)
                
            ],
            # [
            #     sg.InputText(
            #         size=(15, 1), pad=((20, 0), (0, 5)), key="-conf&Año_disponibilidad_ENFICC", enable_events=True)
            # ],
            [
                sg.Text("Ampliar", pad=((0, 0), (0, 0)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 11)),
            ],
            [sg.HSeparator()],
            [

                sg.Text('Aumento ampliación', size=(17, 1), pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(
                    size=(15, 1), pad=((10, 0), (10, 5)), key="-conf&Aumento_ampliación", enable_events=True),
                sg.Text('Costo ampliación', size=(15, 1), pad=((60, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(
                    size=(15, 1), pad=((10, 0), (10, 5)), key="-conf&Costo_ampliación     ", enable_events=True),
            ],
            [
                sg.Text('Año ampliación', size=(17, 1), pad=((10, 0), (10, 5)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(
                    size=(15, 1), pad=((10, 0), (10, 5)), key="-conf&Año_ampliación        ", enable_events=True),
            ],
            [
                sg.Text("Diferir", pad=((0, 0), (0, 0)),
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR, font=("Nakula", 11)),
            ],
            [sg.HSeparator()],
            [
                sg.Text('Años a diferir', size=(17, 1), pad=(
                        (10, 0), (10, 5)), background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR),
                sg.InputText(size=(15, 1), pad=(
                    (10, 0), (10, 5)), key="-conf&Años_a_diferir           ", enable_events=True)
            ],
            # [sg.Column(summary_viewer,  pad=((0, 0), (10, 0)),
            #            background_color=BACKGROUND_COLOR), ],
            [sg.Button('Calcular',  visible=True, font=(
                'Helvetica', 11), key='-calculate', border_width=0, enable_events=True,
                button_color="#454851", pad=((140, 0), (30, 140))
            ),
                sg.Button('Calcular WACC',  visible=True, font=(
                    'Helvetica', 11), key='-wac-calculate', border_width=0, enable_events=True,
                button_color="#454851", pad=((20, 0), (30, 140))
            ),
                sg.Button('Reiniciar Valores',  visible=True, enable_events=True, font=(
                    'Helvetica', 11), key='-default-values', border_width=0,
                button_color="#454851", pad=((20, 0), (30, 140))
            )],
            [sg.Image(source="imgs/loading.gif", key='-GIF-', pad=((180, 0), (0, 5)), size=(25, 25), background_color=BACKGROUND_COLOR, visible=False,),
                sg.Text('Ejecutando procesos, por favor espera ...', size=(50, 1), pad=((10, 0), (0, 5)), key="-message", visible=False,
                        background_color=BACKGROUND_COLOR, text_color=PRIMARY_TEXT_COLOR)]
        ]

        layout = [
            [
                sg.Column(file_list_column, background_color=BACKGROUND_COLOR),
                sg.VSeperator(),
                sg.Column(second_file_list_column,
                          background_color=BACKGROUND_COLOR, size=(600, 580)),
            ]
        ]

        window = sg.Window("Evaluación económica proyectos hidroeléctricos", layout,
                           background_color=BACKGROUND_COLOR)
        while True:
            event, values = window.read(timeout=15)
            window['-GIF-'].update_animation(
                source="imgs/loading.gif", time_between_frames=15)
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == "-FOLDER-":
                folder = values["-FOLDER-"]
                # window["folder_name"].update(
                #     f"  Directorio seleccionado: {folder}")
                continue
            if "-IPC&" in event or "-IPP&" in event or "-PPI&" in event or "-CPI&" in event:
                value, key = event.split("&")
                selection[key] = value
                summary = ""
                for selected in selection:
                    data = []
                    data.append(sg.Text(""))
                    summary = f"{summary}\n\n  {selected}                {selection[selected][1:]}"
                # window["selected_index"].update(summary)
                continue
            if "-conf&" in event:
                value, key = event.split("&")
                input_value = values[event]
                conf_summary = ""
                if "Despacho_central" not in event and values[event] != "":
                    last_digit = values[event][-1]
                    if not last_digit.isnumeric() and last_digit != ".":
                        window[event].update(values[event][0:-1])
                        continue
                selection_conf[key] = input_value
                for selected in selection_conf:
                    conf_summary = f"{conf_summary}\n\n  {selected.replace('_',' ')}        {selection_conf[selected]}"
                # window["selected_conf"].update(conf_summary)
            if event == "-restore-":
                for i in DEFAULT_INDEX_SELECTION:
                    window[f"-IPC&{i}"].update(True)
                    # window["selected_index"].update(DEFAULT_SELECTED_INDEX)

            if "-calculate" in event:
                window["-calculate"].update(disabled=True)
                window["-default-values"].update(disabled=True)
                window["-wac-calculate"].update(disabled=True)
                window["-GIF-"].update(visible=True)
                window["-message"].update("Ejecutando procesos, por favor espera ...",
                                          visible=True, text_color=PRIMARY_TEXT_COLOR)
                final_values = {}
                final_index = {}
                output_message = ""
                try:
                    if folder == "":
                        raise
                    for form_attributes, attributes in METHOD_VALUES.items():
                        if values[f"-conf&{form_attributes}"] == "":
                            raise
                        final_values[attributes] = float(
                            values[f"-conf&{form_attributes}"])
                    for form_attributes, attributes in INDEX_VALUES.items():
                        final_index[attributes] = selection[form_attributes].split(
                            '-')[1]

                    final_values["index_dictionary"] = final_index
                    final_values["working_directory"] = folder
                    if event == "-calculate":
                        print("executing calculate")
                        # execute calculate
                        try:
                            object = pch_conomic_evaluation(final_values['init_year'],
                                                            final_values['end_year'],
                                                            final_values['central_dispatched'],
                                                            final_values['impo_renta'],
                                                            final_values['dias_cobrar'],
                                                            final_values['dias_pagar'],
                                                            final_values['flow_increase'],
                                                            final_values['increase_cost'],
                                                            final_values['year_increase'],
                                                            final_values['index_dictionary'],
                                                            final_values['working_directory'],
                                                            final_values['costo_patrimonio'],
                                                            final_values['differ_option_period'])
                            object.read_input_files()
                            object.calculate_WACC()
                            object.update_dolar_to_peso()
                            object.update_index_rate()
                            object.apply_index()
                            object.calculate_incomes()
                            object.calculate_outcomes()
                            object.calculate_pay_and_gasto()
                            object.calculate_cash_flow()
                            object.calculate_summary_per_serie()
                            object.export_results()
                            object.show_graphs()
                            status = 200
                            response = 'Análisis exitoso'
                        except:
                            status = 600
                            response = 'Error realizando los calculos revise la consola'
                            traceback.print_exc()

                        if status < 500:
                            output_message = response
                            output_color = "#6aa84f"
                        else:
                            output_message = response
                            output_color = "#A54C4C"

                    if event == "-wac-calculate":
                        print("executing wac")
                        try:
                            object = pch_conomic_evaluation(final_values['init_year'],
                                                            final_values['end_year'],
                                                            final_values['central_dispatched'],
                                                            final_values['impo_renta'],
                                                            final_values['dias_cobrar'],
                                                            final_values['dias_pagar'],
                                                            final_values['flow_increase'],
                                                            final_values['increase_cost'],
                                                            final_values['year_increase'],
                                                            final_values['index_dictionary'],
                                                            final_values['working_directory'],
                                                            final_values['costo_patrimonio'],
                                                            final_values['differ_option_period'])
                            object.read_input_files()
                            object.calculate_WACC()
                            status = 200
                            response = 'Wacc calculada: ' + \
                                str(object.calculated_wacc)
                        except:
                            status = 600
                            response = 'Error calculando wacc revise la consola'
                            traceback.print_exc()

                        if status < 500:
                            output_message = response
                            output_color = "#6aa84f"
                        else:
                            output_message = response
                            output_color = "#A54C4C"

                except:
                    traceback.print_exc()
                    output_message = "Debe diligenciar todos los campos del formulario"
                    output_color = "#A54C4C"
                finally:
                    window["-message"].update(output_message,
                                              text_color=output_color)
                    window["-GIF-"].update(visible=False)
                    window["-calculate"].update(disabled=False)
                    window["-default-values"].update(disabled=False)
                    window["-wac-calculate"].update(disabled=False)

            if event == "-default-values":
                selection = DEFAULT_INDEX_SELECTION.copy()
                selection_conf = DEFAULT_SELECTION_CONF.copy()
                for selected in selection_conf:
                    window[f"-conf&{selected}"].update("")
                # window["selected_index"].update(DEFAULT_SELECTED_INDEX)
                # window["selected_conf"].update(DEFAULT_SELECTED_CONF)
                folder = ""
                # window["folder_name"].update(
                #     f" Directorio seleccionado: {folder}")
                window["-FOLDER-"].update(f"")
                for i in DEFAULT_INDEX_SELECTION:
                    window[f"-IPC&{i}"].update(True)
                window["-message"].update(visible=False)
        try:
            window.close()
        except SystemExit:
            print("Closing Window")


if __name__ == '__main__':
    pronosticos_view = PronosticoView()
