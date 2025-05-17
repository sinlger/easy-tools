# Documentação do usuário para a ferramenta online de conversão de TOML para JSON

## 1. Introdução à ferramenta

TOML para JSON é uma ferramenta online prática que analisa dados no formato TOML e os converte para o formato JSON. Os usuários podem facilmente colar ou digitar dados TOML no campo de entrada do lado esquerdo, e o resultado correspondente no formato JSON será gerado automaticamente do lado direito.

## 2. Descrição detalhada das funcionalidades

### 1. Entrada de dados TOML

* No campo de texto do lado esquerdo denominado "Your TOML", os usuários podem colar ou inserir manualmente dados no formato TOML. Este campo de texto permite a entrada de texto em múltiplas linhas, oferecendo espaço suficiente para inserir informações de configuração TOML mais complexas.

### 2. Saída do resultado JSON

* Assim que os dados TOML forem inseridos ou colados no campo de texto do lado esquerdo, a ferramenta realiza automaticamente a análise e a conversão. Os dados JSON convertidos aparecerão no campo de texto do lado direito intitulado "JSON from your TOML". Os usuários poderão visualizar, copiar ou processar esses dados posteriormente.

## 3. Etapas de utilização

1. Abra a página da ferramenta ([https://atoolio.com/toml-to-json](https://atoolio.com/toml-to-json)).
2. No campo de texto do lado esquerdo denominado "Your TOML", cole ou insira os dados TOML que deseja converter.
3. O sistema realizará automaticamente a conversão, e o resultado será exibido no campo de texto do lado direito intitulado "JSON from your TOML".

## 4. Principais características

* Interface simples e intuitiva: A interface é clara e fácil de usar, com um processo operacional simples, sem necessidade de configurações complexas, permitindo que os usuários comecem a usá-la rapidamente.
* Conversão em tempo real: Após inserir os dados TOML, a ferramenta realiza automaticamente a conversão e mostra o resultado, sem necessidade de clicar manualmente em um botão de conversão, aumentando assim a eficiência da conversão.
* Uso online: Nenhum software precisa ser instalado. Desde que você tenha um dispositivo com acesso à internet, poderá utilizar esta ferramenta a qualquer momento e em qualquer lugar para converter dados TOML para JSON.

## 5. Exemplos

### Exemplo 1: Conversão simples de TOML para JSON

Suponha que temos os seguintes dados no formato TOML:
```toml
title = "TOML Example"
owner = "John Doe"
```

Ao colar estes dados no campo de texto do lado esquerdo denominado "Your TOML", a ferramenta os converterá automaticamente para o seguinte formato JSON:
```json
{
  "title": "TOML Example",
  "owner": "John Doe"
}
```

### Exemplo 2: Conversão de TOML para JSON com estrutura aninhada

Temos dados TOML mais complexos:
```toml
[database]
server = "192.168.1.1"
ports = [8001, 8002, 8003]
connection_max = 5000
```

Após inseri-los na ferramenta, obteremos os seguintes dados JSON:
```json
{
  "database": {
    "server": "192.168.1.1",
    "ports": [8001, 8002, 8003],
    "connection_max": 5000
  }
}