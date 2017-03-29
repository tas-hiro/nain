# coding:utf-8

import gspread, os, httplib2
from oauth2client.file import Storage
#from oauth2client.service_account import ServiceAccountCredentials
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

def conn(service=None):

    storage = Storage('./tokens')
    credentials = storage.get()
    http = httplib2.Http()
    http = credentials.authorize(http)
    credentials.refresh(http)
    gc = gspread.authorize(credentials)

    spreadsheet = gc.open_by_key('spread sheet key')
    base_wks = spreadsheet.worksheet('Base')
    domain_wks = spreadsheet.worksheet('CustomerDomain')
    if service is None:
        service_wks = None
    else:
        service_wks = spreadsheet.worksheet(service)
    return [base_wks, domain_wks, service_wks]

def update_worksheet(worksheet, update_lists, range):
    # range = 'A2:C'
    cell_range = range + str(len(update_lists)+100)
    cell_list = worksheet.range(cell_range)
    cell_number = 0
    for j, row in enumerate(update_lists, 1):
        for k, value in enumerate(row, 1):
            cell_list[cell_number].value = value
            cell_number += 1
    worksheet.update_cells(cell_list)


if __name__ == '__main__':
    base, domain, service = conn()
