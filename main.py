import random
import string

length = random.randint(4, 10)
def vocals_repetidos(last):
    vocals = ["A","E","I","O","U","a","e","i","o","u"]
    for i in range(10):
        if last == vocals[i]:
            return 0
    return 1
nick = ''
last = None
while len(nick) < length:
    letra = random.choice(string.ascii_letters)
    vocal_repe_last = vocals_repetidos(last)
    vocal_new = vocals_repetidos(letra)
    if not last:
        last = letra
        nick+=letra
        
    else:

        if letra != last:
            if vocal_repe_last == 1 and vocal_new == 0:
        
                last = letra
                nick+=letra
                
            elif vocal_repe_last == 0 and vocal_new == 1:
                    
                last = letra
                
                nick+=letra

print(nick)