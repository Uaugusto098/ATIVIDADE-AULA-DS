import statistics

def moda(value):
    return statistics.mode(value)
def mediana(value):
    return statistics.median(value)
def media(value):
    return statistics.mean(value)
def variance(value):
    return statistics.variance(value)
def desvio(value):
    return statistics.stdev(value)
def amplitude(value):
    value=max(value)-min(value)
    return value

