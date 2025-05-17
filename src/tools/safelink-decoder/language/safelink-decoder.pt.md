# Documentação do usuário para o decodificador de links seguros do Outlook

## 1. Introdução à ferramenta
O **decodificador de links seguros do Outlook** é uma ferramenta projetada para decodificar os links gerados pelo serviço de e-mail Microsoft Outlook chamados SafeLink. Esta ferramenta permite transformar os links criptografados pelo Outlook SafeLink em seus URLs originais, facilitando assim a identificação do destino real destes links pelos usuários.

## 2. Descrição das funcionalidades
A principal função desta ferramenta é decodificar os links do Outlook SafeLink, ou seja, converter os links criptografados e redirecionados criados pela Microsoft Outlook em endereços web originais.

## 3. Instruções de uso

### Entrada
Cole no campo de entrada o link do Outlook SafeLink que você deseja decodificar. Este link foi criptografado pela Microsoft Outlook por razões de segurança e possui um formato específico.

### Saída
Após clicar no botão "Decode", a ferramenta processará o link inserido e exibirá no campo de saída o URL original decodificado. Caso o link não esteja corretamente formatado ou não possa ser reconhecido, será exibida uma mensagem de erro: "Error: Invalid SafeLinks URL provided" (Erro: URL do SafeLinks inválida fornecida).

## 4. Exemplos de utilização

### Exemplo 1
Entrada (link SafeLink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fexample.com&data=...`
Saída após a decodificação:
`https://example.com`

### Exemplo 2
Entrada (link SafeLink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fmicrosoft.com&data=...`
Saída após a decodificação:
`https://microsoft.com`

### Exemplo 3
Entrada com um link inválido ou mal formatado:
`https://nam02.safelinks.protection.outlook.com/?url=invalidurl&data=...`
Mensagem de erro:
`Error: Invalid SafeLinks URL provided`

## 5. Observações importantes
- Certifique-se de que o link inserido seja um link completo do Outlook SafeLink.