from kerberos_protocol import authentication_server, ticket_granting_server, service_server,get_current_time
from des import decrypt_des, encrypt_des
from datetime import datetime, timedelta




def client(client_data: dict) -> None:
    # C->AS: {c}.
    print('1.C->AS: {c} ')

    package = authentication_server(client_data)

    #
    tgt = package['TICKET'] = decrypt_des(package['TICKET'], C_KEY)
    c_tgs_key = package['KEY'] = decrypt_des(package['KEY'], C_KEY)

    # C->TGS: {TGT}K*AS_TGS, {Aut1} K*C_TGS, {ID}
    aut = {
        'c': client_data['username'] + ' ' + client_data['password'],
        't2': str(get_current_time())
    }
    package = {
        'TICKET': tgt,
        'KEY': c_tgs_key,
        'AUT': encrypt_des(aut, c_tgs_key),
        'ID': SS_ID
    }

    print('3.C->TGS: {TGT}K*AS_TGS, {Aut1} K*C_TGS, {ID} ')

    package = ticket_granting_server(package)

    #
    tgs = package['TICKET'] = decrypt_des(package['TICKET'], c_tgs_key)
    c_ss_key = package['KEY'] = decrypt_des(package['KEY'], c_tgs_key)

    # C->SS: {TGS}K*TGS_SS, {Aut2} K*C_SS
    aut = {
        'c': client_data['username'] + ' ' + client_data['password'],
        't4': str(get_current_time())
    }
    package = {
        'TICKET': tgs,
        'KEY': c_ss_key,
        'AUT': encrypt_des(aut, c_ss_key)
    }

    print('5.C->SS: {TGS}K*TGS_SS, {Aut2} K*C_SS ')

    package = service_server(package)

    #
    t4 = package['t4'] = decrypt_des(package['t4'], c_ss_key)

    # checking SS validation
    if datetime.strptime(aut['t4'], '%Y-%m-%d %H:%M:%S') + timedelta(hours=1) != datetime.strptime(t4, '%Y-%m-%d %H:%M:%S'):
        raise Exception('Client: Invalid Service Server!')
















C_KEY = 'c_key_222'
SS_ID = '0000'