
# Sistema de Gestión - Software FJ

Sistema integral desarrollado en Python para la gestión de clientes, servicios y reservas.

## Objetivo del proyecto

Desarrollar un sistema en Python que permita gestionar clientes, administrar diferentes tipos de servicios y controlar las reservas, aplicando conceptos de programación orientada a objetos, validaciones y manejo de excepciones.

## Funcionalidades principales

- Registro y validación de clientes.
- Gestión de servicios de reserva de salas.
- Alquiler de equipos tecnológicos.
- Administración de asesorías especializadas.
- Creación, confirmación, cancelación y procesamiento de reservas.
- Validación de tarifas, duración, impuestos y descuentos.
- Manejo de excepciones personalizadas.
- Registro de eventos mediante archivos de log.
- Ejecución de 20 simulaciones de prueba.

## Estructura del proyecto

```text
Sistema-Gestion-SoftwareFJ/
├── main.py
├── README.md
├── models/
│   ├── entidades.py
│   ├── cliente.py
│   ├── servicios.py
│   └── reserva.py
├── utils/
│   ├── excepciones.py
│   └── logger.py
└── tests/
    └── simulaciones.py
```

## Tecnologías utilizadas

- Python 3.
- Programación orientada a objetos (POO).
- Git y GitHub.
- GitHub Codespaces.
- Módulo logging.

## Instrucciones de ejecución

1. Abrir el proyecto en GitHub Codespaces.
2. Abrir la terminal.
3. Ejecutar:

```bash
python main.py
```

4. Revisar los resultados en la terminal.

## Pruebas del sistema

El proyecto incluye 20 simulaciones para comprobar la creación y validación de clientes, los diferentes tipos de servicios, la gestión de reservas, el control de disponibilidad, los cálculos y el manejo de excepciones.

Los resultados se registran mediante el módulo logging.
