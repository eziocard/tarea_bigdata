import pandas as pd

#from IPython.display import display

class Bdd():
    def __init__(self,nombre):
        self.nombre = nombre
        self.df = pd.read_csv(self.nombre)

    def get_Df(self):
        return pd.read_csv(self.nombre)

    def get_tabla(self):
        print(self.df.tail())

    def get_name_columnas(self):       
        return self.df.columns.values

    def set_table(self,agregar):
        ultimo_valor = (self.df[self.get_name_columnas()[0]].iloc[-1]) + 1
        agregar[self.get_name_columnas()[0]] = ultimo_valor
        #agregar.update({self.get_name_columnas()[0] : ultimo_valor})
        agregar = pd.DataFrame([agregar])
        print(agregar)
        self.df = pd.concat([self.df, agregar], ignore_index=True)
        self.df.to_csv(self.nombre, index=False)
            

