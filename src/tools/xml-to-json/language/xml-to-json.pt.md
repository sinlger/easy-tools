# Ferramenta de Conversão de XML para JSON

## 1. Introdução
Esta é uma ferramenta online para converter dados no formato XML para o formato JSON. Ela aumenta a eficiência do desenvolvimento e é adequada para cenários em que há necessidade de converter entre formatos de dados XML e JSON.

## 2. Principais Funções

### (1) Entrada de Conteúdo XML
Cole ou escreva os dados XML que deseja converter na área de entrada. Por exemplo, você pode inserir o seguinte conteúdo XML:
```
<a x="1.234" y="It's"/>
```

### (2) Saída de Dados JSON
Após clicar no botão de conversão, a ferramenta exibirá os dados correspondentes no formato JSON na área de saída. Por exemplo, o XML acima será convertido nos seguintes dados JSON:
```json
{
  "a": {
    "_atributos": {
      "x": "1.234",
      "y": "It's"
    }
  }
}
```

### (3) Função de Cópia
Na área de saída de dados JSON, você pode clicar no botão de cópia para copiar os dados JSON gerados para a área de transferência, facilitando seu uso em outros lugares.