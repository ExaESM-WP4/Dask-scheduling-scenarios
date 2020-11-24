import subprocess

#
# note, the worker is always reported as running, even though a job is still pending
# ---> needs a fix in Dask jobqueue?
#
#def get_running_worker_jobs(cluster):
#    worker_jobs = [
#        cluster.workers[worker_id].job_id
#        for worker_id in cluster.workers.keys()
#        if (cluster.workers[worker_id].status == 'running')
#    ]
#    return sorted(worker_jobs)
#

def get_running_worker_jobs(cluster):
    """Fetch identifiers for running Dask worker jobs. Only a workaround, as this not necessarily reports the correct number of actually connected Dask workers."""
    worker_jobs = subprocess.check_output(
        ["squeue -u $USER | grep dask | grep R | awk '{ print $1 }'"],
        shell=True
    ).decode('ascii').strip('\n').split('\n')
    return sorted(worker_jobs)
