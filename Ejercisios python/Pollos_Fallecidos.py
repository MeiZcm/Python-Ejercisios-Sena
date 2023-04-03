def tasa_mortalidad(pollos_inicio, pollos_fallecidos):

    tasa=(pollos_fallecidos/pollos_inicio)*100
    print(tasa)
    return tasa
    

tasa_mortalidad(1000, 20)
