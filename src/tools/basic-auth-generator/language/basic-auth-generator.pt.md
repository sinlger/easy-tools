# Documentação do Gerador de Autenticação Básica

## Descrição das Funções

O gerador de autenticação básica é uma ferramenta que gera cabeçalhos de autorização codificados em Base64 para a autenticação HTTP básica. Ao fornecer um nome de usuário e senha, a ferramenta pode gerar rapidamente o cabeçalho de autorização correspondente, facilitando seu uso pelos desenvolvedores durante o processo de desenvolvimento.

## Instruções de Uso

### Digitar o Nome do Usuário

No campo de entrada "Username", digite o nome de usuário desejado. Pode ser qualquer nome que você quiser utilizar para autenticação.

### Digitar a Senha

Digite a senha correspondente ao nome do usuário no campo "Password". Durante a digitação, o campo da senha será automaticamente ocultado para garantir a segurança da sua senha.

### Visualizar o Cabeçalho de Autorização Gerado

Após digitar o nome do usuário e a senha, a ferramenta irá automaticamente gerar o cabeçalho de autorização correspondente. Este cabeçalho será exibido no seguinte formato:

```
Authorization header:
Authorization: Basic [String codificado em Base64]
```

Aqui, "Basic" indica que o método de autenticação básica está sendo utilizado, e a string posterior é o resultado da codificação em Base64 combinando o nome do usuário e a senha no formato "nome do usuário:senha".

### Copiar o Cabeçalho de Autorização

Se você precisar utilizar o cabeçalho de autorização gerado em outro local, poderá clicar no botão "Copy header" para copiá-lo para a área de transferência. Desta forma, você poderá facilmente colá-lo em arquivos ou código onde for necessário.