import uuid
import os
import tarfile
import docker

def copy_to(src, container):
    cwd = os.getcwd()
    src = cwd + "/" +  src


    os.chdir(os.path.dirname(src))
    srcname = os.path.basename(src)
    tar = tarfile.open(src + '.tar', mode='w')

    try:
        tar.add(srcname)
    finally:
        tar.close()

    data = open(src + '.tar', 'rb').read()
    container.put_archive(os.path.dirname("/test.py"), data)

def createContainer():       
    try:
        client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

        container_id = uuid.uuid4()
        container = client.containers.create("pyimage:latest", command=None, environment={"id": f"{container_id}"}, name=container_id)

        copy_to("b.py", container)

        container.start()
        container.wait()
        
        logs = container.logs()
        print(logs)

        container.kill()

        return logs
    except Exception as e:
        print(e)


