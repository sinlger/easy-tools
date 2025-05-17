# Documentação do Conversor de Docker Run para Docker-Compose

## 1. Visão Geral da Ferramenta

O Conversor de Docker Run para Docker-Compose é uma ferramenta online prática que ajuda os desenvolvedores a transformar comandos da linha de comando "docker run" em arquivos Docker-Compose. Isso simplifica o processo de configuração da orquestração de contêineres e aumenta a eficiência no desenvolvimento.

## 2. Principais Funções

1. **Conversão de Comandos**
   * Os usuários podem colar comandos complexos do Docker, como por exemplo "docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max-size=1g nginx", em um campo de entrada dedicado.
   * A ferramenta analisa automaticamente todos os parâmetros do comando "docker run", incluindo mapeamento de portas ("-p 80:80"), montagem de volumes ("-v /var/run/docker.sock:/tmp/docker.sock:ro"), políticas de reinicialização ("--restart always"), opções de logs ("--log-opt max-size=1g") e nome da imagem ("nginx").

2. **Geração de Arquivos Docker-Compose**
   * A partir dos parâmetros extraídos do comando "docker run", a ferramenta gera o conteúdo correspondente ao arquivo Docker-Compose.
   * O arquivo YAML gerado inclui declarações de versão (por exemplo, "version: '3.9'"), definições de serviços ("services"), especificação da imagem ("image"), configuração de logs ("logging" com "options"), definições de reinicialização ("restart"), alocações de volumes ("volumes") e mapeamentos de portas ("ports"). Assim, toda a informação necessária para orquestrar os contêineres é apresentada de forma completa, permitindo que os usuários a utilizem diretamente ou a modifiquem conforme necessário.

3. **Download do Arquivo**
   * Um botão intitulado "Download docker-compose.yml" permite que os usuários façam o download do arquivo Docker-Compose gerado com apenas um clique, facilitando sua utilização em ambientes reais de projeto.