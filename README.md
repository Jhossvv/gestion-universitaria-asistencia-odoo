# Sistema de Gestión Universitaria y Control de Asistencia en Odoo

Este repositorio contiene un ecosistema de dos módulos personalizados desarrollados para el framework **Odoo**, orientados a automatizar el control académico y la asistencia de estudiantes en un entorno de educación superior.

## Módulos Incluidos

1. **Gestión Universidad (`gestion_universidad`)**: 
   * Administra la estructura base: Carreras, Secciones y Semestres.
   * Registro integral de Estudiantes (asociando Cédula de Identidad única).
   * Implementa validaciones personalizadas en Python para prevenir la duplicación de registros de estudiantes.
   
2. **Gestión de Asistencia (`gestion_asistencia`)**:
   * Módulo dependiente que se acopla dinámicamente a la estructura de `gestion_universidad`.
   * Permite el registro y control de asistencias diarias utilizando campos relacionales (`Many2one`) vinculados directamente a las secciones académicas reales.

## Tecnologías Utilizadas

* **Backend:** Python
* **Frontend de Odoo:** XML (Vistas Tree, Form y Search optimizadas con filtros y agrupaciones)
* **Base de Datos:** PostgreSQL
* **Framework:** Odoo ERP

## Instalación y Despliegue

1. Clona este repositorio dentro de tu directorio de addons personalizados:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
