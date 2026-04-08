import random

def get_level(prompt):
    while True:
        try:    
            question = int(input(prompt))        
            if question > 0 and (question == 1 or question == 2 or question == 3):
                return question        
        except ValueError:
            continue
    
def generate_integer(level):
    r = random
    
    if level == 1:
        num = r.randint(0, 9)
    elif level == 2:
        num = r.randint(10, 99)
    elif level == 3:
        num = r.randint(100, 999)
    else:
        raise ValueError
    
    return num
    
def main():
    ct = 0
    score = 0
    
    nivel = get_level('Level: ')
    
    for rodada in range (1, 10+1, 1):
        ct += 1
        
        x = generate_integer(nivel)
        y = generate_integer(nivel)
        
        for chance in range (1, 3+1, 1):
            try:   
                answer = int(input(f'{x} + {y} = '))
                
                if answer == (x + y):
                    score += 1  
                    break
                
                else:
                    print('EEE')
                    continue
                
                
            except ValueError:
                print('EEE')
                continue
            
        else:
            print(f'{x} + {y} = {x + y}')
            
    print(f'Socre: {score}')
    
    
if __name__ == '__main__':
    main()