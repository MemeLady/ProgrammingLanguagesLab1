import time
from tqdm import tqdm
import sys
import requests

adress=sys.argv[1]

def download(url=''):
    try:
            response=requests.get(url=url, stream=True)
            file_size = int(response.headers.get('Content-length',0))
            default_filename = url.split("/")[-1]
            file_name=default_filename
            buffer_size = 1024
            progress = tqdm(response.iter_content(buffer_size), f"Downloading {file_name}", total=file_size, unit="B",
                    unit_scale=True, unit_divisor=1024)
            with open(file_name, 'wb') as file:
                for chunk in progress.iterable:
                        time.sleep(1)
                        file.write(chunk)
                        progress.update(len(chunk))
            return 'File download complete!'
    except Exception as _ex:
        return'Unable to upload file! Check URL.'

def main():
    print(download(url=adress))

if __name__ == '__main__':
    main()
