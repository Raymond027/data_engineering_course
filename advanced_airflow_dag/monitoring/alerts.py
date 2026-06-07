import logging

logger = logging.getLogger(__name__)


def task_failure_alert(context):
    dag_id = context.get("dag").dag_id
    task_id = context.get("task_instance").task_id

    logger.error(
        f"""
        AIRFLOW FAILURE ALERT

        DAG: {dag_id}
        TASK: {task_id}

        Check Airflow logs immediately.
        """
    )