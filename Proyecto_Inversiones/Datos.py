import pandas as pd
from Sistema_Inversiones import Sistema_Inversiones
from Cliente import Cliente

class Datos:

    @staticmethod
    def guardar(sistema):

        datos = []

        for cliente in sistema.obtener_clientes():

            datos.append({
                "id": cliente.obtener_id(),
                "nombre": cliente.obtener_nombre(),
                "direccion": cliente.obtener_direccion(),
                "fecha_nac": cliente.obtener_fecha_nac()
            })

        df = pd.DataFrame(datos)

        df.to_csv(
            "clientes.csv",
            index=False
        )

    @staticmethod
    def cargar():

        sistema = Sistema_Inversiones()

        try:

            df = pd.read_csv("clientes.csv")

            for _, fila in df.iterrows():

                cliente = Cliente(
                    fila["id"],
                    fila["nombre"],
                    fila["direccion"],
                    fila["fecha_nac"]
                )

                sistema.agregar_cliente(cliente)

        except:
            pass

        return sistema

     
