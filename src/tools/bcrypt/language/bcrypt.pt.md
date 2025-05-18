# Manual de Utilização da Ferramenta de Criptografia de Texto

## 1. Visão Geral da Ferramenta

Esta é uma ferramenta poderosa para criptografar textos, baseada principalmente no algoritmo bcrypt. A ferramenta permite a criptografia de textos e suporta a verificação comparativa entre os valores hash gerados e o texto original, sendo aplicável a cenários relacionados à segurança, como armazenamento e verificação de senhas.

## 2. Acesso à Ferramenta

Digite a URL da página onde esta ferramenta está localizada na barra de endereços do navegador, pressione "Enter" para acessar a página e espere até que todos os elementos da página sejam completamente carregados.

## 3. Guia de Operação

### (1) Criptografar um Texto

1. **Inserir o Texto** : No campo de entrada "Your string", insira o conteúdo textual que deseja criptografar. Por exemplo, a senha definida por um usuário durante o registro.
2. **Configurar Salt count (contagem de sal)** : Clique nos botões "+" ou "-" ao lado de "Salt count" para definir a quantidade de iterações do valor Salt (sal). O Salt é uma sequência aleatoriamente gerada que será adicionada ao texto original antes da criptografia, melhorando assim a segurança e evitando ataques como os de tabela arco-íris. Geralmente, recomenda-se utilizar pelo menos 10 iterações.
3. **Visualizar Resultado da Criptografia** : Após concluir as configurações acima, a ferramenta criptografará automaticamente o texto inserido e exibirá o hash resultante no campo inferior. Esse hash contém informações sobre o algoritmo utilizado, o valor Salt e o texto criptografado. Por exemplo: "$2a$10$0HY6IJrUqS6LMG.LwGUuXemMiXTpBNloPRqFn/Dk5Esl7bj1sXA.xK".