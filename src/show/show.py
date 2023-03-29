from datetime import datetime

def sortList(method,list,timestamp):

    start = timestamp(datetime.now())
    print('# Comprimento: {}'.format(len(list)))
    print('# Inicio: {}'.format(datetime.now()))

    method(list)

    end = timestamp(datetime.now())
    print('# Fim: {}'.format(datetime.now()))
    print('# Tempo: {} ms'.format(end - start))