# -*- coding: utf-8 -*-
import gspread, sys, os, csv, datetime, subprocess
from oauth2client.service_account import ServiceAccountCredentials
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)) + '/../lib')
import spread_sheet

def get_contract_information():
    cmd = 'perl DB/get_customer_contract_info.pl'
    ret = subprocess.check_output(cmd.split(' ')).split('\n')
    customer_list = []
    for line in ret:
        value_line = []
        for value in line.split('\t'):
            value_line.append(value.decode('utf-8'))
        customer_list.append(value_line)
    del customer_list[-1]
    return customer_list

if __name__ == '__main__':
    base_wks, domain_wks, service_wks = spread_sheet.conn()
    customer_list = get_contract_information()
    spread_sheet.update_worksheet(base_wks, customer_list, 'A1:T')
