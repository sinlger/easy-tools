# Documentação do usuário para a ferramenta de formatação e embelezamento SQL

## 1. Visão geral da ferramenta

A ferramenta de formatação e embelezamento SQL é uma plataforma online usada para formatar e melhorar visualmente as consultas SQL escritas. Ela suporta vários dialetos SQL, ajudando os desenvolvedores a lerem e escreverem código SQL de forma mais clara.

## 2. Descrição das funcionalidades

### (1) **Funções básicas**

1. **Embelezamento SQL**: Converte consultas SQL desorganizadas em um formato estruturado e fácil de compreender. Exemplo:

* Consulta original:
```sql
select field1,field2,field3 from my_table where my_condition;
```

* Após o embelezamento:
```sql
SELECT
    field1,
    field2,
    field3
FROM
    my_table
WHERE
    my_condition;
```


### (2) **Opções de configuração**

1. **Seleção de dialeto (Dialect)**: Vários dialetos SQL estão disponíveis, tais como SQL Padrão (Standard SQL), MySQL, PostgreSQL, SQL Server, etc. Selecione o dialeto adequado para seu banco de dados, garantindo que as consultas SQL formatadas obedeçam às regras sintáticas específicas deste banco de dados.
2. **Maiúsculas/minúsculas das palavras-chave (Keyword case)**: As palavras-chave SQL podem ser mostradas em letras maiúsculas (UPPERCASE), minúsculas (lowercase) ou com a primeira letra maiúscula (Capitalized), permitindo manter um estilo uniforme no código. Exemplos:

* Consulta original:
```sql
select * from table;
```

* Em maiúsculas:
```sql
SELECT * FROM table;
```

* Em minúsculas:
```sql
select * from table;
```

* Primeira letra maiúscula:
```sql
Select * From table;
```


3. **Estilo de indentação (Indent style)**: Você pode escolher entre diferentes estilos de indentação, como padrão (standard), 2 espaços (2 spaces), 4 espaços (4 spaces). Isso permite adaptar-se às preferências pessoais ou ao estilo interno da equipe. Exemplos:

* Indentação padrão:
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```

* Com indentação de 2 espaços:
```sql
SELECT
  field1,
  field2
FROM
  my_table
WHERE
  condition;
```

* Com indentação de 4 espaços:
```sql
SELECT
    field1,
    field2
FROM
    my_table
WHERE
    condition;
```


### (3) **Área de entrada e saída**

1. **Área de entrada**: Na caixa de texto à esquerda, você pode colar ou digitar diretamente sua consulta SQL que deseja formatar.
2. **Área de saída**: A caixa de texto à direita mostra em tempo real o resultado após a formatação e o embelezamento. Além disso, há um botão de cópia que facilita transferir a consulta embelezada para a área de transferência (clipboard), para utilizá-la posteriormente onde for necessário.

## 3. Etapas de uso

1. Abra a [página web da ferramenta SQL](https://atoolio.com/sql-prettify).
2. Cole ou digite sua consulta SQL na área de entrada.
3. Escolha as opções adequadas conforme suas necessidades nos menus suspenso sob Dialeto, Maiúsculas/Minúsculas das palavras-chave e Estilo de indentação.
4. Verifique o resultado formatado exibido na área de saída à direita. Caso esteja satisfeito, clique no botão de cópia para salvá-lo na área de transferência.