score = input("Enter Score: ")
flscore = float(score)
if flscore < 0.0:
    print('error')
elif flscore > 1.0:
    print('error')
if flscore < 0.6:
    print('F')
elif flscore >= 0.9:
    print('A')
elif flscore >= 0.8:
    print('B')
elif flscore >= 0.7:
    print('C') 
