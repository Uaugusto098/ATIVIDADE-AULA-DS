import funcao 
Produtos={
    'celular':1200,
    'capa de celular':30,
    'carregador tipo c':50,
    'carregador padrão':20,
    'caixa de som':100,
    'caixinha de som':70,
    'fone de ouvido':60,
    'fone de ouvido sem fio':250,
    'microfone de mesa':170,
    'headset':400,
    'headset para PS4':200,
    'headset para xbox':180,
    'controle de PS4':250,
    'controle de xbox one':200,
    'video game ps4':2000,
    'video game ps4 slim':2500,
    'video game ps4 pro':4000,
    'video game ps5':3600,
    'video game ps5 pro':7000,
    'video game ps5 slim':3000,
    'video game ps5 digital':2800,
    'video game xbox one':2000,
    'video game xbox series x':3000,
    'video game series x pro':4000,
    'video game series s':3500,
    'controle de xbox 360':80,
    'controle de xbox series x':280,
    'jogos de ps4':250,
    'jogos de xbox one':200,
    'jogos de ps5':350,
    'jogos de xbox series s':300
}
listprice=list(Produtos.values())
for i,(chave,valor) in enumerate(Produtos.items()):
    print("\n",chave,'\n custando R$',valor)
print("\nEstatisticas dos Produtos")
print("Moda: ",funcao.moda(listprice))
print("Media: ",funcao.media(listprice))
print("Mediana: ",funcao.mediana(listprice))
print("Amplitude: ",funcao.amplitude(listprice))
print("Variance: ",funcao.variance(listprice))
print("Desvio padrão: ",funcao.desvio(listprice))




    