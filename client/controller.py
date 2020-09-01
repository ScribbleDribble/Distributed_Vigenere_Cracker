import dispy, socket, argparse
import crack
from quadgram_analysis import QuadgramAnalyzer

STAGES = ["CAESAR_GROUPS", "FREQUENCY_ANALYSIS", "KEY_GENERATION", "KEY_EVALUATION"]

def delegate(func_name, *args):
    """ switches client procedure to execute """
    # get function with given name (this function would've been sent with
    # 'dispy_job_depends' and available in global scope)
    func = globals()[func_name]
    return func(*args)


def run_jobs():
    machine1_data = []
    machine2_data = []
    for i, stage in enumerate(STAGES):

        # first two stages to be executed by one machine
        # each stage is a dependency for the next one - must wait until execution has finished

        if stage == "CAESAR_GROUPS":
            job = handle_caesar_groups()
            cluster.wait()
            machine1_data = job()

        elif stage == "FREQUENCY_ANALYSIS":
            job = handle_frequency_analysis(machine1_data)
            cluster.wait()

            machine1_data = job().copy()
            machine2_data = job().copy()

            machine1_data[0] = machine1_data[0][2:]
            machine2_data[0] = machine2_data[0][:2]

        elif stage == "KEY_GENERATION":
            job, job2 = handle_key_generation(machine1_data, machine2_data)
            cluster.wait()

            machine1_data = job()
            machine2_data = job2()

        elif stage == "KEY_EVALUATION":
            job, job2 = handle_key_evaluation(machine1_data, machine2_data)
            cluster.wait()
            print(job(), job2())

def handle_frequency_analysis(data):
    func = crack.frequency_analyzer
    job = cluster.submit(func.__name__, args.key_length, data,
                         dispy_job_depends=[func, crack.decrypt_unknown_key])

    return job


def handle_caesar_groups():
    func = crack.caesar_groups
    job = cluster.submit(func.__name__, args.encrypted_message, args.key_length, dispy_job_depends=[func])
    return job


def handle_key_generation(data, data2):
    func = crack.generate_keys
    job = cluster.submit(func.__name__, data, dispy_job_depends=[func])
    job2 = cluster.submit(func.__name__, data2, dispy_job_depends=[func])

    return job, job2


def handle_key_evaluation(data, data2):
    func = crack.evaluate_keys
    q = QuadgramAnalyzer()
    job = cluster.submit(func.__name__,q, args.encrypted_message, data,
                         dispy_job_depends=[func, crack.sort_score, crack.decrypt])
    job2 = cluster.submit(func.__name__, q, args.encrypted_message, data2,
                          dispy_job_depends=[func, crack.sort_score, crack.decrypt])

    return job, job2


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("encrypted_message", type=str, help="The message you want to decrypt")
    parser.add_argument("key_length", type=int, help="length of the key")
    args = parser.parse_args()

    # fetch IP address of the client
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.connect(("8.8.8.8", 80))

    cluster = dispy.JobCluster(delegate, ip_addr="192.168.0.142", nodes="192.168.0.*", depends=['quadgram_analysis.py', QuadgramAnalyzer])
    import time
    start_time = time.time()
    run_jobs()
    print(f"--- {time.time() - start_time} seconds ---")

    cluster.print_status()
    cluster.close()

