from multiprocessing.dummy import Pool as ThreadPool
import os

FILENAME = 'downList.txt'
THREADS = 8

def download_file(url):
    os.system('curl -O {}'.format(url))

if __name__ == '__main__':
    with open(FILENAME, 'r') as fh:
        links = [x.strip() for x in fh.readlines()]

    pool = ThreadPool(THREADS)
    _ = pool.map(download_file, links)

    pool.close()
    pool.join()
