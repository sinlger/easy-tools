# Documentação dos Códigos de Status HTTP

## 1. Introdução

Os códigos de status HTTP são códigos numéricos de três dígitos enviados pelo servidor como parte da resposta HTTP ao cliente (geralmente um navegador web). Eles indicam o status de uma solicitação e ajudam a compreender se a solicitação foi bem-sucedida, se é necessário redirecionar ou se ocorreram erros.

## 2. Principais Categorias dos Códigos de Status HTTP

### 1xx: Respostas Informativas

Esses códigos indicam que a solicitação foi compreendida e que o servidor continua trabalhando. Exemplos:
- **100 Continue** - O cliente deve continuar com a solicitação.
- **101 Switching Protocols** - O cliente solicitou a troca do protocolo de comunicação, por exemplo, de HTTP para WebSocket.

### 2xx: Solicitação Bem-sucedida

Esses códigos significam que a solicitação foi recebida, compreendida e aceita corretamente. Exemplos:
- **200 OK** - A solicitação foi concluída com sucesso, e os dados solicitados foram encontrados e entregues.
- **201 Created** - Um recurso foi criado com sucesso, geralmente após uma solicitação POST.
- **204 No Content** - A solicitação foi executada com sucesso, mas não há conteúdo para retornar.