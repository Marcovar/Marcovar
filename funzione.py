def saluto_personalizzato(nome):
    saluto = f"Il tuo nome è: {nome} !"
    nome_modificato =(nome.upper())
    return saluto, nome_modificato

variabile_fuori_funzione = saluto_personalizzato("Marco")
print(variabile_fuori_funzione)
print(type(variabile_fuori_funzione))

print("proviamo a inserire una modifica")
