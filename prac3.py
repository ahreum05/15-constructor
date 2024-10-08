from plusGame import PlusGame

pgame = PlusGame()

while True :
    pgame.input()
    print()
    pgame.output()
    print()
    pgame.is_continue()
    
    if not pgame.cont : 
        break

