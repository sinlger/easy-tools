# Documentação do Expansor de Faixa IPv4

## 1. Introdução à Ferramenta

O Expansor de Faixa IPv4 calcula redes IPv4 eficazes com base em endereços IPv4 iniciais e finais fornecidos. Isso inclui blocos de rede válidos (representados na notação CIDR), faixas de endereços e a quantidade total de endereços disponíveis dentro dessa faixa.

## 2. Detalhes das Funcionalidades

### (A) Função Básica de Entrada

1. **Inserção do Endereço Inicial** - No campo "Start address", insira um endereço IPv4 que servirá como ponto inicial, por exemplo, "192.168.1.1".
2. **Inserção do Endereço Final** - No campo "End address", insira um endereço IPv4 que será usado como ponto final, como por exemplo "192.168.6.255".

### (B) Processamento Automático e Exibição dos Resultados

1. **Ajuste da Faixa de Endereços** - A ferramenta ajusta automaticamente os endereços inicial e final para obter uma faixa mais adequada. Por exemplo, "192.168.1.1" será convertido em "192.168.0.0", e "192.168.6.255" se tornará "192.168.7.255".
2. **Cálculo da Quantidade de Endereços** - Será calculada a quantidade total de endereços IPv4 disponíveis na nova faixa, passando, por exemplo, de "1.535" para "2.048", melhorando assim a eficiência no uso dos recursos de endereçamento.
3. **Geração da Notação CIDR** - A notação CIDR correspondente à nova faixa de endereços será exibida, como "192.168.0.0/21", facilitando a administração e configuração da rede.

## 3. Observações Importantes

Certifique-se de que os endereços inicial e final inseridos estejam no formato correto de endereço IPv4, a fim de garantir o funcionamento adequado da ferramenta e resultados precisos.