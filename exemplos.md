Exemplos de requisições:

- Exemplo 1:

# Input:

{
    "text": "Atenção! Sua conta foi bloqueada. Clique aqui para desbloquear."
}

# Output:

{
    "is_phishing": true,
    "confidence": 0.9288972678184793
}
____________________________________________________________________________________________________________________

- Exemplo 2:

# Input:

{
    "text": "Congratulations! You have won a prize of $1,000,000.00. Click here to claim it."
}

# Output:

{
    "is_phishing": true,
    "confidence": 0.9888708221426431
}
____________________________________________________________________________________________________________________

- Exemplo 3:

# Input:

{
    "text": "Olá, tudo bem? Estou enviando o relatório solicitado."
}

# Output:

{
    "is_phishing": false,
    "confidence": 0.5557892498713211
}

