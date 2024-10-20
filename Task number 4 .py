SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"

def draw_lim(filename, color1 = 1, color2 = 20):
    file = open('sequence.txt', 'r')
    list = []
    for number in file:
        if float(number) >= 0:
            list.append(float(number))
    file.close()
    bolshe5 = [(list[i]) for i in range(len(list)) if float(list[i]) > 5]
    menshe5 = [(list[i]) for i in range(len(list)) if float(list[i]) < 5]
    count = len(bolshe5) + len(menshe5)
    prozenti_b5 = (len(bolshe5) / count) * 100
    prozenti_m5 = (len(menshe5) / count) * 100
    bollshe5 = round(prozenti_b5,2) 
    mennshe5 = round(prozenti_m5,2) 
    
    
    
    print(f" {bollshe5}%  {SET_COLOR}{color1}m{'   ' * (len(bolshe5)//5) }{END} положительные числа больше 5")
    print(f" {mennshe5}%  {SET_COLOR}{color2}m{'   ' * (len(menshe5)//5) }{END} положительные числа меньше 5")


if __name__ == "__main__":
    print('Задание №4. Диаграммa процентного соотношения')
    draw_lim('sequence.txt')
    print()