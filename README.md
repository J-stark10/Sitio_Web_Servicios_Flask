# Sitio Web de Tech Solutions

## Descripción

Este es un sitio web desarrollado con Flask para la empresa Tech Solutions, especializada en soluciones tecnológicas. El sitio presenta los servicios ofrecidos, información sobre la empresa, y un formulario de contacto.

## Servicios Ofrecidos

- Desarrollo Web Personalizado
- Acompañamiento a Startups
- Capacitación Especializada
- Talleres Prácticos
- Equipo Profesional
- Servicios de TI Integrales

## Tecnologías Utilizadas

- Flask (Python)
- Bootstrap 4
- FontAwesome
- JavaScript
- HTML + CSS + Jinja2

## Estructura del Proyecto

- app.py: Aplicación principal de Flask
- templates/: Plantillas HTML
  - base.html: Plantilla base
  - index.html: Página principal con servicios
  - nosotros.html: Página "Sobre Nosotros"
  - contacto.html: Página de contacto
- static/: Archivos estáticos (CSS, imágenes)
- requirements.txt: Dependencias de Python

## Cómo Ejecutar

1. Clona o descarga el repositorio.
2. Crea un entorno virtual: python -m venv venv
3. Activa el entorno: venv\Scripts\activate (Windows)
4. Instala las dependencias: pip install -r requirements.txt
5. Ejecuta la aplicación: python app.py
6. Abre http://127.0.0.1:5000 en tu navegador

## Configuración

- El formulario de contacto guarda los mensajes en memoria (lista mensajes_contacto).
- Para envío de emails, configura SMTP en app.py.
