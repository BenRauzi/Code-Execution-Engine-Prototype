import uuid, os, tarfile, docker
import threading
import time
from requests.exceptions import ReadTimeout


def load_file(src, container):
    cwd = os.getcwd()
    src = cwd + "/temp/" + src

    os.chdir(os.path.dirname(src))
    srcname = os.path.basename(src)
    tar = tarfile.open(src + '.tar', mode='w')

    try:
        tar.add(srcname)
    finally:
        tar.close()

    data = open(src + '.tar', 'rb').read()
    container.put_archive("/", data)

    os.chdir("..")

def create_container(container_id):       
    try:    
        client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

        container = client.containers.create("pyimage:latest", command=None, environment={"id": f"{container_id}"}, name=container_id)

        load_file(f"{container_id}.py", container)

        container.start()

        try:
            container.wait(timeout=1)

        except:    
            print("Timed out")
            container.kill()
        
        logs = container.logs(tail=500)

        container.remove() #tidy up container

        return logs
    except Exception as e:
        return e

def create_file(file):
    container_id = uuid.uuid4()

    file.save(f"temp/{container_id}.py")

    return container_id

def clean_temp(container_id):
    cwd = os.getcwd() 

    os.remove(f"{cwd}/temp/{container_id}.py")
    os.remove(f"{cwd}/temp/{container_id}.py.tar")

def run_container(file):
    container_id = create_file(file)

    result = create_container(container_id)

    clean_temp(container_id) #tidy up temp directory

    return result