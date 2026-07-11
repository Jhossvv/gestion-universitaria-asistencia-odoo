# Sistema de Gestión Universitaria (Actualizado) y Control de Asistencia en Odoo

Este repositorio contiene un ecosistema de dos módulos personalizados para el framework **Odoo**. Nota importante: **Aquí se encuentra la versión actualizada y reestructurada del módulo `gestion_universidad`**, la cual fue modificada profundamente en su arquitectura de datos (pasando de campos de texto plano a modelos relacionales `Many2one`) para garantizar una integración nativa y sin conflictos con el sistema de asistencia.

## Sobre esta Actualización

Anteriormente, el módulo de gestión universitaria manejaba estructuras aisladas. En esta actualización presente en el repositorio:
* Se migraron las secciones y carreras a modelos independientes (`estudiante.seccion` y `estudiante.carrera`).
* Se implementaron restricciones avanzadas en Python (`@api.constrains`) para blindar el registro de estudiantes por número de cédula.
* Se adaptó el backend para que el módulo dependiente **`gestion_asistencia`** consuma estos datos relacionales en tiempo real, eliminando errores de validación de datos antiguos.

## Módulos Incluidos

1. **Gestión Universidad (`gestion_universidad` - Versión Actualizada)**: 
   * Administra la estructura base: Carreras, Secciones y Semestres.
   * Registro integral de Estudiantes con validación de Cédula de Identidad única.
   
2. **Gestión de Asistencia (`gestion_asistencia`)**:
   * Módulo dependiente acoplado dinámicamente a la nueva estructura relacional de la universidad para el control de asistencias diarias.
