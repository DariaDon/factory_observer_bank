from patterns import Factory, Client

if __name__ == '__main__':
    #Создаем фабрику
    factory = Factory()

    #Создаем новую заявку на кредит
    credit = factory.get('Credit')
    #Создаем клиента
    client = Client('Иванов Иван Иванович')
    #Присоединяем клиента к наблюдению за заявкой
    credit.attach(client)
    #Изменяем состояние заявки на "одобрено"
    credit.update('одобрено')
    #Отключаем клиента от наблюдения за заявкой
    credit.detach(client)

    #Создаем новую заявку на кредит
    credit = factory.get('Credit')
    #Создаем клиента
    client = Client('Петров Петр Петрович')
    #Присоединяем клиента к наблюдению за заявкой
    credit.attach(client)
    #Изменяем состояние заявки на "отказ"
    credit.update('отказ')
    #Отключаем клиента от наблюдения за заявкой
    credit.detach(client)
