import requests 
import os
from urllib.parse import urlparse

#  request header from the pdf from networks tab in devtools without the first line
header = """ """ 

# {"url of .vtt or .mp4 or .pdf ":"filename with no extentions"}
jobs = {
    'https://emergingtalent.contentcontroller.com/vault/bafa30bb-75df-42fa-bc9e-92a94ec21750/r/courses/...':'Student guide module 1',
    'https://emergingtalent.contentcontroller.com/vault/60b03f65-1fab-4158-a49a-c883297767e3/r/courses/...': 'module 2',
}


buf = header.splitlines()

header_dict = {} # formatting the header to a dict
for i in buf:
    i = i.split(" ", 1)
    i[0] = i[0].replace(":", "")
    i[0] = i[0].replace(" ","")
    header_dict[i[0]] = i[1]

# pan cert only if you have a proxy that requires a middle man cert. typically when you're behind a corporate VPN
pan_cert = "C:\\Users\\Tefo.Motaung\\Documents\\DevOps Repos\\custom-scripts\\certs\\ca-bundle.crt"
for url, filename in jobs.items():

    #  Use verify only if you have a proxy cert.
    r = requests.get(url=url,headers=header_dict,  verify=pan_cert)

    a = urlparse(url)
    a = os.path.basename(a.path)

    asdf , file_extension = os.path.splitext(a)
    filename = filename.replace(":","_")
    filename = filename.replace(" ","_")
    filename = filename.replace("/","_")

    #  path to where you want to save the files
    filename = f"C:/Users/Tefo.Motaung/Downloads/docs/{filename}{file_extension}"

    print(f'Downloaded {filename}')
    open(filename, 'wb').write(r.content)