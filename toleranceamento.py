from time import sleep
import math


def main_program():
    print('''[0] - Fechar Programa.
[1] - Consulta Geral - SR-DQ-001
[2] - Medir Tolerâncias - SR-DQ-001
[3] - Tubo Estruturado Frio "ISO EN 10219-2" - Quadrado e Rectangular
[4] - Erro Admissível Fita Métrica''')


def septit(msg):
    print('-=' * 29)
    print(msg)
    print('-=' * 29)


separador = '-=' * 29
sr_dq_001 = ('''[00] - Menu Principal
[01] - Dimensões Lineares, excepto cantos quebrados "ISO 2768-1"
[02] - Cantos Quebrados “ISO 2768-1”
[03] - Dimensões Angulares “ISO 2768-1”
[04] - Rectitude, Planeza e Paralelismo “ISO 2768-2”
[05] - Perpendicularidade “ISO 2768-2”
[06] - Simetria “ISO 2768-2”
[07] - Batimento Circular “ISO 2768-2”
[08] - Construções Soldadas Dimensões lineares “ISO 13920”
[09] - Construções soldadas Dimensões angulares “ISO 13920”
[10] - Construções Soldadas Rectitude, Planeza e Paralelismo “ISO 13920”''')


septit('\033[1mTolerânciamento\033[m')

