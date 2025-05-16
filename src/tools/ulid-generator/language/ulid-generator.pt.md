# Documentação do usuário para o gerador de ULID

## 1. Visão geral da ferramenta
O gerador de ULID é utilizado para criar identificadores únicos universais aleatórios ordenáveis lexicograficamente (ULID). Os identificadores gerados são únicos e ordenáveis, sendo amplamente utilizados em sistemas distribuídos, como identificadores de registros em bancos de dados, entre outros cenários.

## 2. Descrição das funcionalidades

### (1) Configuração da quantidade
Através da opção "Quantity", é possível definir a quantidade de ULIDs que deseja gerar. O valor padrão é 1, podendo ajustar esta quantidade clicando nos botões de adição/subtração no lado direito.

### (2) Seleção de formato
Dois formatos de saída estão disponíveis:
1. **Raw**: Mostra os ULIDs em formato de texto puro, facilitando sua visualização e uso direto.
2. **JSON**: Exporta os ULIDs gerados no formato JSON, facilitando a chamada e análise por programas.

### (3) Geração e operações
Clique no botão "Refresh" para gerar novos ULIDs; clique no botão "Copy" para copiar os ULIDs gerados para a área de transferência, permitindo colá-los facilmente em outros locais.

## 3. Exemplos

### Exemplo 1: Gerar um único ULID (formato Raw)
Defina "Quantity" como 1 e selecione o formato "Raw", em seguida clique em "Refresh", será gerado um ULID semelhante ao seguinte:
```
01JTJFE7397K54Z6XD2ZQFHDD3
```

### Exemplo 2: Gerar múltiplos ULIDs (formato JSON)
Defina "Quantity" como 3 e selecione o formato "JSON", em seguida clique em "Refresh", serão gerados ULIDs no seguinte formato JSON:
```json
{
  "ulids": [
    "01JTJFE7397K54Z6XD2ZQFHDD3",
    "01JTJFE7397K54Z6XD2ZQFHDD4",
    "01JTJFE3797K54Z6XD2ZQFHDD5"
  ]
}