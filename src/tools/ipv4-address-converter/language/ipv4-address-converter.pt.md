# Documentação do Conversor de Endereços IPv4

## 1. Introdução à Ferramenta

O Conversor de Endereços IPv4 é uma ferramenta online que converte endereços IPv4 para diferentes sistemas numéricos (decimal, hexadecimal, binário) e também para o formato IPv6. Esta ferramenta auxilia desenvolvedores e técnicos de rede a obter rapidamente várias representações de endereços IPv4, facilitando tarefas como configuração de redes, desenvolvimento de software ou análise de segurança.

## 2. Detalhes das Funções

### (A) Entrada do Endereço IPv4
- No campo de entrada da ferramenta, o usuário pode digitar diretamente um endereço IPv4 válido (por exemplo: 192.168.1.1). Após a inserção do endereço, basta clicar no botão "Converter" ou pressionar Enter para que sejam realizadas automaticamente as conversões necessárias.

### (B) Conversão para Formato Decimal
- **Função**: Converter o endereço IPv4 em um valor decimal.
- **Como Utilizar**: Depois de inserir o endereço IPv4, a ferramenta calcula automaticamente o valor decimal correspondente. Esse valor é obtido convertendo cada um dos quatro octetos do endereço IPv4 em números decimais e combinando-os segundo um esquema específico.

### (C) Conversão para Formato Hexadecimal
- **Função**: Converter o endereço IPv4 em uma string hexadecimal.
- **Como Utilizar**: Ao digitar o endereço IPv4, cada octeto será transformado em dois dígitos hexadecimais e, em seguida, concatenados para formar uma única string hexadecimal completa. Por exemplo, o endereço IPv4 192.168.1.1 será convertido para C0A80101 após a conversão.

### (D) Conversão para Formato Binário
- **Função**: Transformar o endereço IPv4 em uma representação binária.
- **Como Utilizar**: Quando o endereço IPv4 é inserido, cada octeto é convertido em um número binário de 8 bits, e os quatro octetos são unidos para formar uma string binária de 32 bits. Exemplificando, o endereço IPv4 192.168.1.1 será apresentado na forma binária como 11000000101010000000000100000001.

### (E) Conversão para Formato IPv6
- **Função**: Converter o endereço IPv4 em uma representação no formato IPv6.
- **Como Utilizar**: A ferramenta produz duas formas distintas de endereços IPv6:
  1. **Endereço IPv6 Completo**: Os primeiros 8 bytes são preenchidos com zeros, enquanto os últimos 8 bytes contêm a representação hexadecimal do endereço IPv4, com o acréscimo de "ffff" antes da parte referente ao IPv4 para identificação. Por exemplo, a partir do endereço IPv4 192.168.1.1, será gerado o seguinte endereço IPv6 completo: 0000:0000:0000:0000:0000:ffff:c0a8:0101.