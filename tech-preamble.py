
import dask_jobqueue as dask_jobqueue
import dask.distributed as dask_distributed
import dask, os

dask.config.set(
    {
        'distributed.dashboard.link':
        "{JUPYTERHUB_BASE_URL}user/{JUPYTERHUB_USER}/{JUPYTERHUB_SERVER_NAME}/proxy/{port}/status"
    }
)
