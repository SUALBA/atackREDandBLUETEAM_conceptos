# 🛡️ ADDP vs APT – Guía de Ciberseguridad

## 🔍 ¿Qué es APT?

**APT (Advanced Persistent Threat)** es un tipo de ataque sofisticado, sostenido en el tiempo, realizado por actores con recursos elevados, como gobiernos o grupos patrocinados por estados.

### Características principales de un APT:
- Ataques **persistentes y dirigidos**.
- Uso de **malware avanzado**, 0-days, phishing, etc.
- Motivaciones: espionaje, sabotaje, robo de información.
- Mantienen **acceso oculto** durante mucho tiempo.
- Técnicas: movimiento lateral, persistencia, exfiltración.

🧠 **Ejemplo**: APT29 (Cozy Bear), vinculado a Rusia.

---

## 🧩 ¿Qué es ADDP?

**ADDP** no es una sigla estándar oficial, pero comúnmente se refiere en el ámbito ofensivo (red team) a:

> **Active Directory Discovery & Privilege escalation**

Es decir, técnicas para:
- **Reconocer estructura y objetos** dentro del entorno Active Directory.
- **Escalar privilegios** usando relaciones mal configuradas, delegaciones, fallos de Kerberos, etc.

Suele formar parte de la cadena de ataque de un APT o de un test de penetración.

---

## ⚔️ Comparativa APT vs ADDP

| Concepto     | APT                               | ADDP                                      |
|--------------|------------------------------------|-------------------------------------------|
| Nivel        | Actor o campaña de amenazas        | Técnicas específicas en entornos AD       |
| Alcance      | Global, persistente y coordinado   | Local al entorno de dominio Windows       |
| Motivación   | Espionaje, sabotaje, infiltración  | Control de dominio y escalada de privilegios |
| Contexto     | Blue Team, inteligencia de amenazas| Red Team, pentesting, ofensiva            |
| Herramientas | Cobalt Strike, PlugX, Mimikatz...  | BloodHound, PowerView, Mimikatz, etc.     |

---

## 🔧 Herramientas destacadas

### 🧠 Para APTs – Inteligencia y análisis

- **MISP** – Plataforma para compartir IOCs y patrones de amenazas.
- **YARA** – Reglas para identificar malware específico.
- **MITRE ATT&CK Navigator** – Mapea técnicas usadas por APTs.
- **Velociraptor** – Análisis forense y búsqueda de amenazas.
- **Sigma Rules** – Reglas SIEM universales.

---

### 🕵️ Para ADDP – Discovery y Privilege Escalation en AD

#### 🧭 Reconocimiento en Active Directory
- **BloodHound** / **Sharphound** – Grafo de relaciones y rutas de escalada.
- **PowerView** – Enumeración de usuarios, grupos, ACLs.
- **ADExplorer** – Explorador gráfico de estructura de AD.
- **LDAPDomainDump** – Dump de datos LDAP del dominio.

#### 🔓 Escalada de privilegios
- **Mimikatz** – Robo de credenciales, pass-the-hash, tickets.
- **Rubeus** – Kerberoasting, AS-REP roasting.
- **CrackMapExec** – Herramienta ofensiva de red todo en uno.
- **Impacket** – Scripts para SMB, Kerberos, DCOM, etc.

---

## 🧪 BONUS: Herramientas usadas por APTs reales

- **Cobalt Strike** – Framework ofensivo profesional.
- **PlugX** – RAT usado por grupos chinos.
- **Empire** – Post-explotación PowerShell.
- **Metasploit** – Plataforma modular de explotación.
- **APT Simulator** – Simulador de tácticas APT para testing.

---

## ✅ ¿Cómo usar esta información?

- 💻 Para **pentesters**: practicar rutas de escalada y análisis en entornos AD simulados.
- 🛡️ Para **blue teams**: identificar técnicas comunes de persistencia y detección.
- 🧠 Para **formación**: estudiar APTs reales (MITRE) y entrenar detección con herramientas como Sysmon + ELK.

---


