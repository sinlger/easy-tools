# Analisador de URL

## 1. Visão Geral da Ferramenta
O Analisador de URL é uma ferramenta online para analisar cadeias de URL, capaz de decompor URLs complexas em várias componentes, incluindo protocolo, nome de utilizador, palavra-passe, nome do anfitrião, porta, caminho, parâmetros, etc., facilitando aos desenvolvedores compreender rapidamente a estrutura e as informações detalhadas da URL, permitindo a construção, depuração e análise de solicitações de rede.

## 2. Detalhes das Funcionalidades

  1. **Campo de Entrada**
     * Fornece um campo de entrada onde você pode inserir a cadeia de URL que deseja analisar.

  2. **Exibição dos Resultados da Análise**
     * **Protocolo (Protocol)** : Mostra a parte do protocolo da URL, por exemplo "https:", indicando o protocolo de transmissão de rede utilizado pela URL.
     * **Nome de Utilizador (Username)** : Se a URL contém informações sobre o nome de utilizador, estas serão exibidas aqui, utilizadas para identificar a identidade do utilizador fornecida na URL.
     * **Palavra-passe (Password)** : Mostra a parte da palavra-passe na URL, juntamente com o nome de utilizador, utilizada para autenticação da identidade do utilizador.
     * **Nome do Anfitrião (Hostname)** : Mostra o nome de domínio correspondente à URL, por exemplo "atoolio.com", representando o nome do servidor alvo.
     * **Porta (Port)** : Mostra o número da porta especificado na URL, utilizada para determinar a porta específica no servidor onde o serviço está disponível. Por padrão, diferentes protocolos têm portas padrão diferentes, por exemplo, a porta 80 para HTTP e a porta 443 para HTTPS.
     * **Caminho (Path)** : Mostra a parte do caminho na URL, por exemplo "/url-parser", apontando para uma localização específica de recurso ou serviço no servidor.
     * **Parâmetros (Params)** : Lista a parte dos parâmetros de consulta na URL, começando com "?", seguida por vários pares "chave-valor" como parâmetros, por exemplo "?key1=value&key2=value2", utilizados para enviar informações adicionais e instruções ao servidor.
     * **Exibição Detalhada dos Parâmetros** : Cada par chave-valor dos parâmetros de consulta é exibido individualmente, mostrando claramente o nome de cada parâmetro e seu valor correspondente.

## 3. Etapas de Utilização

  1. Abra seu navegador e visite a página web [Analisador de URL](https://atoolio.com/url-parser).
  2. No campo de entrada, digite a cadeia de URL que deseja analisar, por exemplo "https://me:pwd@atoolio.com:3000/url-parser?key1=value&key2=value2#the-hash".
  3. Clique no botão de análise (normalmente, pressionar Enter também pode iniciar a análise), a ferramenta analisará automaticamente a URL inserida e mostrará os detalhes de cada componente abaixo.
  4. Verifique o resultado da análise e copie, se necessário, a parte correspondente dos componentes para utilização em tarefas subsequentes de desenvolvimento, depuração ou outras operações.

## 4. Exemplos

  1. **Exemplo 1**
     * URL Inserida: "http://user:pass@example.com:8080/page?param1=hello&param2=world"
     * Resultado da Análise:
       * Protocolo: http:
       * Nome de Utilizador: user
       * Palavra-passe: pass
       * Nome do Anfitrião: example.com
       * Porta: 8080
       * Caminho: /page
       * Parâmetros: ?param1=hello&param2=world
       * Exibição Detalhada dos Parâmetros:
         * param1: hello
         * param2: world

  2. **Exemplo 2**
     * URL Inserida: "https://www.google.com/s?wd=Analisador de URL"
     * Resultado da Análise:
       * Protocolo: https:
       * Nome de Utilizador: (nenhum)
       * Palavra-passe: (nenhuma)
       * Nome do Anfitrião: www.google.com
       * Porta: (porta padrão 443, não exibida)
       * Caminho: /s
       * Parâmetros: ?wd=Analisador de URL
       * Exibição Detalhada dos Parâmetros:
         * wd: Analisador de URL