{Stalker Red}:

Brutal Force Password Generate:

- Defina o tamanho da senha desejada na linha 21, dentro da chamada da função generateRandPw().
- Execute o código. Ele irá gerar uma senha aleatória e iniciará o processo de força bruta para tentar adivinhá-la.
- O processo de força bruta pode levar um tempo considerável, dependendo do tamanho da senha. O progresso é exibido na tela.
- Quando o processo for concluído, o programa exibirá a senha adivinhada e o tempo que levou para encontrá-la.

Este script gera uma senha aleatória, incluindo letras minúsculas, números e caracteres especiais, e então tenta encontrá-la através de uma força bruta, tentando todas as combinações possíveis. O tempo estimado para encontrar a senha é calculado e exibido, juntamente com o tempo total gasto para encontrar a senha.
A senha gerada aleatoriamente será exibida e o script tentará encontrá-la.


Brute Force Login Attempt:

O código é um script de força bruta para tentar fazer login em uma aplicação web usando um nome de usuário e uma senha fornecidos. Ele usa a biblioteca requests para enviar uma solicitação POST para a URL especificada com os dados de login. Se a resposta do servidor for 200 OK, significa que a tentativa de login foi bem-sucedida e a função retorna True. Caso contrário, a função registra a tentativa de login e retorna False. Existe uma limitação de tentativas de login e um tempo mínimo entre tentativas de login.

Você deve fornecer o link da área de login e nome de usuario e a lista de arquivos de dicionário. O código verifica se o arquivo "dicionario.txt" existe e se sim, lê-o para obter a lista de palavras-chave.

Faça o download dos dicionarios e inclua na mesma pasta do projeto pelo link: https://github.com/berzerk0/Probable-Wordlists/tree/master/Real-Passwords 
você poderá incluir vários ao mesmo tempo para leitura

**NOTAS**

Este código é um exemplo de como a técnica de força bruta pode ser utilizada para tentar adivinhar uma senha. Ele estima o tempo necessário para adivinhar a senha com base no comprimento da senha e no número de caracteres do alfabeto, e então tenta todas as combinações possíveis de caracteres. O código gera uma senha aleatória e a passa para a função de força bruta, que tenta adivinhar a senha. O tempo necessário para adivinhar a senha é calculado e exibido no final. 
Este código é apenas um exemplo didático e não deve ser usado para adivinhar senhas de forma ilegal.