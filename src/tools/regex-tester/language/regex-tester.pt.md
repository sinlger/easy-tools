# Documentação do usuário para o Regex Tester da A Toolio

## 1. Introdução à ferramenta

O **Regex Tester da A Toolio** é uma ferramenta online que permite testar expressões regulares por meio da inserção de textos de exemplo. Sua interface clara e funções práticas o tornam adequado tanto para iniciantes quanto para desenvolvedores experientes.

## 2. Descrição detalhada das funcionalidades

### (1) Área de entrada para expressões regulares

Digite na caixa de texto a expressão regular que você deseja testar. Um link para uma tabela de referência rápida de expressões regulares também é fornecido para ajudá-lo durante a utilização. Por exemplo, a expressão regular \w+ pode ser usada para encontrar uma ou mais palavras.

### (2) Opções do Regex Tester

As opções incluem: Busca global (g), Ignorar maiúsculas/minúsculas (i), Modo multilinha (m), Modo de linha única (s), Suporte a Unicode (u) e Suporte a conjunto Unicode (v). Selecione as opções apropriadas de acordo com suas necessidades específicas.

- Busca global (g): Procura todas as correspondências no texto completo.
- Ignorar maiúsculas/minúsculas (i): Encontra correspondências ignorando diferenças entre letras maiúsculas e minúsculas.
- Modo multilinha (m): Trata a entrada como um texto composto por múltiplas linhas, permitindo pesquisas no início e no final de cada linha.
- Modo de linha única (s): Considera todo o texto como uma única linha, facilitando buscas que atravessam várias linhas.
- Suporte a Unicode (u): Ativa o suporte a caracteres Unicode.
- Suporte a conjunto Unicode (v): Suporta conjuntos avançados de caracteres Unicode.

Exemplo: A expressão regular \d{3}-\d{3}-\d{4} pode identificar vários números de telefone em um texto quando a busca global está ativada.

### (3) Área de entrada do texto a ser analisado

Digite na caixa de texto o conteúdo no qual você deseja encontrar correspondências. A ferramenta realiza a pesquisa com base na expressão regular inserida e nas opções selecionadas. Por exemplo, ao usar a expressão regular \w+ no texto "Encontre palavras neste texto", será possível localizar todas as palavras individuais.