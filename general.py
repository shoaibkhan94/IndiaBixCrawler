import os
import sys
import codecs

# Each website you crawl is a separate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# create_project_dir("The New Boston")

# Create queue and crawled files(if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.exists(queue):
        write_file(queue, base_url)
    if not os.path.exists(crawled):
        write_file(crawled, '')

# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
# create_data_files("The New Boston", "https://thenewboston.com")

# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        try:
            file.write(data+'\n')
        except Exception as e:
            print('Error: ' + data + str(e))



# Delete the content of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

#Read a file and convert each line into a set item
def file_to_set(file_name):
    results=set()
    with open(file_name,'rt',encoding='utf-8') as f:
        try:
            for line in f:
                results.add(line.replace('\n',''))
        except Exception as e:
            print('New Error: ' + str(e))
              
    return results

#Iterate set, each item in set will be a new line in a file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='ignore').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

