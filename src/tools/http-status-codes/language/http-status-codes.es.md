# Documentación de los Códigos de Estado HTTP

## 1. Introducción

Los códigos de estado HTTP son códigos numéricos de tres dígitos que el servidor envía como parte de la respuesta HTTP al cliente (normalmente un navegador web). Estos códigos indican el estado de una solicitud y ayudan a comprender si la solicitud fue exitosa, si se requieren redirecciones o si se produjeron errores.

## 2. Principales Categorías de los Códigos de Estado HTTP

### 1xx: Respuestas Informativas

Estos códigos indican que la solicitud ha sido comprendida y que el servidor sigue trabajando. Ejemplos:
- **100 Continue** - El cliente debería continuar con la solicitud.
- **101 Switching Protocols** - El cliente ha solicitado cambiar el protocolo de comunicación, por ejemplo, de HTTP a WebSocket.

### 2xx: Solicitud Exitosa

Estos códigos significan que la solicitud ha sido recibida, comprendida y aceptada correctamente. Ejemplos:
- **200 OK** - La solicitud se completó con éxito, y los datos solicitados fueron encontrados y entregados.
- **201 Created** - Un recurso ha sido creado exitosamente, generalmente después de una solicitud POST.
- **204 No Content** - La solicitud se completó con éxito, pero no hay contenido para devolver.