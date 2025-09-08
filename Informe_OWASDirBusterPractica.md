---
title: "Análisis de Escaneo con DirBuster"
author: "Máster de Ciberseguridad"
date: "2025-07-28"
---

# 🛡️ Análisis Técnico: Descubrimiento de Directorios con DirBuster

## 🎯 Objetivo de la práctica

El objetivo es llevar a cabo un escaneo de fuerza bruta sobre un servidor web para identificar directorios y archivos ocultos que puedan representar riesgos de seguridad. La herramienta utilizada es **OWASP DirBuster**, operando en una máquina virtual .

Esta técnica forma parte de la fase de **reconocimiento y enumeración** dentro de una auditoría de seguridad web o pentesting.

---

## 🛠️ Herramienta: OWASP DirBuster

DirBuster es una herramienta desarrollada por OWASP que permite realizar ataques de diccionario sobre rutas web. Busca archivos y directorios ocultos mediante combinaciones sistemáticas de nombres y extensiones conocidas.

### Características clave:

- Diccionarios personalizables.
- Definición de extensiones (.php, .html, .bak, .zip...).
- Detección por códigos de estado HTTP (200, 403, 404...).
- Escaneo multihilo (alta velocidad).

---

## 🖼️ Descripción de la sesión

**IP objetivo:** `http://10.0.2.13:80`

**Extensiones utilizadas:** `.php`, `.html`, `.htm`, `.txt`, `.bak`, `.zip`

**Total de peticiones estimadas:** 22.937.002  
**Progreso al momento de la captura:** ~8%  
**Velocidad de escaneo:** 390 requests/segundo  
**Hilos activos:** 10  
**Tiempo estimado restante:** ~15 horas  

DirBuster estaba escaneando la raíz del servidor `/`, usando un diccionario amplio y aplicando cada palabra a diferentes extensiones comunes en aplicaciones web.

---

## 🔍 ¿Qué busca encontrar DirBuster?

- **Directorios confidenciales**: `/admin`, `/config`, `/uploads`
- **Archivos de configuración**: `config.php`, `database.ini`
- **Backups o ficheros olvidados**: `index.bak`, `backup.zip`
- **Rutas de desarrollo**: `test.html`, `dev/`

Esto puede llevar al descubrimiento de información sensible, rutas de administración sin protección o archivos mal configurados.

---

## 🔎 Interpretación de resultados

Durante el escaneo se detectaron:

- **7 directorios**
- **6 archivos**
- **0 errores de conexión**
- Respuestas variadas: se espera evaluar los códigos HTTP para priorizar qué rutas investigar.

| Código HTTP | Significado | Acción recomendada |
|-------------|-------------|--------------------|
| 200 OK      | Recurso accesible | Visitar o auditar |
| 403 Forbidden | Protegido pero existente | Intentar bypass o anotar |
| 404 Not Found | No existe | Ignorar |

---

## 🧠 Análisis avanzado

### Buenas prácticas en pentesting:

- Usar diccionarios adaptados (según tecnología: WordPress, Apache, etc.).
- No abusar de los hilos para evitar detección o caída del servidor.
- Complementar con otras herramientas: `gobuster`, `ffuf`, `nikto`, `nmap`, `Burp Suite`.

### Desde el punto de vista defensivo (blue team):

- Limitar accesos con autenticación.
- Configurar correctamente permisos de archivos.
- No dejar backups accesibles en producción.
- Implementar WAFs o IDS para detectar escaneos.

---

## 📌 Conclusión

DirBuster permite detectar recursos ocultos que pueden ser críticos para la seguridad de una aplicación web. Esta práctica demuestra cómo un atacante o auditor puede descubrir información sensible con simples peticiones automatizadas.

Es una herramienta esencial en auditorías web y parte de la caja de herramientas estándar de cualquier profesional de ciberseguridad ofensiva o defensiva.

---

## 📂 Recursos adicionales

- [OWASP DirBuster - Proyecto oficial](https://owasp.org/www-project-dirbuster/)
- [Diccionarios comunes para pentesting](https://github.com/danielmiessler/SecLists)
- [FFUF - Herramienta moderna alternativa](https://github.com/ffuf/ffuf)
- Curso de Ciberseguridad Web - Pentesting y Enumeración

---

> _Práctica realizada en entorno controlado con fines educativos ._  

***
© 2025 [sualba.dev] Todos los derechos reservados</p>
Este material forma parte de mi portfolio profesional y ha sido desarrollado como parte de mi formación en ciberseguridad.