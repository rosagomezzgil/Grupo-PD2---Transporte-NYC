from __future__ import annotations

from pathlib import Path

from src.pipeline_runner import ejecutar_modulo, print_done, print_stage


def main() -> None:
    # Estamos en: src/procesamiento/main.py
    # Subimos 2 niveles para llegar a la raiz del proyecto
    project_root = Path(__file__).resolve().parents[2]
    print_stage("PREPROCESAMIENTO", "Capas 1 -> 2 -> 3")

    modulos = [
        "src.procesamiento.capa1.main",
        "src.procesamiento.capa2.main",
        "src.procesamiento.capa3.main",
    ]

    for m in modulos:
        ejecutar_modulo(m, project_root)

    print_done("PREPROCESAMIENTO COMPLETADO CORRECTAMENTE")


if __name__ == "__main__":
    main()
