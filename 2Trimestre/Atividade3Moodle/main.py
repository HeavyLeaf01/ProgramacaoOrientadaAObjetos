from Modelos import *
import os
import time

if __name__ == "__main__":
    print("Bem-vindo ao RPG de Laboratório\n")
    
    print("[Sistema] Criando personagens...")
    
    heroi = Heroi("Super Python", 100.0, "Guido", "Comunidade")
    poderHeroi = Poder(25.0, 15.0)
    heroi.addPoder(poderHeroi)
    
    vilao = Vilao("Bugs O Terrível", 100.0, 99)
    poderVilao = Poder(20.0, 10.0)
    vilao.addPoder(poderVilao)
    
    print("-> Jogador 1: " + heroi.nome + " (Vida: " + str(heroi.life) + ")")
    print("-> Jogador 2: " + vilao.nome + " (Vida: " + str(vilao.life) + ")\n")
    
    rodada = 1
    
    while heroi.life > 0 and vilao.life > 0:
        print("--- RODADA " + str(rodada) + " ---")
        print(heroi.nome + " [Vida: " + str(heroi.life) + "] VS " + vilao.nome + " [Vida: " + str(vilao.life) + "]\n")
        
        print("Opções de Ação: [A] Atacar | [D] Defender | [N] Nada | [H] Usar Hack (Só Herói)")
        acao1 = input("Jogador 1 (" + heroi.nome + "), escolha sua ação: ")
        acao1 = acao1.strip().upper()
        
        if acao1 == "H":
            heroi.taDeHack()
            acao1 = "N"
            
        acao2 = input("Jogador 2 (" + vilao.nome + "), escolha sua ação: ")
        acao2 = acao2.strip().upper()
        
        print("\n[Sistema] Processando embate...")
        time.sleep(1)
        
        p1Poder = heroi.usarPoder()
        p2Poder = vilao.usarPoder()
        
        atk1 = p1Poder.nivelAtaque
        def1 = p1Poder.nivelDefesa
        atk2 = p2Poder.nivelAtaque
        def2 = p2Poder.nivelDefesa
        
        if acao1 == "A" and acao2 == "A":
            diff = atk1 - atk2
            if diff > 0:
                print("-> Combate de ataques! " + heroi.nome + " venceu a disputa e tirou " + str(diff) + " de vida de " + vilao.nome + ".")
                vilao.life -= diff
            elif diff < 0:
                print("-> Combate de ataques! " + vilao.nome + " venceu a disputa e tirou " + str(abs(diff)) + " de vida de " + heroi.nome + ".")
                heroi.life -= abs(diff)
            else:
                print("-> Os ataques colidiram e se anularam! Ninguém tomou dano. =)")
                
        elif acao1 == "A" and acao2 == "D":
            diff = atk1 - def2
            if diff > 0:
                print("-> O ataque de " + heroi.nome + " quebrou a defesa! " + vilao.nome + " perdeu " + str(diff) + " de vida. >=/")
                vilao.life -= diff
            else:
                print("-> " + vilao.nome + " defendeu o ataque de " + heroi.nome + " com sucesso! =)")
                
        elif acao1 == "D" and acao2 == "A":
            diff = atk2 - def1
            if diff > 0:
                print("-> O ataque de " + vilao.nome + " quebrou a defesa! " + heroi.nome + " perdeu " + str(diff) + " de vida. >=/")
                heroi.life -= diff
            else:
                print("-> " + heroi.nome + " defendeu o ataque de " + vilao.nome + " com sucesso! =)")
                
        elif acao1 == "D" and acao2 == "D":
            print("-> Ambos defenderam! Estresse da batalha faz ambos perderem 10% de vida. =(")
            heroi.life -= (heroi.life * 0.10)
            vilao.life -= (vilao.life * 0.10)
            
        elif acao1 == "D" and acao2 == "N":
            print("-> " + heroi.nome + " ficou na defensiva à toa e perdeu 20% de vida. " + vilao.nome + " descansou e ganhou 1 ponto de vida.")
            heroi.life -= (heroi.life * 0.20)
            vilao.life += 1.0
            
        elif acao1 == "N" and acao2 == "D":
            print("-> " + vilao.nome + " ficou na defensiva à toa e perdeu 20% de vida. " + heroi.nome + " descansou e ganhou 1 ponto de vida.")
            vilao.life -= (vilao.life * 0.20)
            heroi.life += 1.0
            
        elif acao1 == "A" and acao2 == "N":
            print("-> " + vilao.nome + " estava distraído! " + heroi.nome + " acertou em cheio, tirando " + str(atk1) + " de vida. =(")
            vilao.life -= atk1
            
        elif acao1 == "N" and acao2 == "A":
            print("-> " + heroi.nome + " estava distraído! " + vilao.nome + " acertou em cheio, tirando " + str(atk2) + " de vida. =(")
            heroi.life -= atk2
            
        elif acao1 == "N" and acao2 == "N":
            print("-> Os dois descansaram. Ambos ganham 1 ponto de vida. =)")
            heroi.life += 1.0
            vilao.life += 1.0
            
        else:
            print("Opção inválida! >=/ \n")

        input()
        os.system("cls" if os.name == "nt" else "clear")
        rodada += 1

    print("FIM DE BATALHA!\n")
    if heroi.life <= 0 and vilao.life <= 0:
        print("Empate! Os dois caíram exaustos no campo de batalha.")
    elif heroi.life > 0:
        print("VITÓRIA DO JOGADOR 1: " + heroi.nome + " salvou o dia! =)")
    else:
        print("VITÓRIA DO JOGADOR 2: " + vilao.nome + " espalhou o caos! >=/")