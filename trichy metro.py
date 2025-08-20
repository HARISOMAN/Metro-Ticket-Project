dic ={'samayapuram':1,'1_tollgate':2,'srirangam':3,'chinthamani':4,'cbs':5,'wb_road':6,'gandhi_market':7,'thillai_nagar':8,'tennur':9,'anna_nager':10,'padugai':11,'tmbs':12}
boarding=input('enter the starting station:').lower()
destination=input('enter the end station:').lower()
journey=int(input('enter 1.single journey 2.double journey:'))

if destination!=dic and boarding!=dic:
    print(f'{'-' * 30}')
    print(f'sorry your boarding or destination point  is not available')
    print(f'{'-' * 30}')
    if journey==1:
        t_price = abs( dic[destination] - dic[boarding])
        if t_price>=2 and t_price<4:
            n_price=2*8
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to single journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{n_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)
        elif t_price>=4 and t_price<6:
            n_price = 3 * 8
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to single journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{n_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)
        elif t_price>=6 and t_price<8:
            n_price = 4 * 8
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to single journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{n_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)
        elif t_price>8:
            n_price = 5 * 8
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to single journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{n_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)
        elif t_price<2:
            n_price = 8
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to single journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{n_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)

    #for the double journey option
    if journey==2:
        t_price = abs(dic[destination] - dic[boarding])
        n_price=2*8
        if t_price>=2 and t_price<4:
            a_price=n_price*2
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to double journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{a_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)
        elif t_price>=4 and t_price<6:
            a_price=n_price*3
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to double journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{a_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)
        elif t_price>=6 and t_price<8:
            a_price=n_price*4
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to double journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{a_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)
        elif t_price>8:
            a_price=n_price*5
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to double journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{a_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)
        elif t_price<2:
            a_price=n_price
            print(f'{'-' * 30}')
            print(f'Welcome to TRICHY METRO RAIL')
            print(f'you choose to double journey')
            print(f'your boarding point :{boarding}')
            print(f'your destination point:{destination}')
            print(f'fare:-{a_price}')
            print(f'Happy journey with owr TMR..')
            print('-' * 30)

    else:
        print(f'{'-' * 30}')
        print(f'sorry your journey option is not available')
        print(f'{'-' * 30}')

