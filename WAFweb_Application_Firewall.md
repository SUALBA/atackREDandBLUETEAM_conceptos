# 📘 Web Application Firewall (WAF)

## 🔐 ¿Qué es un WAF?

Un **Web Application Firewall (WAF)** es un tipo de firewall diseñado específicamente para proteger aplicaciones web supervisando, filtrando o bloqueando el tráfico HTTP/S hacia y desde dichas aplicaciones. Su propósito principal es proteger frente a ataques dirigidos al nivel de aplicación, como inyecciones de código malicioso.

---

## 🎯 Diferencias entre WAF y Network Firewall

| Característica         | WAF                                          | Network Firewall                       |
|------------------------|----------------------------------------------|----------------------------------------|
| Nivel de protección    | Capa de aplicación (HTTP/HTTPS)              | Capa de red (IP, TCP, UDP, etc.)       |
| Tipo de amenazas       | Inyección SQL, XSS, CSRF, etc.               | Escaneos de puertos, DDoS, malware     |
| Tráfico que inspecciona| HTTP/HTTPS                                   | Todo tipo de tráfico de red            |
| Ubicación              | Delante de las aplicaciones web              | Entre redes o hacia Internet           |
| Enfoque                | Analiza el contenido de las peticiones web   | Controla el acceso entre redes         |

---

## 🧪 Ejemplos de uso

1. **E-commerce**: Filtrado de inyecciones SQL que buscan extraer información de tarjetas de crédito.
2. **Portales bancarios**: Prevención de ataques XSS que podrían robar credenciales de usuario.
3. **APIs REST**: Limitación de métodos HTTP y validación de entradas.
4. **Sistemas de login**: Protección contra ataques de fuerza bruta y CSRF.
5. **Plataformas SaaS**: Monitorización continua para detectar y mitigar comportamientos anómalos.

---

## 🧷 Tipos de ataques que previene un WAF

- **Inyección SQL**: Manipulación de consultas a bases de datos.
- **Cross-Site Scripting (XSS)**: Inyección de scripts maliciosos en páginas web.
- **Cross-Site Request Forgery (CSRF)**: Falsificación de solicitudes desde usuarios autenticados.
- **File Inclusion**: Inclusión de archivos maliciosos mediante rutas manipuladas.
- **Remote Code Execution (RCE)**: Ejecución remota de código en el servidor.
- **Directory Traversal**: Acceso no autorizado a archivos y directorios del sistema.

---

## 🛠️ Usos prácticos y beneficios

- **Filtrado y validación de entradas**: Bloquea inputs sospechosos antes de llegar al backend.
- **Protección frente a 0-days**: Muchos WAFs utilizan inteligencia artificial y actualizaciones automáticas.
- **Cumplimiento normativo**: Ayuda a cumplir con normativas como **PCI-DSS**, **GDPR**, **HIPAA**.
- **Auditoría y logging**: Registro de intentos de ataque para análisis forense.
- **Mitigación de bots y scraping**: Algunos WAFs modernos detectan y bloquean bots automatizados.

---

## 🧱 Tipos de WAF

1. **Basados en red (hardware)**: Dispositivos físicos que protegen en el perímetro.
2. **Basados en host (software)**: Instalados en el servidor de la aplicación.
3. **Basados en la nube**: Servicios ofrecidos por terceros (ej: Cloudflare, AWS WAF).

---

## ⚙️ Ejemplo práctico (Regla simple)

```regex
# Bloquea peticiones que intentan hacer una inyección SQL
GET .*?(\%27)|(\')|(\-\-)|(\%23)|(#)
