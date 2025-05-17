# Documentação do usuário para o gerador de espaços reservados SVG

## 1. Visão geral da ferramenta

O gerador de espaços reservados SVG é uma ferramenta online conveniente para criar rapidamente imagens SVG personalizadas para uso como placeholders. Esses espaços reservados podem ser utilizados durante o processo de desenvolvimento de aplicativos para exibição temporária de imagens, ajudando os desenvolvedores a projetar e visualizar o layout da interface antes de ter conteúdo real de imagem.

## 2. Descrição das funcionalidades

### (1) **Configurações de tamanho**

* **Largura e altura**: Você pode definir a largura e a altura do espaço reservado (em pixels) por meio de campos de entrada. Além disso, há botões '+' e '-' para ajustar rapidamente as dimensões.
* **Usar tamanho exato**: Ao ativar esta opção, você garante que o espaço reservado SVG gerado seja exibido estritamente conforme a largura e altura especificadas.

### (2) **Personalização de cores**

* **Cor de fundo**: Insira um código de cor hexadecimal (por exemplo, "#cccccc") para personalizar a cor de fundo do espaço reservado.
* **Cor do texto**: Da mesma forma, insira um código hexadecimal (por exemplo, "#333333") para definir a cor do texto exibido no espaço reservado.

### (3) **Configurações de texto**

* **Tamanho da fonte**: Digite um valor numérico e selecione uma unidade adequada (como pixels) para ajustar o tamanho do texto mostrado no espaço reservado.
* **Texto personalizado**: Digite o conteúdo desejado na caixa de texto; por padrão, ele mostra "largura x altura" (por exemplo, "600x350").

### (4) **Visualização e saída**

* **Visualização em tempo real**: Na área de visualização à direita, você pode ver em tempo real o efeito do espaço reservado SVG gerado com base nas configurações feitas.
* **Elemento HTML SVG**: Mostra o código SVG gerado, que pode ser copiado e usado diretamente no desenvolvimento web.
* **SVG em Base64**: Oferece a possibilidade de converter a imagem SVG em uma string codificada em Base64, útil em cenários que exigem esse formato especial.

## 3. Etapas de uso detalhadas

1. Acesse o site do [gerador de espaços reservados SVG](https://atoolio.com/svg-placeholder-generator).
2. Configure a largura e a altura do espaço reservado conforme necessário. Por exemplo, se quiser gerar um espaço reservado de 800 pixels de largura e 450 pixels de altura, digite "800" no campo "Width (in px)" e "450" no campo "Height (in px)".
3. Personalize a cor de fundo e a cor do texto. Se desejar um fundo azul claro (por exemplo, "#e6f7ff") e texto azul escuro (por exemplo, "#1890ff"), insira os códigos de cor correspondentes nos campos apropriados.
4. Defina o tamanho da fonte e o texto personalizado. Suponha que o tamanho da fonte seja de 20 pixels e que você queira mostrar o texto "Sample", então insira "20" no campo "Font size" e "Sample" no campo "Custom text".
5. Verifique a área de visualização no lado direito para confirmar que a imagem do espaço reservado está de acordo com suas expectativas.
6. Dependendo das suas necessidades reais, escolha copiar o código fornecido pelo "SVG HTML element", ou a string codificada em Base64, e cole-a no projeto de desenvolvimento correspondente. Alternativamente, clique no botão "Download svg" para baixar diretamente o arquivo SVG gerado.