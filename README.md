# Web Page Fetcher

This is a command-line program written in Python that fetches web pages and saves them to disk for later retrieval and browsing. It also records metadata about the fetched web pages including the date and time of the last fetch, the number of links on the page, and the number of images on the page.

## Usage

1. Clone the repository:

`git clone https://github.com/rahul-anand1/Webpage_Fetcher.git`

2. Navigate to the project directory:

`cd Webpage_Fetcher`


3. Install dependencies:

`pip install -r Requirements.txt`


4. Run the script with URLs as command-line arguments:

`python fetch.py https://www.google.com https://yahoo.com`


## Docker Setup

Alternatively, you can use Docker to run the script in a container:

1. Build the Docker image:

`docker build -t web-page-fetcher .`


2. Run the Docker container with URLs as command-line arguments:

`docker run fetch-webpages python3 main.py http://www.google.com https://yahoo.com`


## Output

- The HTML content of each fetched web page will be saved to separate files in the result directory.
- Metadata about each fetched web page, including the date and time of the last fetch, the number of links, and the number of images, will be printed to the console.


