# 🎥 RTSP (Real Time Streaming Protocol)

> 📡 **RTSP** es un protocolo de red de la capa de aplicación diseñado para controlar la transmisión de datos de audio y vídeo en tiempo real.

## 📋 1. Descripción general

- **📖 Nombre completo**: Real Time Streaming Protocol
- **📜 RFC**: Definido originalmente en la RFC 2326 (1998) y actualizado en la RFC 7826 (2016)
- **🎯 Propósito**: Proporcionar mecanismos de control (play, pause, teardown, etc.) sobre flujos multimedia que se transportan normalmente vía RTP/RTCP

## 🏗️ 2. Arquitectura y puertos

- **🔄 Cliente–servidor**: Un cliente RTSP (por ejemplo, VLC, FFmpeg, cámaras IP) envía comandos a un servidor RTSP, que gestiona los flujos multimedia
- **🚪 Puerto por defecto**: TCP/554 (aunque puede configurarse otro)
- **🚚 Transporte de medios**:
  - El control (señalización) va por RTSP sobre TCP (o a veces UDP)
  - Los datos multimedia se envían típicamente por RTP (Real-time Transport Protocol), y la sincronización se supervisa con RTCP

## 🔄 3. Flujo de comunicación

- **🔧 SETUP**: El cliente solicita establecer un "canal" para cada pista (audio, vídeo), negociando puertos y transporte (RTP/UDP, RTP/TCP "interleaved", etc.)
- **▶️ PLAY**: Inicia la reproducción del flujo multimedia
- **⏸️ PAUSE**: Pausa la transmisión, el servidor mantiene la sesión activa
- **🔚 TEARDOWN**: Finaliza la sesión y libera recursos
- **⚙️ GET_PARAMETER / SET_PARAMETER**: Consultas o modificaciones de parámetros (p. ej., nivel de volumen, resolución)

> 💡 **Nota**: Cada petición RTSP es similar a una petición HTTP (línea de petición, cabeceras, CRLF), aunque con métodos específicos de streaming.

## 🛠️ 4. Principales métodos RTSP

| Método | Función | Emoji |
|--------|---------|-------|
| OPTIONS | Solicita al servidor la lista de métodos soportados | 🤔 |
| DESCRIBE | Obtiene la descripción del medio (SDP – Session Description Protocol) | 📝 |
| SETUP | Configura el transporte para una o varias sesiones (cámaras IP suelen usarlo) | 🔧 |
| PLAY | Comienza la transmisión desde cierta posición de tiempo | ▶️ |
| PAUSE | Pausa la transmisión | ⏸️ |
| TEARDOWN | Cierra la sesión y libera conexiones | 🔚 |
| ANNOUNCE | (Servidor → Cliente) Informa de nuevos medios o cambios | 📢 |
| RECORD | (Cliente → Servidor) Envía medios al servidor (p. ej., videovigilancia) | 🎬 |
| REDIRECT | Indica al cliente que reconfigure a otro servidor/medio | 🔀 |

## 💼 5. Usos habituales

- 📹 **Cámaras IP y DVR/NVR** para videovigilancia
- 🎮 **Servidores de streaming** (Wowza, GStreamer, Darwin Streaming Server)
- 📺 **Reproductores multimedia**: VLC, QuickTime, FFmpeg, etc.
- 📞 **Aplicaciones VoIP y videoconferencia** como método de control de sesión

## ⚡ 6. Comparación con HTTP

| Característica | RTSP | HTTP |
|----------------|------|------|
| **Tipo** | 🎥 Control de streaming | 📄 Transferencia de archivos |
| **Tiempo real** | ✅ Sí | ❌ No |
| **Métodos especiales** | ▶️ PLAY, ⏸️ PAUSE | 📥 GET, 📤 POST |
| **Transporte de datos** | 🚫 No (usa RTP/RTCP) | ✅ Sí |
| **Propósito** | 🎛️ Señalización | 📦 Contenido |

> 🔍 **Diferencia clave**: RTSP no transporta los datos multimedia; se limita a señalización. RTP/RTCP se encargan del transporte real.

## 🎬 7. Ejemplo de sesión RTSP

```
🔍 C → S: OPTIONS rtsp://camara.local/stream1 RTSP/1.0
           CSeq: 1

✅ S → C: RTSP/1.0 200 OK
           CSeq: 1
           Public: DESCRIBE, SETUP, TEARDOWN, PLAY, PAUSE

📝 C → S: DESCRIBE rtsp://camara.local/stream1 RTSP/1.0
           CSeq: 2
           Accept: application/sdp

📋 S → C: RTSP/1.0 200 OK
           CSeq: 2
           Content-Type: application/sdp
           […SDP with codecs, puertos…]

🔧 C → S: SETUP rtsp://camara.local/stream1/trackID=1 RTSP/1.0
           CSeq: 3
           Transport: RTP/AVP;unicast;client_port=5000-5001

⚙️ S → C: RTSP/1.0 200 OK
           CSeq: 3
           Transport: RTP/AVP;unicast;client_port=5000-5001;server_port=8000-8001
           Session: 12345678

▶️ C → S: PLAY rtsp://camara.local/stream1 RTSP/1.0
           CSeq: 4
           Session: 12345678

🎥 S → C: RTSP/1.0 200 OK
           CSeq: 4
           Session: 12345678
```

> 📝 **Flujo explicado**: 
> 1. 🔍 Comprueba comandos disponibles (OPTIONS)
> 2. 📝 Solicita descripción de sesión (DESCRIBE)
> 3. 🔧 Configura canal de transporte (SETUP)
> 4. ▶️ Inicia el streaming (PLAY)

## 🎯 Resumen

> 🌟 **RTSP** es el estándar de facto para controlar flujos multimedia en tiempo real, separando la señalización (RTSP) del transporte de datos (RTP/RTCP). 

### ✨ Ventajas principales:
- 🎛️ **Control granular**: pause, play, teardown en tiempo real
- 🔄 **Versatilidad**: videovigilancia, streaming profesional, VoIP
- ⚡ **Eficiencia**: separación clara entre control y datos
- 📡 **Estándar**: RFC oficial, ampliamente soportado

---

> 💡 **Perfect for**: Cualquier escenario donde necesites pausar, avanzar o detener un flujo de audio/vídeo de forma dinámica.