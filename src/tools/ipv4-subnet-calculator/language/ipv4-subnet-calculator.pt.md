# Documentação do Calculador de Sub-redes IPv4

O calculador de sub-redes IPv4 é uma ferramenta online prática utilizada para analisar blocos CIDR IPv4 e obter informações detalhadas sobre as sub-redes. Abaixo está a descrição das funções e instruções de uso desta ferramenta:

## 1. Função de entrada

No campo de entrada, o usuário pode digitar um endereço IPv4 com ou sem máscara de sub-rede. Por exemplo, ao inserir "192.168.0.1/24", a ferramenta realiza os cálculos correspondentes com base nessa entrada.

## 2. Resultados do cálculo

1. **Máscara da rede (Netmask)**
   * Exibe a combinação do endereço IPv4 e sua máscara de sub-rede no formato CIDR, como por exemplo "192.168.0.0/24", permitindo que o usuário compreenda claramente a faixa de rede atual.

2. **Endereço da rede (Network address)**
   * Fornece o endereço de rede dentro da sub-rede, sendo um endereço especial utilizado para identificar toda a rede. Por exemplo, "192.168.0.0" indica o ponto inicial dessa sub-rede.

3. **Máscara de rede (Network mask)**
   * Apresenta a máscara de sub-rede em forma decimal, tal como "255.255.255.0", usada para determinar a divisão entre a parte da rede e a parte do host no endereço IP.

4. **Máscara de rede em formato binário (Network mask in binary)**
   * Mostra a máscara de sub-rede em notação binária, como por exemplo "11111111.11111111.11111111.00000000", ajudando a entender melhor seu funcionamento.

5. **Notação CIDR (CIDR notation)**
   * Exibe a representação CIDR da máscara de sub-rede, como "/24", uma forma concisa de expressar seu comprimento, facilitando a rápida compreensão da segmentação da rede.

6. **Máscara curinga (Wildcard mask)**
   * Oferece o valor da máscara curinga, por exemplo "0.0.0.255", complementar à máscara de sub-rede, frequentemente usada em certas configurações de dispositivos e softwares de rede.

7. **Tamanho da rede (Network size)**
   * Informa a quantidade total de endereços IP disponíveis na sub-rede, como por exemplo "256", possibilitando ao usuário conhecer a capacidade desta sub-rede.

8. **Primeiro endereço utilizável (First address)**
   * Mostra o primeiro endereço IP disponível para atribuição a um host dentro da sub-rede, por exemplo "192.168.0.1", indicando o início do intervalo de endereços disponíveis.

9. **Último endereço utilizável (Last address)**
   * Apresenta o último endereço IP disponível para atribuição a um host dentro da sub-rede, como "192.168.0.254", marcando o fim do intervalo de endereços disponíveis.

10. **Endereço de broadcast (Broadcast address)**
    * Fornecido o endereço de broadcast desta sub-rede, como "192.168.0.255", usado para enviar mensagens a todos os hosts presentes na sub-rede.

11. **Classe do endereço IP (IP class)**
    * Indica a classe à qual pertence o endereço IP, como por exemplo "C", ajudando o usuário a reconhecer como este endereço se classifica.

## 3. Funcionalidade de navegação

São disponibilizados botões intitulados "Bloco anterior (Previous block)" e "Próximo bloco (Next block)", tornando fácil para o usuário alternar rapidamente entre blocos adjacentes de sub-redes e visualizar suas informações.