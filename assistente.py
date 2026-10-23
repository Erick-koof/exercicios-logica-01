print('Olá, eu sou a sua assistente, Kappi. O que deseja fazer hoje?')

comando = input('Digite um comando: ')

match comando:
    case 'oi' | 'olá':
        print('Oi, como vai você')
    case 'tchau' | 'sair' | 'exit':
        print('Tchau, foi bom conversar com você')
    case 'piada':
        print('Sabe qual é o padroeiro das pessoas que trabalham com TI? O São Login')
    case 'clima' | 'previsão do tempo':
        print('Ta Muiito quente!! Deve ter passado de 40°C')   
    case _:
        print('Desculpe, não entendi o comando.')