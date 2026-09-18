"""Modelo de dominio para las citas médicas de la IPS MediSENA."""


class CitaMedica:
    """Representa una solicitud de atención médica."""

    PORCENTAJE_DESCUENTO = 0.15

    def __init__(
        self,
        id_cita: str,
        paciente: str,
        especialidad: str,
        medico_asignado: str,
        costo_consulta: float,
        es_urgencia: bool,
    ) -> None:
        self.id_cita = id_cita
        self.paciente = paciente
        self.especialidad = especialidad
        self.medico_asignado = medico_asignado
        self.costo_consulta = float(costo_consulta)
        self.es_urgencia = bool(es_urgencia)

    def calcular_costo_final(self) -> float:
        """Aplica 15% de descuento cuando la cita NO es de urgencia."""
        if not self.es_urgencia:
            return round(self.costo_consulta * (1 - self.PORCENTAJE_DESCUENTO), 2)
        return round(self.costo_consulta, 2)

    def a_diccionario(self) -> dict:
        """Serializa la instancia con llaves en snake_case."""
        return {
            "id_cita": self.id_cita,
            "paciente": self.paciente,
            "especialidad": self.especialidad,
            "medico_asignado": self.medico_asignado,
            "costo_consulta": self.costo_consulta,
            "es_urgencia": self.es_urgencia,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "CitaMedica":
        """Reconstruye un objeto a partir de un diccionario del JSON."""
        return cls(**datos)

    def __str__(self) -> str:
        tipo = "URGENCIA" if self.es_urgencia else "PROGRAMADA"
        return (
            f"[{self.id_cita}] {self.paciente} | {self.especialidad} | "
            f"Dr(a). {self.medico_asignado} | {tipo} | "
            f"Base: ${self.costo_consulta:,.2f} | Final: ${self.calcular_costo_final():,.2f}"
        )