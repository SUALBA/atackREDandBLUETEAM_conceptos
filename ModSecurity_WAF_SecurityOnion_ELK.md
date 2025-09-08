# 🛡️ ModSecurity: El WAF Open Source para Defensa Profesional

## 📌 Introducción
**ModSecurity** es un **Web Application Firewall (WAF)** de código abierto que protege aplicaciones web frente a ataques comunes como **SQL Injection, Cross-Site Scripting (XSS)**, **CSRF**, **Path Traversal** o **Inyección de comandos**.  

Se integra con servidores **Apache, Nginx e IIS**, y se puede usar tanto en **modo detección (IDS)** como en **modo prevención (IPS)**.  
Es ampliamente utilizado junto con el **OWASP Core Rule Set (CRS)**, un conjunto de reglas preconfiguradas contra amenazas conocidas.

---

## 📌 ¿Por qué usar ModSecurity?
- ✅ Open Source y con soporte comunitario (OWASP).  
- ✅ Compatible con entornos de producción y laboratorio.  
- ✅ Flexible: se pueden crear **reglas personalizadas** para escenarios específicos.  
- ✅ Integración con **Security Onion + ELK** para análisis avanzado y correlación de alertas.  
- ✅ Ayuda a cumplir normativas como **PCI DSS** e **ISO 27001**.  

---

## ⚙️ Funcionamiento de ModSecurity
ModSecurity analiza el tráfico HTTP/HTTPS interceptando solicitudes antes de que lleguen a la aplicación.

### Sintaxis básica de una regla
```apache
SecRule VARIABLES OPERATOR ACTIONS

VARIABLES → parte del tráfico a inspeccionar (ARGS, HEADERS, BODY).

OPERATORS → qué patrón buscar (@rx, @contains, @beginsWith).

ACTIONS → qué hacer (deny, log, status:403, redirect).

📌 Ejemplos de Reglas
🚫 SQL Injection

SecRule ARGS "@rx select.+from" \
"id:1002,phase:2,deny,status:403,msg:'SQL Injection detectada'"

🚫 Cross-Site Scripting (XSS)

SecRule ARGS "@rx <script>" \
"id:1003,phase:2,deny,status:403,msg:'Intento de XSS detectado'"

🚫 Path Traversal

SecRule REQUEST_URI "@rx \.\./" \
"id:930110,phase:2,block,severity:CRITICAL,msg:'Path Traversal Detectado'"

📌 Integración con OWASP Core Rule Set (CRS)
El OWASP CRS es un conjunto de reglas listas para usar que cubre los principales ataques web.

Instalación:
git clone https://github.com/coreruleset/coreruleset /etc/modsecurity-crs
cd /etc/modsecurity-crs
cp crs-setup.conf.example crs-setup.conf

Habilitación en Apache/Nginx:
Include /etc/modsecurity-crs/crs-setup.conf
Include /etc/modsecurity-crs/rules/*.conf


📊 ModSecurity + Security Onion + ELK
Para un nivel profesional, los logs de ModSecurity pueden integrarse con Security Onion usando Filebeat y visualizarse en Kibana.

Configuración Filebeat
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/modsec_audit.log

output.logstash:
  hosts: ["<IP_SECURITY_ONION>:5044"]

  Esto permite:

📌 Correlación de alertas ModSecurity con Suricata y Zeek.

📌 Dashboards en Kibana con ataques detectados.

📌 Alertas automáticas según severidad (CRITICAL, HIGH, etc.).

📌 Buenas Prácticas
1.Activar CRS y luego añadir reglas personalizadas según tu aplicación.

2.Empezar en modo DetectionOnly para evitar falsos positivos.

3.Usar acciones de transformación (t:lowercase, t:urlDecodeUni) para normalizar entradas.

4.Revisar logs en tiempo real:
 tail -f /var/log/modsec_audit.log

5.Actualizar reglas periódicamente (OWASP CRS).

6.Integrar con un SIEM para correlación (ej. Security Onion + ELK).

📌 Recursos Útiles
    OWASP CRS

    ModSecurity GitHub

    Security Onion Docs

    MITRE ATT&CK (para mapear técnicas de ataque)

✅ Conclusión
ModSecurity es una herramienta esencial para proteger aplicaciones web contra ataques avanzados.
Combinado con OWASP CRS y la integración con Security Onion + ELK, se convierte en un pilar fundamental de un SOC moderno para la detección y prevención de amenazas.

💡 Consejo: Aprende a escribir y ajustar tus propias reglas. Esa es la diferencia entre un administrador básico y un profesional WAF.



# 🛡️ ModSecurity y WAF: Guía Completa para Profesionales de Ciberseguridad

## 📌 Introducción

Las **aplicaciones web** son uno de los principales objetivos de los atacantes.  
Según OWASP, más del 70% de los ataques en internet explotan vulnerabilidades en aplicaciones web.  
Aquí entra en juego el **Web Application Firewall (WAF)** y, entre ellos, el más popular **ModSecurity**.  

Un WAF protege aplicaciones filtrando tráfico HTTP/HTTPS y bloqueando intentos de explotación como:

- SQL Injection  
- Cross-Site Scripting (XSS)  
- Path Traversal / LFI / RFI  
- Inyección de comandos  
- Fuerza bruta y escaneo de vulnerabilidades  

---

## 📊 ¿Qué es ModSecurity?

**ModSecurity** es un **WAF de código abierto** creado por SpiderLabs y mantenido por OWASP.  
Permite inspeccionar el tráfico web en tiempo real y aplicar **reglas personalizadas** para detectar y bloquear ataques.  

✅ Compatible con:  
- Apache  
- Nginx  
- IIS  

✅ Modos de operación:
- **DetectionOnly (IDS)** → solo registra intentos.  
- **Blocking (IPS)** → bloquea el tráfico malicioso.  

✅ Integración con:
- **OWASP Core Rule Set (CRS)**  
- **Security Onion + ELK** para correlación y monitoreo.  

---

## 🏗️ Arquitectura de un WAF con ModSecurity

```ascii
       ┌────────────┐
       │   Cliente  │
       └─────┬──────┘
             │  Petición HTTP
             ▼
      ┌──────────────┐
      │    WAF       │
      │ ModSecurity  │
      └─────┬────────┘
            │ Análisis con Reglas
            │ (CRS + personalizadas)
            ▼
       ┌──────────────┐
       │ Aplicación   │
       │   Web        │
       └──────────────┘


