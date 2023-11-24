import os
from argparse import ArgumentParser
import subprocess

def make_submisison_file_content(executable, arguments, output, error, log, cpus=1, gpus=0, memory=1000, disk="1G"):
    d = {
        'executable': executable,
        'arguments': arguments,
        'output': output,
        'error': error,
        'log': log,
        'request_cpus': cpus,
        'request_gpus': gpus,
        'request_memory': memory,
        'request_disk': disk
    }
    return d

def run_job(uid, bid, d):
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    job_file = os.path.join('tmp', uid)
    with open(job_file, 'w') as f:  
        for key, value in d.items():  
            f.write(f'{key} = {value}\n')
        f.write("queue")

    subprocess.run(["condor_submit_bid", str(bid), job_file]) 