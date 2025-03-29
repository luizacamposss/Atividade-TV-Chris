"""
Faça um programa  que simule o funcionamento de uma TV, implemente as suas funções básicas, sabendo que, inicialmente a TV deve estar desligada, no canal 1 e volume 0. O programa deve permitir que o usuário escolha o que ele deseja fazer com a TV. Para isso o programa deve oferecer as seguintes opções:

1 - Ligar/Desligar: Se estiver ligada, desliga e se estiver desligada, liga
2 - Alterar Canal: Só altera o canal indicado se a TV estiver ligada e se o canal for válido (1, 3, 5, 7 e 11)
3 - Aumentar Volume: Incrementa o volume somente se a TV estiver ligada e até ao volume máximo (100)
4 - Diminuir Volume: Decrementa o volume somente se a TV estiver ligada e até ao volume mínimo (0)
5- Sair do simulador

O programa deve ser modularizado ou seja, para cada uma das opções ofertadas, deve ser implementada uma função.

Sempre que uma das opções for executada, o programa deve exibir o status atual da TV (ligada ou desligada, canal e volume)
"""

class TV:
    def __init__(self):
        self.estado = 0  
        self.canal = 1
        self.volume = 0
        self.canais_validos = [1, 3, 5, 7, 11]
    
    def mostrar_status(self):
        print("\nStatus da TV")
        print(f"Estado: {'Ligada' if self.estado == 1 else 'Desligada'}")
        if self.estado == 1:
            print(f"Canal: {self.canal}")
            print(f"Volume: {self.volume}")
        print()
    
    def ligar_desligar(self):
        self.estado = 1 - self.estado  # Alterna entre 0 e 1
        print(f"TV {'ligada' if self.estado == 1 else 'desligada'}")
        self.mostrar_status()
    
    def alterar_canal(self, novo_canal):
        if self.estado == 0:
            print("TV desligada. Não é possível alterar o canal.")
            return
        
        if novo_canal in self.canais_validos:
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal inválido. Canais disponíveis: 1, 3, 5, 7, 11")
        
        self.mostrar_status()
    
    def ajustar_volume(self, operacao):
        if self.estado == 0:
            print("TV desligada. Não é possível alterar o volume.")
            return
        
        if operacao == '+':
            if self.volume < 100:
                self.volume += 1
                print(f"Volume aumentado para {self.volume}")
            else:
                print("Volume já está no máximo (100)")
        elif operacao == '-':
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume diminuído para {self.volume}")
            else:
                print("Volume já está no mínimo (0)")
        
        self.mostrar_status()

def main():
    tv = TV()
    
    while True:
        print("\nMenu do Simulador de TV")
        print("1 - Ligar/Desligar")
        print("2 - Alterar Canal")
        print("3 - Aumentar Volume")
        print("4 - Diminuir Volume")
        print("5 - Sair do simulador")
        
        opcao = input("Escolha uma opção: ")
        
        match opcao:
            case '1':
                tv.ligar_desligar()
            
            case '2':
                if tv.estado == 1:
                    try:
                        canal = int(input("Digite o número do canal (1, 3, 5, 7, 11): "))
                        tv.alterar_canal(canal)
                    except ValueError:
                        print("Por favor, digite um número válido.")
                else:
                    print("TV desligada. Não é possível alterar o canal.")
            
            case '3':
                tv.ajustar_volume('+')
            
            case '4':
                tv.ajustar_volume('-')
            
            case '5':
                print("Encerrando o simulador de TV...")
                break
            
            case _:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

main()

