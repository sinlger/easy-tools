# Documentação do usuário para o gerador de par de chaves RSA

## 1. Visão geral da ferramenta

Esta ferramenta online permite a geração fácil de certificados PEM aleatórios contendo uma chave privada e uma chave pública RSA. É especialmente útil para desenvolvedores que precisam criar rapidamente um par de chaves RSA durante o processo de desenvolvimento.

## 2. Descrição das funcionalidades

### (1) **Configuração do comprimento da chave**

* **Função**: O usuário pode definir o comprimento da chave (expresso em bits) dentro de uma faixa determinada.
* **Ação**: Digite no campo "Bits" o comprimento desejado, como por exemplo os comuns 2048 bits. A ferramenta suporta uma faixa específica de tamanhos de chave, garantindo que a chave gerada atenda aos requisitos de segurança e uso.
* **Objetivo**: Geralmente, quanto maior o comprimento da chave, maior é a segurança, porém isso pode reduzir a velocidade de criptografia e descriptografia. Por isso, é importante escolher este comprimento com base no cenário prático de utilização.

### (2) **Atualização do par de chaves**

* **Função**: Permite gerar rapidamente um novo par de chaves RSA aleatório.
* **Ação**: Clique no botão "Refresh key-pair", o sistema irá regenerar um novo par composto por chave pública e privada com base no comprimento atual configurado.
* **Objetivo**: Quando há necessidade de gerar múltiplos pares de chaves diferentes para testes ou uso direto, basta pressionar o botão Refresh sem ter que modificar manualmente outros parâmetros, aumentando assim sua eficiência de trabalho.

### (3) **Chave pública - Exibição e gerenciamento**

* **Função**: Mostra a chave pública RSA gerada e oferece operações convenientes para seu uso.
* **Apresentação**: Na seção "Public key", a chave pública aparece no formato padrão PEM, incluindo as marcações "-----BEGIN PUBLIC KEY-----" e "-----END PUBLIC KEY-----", permitindo usá-la imediatamente em suas aplicações.
* **Função de cópia**: O botão de cópia ao lado facilita ao usuário copiar facilmente a chave pública para a área de transferência (clipboard), possibilitando colá-la em outros locais, como arquivos de configuração ou segmentos de código.

### (4) **Chave privada - Exibição e gerenciamento**

* **Função**: Mostra a chave privada RSA gerada e oferece um método simples para utilizá-la.
* **Apresentação**: Na seção "Private key", também é usado o formato PEM padrão, com as marcações "-----BEGIN RSA PRIVATE KEY-----" e "-----END RSA PRIVATE KEY-----", permitindo ao usuário empregar esta chave para realizar operações como criptografia, descriptografia ou assinaturas digitais.
* **Função de cópia**: O botão de cópia adjacente facilita a cópia rápida da chave privada para que possa ser usada em ambientes seguros, por exemplo, para armazenamento em servidores ou configuração em aplicações.

## 3. Exemplos de cenários de aplicação

1. Os desenvolvedores podem usar esta ferramenta quando precisarem de chaves de teste rápidas enquanto desenvolvem aplicações baseadas no algoritmo de criptografia RSA. Podem selecionar um comprimento adequado de chave, gerar um par usando o botão Refresh e então utilizar a chave pública para criptografar e a privada para testes de descriptografia.
2. Ao configurar protocolos de comunicação segura (como SSL/TLS), caso precise de um certificado autoassinado ou de um par de chaves para um ambiente de teste, você poderá gerá-los aqui e configurar a chave pública e a privada respectivamente nos lugares apropriados no servidor e cliente.