⚙️ Sintaxis de Reglas ModSecurity

SecRule VARIABLES OPERATOR ACTIONS

Componentes
VARIABLES → parte del tráfico a inspeccionar

OPERATORS → qué patrón buscar

ACTIONS → qué hacer cuando coincide

Ejemplo simple:
    SecRule ARGS "@rx select.+from" \
    "id:1002,phase:2,deny,status:403,msg:'SQL Injection detectada'"

📌 VARIABLES Comunes
    ARGS → todos los parámetros de la petición.

    ARGS_GET → parámetros GET.

    ARGS_POST → parámetros POST.

    REQUEST_URI → URL solicitada.

    REQUEST_HEADERS → cabeceras de la petición.

    REQUEST_BODY → cuerpo de la petición (POST/PUT).

    REQUEST_COOKIES → cookies enviadas.

    REMOTE_ADDR → IP del cliente.

📌 OPERATORS Comunes
    @rx → expresión regular.

    @contains → contiene una cadena.

    @beginsWith → comienza con.

    @endsWith → termina con.

    @ipMatch → coincide con IP o rango.

    @pm → lista de palabras clave.

Ejemplo:

    SecRule REQUEST_LINE "@contains .php" \
    "id:150,phase:1,deny,status:403,msg:'Intento de acceso a PHP detectado'"

📌 ACTIONS Comunes
    deny → bloquear la petición.

    log → registrar en el log.

    status:403 → devolver código 403.

    t:lowercase → convertir entrada a minúsculas antes de evaluar.

    severity:CRITICAL → nivel de criticidad.

Ejemplo con múltiples transformaciones:

    SecRule ARGS "(asfunction|javascript|vbscript)" \
    "id:146,phase:2,deny,t:lowercase,t:removeNulls,t:removeWhitespace,msg:'Detección de script malicioso'"

📌 Ejemplos de Reglas Avanzadas
🚫 Path Traversal

SecRule REQUEST_URI|ARGS "@rx \.\./" \
"id:930110,phase:2,block,severity:CRITICAL,msg:'Path Traversal Detectado'"

🚫 Cross-Site Scripting (XSS)

SecRule ARGS "@rx <script>" \
"id:941110,phase:2,block,severity:CRITICAL,msg:'XSS detectado'"

