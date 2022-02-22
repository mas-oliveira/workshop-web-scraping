import requests
from bs4 import BeautifulSoup

def get_converted_amount(source_code, destination_code, amount):
    url = f"https://wise.com/gb/currency-converter/{source_code}-to-{destination_code}-rate?amount={amount}"

    request = requests.get(url)
    html_content = request.text
    soup = BeautifulSoup(html_content, 'html.parser')

    multiplier = soup.find("span", class_="text-success").text
    print(multiplier)
    #multiplier = multiplier.text #passar para a linha de cima

    converted_amount = float(multiplier) * amount

    return converted_amount