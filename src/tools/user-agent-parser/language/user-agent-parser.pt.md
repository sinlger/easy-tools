# Documentação do analisador de agente do usuário online

## 1. Visão geral da ferramenta

O analisador de agente do usuário online pode detectar e analisar com precisão informações sobre o navegador, motor de renderização, sistema operacional, arquitetura da CPU e tipo/modelo do dispositivo a partir da string do agente do usuário, ajudando os desenvolvedores a obter rapidamente detalhes relacionados ao cliente.

## 2. Descrição das funcionalidades

### (1) Detecção do navegador

É capaz de identificar com precisão o tipo de navegador utilizado pelo usuário e sua versão específica. Por exemplo, quando uma determinada string é inserida, se exibir "Edge 135.0.0.0", isso indica que o navegador do cliente é o Edge e a versão é 135.0.0.0.

### (2) Detecção do motor de renderização

Apresenta claramente o motor de renderização utilizado pelo navegador e sua respectiva versão. Por exemplo, "Blink 135.0.0.0" significa que o motor de renderização é o Blink e a versão é 135.0.0.0.

### (3) Detecção do sistema operacional

Mostra detalhadamente o nome do sistema operacional e sua versão. Como "Windows 10", o que implica que o sistema operacional é o Windows e a versão é a 10.

### (4) Detecção das informações do dispositivo

Permite obter informações como tipo de dispositivo, modelo e fabricante (se disponível). Por exemplo, alguns dispositivos podem mostrar completamente o modelo do dispositivo, no entanto, também existem casos em que não há disponibilidade de modelo, tipo ou fabricante do dispositivo, aparecendo então a mensagem correspondente: "No device model/type/vendor available".

### (5) Detecção das informações da CPU

É possível identificar características relacionadas à CPU. Por exemplo, se for exibido "amd64", isso indica que a arquitetura da CPU é do tipo amd64.

## 3. Exemplos de uso

### Exemplo um: Caso comum de navegador desktop

Suponha que a string do agente do usuário seja:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0

Após inserir esta string no analisador:

  * **Navegador**: É reconhecido como Edge 135.0.0.0.
  * **Motor**: É identificado como Blink 135.0.0.0.
  * **Sistema Operacional**: Trata-se do Windows 10.
  * **Dispositivo**: Não há modelo específico, tipo ou fabricante do dispositivo disponível, portanto, será exibida a mensagem adequada.
  * **CPU**: Sua arquitetura é amd64.

### Exemplo dois: Navegador em dispositivo móvel

Tomemos como exemplo a seguinte string do agente do usuário:
Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1

Após inseri-la no analisador:

  * **Navegador**: Pode-se identificar o navegador Safari juntamente com a versão correspondente no sistema iOS (a versão exata dependerá do resultado da análise).
  * **Motor**: Será apresentado o motor Webkit com seus detalhes de versão.
  * **Sistema Operacional**: É identificado claramente como iOS, acompanhado de seu número de versão (por exemplo, 16_6_1 etc.).
  * **Dispositivo**: São obtidas informações do dispositivo, como por exemplo que se trata de um iPhone (o modelo específico dependerá dos resultados da análise).
  * **CPU**: Mostrará a arquitetura da CPU adaptada a dispositivos móveis (se houver parte claramente identificável).