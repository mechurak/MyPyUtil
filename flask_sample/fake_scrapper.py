import time


def get_jobs(word):
    print('Fake Scrapping...')
    time.sleep(2)
    return [
        {
            'title': 'title1',
            'company': 'company1',
            'location': 'location1',
            'link': f'https://www.somewhere.com/test1'
        },
        {
            'title': 'title2',
            'company': 'company2',
            'location': 'location2',
            'link': f'https://www.somewhere.com/test2'
        },
        {
            'title': 'title3',
            'company': 'company3',
            'location': 'location3',
            'link': f'https://www.somewhere.com/test3'
        }
    ]
