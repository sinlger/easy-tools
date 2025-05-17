# Documentação do usuário para a ferramenta de conversão de TOML para YAML

## Visão geral

TOML para YAML é uma ferramenta online que permite aos usuários converter facilmente arquivos de configuração no formato TOML (Tom's Obvious, Minimal Language) para o formato YAML (YAML Ain't Markup Language). Isso é especialmente útil para desenvolvedores que precisam migrar configurações entre diferentes sistemas ou integrar múltiplas tecnologias.

## Layout da interface

A interface da ferramenta é simples e intuitiva, composta principalmente pelas seguintes partes:

1. Campo de texto à esquerda: Esta é a área onde os usuários podem inserir ou colar texto no formato TOML, identificado como "Seu TOML".
2. Campo de texto à direita: É usado para exibir o texto convertido no formato YAML, identificado como "YAML a partir do seu TOML".
3. Botão de conversão central: Após inserir o texto TOML, os usuários podem clicar neste botão para executar a conversão.

## Descrição das funções

### Inserção do texto TOML

- Os usuários podem inserir diretamente texto de configuração no formato TOML no campo de texto à esquerda.
- Também podem copiar texto TOML de outros arquivos ou editores e colá-lo neste campo de texto.

### Operação de conversão

- Depois de inserir ou colar o texto TOML, clique no botão de conversão central. O sistema analisará imediatamente o texto TOML inserido e o converterá para o formato YAML.
- Após a conclusão da conversão, o texto YAML resultante será exibido no campo de texto à direita.

### Visualização do resultado YAML

- O campo de texto à direita exibe completamente o texto YAML convertido.
- Aqui, os usuários podem verificar se o resultado da conversão é preciso e se a estrutura do texto YAML atende às suas expectativas.

### Cópia do texto YAML

- Os usuários podem selecionar e copiar todo o texto YAML no campo de texto à direita, o que é conveniente para usá-lo em outros lugares, como colá-lo em arquivos de configuração ou enviá-lo para outras pessoas.

## Exemplos

### Exemplo 1: Conversão básica

**Entrada no formato TOML:**

```toml
# Este é um exemplo simples de TOML
title = "Exemplo de TOML"

[author]
name = "Zhang San"
age = 28
e-mail = "zhangsan@example.com"
```

**Saída no formato YAML:**

```yaml
# Este é o exemplo convertido para YAML
title: Exemplo de TOML

author:
  name: Zhang San
  age: 28
  e-mail: zhangsan@example.com
```

### Exemplo 2: Conversão de estruturas complexas

**Entrada no formato TOML:**

```toml
# Exemplo de TOML com estrutura mais complexa
database:
  host = "localhost"
  port = 3306
  user = "admin"
  password = "securepassword"

[features]
logging = true
debug = false

[[servers]]
name = "main-server"
port = 8080

[[servers]]
name = "secondary-server"
port = 8081
```

**Saída no formato YAML:**

```yaml
# Exemplo de YAML com estrutura mais complexa
database:
  host: localhost
  port: 3306
  user: admin
  password: securepassword

features:
  logging: true
  debug: false

servers:
  - name: main-server
    port: 8080
  - name: secondary-server
    port: 8081
```

## Observações importantes

- Se o formato TOML inserido não estiver correto, a conversão poderá falhar e o sistema poderá exibir mensagens de erro.
- A ferramenta suporta a maioria das estruturas de sintaxe TOML comuns, mas para alguns elementos de sintaxe especiais ou pouco utilizados, talvez não seja possível uma conversão perfeita.
- O texto YAML gerado pode apresentar pequenas diferenças de formato dependendo da versão e especificações do YAML utilizadas.