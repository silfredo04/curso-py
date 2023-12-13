vacaciones = False
diaDescanso = False


if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer')




vacaciones = False
diaDescanso = True


if not(vacaciones or diaDescanso):
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')