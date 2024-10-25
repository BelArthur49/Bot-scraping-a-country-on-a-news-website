import requests
from bs4 import BeautifulSoup

def search_igihugu_for_burundi():
    base_url = 'https://www.igihe.com'
    search_url = f'{base_url}/spip.php?page=recherche&recherche=burundi'
    response = requests.get(search_url)

    if response.status_code != 200:
        print(f'Failed to retrieve search results: {response.status_code}')
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Search for any element containing the word 'Burundi'
    elements = soup.find_all(text=lambda text: text and 'burundi' in text.lower())

    if not elements:
        print("No elements found containing the word 'Burundi'.")
        return

    for element in elements:
        # Print the text of the element
        print(f'Text: {element.strip()}')

        # If the element is within a link, print the link as well
        link = element.find_parent('a')
        if link and 'href' in link.attrs:
            full_link = link['href']
            if not full_link.startswith('http'):
                full_link = base_url + full_link
            print(f'Link: {full_link}')
        print('---')

if __name__ == '__main__':
    search_igihugu_for_burundi()

'''import requests
from bs4 import BeautifulSoup

def search_igihugu_for_burundi():
    base_url = 'https://www.igihe.com'
    search_url = f'{base_url}/spip.php?page=recherche&recherche=burundi'
    response = requests.get(search_url)

    if response.status_code != 200:
        print(f'Failed to retrieve search results: {response.status_code}')
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Search through different tags
    elements = []
    tags_to_search = ['p', 'a', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']

    for tag in tags_to_search:
        elements.extend(soup.find_all(tag, text=lambda text: text and 'burundi' in text.lower()))

    if not elements:
        print("No elements found containing the word 'Burundi'.")
        return

    for element in elements:
        # Print the text of the element
        print(f'Text: {element.get_text(strip=True)}')

        # If the element is within a link, print the link as well
        link = element.find_parent('a')
        if link and 'href' in link.attrs:
            full_link = link['href']
            if not full_link.startswith('http'):
                full_link = base_url + full_link
            print(f'Link: {full_link}')
        print('---')

if __name__ == '__main__':
    search_igihugu_for_burundi()

'''
import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Failed to retrieve page: {response.status_code}')
        return None
    return response.content

def extract_articles(content):
    soup = BeautifulSoup(content, 'html.parser')
    articles = []

    tags_to_search = ['p', 'a', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    for tag in tags_to_search:
        elements = soup.find_all(tag, text=lambda text: text and 'burundi' in text.lower())
        for element in elements:
            text = element.get_text(strip=True)
            link = element.find_parent('a')
            if link and 'href' in link.attrs:
                full_link = link['href']
                if not full_link.startswith('http'):
                    full_link = base_url + full_link
                articles.append((text, full_link))
            else:
                articles.append((text, None))
    return articles

def search_igihugu_for_burundi():
    base_url = 'https://www.igihe.com'
    search_url_template = f'{base_url}/spip.php?page=recherche&recherche=burundi&debut_articles={{}}'
    articles = []
    start = 0

    while True:
        search_url = search_url_template.format(start)
        content = fetch_page_content(search_url)
        if content is None:
            break

        new_articles = extract_articles(content)
        if not new_articles:
            break

        articles.extend(new_articles)
        start += 10  # Update according to the site's pagination step

    if not articles:
        print("No elements found containing the word 'Burundi'.")
        return

    for text, link in articles:
        print(f'Text: {text}')
        if link:
            print(f'Link: {link}')
        print('---')

if __name__ == '__main__':
    search_igihugu_for_burundi() 