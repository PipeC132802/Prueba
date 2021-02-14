import pandas as pd

class ResultElections:

    def __init__(self):
        self.file, self.data_frame, self.data_grouped = None, None, None

    def read_file(self):
        self.file = pd.ExcelFile('resultados_elecciones.xlsx')

    def set_data_frame(self):
        self.data_frame = self.file.parse('data')

    def group_by_fields(self):
        self.data_grouped = self.data_frame.groupby(
            ['candidato', 'partido', 'nombre_puesto', 'municipio', 'departamento']
        ).votos.sum()

    def write_file(self):
        self.data_grouped.to_csv('data_grouped.csv')


results_elections = ResultElections()
results_elections.read_file()
results_elections.set_data_frame()
results_elections.group_by_fields()
results_elections.write_file()
