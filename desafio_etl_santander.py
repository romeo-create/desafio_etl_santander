# Como o API caiu, estou criando os usúarios direto no vscode. 

# ---- EXTRACT (extração) ---- # 

# Agora cada usuário é um dicionário separado por chaves { } dentro da lista [ ]
users = [
    { 'id' : 1 , 'name' : 'Marcelo Ribeiro' , 'news' : [] },
    { 'id' : 2 , 'name' : 'Ryane Silva' , 'news' : [] },
    { "id" : 3 , 'name' : 'Ana Monteiro' , 'news' : [] },
    { 'id' : 4 , 'name' : 'Lucas Mendonça' , 'news' : [] }
]

# ---- TRANSFORM (tranformação) ---- # 

 # aqui vou criar uma mensagem com assunto bancário em loop diferente para cada usúario. 

for user in users:
    if user['id'] == 1:
        # Assunto investimentos / Educação Finaceira
        mensagem = f" Oi, {user["name"]} Sabia que deixar dinheiro parado na conta rende menos? Conheça nossas opções de CDB com liquidez diária."
         
    elif user ['id'] == 2:
        # Assunto Segurança / Prevenção de Fraudes 
        mensagem = f" Atenção, {user["name"]}! O banco nunca solicita sua senha ou token por ligação. Mantenha sua conta segura e não compartilhe seus dados."

    elif user ['id'] == 3:
        # Assunto Crédito / Financiamento e Empréstimo 
        mensagem = f" Olá, {user["name"]} Temos uma linha de Crédito pré-aprovada esperando por você, para tirar aquele projeto do papel, confira as taxas no app."

    elif user ['id'] == 4:
        # Assunto Relacionamento / Aumento de limite no cartão
        mensagem = f" Parabéns, {user["name"]}! Pelo seu histórico de pagamento, analisamos sua conta e liberamos um novo limite para o seu cartão de crédito."
         
    # Adicionar a mensagem  específica na lista de 'news' do usúario correspondente.
    user['news'].append(mensagem)

# ---- LOAD ---- #

# Não tem API para enviar, então vou apenas executar o programa.

print(" ---- FLUXO DE ETL CONCLUÍDO COM SUCESSO! ----")

for user in users:
    print(f"\nID: {user['id']} |  Nome: {user['name']}")
    print(f"Mensagem: {user['news'] [0]}")
    print("\n --------------------------------------------")