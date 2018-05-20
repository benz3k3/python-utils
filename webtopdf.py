import pdfkit
import os
import sys
from urllib import parse

homedir = os.environ['HOME']

path = homedir + "/books/"

def main():
    # print command line arguments
    for url in sys.argv[1:]:
        domain = "{0.netloc}".format(parse.urlsplit(url))
        url_parts = parse.urlparse(url)
        path_parts = url_parts[2].rpartition('/')
        urn =  path_parts[2]
        pdf = path + domain + "-" +  urn + ".pdf"
        print ("Generating pdf:"+pdf)
        pdfkit.from_url(url, pdf)
        
        

if __name__ == "__main__":
    main()
	
