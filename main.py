"""Menu interactivo del modulo de gestion de citas medicas de MediSENA."""

from src.cita import CitaMedica
from src.gestion_datos import cargar_citas, guardar_citas


def listar_citas(citas: list) -> None:
    if not citas:
        print("\nNo hay citas registradas.")
        return
    print(f"\n--- CITAS REGISTRADAS ({len(citas)}) ---")
    for datos in citas:
        print(CitaMedica.desde_diccionario(datos))


def pedir_costo() -> float:
    while True:
        try:
            valor = float(input("Costo de la consulta: "))
            if valor <= 0:
                print("El costo debe ser mayor que cero.")
                continue
            return valor
        except ValueError:
            print("Valor invalido. Digite un numero (ej: 45000.50).")


def registrar_cita(citas: list) -> None:
    id_cita = input("\nID de la cita (ej: CIT-2026-01): ").strip().upper()
    if any(c["id_cita"] == id_cita for c in citas):
        print(f"Error: ya existe una cita con el ID {id_cita}.")
        return

    paciente = input("Nombre del paciente: ").strip()
    especialidad = input("Especialidad: ").strip()
    medico = input("Medico asignado: ").strip()
    costo = pedir_costo()
    es_urgencia = input("Es urgencia? (s/n): ").strip().lower() == "s"

    cita = CitaMedica(id_cita, paciente, especialidad, medico, costo, es_urgencia)
    citas.append(cita.a_diccionario())
    guardar_citas(citas)
    print(f"Cita registrada. Costo final: ${cita.calcular_costo_final():,.2f}")


def consultar_ingresos(citas: list) -> None:
    total = sum(
        CitaMedica.desde_diccionario(datos).calcular_costo_final() for datos in citas
    )
    print(f"\nIngresos proyectados: ${total:,.2f}")


def main() -> None:
    citas = cargar_citas()
    opciones = {
        "1": "Listar citas",
        "2": "Registrar nueva cita",
        "3": "Consultar total de ingresos proyectados",
        "4": "Salir",
    }

    while True:
        print("\n===== MEDISENA - GESTION DE CITAS =====")
        for clave, texto in opciones.items():
            print(f"{clave}. {texto}")

        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            listar_citas(citas)
        elif opcion == "2":
            registrar_cita(citas)
        elif opcion == "3":
            consultar_ingresos(citas)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
