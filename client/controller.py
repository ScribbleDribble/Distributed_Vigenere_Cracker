import dispy, socket, argparse
import crack
import sys
from quadgram_analysis import QuadgramAnalizer


def delegate(func_name, *args):
    """ switches client procedure to execute """
    # get function with given name (this function would've been sent with
    # 'dispy_job_depends' and available in global scope)
    func = globals()[func_name]
    return func(*args)


def run_jobs():
    jobs = []
    for i in range(4):
        if i == 0:
            func = crack.caesar_groups
            job = cluster.submit(func.__name__, str(sys.argv[1]), 3, dispy_job_depends=[func])
            job.id = i

            if not job:
                print(f"Failed to create job {i}")
                continue

            jobs.append(job)

    # cluster.wait()
    for job in jobs:
        result = job()
        print(f"{result}")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("Encrypted_Message", type=str, help="The message you want to decrypt")
    parser.add_argument("Key_Length", type=int, help="length of the key")
    args = parser.parse_args()

    # fetch IP address of the client
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.connect(("8.8.8.8", 80))
    cluster = dispy.JobCluster(delegate, ip_addr="192.168.0.101", nodes="192.168.0.*", depends=[QuadgramAnalizer])

    run_jobs()

    cluster.print_status()
    cluster.close()

