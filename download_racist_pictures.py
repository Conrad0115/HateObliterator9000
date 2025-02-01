import requests
import csv 

racist_id = 0

if __name__ == '__main__':
    with open('images.csv') as racism:
        racism_dict = csv.DictReader(racism)
        for d in racism_dict:
            img = requests.get(d['Image_URL']).content
            with open(f'racistpics/racist_{racist_id}.jpg', 'wb') as handler:
                handler.write(img)
            racist_id += 1
