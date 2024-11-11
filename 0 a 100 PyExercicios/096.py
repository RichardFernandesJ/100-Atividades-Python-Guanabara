def control_terrenos(largura, comprimento):
    area_terreno = largura * comprimento
    area_terreno = float(area_terreno)
    print(f"A área de um terreno {largura} x {comprimento} é de {area_terreno}m².")


largura = float(input("LARGURA (M): "))
comprimento = float(input("COMPRIMENTO (M): "))
control_terrenos(largura, comprimento)