🚫 SQL Injection

SecRule ARGS "@rx union.*select.*from" \
"id:942270,phase:2,block,severity:CRITICAL,msg:'SQL Injection detectada'"

🚫 PHP Injection

SecRule ARGS "@rx <\?php" \
"id:933100,phase:2,block,severity:CRITICAL,msg:'Inyección de PHP detectada'"

🚫 Bloquear Scanners (ej. Nikto)

SecRule REQUEST_HEADERS:User-Agent "nikto" \
"id:913100,phase:2,block,severity:CRITICAL,msg:'Nikto Scanner Detectado'"

📌 OWASP Core Rule Set (CRS)
El CRS provee una cobertura base contra OWASP Top 10.

Instalación

    git clone https://github.com/coreruleset/coreruleset /etc/modsecurity-crs

    cd /etc/modsecurity-crs

    cp crs-setup.conf.example crs-setup.conf

Activación en Apache

Include /etc/modsecurity-crs/crs-setup.conf
Include /etc/modsecurity-crs/rules/*.conf

📊 Integración con Security Onion + ELK
Para monitoreo nivel SOC profesional:

1.Configura ModSecurity para logs en JSON:
    SecAuditLogFormat JSON
    SecAuditLog /var/log/modsec_audit.log

2.Instala Filebeat en el servidor web:
    sudo apt install filebeat

3.Configura filebeat.yml:

filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/modsec_audit.log

output.logstash:
  hosts: ["<IP_SECURITY_ONION>:5044"]


4.Verifica en Kibana:

    event.module: modsecurity

🧪 Laboratorio de Pruebas

Requisitos
    Kali Linux (atacante)

    Ubuntu/Debian con Apache + ModSecurity (defensa)

    Security Onion (monitorización)

Prueba de SQL Injection

    curl "http://victima.local/product.php?id=1' OR '1'='1"

Resultado esperado:

    Bloqueo con 403 Forbidden

    Log en /var/log/modsec_audit.log

    Alerta en Kibana

📌 Buenas Prácticas
    Empezar en modo DetectionOnly, luego pasar a bloqueo.

    Aplicar CRS como base y luego añadir reglas personalizadas.

    Normalizar entradas (t:lowercase, t:urlDecodeUni).

    Monitorear falsos positivos y ajustar reglas.

    Actualizar CRS periódicamente.

    Correlacionar alertas en un SIEM para detección avanzada.

📚 Recursos Recomendados
    🔗 OWASP Core Rule Set https://coreruleset.org/

    🔗 Repositorio ModSecurity https://github.com/SpiderLabs/ModSecurity

    🔗 Documentación Security Onion https://docs.securityonion.net/

    🔗 MITRE ATT&CK Framework https://attack.mitre.org/

    🔗 Suricata IDS/IPS https://suricata.io/

✅ Conclusión
ModSecurity no es solo un WAF, es una plataforma de defensa avanzada cuando se combina con OWASP CRS y herramientas como Security Onion + ELK.
Dominarlo te convertirá en un profesional WAF capaz de prevenir, detectar y analizar ataques en tiempo real.

💡 Consejo Final: No te limites a las reglas por defecto. Escribir y tunear reglas personalizadas es la clave para diferenciarte como experto en ciberseguridad.



# 📌 ModSecurity Cheat Sheet – Reglas y Ejemplos

Un resumen práctico de las **VARIABLES, OPERATORS y ACTIONS** de ModSecurity, con ejemplos listos para usar.  
Ideal como **chuleta rápida** para administradores de WAF.

---

## 🔹 VARIABLES (Qué inspeccionar)

| Variable                  | Descripción                                   | Ejemplo uso |
|---------------------------|-----------------------------------------------|-------------|
| `ARGS`                   | Todos los parámetros de la petición            | `SecRule ARGS ...` |
| `ARGS_GET`               | Solo parámetros GET                           | `SecRule ARGS_GET ...` |
| `ARGS_POST`              | Solo parámetros POST                          | `SecRule ARGS_POST ...` |
| `REQUEST_URI`            | URI completa de la petición                   | `SecRule REQUEST_URI ...` |
| `REQUEST_HEADERS`        | Todas las cabeceras                           | `SecRule REQUEST_HEADERS ...` |
| `REQUEST_BODY`           | Cuerpo de la petición                         | `SecRule REQUEST_BODY ...` |
| `REQUEST_COOKIES`        | Cookies enviadas por el cliente               | `SecRule REQUEST_COOKIES ...` |
| `REMOTE_ADDR`            | Dirección IP del cliente                      | `SecRule REMOTE_ADDR ...` |

---

## 🔹 OPERATORS (Qué buscar)

| Operador         | Descripción                          | Ejemplo |
|------------------|--------------------------------------|---------|
| `@rx`           | Expresión regular                    | `SecRule ARGS "@rx select.+from"` |
| `@contains`     | Contiene cadena específica            | `SecRule REQUEST_URI "@contains .php"` |
| `@beginsWith`   | Empieza con                          | `SecRule REQUEST_URI "@beginsWith /admin"` |
| `@endsWith`     | Termina con                          | `SecRule REQUEST_URI "@endsWith .exe"` |
| `@ipMatch`      | Coincide con IP o rango              | `SecRule REMOTE_ADDR "@ipMatch 192.168.1.0/24"` |
| `@pm`           | Lista de palabras                    | `SecRule ARGS_NAMES "@pm passwd pwd login"` |

---

## 🔹 ACTIONS (Qué hacer)

| Acción              | Función                                               | Ejemplo |
|---------------------|-------------------------------------------------------|---------|
| `deny`             | Bloquear la petición                                  | `deny,status:403` |
| `log`              | Registrar en log                                      | `log,msg:'XSS detectado'` |
| `status`           | Código HTTP de respuesta                              | `status:403` |
| `t:lowercase`      | Convertir a minúsculas antes de evaluar                | `t:lowercase` |
| `t:urlDecodeUni`   | Decodificar URLs (UTF-8)                              | `t:urlDecodeUni` |
| `t:removeNulls`    | Eliminar bytes nulos                                  | `t:removeNulls` |
| `severity`         | Nivel de criticidad (`CRITICAL`, `HIGH`, etc.)        | `severity:'CRITICAL'` |
| `capture`          | Guardar coincidencia para análisis posterior          | `capture` |
| `id`               | Identificador único de la regla                        | `id:1001` |

---

## 🔹 Ejemplos de Reglas

### 🚫 Bloquear SQL Injection
```apache
SecRule ARGS "@rx select.+from" \
"id:1002,phase:2,deny,status:403,msg:'SQL Injection detectada'"


🚫 Bloquear XSS
SecRule ARGS "@rx <script>" \
"id:1003,phase:2,deny,status:403,msg:'XSS detectado'"

🚫 Bloquear Path Traversal
SecRule REQUEST_URI "@rx \.\./" \
"id:930110,phase:2,deny,status:403,msg:'Path Traversal detectado'"

🚫 Bloquear IP específica
SecRule REMOTE_ADDR "@ipMatch 192.168.1.50" \
"id:2001,phase:1,deny,status:403,msg:'Bloqueo de IP sospechosa'"

🚫 Bloquear escáner Nikto
SecRule REQUEST_HEADERS:User-Agent "nikto" \
"id:913100,phase:2,block,severity:CRITICAL,msg:'Scanner Nikto detectado'"


🔹 Buenas Prácticas
    Empezar con DetectionOnly para reducir falsos positivos.

    Normalizar entradas con transformaciones (t:lowercase, t:urlDecodeUni).

    Usar IDs únicos para cada regla.

    Revisar logs en tiempo real:
        tail -f /var/log/modsec_audit.log
    Actualizar periódicamente el OWASP CRS.

    Integrar con un SIEM (Security Onion + ELK) para correlación avanzada.

📚 Recursos
OWASP CRS https://coreruleset.org/

ModSecurity GitHub https://github.com/SpiderLabs/ModSecurity

Suricata IDS/IPS https://suricata.io/

Security Onion Docs https://docs.securityonion.net/

✅ Conclusión
Este Cheat Sheet de ModSecurity es tu aliado para recordar rápidamente
cómo crear, ajustar y aplicar reglas WAF.

💡 Tip: La diferencia entre un admin básico y un profesional WAF está en el fine-tuning de reglas y la correlación con ELK/Security Onion.


***
>© 2025 [sualba.dev] Todos los derechos reservados
Este material forma parte de mi portfolio profesional y ha sido desarrollado como parte de mi formación en ciberseguridad.