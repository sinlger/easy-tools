# Documentação do Gerador IPv6 ULA

**1. Descrição da Ferramenta**

O gerador IPv6 ULA é uma ferramenta online projetada para ajudar os usuários a gerar endereços IPv6 locais não roteáveis de acordo com o padrão RFC4193. É adequado para criar identificadores de rede únicos dentro de uma rede local que não podem ser roteados na Internet.

**2. Principais Funcionalidades**

1. **Geração Aleatória de ULA Baseada em Múltiplos Fatores**
   * Esta ferramenta utiliza o primeiro método recomendado pela IETF, combinando o carimbo de data/hora atual e o endereço MAC através do algoritmo SHA1 e, em seguida, extrai os 40 bits inferiores para gerar endereços ULA aleatórios. Isso garante um alto nível de aleatoriedade e unicidade nos endereços gerados, reduzindo significativamente o risco de conflitos de endereços e fornecendo identificadores de rede locais confiáveis para os dispositivos dentro da rede local.

2. **Entrada e Processamento dos Endereços MAC**
   * Os usuários podem inserir manualmente endereços MAC no campo designado seguindo o formato padrão (por exemplo, "20:37:06:12:34:56"). A ferramenta usará este endereço MAC como um dos parâmetros essenciais para a geração do endereço ULA, combinando-o com outros fatores no cálculo, produzindo assim um endereço ULA vinculado a esse endereço MAC específico.

3. **Geração de Endereços ULA e Blocos de Roteamento Associados**

   * **IPv6 ULA**: A ferramenta gera um endereço IPv6 ULA completo que começa com "fd", conforme o formato padrão RFC4193 para endereços ULA locais. Por exemplo, "fd1d:dba9:6f7b::/48", onde "/48" indica que o comprimento do prefixo deste endereço ULA é de 48 bits. Ele fornece identificadores de rede únicos para os dispositivos na rede local, podendo ser utilizados para configurações de rede e comunicação interna.
   * **Primeiro Bloco Roável**: Gera-se o primeiro bloco de endereços atribuível a hosts ou sub-redes, por exemplo, "fd1d:dba9:6f7b:0::/64", representando o primeiro bloco dentro da faixa de endereços ULA. Isso ajuda o usuário a compreender a faixa inicial disponível para alocação, facilitando o planejamento de redes e a gestão de endereços.
   * **Último Bloco Roável**: O último bloco de endereços atribuível também é produzido, como "fd1d:dba9:6f7b:ffff::/64", indicando o último bloco dentro da faixa de endereços ULA que pode ser atribuído a hosts ou sub-redes. Assim, o usuário tem clareza sobre a extensão final dos endereços disponíveis, permitindo uma implantação eficiente da rede e configuração de dispositivos.

**3. Cenários de Aplicação**

1. Em redes locais corporativas, atribuir endereços IPv6 exclusivos aos dispositivos. Isso evita conflitos com endereços IPv6 públicos enquanto assegura a comunicação normal entre os dispositivos dentro da rede local.

2. Em ambientes de teste de rede, gerar endereços ULA locais não roteáveis permite simular cenários de rede, realizar testes de configuração de equipamentos de rede e aplicações sem consumir recursos oficiais de endereços IPv6 da Internet.

3. Em redes domésticas, atribuir endereços ULA a roteadores e dispositivos inteligentes aumenta a estabilidade e segurança da rede, prevenindo acessos não autorizados de redes externas.

**4. Instruções de Uso**

1. Acesse o site do gerador IPv6 ULA em [https://atoolio.com/ipv6-ula-generator](https://atoolio.com/ipv6-ula-generator).
2. Se você já conhecer o endereço MAC do dispositivo, insira-o no campo "MAC address" no formato padrão. Caso não saiba o endereço MAC, deixe o campo vazio; a ferramenta pode usar um endereço MAC padrão ou gerá-lo aleatoriamente (dependendo da lógica real da ferramenta).
3. Clique no botão de geração (como "Generate", embora o nome possa variar conforme a interface) para que a ferramenta calcule e gere o endereço IPv6 ULA correspondente, bem como o primeiro e o último blocos roteáveis, baseando-se no endereço MAC inserido (ou padrão) e no carimbo de data/hora atual.
4. Verifique as informações dos endereços gerados e utilize-as conforme necessário para configurar dispositivos na rede local, planejar a infraestrutura de rede ou realizar testes de conectividade.

**5. Observações Importantes**

1. Os endereços ULA gerados são exclusivamente destinados ao uso dentro da rede local e não podem ser roteados ou utilizados para comunicação na Internet. Para dispositivos que necessitem se comunicar com a Internet, devem ser configurados com endereços IPv6 unicast globais roteáveis.

2. Certifique-se de que o endereço MAC inserido seja correto. Um erro pode afetar a unicidade e a relação do endereço ULA gerado, causando possíveis problemas na configuração da rede.

3. Os endereços ULA devem permanecer únicos dentro da rede local. Evite repetir o uso do mesmo endereço ULA para evitar conflitos de rede que possam prejudicar a comunicação normal dos dispositivos.