try:
    while True:
        main_program()

        print(separador)
        main_menu = int(input('Insira a sua opção: '))
        print(separador)

        if main_menu == 0:
            break
        elif main_menu == 1:
            while True:
                sleep(1)
                print(sr_dq_001)
                septit('Insira o número do tipo de tolerância que pretende saber: ')
                user_input = int(input('> '))

                try:
                    if user_input == 0:
                        break

                    elif user_input == 1:
                        septit('[01] - Dimensões Lineares, excepto cantos quebrados "ISO 2768-1"')
                        dimensao_nominal = float(input('Quantifique: '))
                        if 0 < dimensao_nominal <= 6:
                            septit('± 0,1mm')
                        elif 6 < dimensao_nominal <= 30:
                            septit('± 0,2mm')
                        elif 30 < dimensao_nominal <= 120:
                            septit('± 0,3mm')
                        elif 120 < dimensao_nominal <= 400:
                            septit('± 0,5mm')
                        elif 400 < dimensao_nominal <= 1000:
                            septit('± 0,8mm')
                        elif 1000 < dimensao_nominal <= 2000:
                            septit('± 1,2mm')
                        elif 2000 < dimensao_nominal <= 4000:
                            septit('± 2mm')
                        else:
                            septit('<<< Min = 0,5mm | Max = 4000mm >>>')

                    elif user_input == 2:
                        septit('[02] - Cantos Quebrados “ISO 2768-1”')
                        dimensao_nominal = float(input('Quantifique: '))
                        if 0 < dimensao_nominal <= 3:
                            septit('± 0,2mm')
                        elif 3 < dimensao_nominal <= 6:
                            septit('± 0,5mm')
                        elif 6 < dimensao_nominal:
                            septit('± 1mm')
                        else:
                            septit('<<< Min = 0,5mm | Max = ∞ >>>')

                    elif user_input == 3:
                        septit('[03] - Dimensões Angulares “ISO 2768-1”')
                        dimensao_nominal = float(input('Quantifique: '))
                        if 0 < dimensao_nominal <= 10:
                            septit('± 1º')
                        elif 10 < dimensao_nominal <= 50:
                            septit("± 30'")
                        elif 50 < dimensao_nominal <= 120:
                            septit("± 20'")
                        elif 120 < dimensao_nominal <= 400:
                            septit("± 10'")
                        elif 400 < dimensao_nominal:
                            septit("± 5'")
                        else:
                            septit('<<< Min = 0,01mm | Max = ∞ >>>')

                    elif user_input == 4:
                        septit('[04] - Rectitude, Planeza e Paralelismo “ISO 2768-2”')
                        dimensao_nominal = float(input('Quantifique: '))
                        if 0 < dimensao_nominal <= 10:
                            septit('± 0,05mm')
                        elif 10 < dimensao_nominal <= 30:
                            septit("± 0,1mm")
                        elif 30 < dimensao_nominal <= 100:
                            septit("± 0,2mm")
                        elif 100 < dimensao_nominal <= 300:
                            septit("± 0,4mm")
                        elif 300 < dimensao_nominal <= 1000:
                            septit("± 0,6mm")
                        elif 1000 < dimensao_nominal <= 3000:
                            septit("± 0,8mm")
                        else:
                            septit('<<< Min = 0,01mm | Max = 3000mm >>>')

                    elif user_input == 5:
                        septit('[05] - Perpendicularidade “ISO 2768-2”')
                        dimensao_nominal = float(input('Quantifique: '))
                        if 0 < dimensao_nominal <= 100:
                            septit('± 0,4mm')
                        elif 100 < dimensao_nominal <= 300:
                            septit("± 0,6mm")
                        elif 300 < dimensao_nominal <= 1000:
                            septit("± 0,8mm")
                        elif 1000 < dimensao_nominal <= 3000:
                            septit("± 1mm")
                        else:
                            septit('<<< Min = 0,01mm | Max = 3000mm >>>')

                    elif user_input == 6:
                        septit('[06] - Simetria “ISO 2768-2”')
                        dimensao_nominal = float(input('Quantifique: '))
                        if 0 < dimensao_nominal <= 300:
                            septit('± 0,6mm')
                        elif 300 < dimensao_nominal <= 1000:
                            septit('± 0,8mm')
                        elif 1000 < dimensao_nominal <= 3000:
                            septit('± 1mm')
                        else:
                            septit('<<< Min = 0,01mm | Max = 3000mm >>>')

                    elif user_input == 7:
                        septit('[07] - Batimento Circular “ISO 2768-2”')
                        septit('0,2mm')

                    elif user_input == 8:
                        septit('[08] - Construções Soldadas Dimensões lineares “ISO 13920”')
                        dimensao_nominal = float(input('Quantifique: '))
                        if 0 < dimensao_nominal <= 30:
                            septit('± 1mm')
                        elif 30 < dimensao_nominal <= 1000:
                            septit('± 2mm')
                        elif 120 < dimensao_nominal <= 400:
                            septit('± 2mm')
                        elif 1000 < dimensao_nominal <= 2000:
                            septit('± 3mm')
                        elif 2000 < dimensao_nominal <= 4000:
                            septit('± 4mm')
                        elif 4000 < dimensao_nominal <= 8000:
                            septit('± 5mm')
                        elif 8000 < dimensao_nominal <= 12000:
                            septit('± 6mm')
                        elif 12000 < dimensao_nominal <= 16000:
                            septit('± 7mm')
                        elif 16000 < dimensao_nominal <= 20000:
                            septit('± 8mm')
                        elif dimensao_nominal > 20000:
                            septit('± 9mm')
                        else:
                            septit('<<< Min = 2mm | Max = ∞ >>>')

                    elif user_input == 9:
                        septit('[09] - Construções soldadas Dimensões angulares “ISO 13920”')
                        dimensao_nominal = float(input('Quantifique: '))
                        escolha_09 = int(input('\n[01] - Tolerâncias [graus e minutos] | [02] - Tolerâncias Calculadas e Arredondadas [mm/m]'))
                        if escolha_09 == 1:
                            if 0 < dimensao_nominal <= 400:
                                septit("± 45'")
                            elif 400 < dimensao_nominal <= 1000:
                                septit("± 15'")
                            elif dimensao_nominal > 1000:
                                septit("± 10'")
                            else:
                                septit('Min = 0,01mm | Max = ∞')
                        elif escolha_09 == 2:
                            if 0 < dimensao_nominal <= 400:
                                septit("± 13mm")
                            elif 400 < dimensao_nominal <= 1000:
                                septit("± 4,5mm")
                            elif dimensao_nominal > 1000:
                                septit("± 3mm")
                            else:
                                septit('<<< Min = 0,01mm | Max = ∞ >>>')

                    elif user_input == 10:
                        septit('[10] - Construções Soldadas Rectitude, Planeza e Paralelismo “ISO 13920”')
                        dimensao_nominal = float(input('Quantifique: '))
                        if 30 < dimensao_nominal <= 120:
                            septit('± 1mm')
                        elif 120 < dimensao_nominal <= 1000:
                            septit('± 1,5mm')
                        elif 1000 < dimensao_nominal <= 2000:
                            septit('± 2mm')
                        elif 2000 < dimensao_nominal <= 4000:
                            septit('± 3mm')
                        elif 4000 < dimensao_nominal <= 8000:
                            septit('± 4mm')
                        elif 8000 < dimensao_nominal <= 12000:
                            septit('± 5mm')
                        elif 12000 < dimensao_nominal <= 16000:
                            septit('± 6mm')
                        elif 16000 < dimensao_nominal <= 20000:
                            septit('± 7mm')
                        elif dimensao_nominal > 20000:
                            septit('± 8mm')
                        else:
                            septit('<<< Min = 30mm | Max = ∞ >>>')
                except ValueError:
                    septit('Opção Inválida.')
        elif main_menu == 2:
            while True:
                sleep(1)
                print(sr_dq_001)
                septit('Insira o número do tipo de tolerância que pretende saber: ')

                user_input = int(input('> '))
                if user_input == 0:
                    break

                elif user_input == 1:
                    septit('[01] - Dimensões Lineares, excepto cantos quebrados "ISO 2768-1"')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    empeno = float(input('Quantifique o empeno em [mm]: '))
                    if 0 < dimensao_nominal <= 6:
                        if empeno <= 0.1:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.1mm')
                    elif 6 < dimensao_nominal <= 30:
                        if empeno <= 0.2:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.2mm')
                    elif 30 < dimensao_nominal <= 120:
                        if empeno <= 0.3:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.3mm')
                    elif 120 < dimensao_nominal <= 400:
                        if empeno <= 0.5:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.5mm')
                    elif 400 < dimensao_nominal <= 1000:
                        if empeno <= 0.8:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.8mm')
                    elif 1000 < dimensao_nominal <= 2000:
                        if empeno <= 1.2:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 1.2mm')
                    elif 2000 < dimensao_nominal <= 4000:
                        if empeno <= 2:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 2mm')
                    else:
                        septit('<<< Min = 0,5mm | Max = 4000mm >>>')

                elif user_input == 2:
                    septit('[02] - Cantos Quebrados “ISO 2768-1”')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    empeno = float(input('Quantifique o empeno em [mm]: '))
                    if 0 < dimensao_nominal <= 3:
                        if empeno <= 0.2:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.2mm')
                    elif 3 < dimensao_nominal <= 6:
                        if empeno <= 0.5:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.5mm')
                    elif 6 < dimensao_nominal:
                        if empeno <= 1:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 1mm')
                    else:
                        septit('<<< Min = 0,5mm | Max = ∞ >>>')

                elif user_input == 3:
                    septit('[03] - Dimensões Angulares “ISO 2768-1”')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    empeno = float(input('Quantifique o empeno em minutos: '))
                    if 0 < dimensao_nominal <= 10:
                        if empeno <= 60:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f"Fora de Tolerância. Max/Min Admissivel = ± 60'")
                    elif 10 < dimensao_nominal <= 50:
                        if empeno <= 30:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f"Fora de Tolerância. Max/Min Admissivel = ± 30'")
                    elif 50 < dimensao_nominal <= 120:
                        if empeno <= 20:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f"Fora de Tolerância. Max/Min Admissivel = ± 20'")
                    elif 120 < dimensao_nominal <= 400:
                        if empeno <= 10:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f"Fora de Tolerância. Max/Min Admissivel = ± 10'")
                    elif 400 < dimensao_nominal:
                        if empeno <= 5:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f"Fora de Tolerância. Max/Min Admissivel = ± 5'")
                    else:
                        septit('<<< Min = 0,01mm | Max = ∞ >>>')

                elif user_input == 4:
                    septit('[04] - Rectitude, Planeza e Paralelismo “ISO 2768-2”')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    empeno = float(input('Quantifique o empeno [mm]: '))
                    if 0 < dimensao_nominal <= 10:
                        if empeno <= 0.05:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.05mm')
                    elif 10 < dimensao_nominal <= 30:
                        if empeno <= 0.1:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.1mm')
                    elif 30 < dimensao_nominal <= 100:
                        if empeno <= 0.2:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.2mm')
                    elif 100 < dimensao_nominal <= 300:
                        if empeno <= 0.4:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.4mm')
                    elif 300 < dimensao_nominal <= 1000:
                        if empeno <= 0.6:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.6mm')
                    elif 1000 < dimensao_nominal <= 3000:
                        if empeno <= 0.8:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.8mm')
                    else:
                        septit('<<< Min = 0,01mm | Max = 3000mm >>>')

                elif user_input == 5:
                    septit('[05] - Perpendicularidade “ISO 2768-2”')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    empeno = float(input('Quantifique o empeno [mm]: '))
                    if 0 < dimensao_nominal <= 100:
                        if empeno <= 0.4:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.4mm')
                    elif 100 < dimensao_nominal <= 300:
                        if empeno <= 0.6:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.6mm')
                    elif 300 < dimensao_nominal <= 1000:
                        if empeno <= 0.8:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.8mm')
                    elif 1000 < dimensao_nominal <= 3000:
                        if empeno <= 1:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 1mm')
                    else:
                        septit('<<< Min = 0,01mm | Max = 3000mm >>>')

                elif user_input == 6:
                    septit('[06] - Simetria “ISO 2768-2”')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    empeno = float(input('Quantifique o empeno [mm]: '))
                    if 0 < dimensao_nominal <= 300:
                        if empeno <= 0.6:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.6mm')
                    elif 300 < dimensao_nominal <= 1000:
                        if empeno <= 0.8:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 0.8mm')
                    elif 1000 < dimensao_nominal <= 3000:
                        if empeno <= 1:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 1mm')
                    else:
                        septit('<<< Min = 0,01mm | Max = 3000mm >>>')

                elif user_input == 7:
                    septit('[07] - Batimento Circular “ISO 2768-2”')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    empeno = float(input('Quantifique o empeno [mm]: '))
                    if empeno > 0.2:
                        septit('Fora de Tolerância.')

                elif user_input == 8:
                    septit('[08] - Construções Soldadas Dimensões lineares “ISO 13920”')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    empeno = float(input('Quantifique o empeno [mm]: '))
                    if 0 < dimensao_nominal <= 300:
                        if empeno <= 1:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 1mm')
                    elif 30 < dimensao_nominal <= 1000:
                        if empeno <= 2:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 2mm')
                    elif 120 < dimensao_nominal <= 400:
                        if empeno <= 2:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 2mm')
                    elif 1000 < dimensao_nominal <= 2000:
                        if empeno <= 3:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 3mm')
                    elif 2000 < dimensao_nominal <= 4000:
                        if empeno <= 4:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 4mm')
                    elif 4000 < dimensao_nominal <= 8000:
                        if empeno <= 5:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 5mm')
                    elif 8000 < dimensao_nominal <= 12000:
                        if empeno <= 6:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 6mm')
                    elif 12000 < dimensao_nominal <= 16000:
                        if empeno <= 7:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 7mm')
                    elif 16000 < dimensao_nominal <= 20000:
                        if empeno <= 8:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 8mm')
                    elif dimensao_nominal > 20000:
                        if empeno <= 9:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 9mm')
                    else:
                        septit('<<< Min = 2mm | Max = ∞ >>>')

                elif user_input == 9:
                    septit('[09] - Construções soldadas Dimensões angulares “ISO 13920”')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    escolha_09 = int(input('\n[01] - Tolerâncias [graus e minutos] | [02] - Tolerâncias Calculadas e Arredondadas [mm/m]'))
                    if escolha_09 == 1:
                        empeno = float(input('Quantifique o empeno em minutos: '))
                        if 0 < dimensao_nominal <= 400:
                            if empeno <= 45:
                                septit('Dentro de Tolerância.')
                            else:
                                septit(f'Fora de Tolerância. Max/Min Admissivel = ± 45')
                        elif 400 < dimensao_nominal <= 1000:
                            if empeno <= 15:
                                septit('Dentro de Tolerância.')
                            else:
                                septit(f'Fora de Tolerância. Max/Min Admissivel = ± 15')
                        elif dimensao_nominal > 1000:
                            if empeno <= 10:
                                septit('Dentro de Tolerância.')
                            else:
                                septit(f'Fora de Tolerância. Max/Min Admissivel = ± 10')
                        else:
                            septit('Min = 0,01mm | Max = ∞')
                    elif escolha_09 == 2:
                        empeno = float(input('Quantifique o empeno em [mm]: '))
                        if 0 < dimensao_nominal <= 400:
                            if empeno <= 13:
                                septit('Dentro de Tolerância.')
                            else:
                                septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 13mm')
                        elif 400 < dimensao_nominal <= 1000:
                            if empeno <= 4.5:
                                septit('Dentro de Tolerância.')
                            else:
                                septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 4,5mm')
                        elif dimensao_nominal > 1000:
                            if empeno <= 3:
                                septit('Dentro de Tolerância.')
                            else:
                                septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 3mm')
                        else:
                            septit('<<< Min = 0,01mm | Max = ∞ >>>')

                elif user_input == 10:
                    septit('[10] - Construções Soldadas Rectitude, Planeza e Paralelismo “ISO 13920”')
                    dimensao_nominal = float(input('Quantifique a dimensão da cota em [mm]: '))
                    empeno = float(input('Quantifique o empeno [mm]: '))
                    if 30 < dimensao_nominal <= 120:
                        if empeno <= 1:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 1mm')
                    elif 120 < dimensao_nominal <= 1000:
                        if empeno <= 1.5:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 1,5mm')
                    elif 1000 < dimensao_nominal <= 2000:
                        if empeno <= 2:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 2mm')
                    elif 2000 < dimensao_nominal <= 4000:
                        if empeno <= 3:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 3mm')
                    elif 4000 < dimensao_nominal <= 8000:
                        if empeno <= 4:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 4mm')
                    elif 8000 < dimensao_nominal <= 12000:
                        if empeno <= 5:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 5mm')
                    elif 12000 < dimensao_nominal <= 16000:
                        if empeno <= 6:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 6mm')
                    elif 16000 < dimensao_nominal <= 20000:
                        if empeno <= 7:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 7mm')
                    elif dimensao_nominal > 20000:
                        if empeno <= 8:
                            septit('Dentro de Tolerância.')
                        else:
                            septit(f'Fora de Tolerância. Tem {dimensao_nominal + empeno}mm. Max/Min Admissivel = ± 8mm')
                    else:
                        septit('<<< Min = 30mm | Max = ∞ >>>')

        elif main_menu == 3:
            while True:
                septit('[11] - Aço Estruturado Soldado a Frio "ISO EN 10219-2" - Quadrado e Rectangular')

                sleep(1)
                print('''[00] - Voltar Atrás.
[01] - Torcimento (V)
[02] - Retidão
[03] - Quadratura de lado
[04] - Concavidade - Convexidade
[05] - Espessura (T)''')

                septit('Insira o número do tipo de tolerância que pretende saber: ')

                escolha_11 = int(input('> '))

                if escolha_11 == 0:
                    break

                elif escolha_11 == 1:
                    septit('[01] - Torcimento (V)')
                    dimensao_nominal = float(input('\nComprimento [mm]: '))
                    twist = (dimensao_nominal / 2000) + 2
                    septit(f'2mm + 0.5mm/M comprimento.\nTolerância Máxima Admissível = ±{twist}mm')

                elif escolha_11 == 2:
                    septit('[02] - Retidão')
                    dimensao_nominal = float(input('\nComprimento [mm]: '))
                    straightness = (dimensao_nominal * 0.15) / 100
                    septit(f'0.15% do total do comprimento.\nTolerância Máxima Admissivel = ±{straightness}mm')

                elif escolha_11 == 3:
                    septit('[03] - Quadratura de lado')
                    dimensao_nominal = float(input('\nComprimento [mm]: '))
                    septit(f'Tolerância Máxima Admissível = 90º ± 1º ')

                elif escolha_11 == 4:
                    septit('[04] - Concavidade - Convexidade')
                    dimensao_nominal = float(input('\nQuantifique: '))
                    concavity = (dimensao_nominal * 0.8) / 100
                    print(separador)
                    print('Max 0,8% of a minimum of 0,5mm.')
                    if concavity < 0.5:
                        print(f'Tolerância Máxima Admissível = 0,5mm')
                        print(separador)
                    elif concavity > 0.5:
                        print(f'Tolerância Máxima Admissível = {concavity}')
                        print(separador)
                    else:
                        print('Valor Inválido.')
                        print(separador)

                elif escolha_11 == 5:
                    septit('[05] - Espessura (T)')
                    x = float(input('\nQuantifique a dimensão pretendida: [mm] '))
                    print(separador)
                    print('T <= 5mm: ± 10% | T > 5mm: 0,50mm')
                    if 0 < x <= 5:
                        septit(f'Tolerância Máxima Admissível = {(x * 10) / 100}')
                    elif x > 5:
                        septit(f'Tolerância Máxima Admissível = ± 0,50mm')
                    else:
                        septit('Valor Inválido.')
                else:
                    septit('Opção Inválida.')
        elif main_menu == 4:
            septit('[04] - Erro Admissível Fita Métrica')

            septit(f'{"No.":^4}{"Classe":<4}{"a(mm)":>10}{"b":>7}{"c(mm)":>14}')
            print(f'{"[01]":^4}{"I":>4}{"0,1":>10}{"0,1":>10}{"0,1":>12}')
            print(f'{"[02]":^4}{"II":>4}{"0,3":>10}{"0,2":>10}{"0,2":>12}')
            print(f'{"[03]":^4}{"III":>4}{"0,6":>10}{"0,4":>10}{"0,3":>12}')
            print(f'{"[04]":^4}{"D":>4}{"1,5":>10}{"0":>10}{"0":>12}')
            print(f'{"[05]":^4}{"S":>4}{"1,5":>10}{"0":>10}{"0":>12}')
            while True:
                print(separador)
                help_ema = int(input('INFORMAÇÕES? [0] NÃO | [1] SIM '))
                print(separador)
                if help_ema == 0:
                    break
                elif help_ema == 1:
                    septit('''O valor do ema, positivo ou negativo, em milímetros, entre duas marcações não consecutivas da escala é 
igual a a + (b x L) , onde L é o valor do comprimento, arredondado por excesso ao metro inteiro seguinte, e a e b 
são dados pelo tabela abaixo. Se um intervalo terminal for limitado por uma superfície, o valor do ema para qualquer 
distância que se inicie nesse ponto é acrescido do valor de c .''')
                else:
                    print('Opção Inválida.')
            classe = int(input('Insira a classe pretendida:'))
            comprimento = float(input('Quantifique a distância a medir em Metro: '))
            print(separador)
            c = int(input('[00] - Intervalo Não Limitado\n[01] - Intervalo Limitado\nIndique:'))
            print(separador)
            if classe == 1:
                if c == 0:
                    septit(f'Erro Máximo Admíssivel = {0.1 + (0.1 * math.ceil(comprimento)):.2f}mm')
                elif c == 1:
                    septit(f'Erro Máximo Admíssivel = {0.1 + (0.1 * math.ceil(comprimento)) + 0.1:.2f}mm')
                else:
                    septit('Opção Inválida')
            elif classe == 2:
                if c == 0:
                    septit(f'Erro Máximo Admíssivel = {0.3 + (0.2 * math.ceil(comprimento)):.2f}mm')
                elif c == 1:
                    septit(f'Erro Máximo Admíssivel = {0.3 + (0.2 * math.ceil(comprimento)) + 0.2:.2f}mm')
                else:
                    septit('Opção Inválida')
            elif classe == 3:
                if c == 0:
                    septit(f'Erro Máximo Admíssivel = {0.6 + (0.4 * math.ceil(comprimento)):.2f}mm')
                elif c == 1:
                    septit(f'Erro Máximo Admíssivel = {0.6 + (0.4 * math.ceil(comprimento)) + 0.3:.2f}mm')
                else:
                    septit('Opção Inválida')
            elif classe == 4:
                if c == 0:
                    septit(f'Erro Máximo Admíssivel = {1.5 + (0 * math.ceil(comprimento)):.2f}mm')
                elif c == 1:
                    septit(f'Erro Máximo Admíssivel = {1.5 + (0 * math.ceil(comprimento)) + 0:.2f}mm')
                else:
                    septit('Opção Inválida')
            elif classe == 5:
                if c == 0:
                    septit(f'Erro Máximo Admíssivel = {1.5 + (0 * math.ceil(comprimento)):.2f}mm')
                elif c == 1:
                    septit(f'Erro Máximo Admíssivel = {1.5 + (0 * math.ceil(comprimento)) + 0:.2f}mm')
                else:
                    septit('Opção Inválida')
            else:
                septit('Opção Inválida')
        else:
            septit('Opção Inválida')

    septit('<<< Programa Finalizado >>>')
except ValueError:
    septit('Opção Inválida - Reinicialize o programa novamente.')
