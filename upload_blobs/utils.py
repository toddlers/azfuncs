def parse_conn_string(storage_connection_string):
    conn = storage_connection_string.split(';')
    for l in conn:
        ss = l.split('=',1)
        if len(ss) != 2:
            continue
        if ss[0] == 'AccountName':
           storage_account = ss[1] 
        if ss[0] == 'AccountKey':
           storage_key = ss[1]
    return storage_account, storage_key