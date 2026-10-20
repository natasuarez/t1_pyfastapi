import requests

# URL base de tu API en Render
BASE_URL = "https://t1-pyfastapi-8rp8.onrender.com"


def mostrar_menu():
  """Muestra el menú principal en la consola."""
  print("\n--- GESTIÓN DE APRENDICES (CONSOLA) ---")
  print("1. Registrar nuevo aprendiz")
  print("2. Listar todos los aprendices")
  print("3. Buscar aprendiz por ID")
  print("4. Actualizar aprendiz")
  print("5. Eliminar aprendiz")
  print("6. Salir")


def registrar_aprendiz():
  """Solicita los datos del aprendiz y los envía a la API mediante POST."""
  print("\n--- Registrar Nuevo Aprendiz ---")
  document = input("Ingrese el Documento/ID: ")
  firstname = input("Ingrese el Nombre: ")
  lastname = input("Ingrese el Apellido: ")

  try:
    age = int(input("Ingrese la Edad: "))
  except ValueError:
    age = 0

  email = input("Ingrese el Correo electrónico: ")
  program = input("Ingrese el Programa: ")

  try:
    record_number = int(input("Ingrese el Número de registro: "))
  except ValueError:
    record_number = 0

  # Nombres de campos ajustados al modelo 'traineeModel' de tu FastAPI
  data = {
      "document": document,
      "firstname": firstname,
      "lastname": lastname,
      "age": age,
      "email": email,
      "program": program,
      "record_number": record_number,
  }

  try:
    response = requests.post(f"{BASE_URL}/trainees/", json=data)
    if response.status_code in [200, 201]:
      print(" Aprendiz registrado exitosamente.")
    else:
      print(f" Error del servidor: {response.json()}")
  except requests.exceptions.ConnectionError:
    print(" No se pudo conectar con el servidor/API.")


def listar_aprendices():
  """Consulta y muestra todos los aprendices registrados mediante GET."""
  print("\n--- Lista de Aprendices ---")
  try:
    response = requests.get(f"{BASE_URL}/trainees/")
    if response.status_code == 200:
      aprendices = response.json()
      if not aprendices:
        print("No hay aprendices registrados.")
        return
      for a in aprendices:
        doc = a.get("document", a.get("id", "Sin ID"))
        nombre = a.get("firstname", a.get("nombre", ""))
        apellido = a.get("lastname", a.get("apellido", ""))
        print(f"ID/Documento: {doc} | Nombre: {nombre} {apellido}")
    else:
      print(" Error al obtener los datos.")
  except requests.exceptions.ConnectionError:
    print(" No se pudo conectar con el servidor/API.")


def buscar_aprendiz():
  """Busca un aprendiz específico por su ID mediante GET."""
  print("\n--- Buscar Aprendiz por ID ---")
  aprendiz_id = input("Ingrese el ID/Documento del aprendiz: ")
  try:
    response = requests.get(f"{BASE_URL}/trainees/{aprendiz_id}")
    if response.status_code == 200:
      a = response.json()
      print(f"\nID/Documento: {a.get('document', a.get('id'))}")
      print(f"Nombre: {a.get('firstname', a.get('nombre'))}")
      print(f"Apellido: {a.get('lastname', a.get('apellido'))}")
      print(f"Correo: {a.get('email', a.get('gmail'))}")
      print(f"Programa: {a.get('program')}")
    else:
      print(" Aprendiz no encontrado.")
  except requests.exceptions.ConnectionError:
    print(" No se pudo conectar con el servidor/API.")


def actualizar_aprendiz():
  """Actualiza los datos de un aprendiz por su ID mediante PUT."""
  print("\n--- Actualizar Aprendiz ---")
  aprendiz_id = input("Ingrese el ID/Documento del aprendiz a actualizar: ")

  print("Deje el campo vacío si no desea actualizarlo.")
  nuevo_nombre = input("Nuevo nombre: ")

  data = {}
  if nuevo_nombre.strip():
    data["firstname"] = nuevo_nombre

  if not data:
    print("No se realizaron cambios.")
    return

  try:
    response = requests.put(f"{BASE_URL}/trainees/{aprendiz_id}", json=data)
    if response.status_code == 200:
      print(" Aprendiz actualizado correctamente.")
    else:
      print(f" Error al actualizar: {response.json()}")
  except requests.exceptions.ConnectionError:
    print(" No se pudo conectar con el servidor/API.")


def eliminar_aprendiz():
  """Elimina un aprendiz por su ID mediante DELETE."""
  print("\n--- Eliminar Aprendiz ---")
  aprendiz_id = input("Ingrese el ID/Documento del aprendiz a eliminar: ")
  confirmacion = input(
      f"¿Está seguro de eliminar al aprendiz {aprendiz_id}? (s/n): "
  )

  if confirmacion.lower() == "s":
    try:
      response = requests.delete(f"{BASE_URL}/trainees/{aprendiz_id}")
      if response.status_code == 200:
        print(" Aprendiz eliminado correctamente.")
      else:
        print(" Aprendiz no encontrado o error al eliminar.")
    except requests.exceptions.ConnectionError:
      print(" No se pudo conectar con el servidor/API.")
  else:
    print("Operación cancelada.")


def main():
  """Función principal que controla el flujo del menú."""
  while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción (1-6): ")

    if opcion == "1":
      registrar_aprendiz()
    elif opcion == "2":
      listar_aprendices()
    elif opcion == "3":
      buscar_aprendiz()
    elif opcion == "4":
      actualizar_aprendiz()
    elif opcion == "5":
      eliminar_aprendiz()
    elif opcion == "6":
      print("\nSaliendo del sistema. ¡Hasta luego!")
      break
    else:
      print("\n Opción inválida. Por favor, seleccione un número del 1 al 6.")

    input("\nPresione Enter para continuar...")


if __name__ == "__main__":
  main()