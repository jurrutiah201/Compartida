def interes_compuesto(principal, tasa, tiempo):
    """
    Calcula el interés compuesto.
    principal: monto inicial
    tasa: tasa anual en decimal (por ejemplo, 0.05 = 5%)
    tiempo: número de años
    """
    if principal <= 0 or tasa < 0 or tiempo < 0:
        raise ValueError("Los parámetros deben ser positivos.")
    monto_final = principal * (1 + tasa) ** tiempo
    return round(monto_final - principal, 2)


def cuota_prestamo(principal, tasa_anual, meses):
    """
    Calcula la cuota fija mensual de un préstamo (sistema francés).
    """
    if principal <= 0 or tasa_anual < 0 or meses <= 0:
        raise ValueError("Los parámetros deben ser positivos.")
    tasa_mensual = tasa_anual / 12
    if tasa_mensual == 0:
        return round(principal / meses, 2)
    cuota = principal * (tasa_mensual * (1 + tasa_mensual) ** meses) / ((1 + tasa_mensual) ** meses - 1)
    return round(cuota, 2)
