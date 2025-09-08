# 🛡️ Ejercicios Avanzados Wazuh - Logs + Reglas MITRE

Esta colección incluye logs realistas para detección de amenazas y las reglas Wazuh correspondientes con explicaciones claras.

---

## 🔁 Ejemplo 6 - 🧪 Escaneo de red sospechoso (SYN scan)

**Log:**
```text
ownapp:DANGER,10.0.0.100,10.0.0.1,4444,135,tcp,606001,5
```

**Explicación:**  
Actividad en puerto RPC (135) desde origen no habitual. Podría indicar un escaneo SYN o descubrimiento lateral.

**Regla Wazuh:**
```xml
<rule id="100106" level="10">
  <if_sid>100003</if_sid>
  <match>DANGER</match>
  <field name="puertodestino">135</field>
  <description>Posible escaneo RPC detectado</description>
  <mitre>
    <id>T1046</id> <!-- Network Service Scanning -->
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 7 - 🛰️ Transferencia FTP no autorizada

**Log:**
```text
ownapp:ALERT,192.168.1.5,192.168.1.10,54321,21,tcp,707002,4
```

**Explicación:**  
Puerto FTP (21) activo con severidad 4. Puede ser una transferencia sin control.

**Regla Wazuh:**
```xml
<rule id="100107" level="7">
  <if_sid>100003</if_sid>
  <match>ALERT</match>
  <field name="puertodestino">21</field>
  <description>Posible intento de transferencia por FTP</description>
  <mitre>
    <id>T1105</id> <!-- Ingress Tool Transfer -->
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 8 - 💻 Uso de RDP sin autorización

**Log:**
```text
ownapp:DANGER,172.16.2.5,172.16.2.10,5555,3389,tcp,808003,5
```

**Explicación:**  
Intento de conexión al puerto RDP (3389) con severidad crítica.

**Regla Wazuh:**
```xml
<rule id="100108" level="10">
  <if_sid>100003</if_sid>
  <match>DANGER</match>
  <field name="puertodestino">3389</field>
  <description>Intento de acceso remoto vía RDP</description>
  <mitre>
    <id>T1021.001</id> <!-- Remote Desktop Protocol -->
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 9 - 📡 Exfiltración DNS sospechosa

**Log:**
```text
ownapp:WARNING,10.1.1.10,8.8.8.8,40000,53,udp,909004,3
```

**Explicación:**  
Tráfico DNS a un servidor externo (Google) con severidad moderada.

**Regla Wazuh:**
```xml
<rule id="100109" level="5">
  <if_sid>100003</if_sid>
  <match>WARNING</match>
  <field name="puertodestino">53</field>
  <description>Tráfico DNS potencialmente anómalo</description>
  <mitre>
    <id>T1048.003</id> <!-- Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol -->
  </mitre>
</rule>
```

---

## 🔁 Ejemplo 10 - 🧷 Comunicación SMB interna sospechosa

**Log:**
```text
ownapp:ALERT,192.168.0.50,192.168.0.55,45000,445,tcp,101010,4
```

**Explicación:**  
Puerto 445 (SMB) usado en entorno interno sin justificación clara.

**Regla Wazuh:**
```xml
<rule id="100110" level="6">
  <if_sid>100003</if_sid>
  <match>ALERT</match>
  <field name="puertodestino">445</field>
  <description>Acceso sospechoso a SMB</description>
  <mitre>
    <id>T1021.002</id> <!-- SMB/Windows Admin Shares -->
  </mitre>
</rule>
```

---

## ✅ Recomendaciones para examen

- Practica escribir logs tú mismo y diseña reglas para ellos.
- Recuerda qué protocolos comunes corresponden a qué puertos:
  - `21` → FTP
  - `22` → SSH
  - `53` → DNS
  - `135` → RPC
  - `445` → SMB
  - `3389` → RDP
- Asócialos a técnicas MITRE relevantes para subir nivel profesional de tus reglas.

***
sualba.dev © 2025 Todos los derechos reservados