# Proyecto MyChar - Puesta en Producción Segura

## Información General
* **Descripción:** Script en Python que analiza una lista de palabras para determinar cuál es la más larga, aplicando un criterio alfabético en caso de empate.
* **Tecnologías:** Python 3.10+, Git para control de versiones y GitHub como repositorio remoto.

## Guía de Despliegue
Para instalar y ejecutar este programa de forma segura:
1. **Clonar el repositorio:** `git clone https://github.com/garohezcorporativo/mi-proyecto-seguro.git`
2. **Entrar en la carpeta:** `cd mi-proyecto-seguro`
3. **Ejecutar el script:** `python mychar.py`

## Tabla de Trazabilidad (Historial de Versiones)
| Fecha | Versión | Descripción de los cambios |
| :--- | :--- | :--- |
| 15/11/2025 | v1.0 | Creación del código original (Unidad 1). |
| 10/05/2026 | v1.1 | Inicialización de Git, gestión de ramas y documentación. |

## Checklist de Seguridad (Higiene del Repositorio)
Se han aplicado filtros para ignorar los siguientes archivos y proteger la integridad del sistema:
* **`__pycache__/`**: Archivos compilados que no deben ser públicos.
* **`.venv/`**: Entornos virtuales locales que contienen binarios pesados.
* **`*.log`**: Registros de errores que podrían exponer rutas o datos del sistema.