import json

def lambda_handler(event, context):
    try:
        # Extraemos los parámetros del evento
        numero1 = int(event["numero1"])  # Convertir numero1 a entero
        numero2 = int(event["numero2"])  # Convertir numero2 a entero
        funciones = event["funciones"]  # Array de operaciones

        resultados = {}

        # Iterar sobre las funciones
        for funcion in funciones:
            funcion = funcion.lower()
            if funcion == "suma":
                resultados[funcion] = numero1 + numero2
            elif funcion == "resta":
                resultados[funcion] = numero1 - numero2
            elif funcion == "multiplicacion":
                resultados[funcion] = numero1 * numero2
            elif funcion == "division":
                if numero2 == 0:
                    resultados[funcion] = "Error: No se puede dividir por cero"
                else:
                    resultados[funcion] = numero1 / numero2
            else:
                resultados[funcion] = "Funcion no soportada"

        # Respuesta con todos los resultados
        return {
            "statusCode": 200,
            "body": json.dumps({"resultados": resultados})
        }

    except (ValueError, KeyError):
        # En caso de error en la conversión de los números o de parámetros faltantes
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Entrada inválida"})
        }

    except Exception as e:
        # Capturamos cualquier otro error
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
