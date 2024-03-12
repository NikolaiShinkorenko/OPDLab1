from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import load_workbook

def excel(jobs):
    df = pd.DataFrame({'Jobs': jobs})
    df.to_excel('./Lab1/python_jobs.xlsx')

    wb = load_workbook('Lab1/python_jobs.xlsx')
    ws = wb.active
    ws.column_dimensions['B'].width = 60
    wb.save('Lab1/python_jobs.xlsx')

def parse():
    proxies = {
        'http': 'http://proxy.omgtu:8080',
        'https': 'http://proxy.omgtu:8080'
    }
    url = 'https://hh.ru/vacancies/programmist_python?customDomain=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    page = requests.get(url, headers=headers)  # add proxies=proxies for OmSTU computers
    print(f"Page status: {page.status_code}")

    soup = BeautifulSoup(page.text, 'html.parser')
    block = soup.find_all('span', class_='serp-item__title serp-item__title-link')

    job_list = []
    for data in block:
        job_list.append(data.text)

    excel(job_list)

if __name__ == '__main__':
    parse()
