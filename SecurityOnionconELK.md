🛡️ ¿Qué es Security Onion?
Es una distribución Linux especializada en detección y análisis de intrusos (IDS/NSM). Incluye herramientas como:

🧩 Zeek (IDS pasivo)

🧪 Suricata (IDS activo + firmas)

📊 Elasticsearch + Logstash + Kibana (ELK stack)

🐙 Wazuh (opcional)

🧠 TheHive, CyberChef, pcap-ng, Snort, osquery, etc.

📌 1. Requisitos Previos
Hardware recomendado (mínimo):

CPU: 4+ cores

RAM: 8 GB (ideal 16 GB)

Disco: 200 GB SSD

Virtualización: VirtualBox o VMware (también puedes hacerlo bare-metal).

ISO de Security Onion:
👉 Descargar desde https://securityonion.net



📌 2. Instalación de Security Onion
Crea una VM en VirtualBox/VMware:

Asigna 2 interfaces de red:

NAT / Bridged (para Internet y actualizaciones).

Host-Only o Promiscuo (para capturar tráfico).

Arranca la VM con la ISO de Security Onion.

Sigue el instalador gráfico:

Elige Standard Installation.

Configura hostname (ejemplo: soc-node1).

Establece contraseñas para soadmin y sysadmin.

Selecciona HVM mode para máximo rendimiento.

📌 3. Configuración Inicial
Ejecuta el asistente de configuración:

bash
sudo so-setup

Pasos:

Selecciona el modo:

Evaluation Mode (más fácil para laboratorio).

Production Mode (si lo usas en empresa).

Define el rol del nodo:

Manager + Sensor (laboratorio).

Solo Manager o Sensor (infra grande).

Configura interfaces de captura (ej. eth1).

Habilita Elastic Stack (ES, Logstash, Kibana).

📌 4. Acceso a la Consola Web
Navega desde tu navegador a:

cpp

https://<IP_DE_SECURITY_ONION>

Login con usuario:
nginx

soadmin

📌 5. Verificación de ELK (Elastic Stack)
Security Onion trae ya preconfigurado:

ElasticSearch → almacena logs.

Logstash → procesa logs de Zeek, Suricata, Wazuh.

Kibana (SO Dashboards) → interfaz gráfica para búsqueda.

Ejemplo: buscar logs de Suricata en Kibana.

kibana

event.module: suricata AND event.action: alert

📌 6. Integración de Suricata + Zeek + Wazuh
Suricata (IDS/IPS): analiza tráfico y genera alertas.

Zeek: más enfoque en análisis de comportamiento.

Wazuh: monitorización de host y correlación de alertas.

Comandos útiles:

bash

sudo so-status      # Ver estado de los servicios
sudo so-allow       # Permitir acceso remoto a Kibana
sudo so-elasticsearch-query '*'  # Probar búsqueda en ES

📌 7. Crear Dashboards en Kibana
Filtra por IDS → event.module:suricata.

Filtra por WAF (si integras ModSecurity logs).

Crea visualizaciones de:

Top 10 IPs atacantes

Tipos de ataques detectados

Alertas críticas (severity: CRITICAL)

📌 8. Integración con ModSecurity (Opcional Avanzado)
En tu servidor con Apache/Nginx + ModSecurity:
Configura el logging en JSON:

apache

SecAuditLogFormat JSON
SecAuditLog /var/log/modsec_audit.log
Envía los logs a Security Onion vía Filebeat:

bash
sudo apt install filebeat
Configura filebeat.yml:

yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/modsec_audit.log

output.logstash:
  hosts: ["<IP_SECURITY_ONION>:5044"]
Reinicia Filebeat:

bash
sudo systemctl restart filebeat

Verifica en Kibana → los logs de ModSecurity aparecerán en tiempo real.

📌 9. Buenas Prácticas de Profesional
Usar reglas Suricata actualizadas:

bash
sudo so-rule-update
Configurar alertas automáticas → integración con Slack, email o TheHive.

Tuning de reglas para reducir falsos positivos.

Integración con MITRE ATT&CK para clasificar alertas.

📌 10. Recursos Extra
Documentación oficial: https://docs.securityonion.net

OWASP CRS: https://coreruleset.org

Cheat Sheet Suricata: Suricata Rules Reference

✅ Con Security Onion + ELK + ModSecurity, tienes un SOC casero nivel profesional.
Esto te permite practicar detección, análisis y respuesta ante incidentes como lo harías en un Blue Team real.

***
>© 2025 [sualba.dev] Todos los derechos reservados
Este material forma parte de mi portfolio profesional y ha sido desarrollado como parte de mi formación en ciberseguridad.