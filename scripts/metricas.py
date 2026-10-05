#!/usr/bin/env python3
"""Métricas de Ágora a partir de sesiones.csv.

Uso:
    python3 metricas.py                      # últimos 7 días, sesiones.csv en la carpeta actual
    python3 metricas.py ruta/sesiones.csv    # otra ruta
    python3 metricas.py --dias 28            # ventana mensual

Solo usa la biblioteca estándar de Python 3.
"""
import argparse
import csv
import datetime as dt
import statistics as st


def num(fila, clave):
    valor = (fila.get(clave) or "").strip()
    try:
        return float(valor.replace(",", ".")) if valor else None
    except ValueError:
        return None


def media(filas, clave):
    valores = [v for v in (num(f, clave) for f in filas) if v is not None]
    return f"{st.mean(valores):.1f}" if valores else "—"


def main():
    p = argparse.ArgumentParser(description="Resumen de métricas de Ágora")
    p.add_argument("csv", nargs="?", default="sesiones.csv")
    p.add_argument("--dias", type=int, default=7)
    a = p.parse_args()

    with open(a.csv, encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    desde = dt.date.today() - dt.timedelta(days=a.dias)
    S = [f for f in filas if f.get("fecha") and dt.date.fromisoformat(f["fecha"]) > desde]
    if not S:
        print(f"No hay sesiones en los últimos {a.dias} días.")
        return

    ok = sum(num(f, "recup_ok") or 0 for f in S)
    tot = sum(num(f, "recup_total") or 0 for f in S)
    brechas = []
    for f in S:
        pred, rok, rtot = num(f, "prediccion_pct"), num(f, "recup_ok"), num(f, "recup_total")
        if pred is not None and rok is not None and rtot:
            brechas.append(pred - 100 * rok / rtot)
    validas = [int(sum(num(f, f"n{i}") or 0 for f in S)) for i in range(1, 6)]
    puntos = sum(n * nivel for nivel, n in enumerate(validas, start=1))
    minutos = sum(num(f, "min_real") or 0 for f in S)

    print(f"Ágora · últimos {a.dias} días · {len(S)} sesiones · {minutos:.0f} min")
    print(f"Recuperación sin apuntes: {ok / tot:.0%}" if tot else "Recuperación sin apuntes: —")
    if brechas:
        sesgo = st.mean(brechas)
        tipo = "sobreconfianza" if sesgo > 0 else "subconfianza" if sesgo < 0 else "calibrada"
        print(f"Calibración: {st.mean(abs(b) for b in brechas):.1f} pts de brecha media ({tipo})")
    print(f"Soluciones válidas N1–N5: {'/'.join(map(str, validas))} · puntos: {puntos}")
    print(f"Explicación {media(S, 'explicacion')}/4 · Transferencia {media(S, 'transferencia')}/4 · "
          f"Preguntas {media(S, 'preguntas')}/4")
    print(f"Sueño medio {media(S, 'sueno_h')} h · Energía media {media(S, 'energia')}/5")

    if tot:
        r = ok / tot
        if r < 0.60:
            regla = "Recuperación <60 %: sin contenido nuevo; solo recuperación, ejemplos resueltos y prerrequisitos."
        elif r < 0.80:
            regla = "Recuperación 60–79 %: contenido nuevo a la mitad; recuperación al doble."
        elif r <= 0.90:
            regla = "Recuperación 80–90 %: mantener dificultad y espaciar repasos."
        else:
            regla = "Recuperación >90 %: subir complejidad solo si hay transferencia ≥3 en un problema N4."
        print(f"Regla sugerida (§12.1): {regla}")


if __name__ == "__main__":
    main()
