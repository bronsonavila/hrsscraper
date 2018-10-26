#! /usr/bin/env python3

import os
import requests
import bs4

# Begin with the first URL in the HRS directory:
url = 'https://www.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042F/01-USCON/USCON_0001-0001.htm'

# Create "/data" directory, and set it to be the current working directory:
os.makedirs('data', exist_ok=True)
projectDataPath = os.getcwd() + '/data/'    # Keep ending slash (see line 51)
os.chdir(projectDataPath)


def setNextPath(soup, cssSelector):
    # Three pages in the HRS directory contain broken links. The following
    # conditional check will set "nextPath" to the appropriate path:
    if fileName == 'Vol05_Ch0261-0319/HRS0279A/HRS_0279A-0009.htm':
        return '/hrscurrent/Vol05_Ch0261-0319/HRS0279D/HRS_0279D-.htm'
    elif fileName == 'Vol06_Ch0321-0344/HRS0344/HRS_0344-0004.htm':
        return '/hrscurrent/Vol07_Ch0346-0398/HRS0346/HRS_0346-.htm'
    elif fileName == 'Vol11_Ch0476-0490/HRS0489P/HRS_0489P-.htm':
        return '/hrscurrent/Vol11_Ch0476-0490/HRS0489P/HRS_0489P-0001.htm'
    else:
        return soup.select(cssSelector)[0].a['href']


# Scraping will terminate when "taskComplete" set to True:
taskComplete = False

while not taskComplete:
    # Request the first statute in the HRS:
    response = requests.get(url)

    # Raise an exception if a problem occurs after submitting request:
    response.raise_for_status()

    # Set file destination path (e.g., '/Vol01_Ch0001-0042F/01-USCON/USCON_0001-0001.htm'):
    fileName = response.url.split(
        'https://www.capitol.hawaii.gov/hrscurrent/')[1]

    # Parse HTTP response, convert <div class="WordSection1"> to string, and
    # remove carriage returns and non-breaking space characters:
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    htmlContent = str(soup.select('.WordSection1')[0]).replace(
        '\r\n', ' ').replace('\xa0', '')

    # Make directory and save body of HTML to new file:
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(projectDataPath + fileName, 'w') as file:
        file.write(htmlContent)
        print('Downloaded: ' + fileName)

    try:
        # Extract path for next statute in the HRS (e.g., '/hrscurrent/Vol01_Ch0001-0042F/01-USCON/USCON_0001-0002.htm').
        # Throws an exception if the given CSS selector is not found:
        nextPath = setNextPath(soup, 'center > table > tr > td:nth-of-type(3)')
        url = 'https://www.capitol.hawaii.gov' + nextPath
    except:
        # End the process when there is no longer a valid "nextPath" to access:
        taskComplete = True
        print('Done')
