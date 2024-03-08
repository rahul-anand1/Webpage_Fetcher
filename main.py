""" Coding Take Home Test """
import requests
import sys
import os
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import shutil

def requesting_webpage(url):
    """
    Function to request the webpage for fetching the information in the page.
    
    Inputs:
        * url: URL of the page
    Returns:
        The text of the page as a response
    """
    try:
        response = requests.get(url)
        return response.text
    except Exception as ex:
        print("Error in fetching {} url.".format(url))


def save_page(content, url):
    """
    Function to save the content as text of the webpage in a file.
    
    Inputs:
        * content: The content of the webpage
        * url: URL of the page
    Returns:
        File name
    """
    filename = url.split("//")[-1].replace("/", "_") + ".html"
    if not os.path.exists(os.path.join("result", filename[:-5])):
        os.makedirs(os.path.join("result", filename[:-5]))
    with open(os.path.join("result", filename[:-5], filename), 'w') as filewrite:
        filewrite.write(content)
    return filename

def download_assets(html_content, url):
    """
    Function to save all the content of the webpage in a file.
    
    Inputs:
        * content: The content of the webpage
        * url: URL of the page
    Returns:
        None
    """
    filename = url.split("//")[-1].replace("/", "_") + ".html"
    if not os.path.exists(os.path.join("result", filename[:-5])):
        os.makedirs(os.path.join("result", filename[:-5]))
    local_dir = os.path.join("result", filename[:-5])
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup.find_all(['img', 'link', 'script']):
        if tag.has_attr('src'):
            asset_url = urljoin(url, tag['src'])
            asset_file_name = os.path.basename(asset_url)
            asset_local_path = os.path.join(local_dir, asset_file_name)
            try:
                asset_response = requests.get(asset_url, stream=True)
                asset_response.raise_for_status()
                with open(asset_local_path, 'wb') as asset_file:
                    shutil.copyfileobj(asset_response.raw, asset_file)
                print(f"Downloaded asset: {asset_url}")
            except Exception as e:
                print(f"Error downloading asset {asset_url}: {e}")

def main():
    urls = sys.argv[1:]
    if not os.path.exists("result"):
        os.makedirs("result")
    for item in urls:
        resp = requesting_webpage(item)
        if resp:
            soup = BeautifulSoup(resp, 'html.parser')
            file_name = save_page(resp, item)
            download_assets(resp, item)
            print(" ==== Metadata ==== ")
            print("URL: ", item)
            print("File Name: ", file_name)
            print("Fetched Time: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("Number of links: ", str(len(soup.find_all("a"))))
            print("Number of images: ", str(len(soup.find_all("img"))))
