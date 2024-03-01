from des import encrypt_des, decrypt_des
from datetime import datetime, timedelta

DATABASE = {
    'dar': 'dar822'
}


PERIOD =  timedelta(hours=1)

def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def authentication_server(client_data: dict) -> dict:

    if client_data['username'] not in DATABASE:
        raise Exception('AS: There is no user with that name!')
    elif client_data['password'] != DATABASE[client_data['username']]:
        raise Exception('AS: Invalid password!')
    else:
        print('AUT SUCCESS!')

    # AS->C: {{TGT}K*AS_TGS, K*C_TGS}K*C,
    ticket_granting_ticket = {
        'c': client_data['username'] + ' ' + client_data['password'],
        'tgs': TGS_ID,
        't1': str(get_current_time()),
        'p1': str(PERIOD)
    }
    package = {
        'TICKET': encrypt_des(encrypt_des(ticket_granting_ticket, AS_TGS_KEY), C_KEY),
        'KEY': encrypt_des(C_TGS_KEY, C_KEY)
    }

    print('2.AS->C: {{TGT}K*AS_TGS, K*C_TGS}K*C ')

    return package


def ticket_granting_server(package: dict) -> dict:
    #
    tgt = package['TICKET'] = decrypt_des(package['TICKET'], AS_TGS_KEY)
    aut = package['AUT'] = decrypt_des(package['AUT'], package['KEY'])

    #
    if aut['c'] != tgt['c']:
        raise Exception('TGS: Invalid AUT block!')
    #
    hours, minutes, seconds = map(int, tgt['p1'].split(':'))
    time_delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    print(datetime.strptime(tgt['t1'], '%Y-%m-%d %H:%M:%S') + time_delta)
    if datetime.strptime(tgt['t1'], '%Y-%m-%d %H:%M:%S') + time_delta < datetime.now():
        raise Exception('TGS: Session time is up!')

    # TGS->C: {{TGS}K*TGS_SS,K*C_SS}K*C_TGS
    ticket_granting_service = {
        'c': tgt['c'],
        'ss': package['ID'],
        't3': str(get_current_time()),
        'p2': str(PERIOD)
    }
    package = {
        'TICKET': encrypt_des(encrypt_des(ticket_granting_service, TGS_SS_KEY), C_TGS_KEY),
        'KEY': encrypt_des(C_SS_KEY, C_TGS_KEY)
    }

    print('4.TGS->C: {{TGS}K*TGS_SS,K*C_SS}K*C_TGS ')

    return package


def service_server(package: dict) -> dict:
    #
    tgt = package['TICKET'] = decrypt_des(package['TICKET'], TGS_SS_KEY)
    aut = package['AUT'] = decrypt_des(package['AUT'], package['KEY'])

    #
    if aut['c'] != tgt['c']:
        raise Exception('SS: Invalid AUT block!')
    #
    hours, minutes, seconds = map(int, tgt['p2'].split(':'))
    time_delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    print(datetime.strptime(tgt['t3'], '%Y-%m-%d %H:%M:%S') + time_delta)
    if datetime.strptime(tgt['t3'], '%Y-%m-%d %H:%M:%S') + time_delta < datetime.now():
        raise Exception('TGS: Session time is up!')

    # SS->C: {t4+1}K*C_SS
    modified_aut = {
        't4': encrypt_des(str(datetime.strptime(tgt['t3'], '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)), package['KEY'])
    }

    print('6.SS->C: {t4+1}K*C_SS ')

    return modified_aut
























C_KEY = 'c_key_222'
C_TGS_KEY = 'c_tgs_key_222'
AS_TGS_KEY = 'as_tgs_key_222'
TGS_SS_KEY = 'tgs_ss_key_222'
C_SS_KEY = 'c_ss_key_222'


TGS_ID = '2222'
SS_ID = '0000'
