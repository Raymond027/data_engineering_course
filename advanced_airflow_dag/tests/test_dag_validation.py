from airflow.models import DagBag


def test_dag_loaded():

    dag_bag = DagBag()

    assert (
        len(dag_bag.import_errors) == 0
    ), f"DAG import errors found: {dag_bag.import_errors}"


def test_dag_exists():

    dag_bag = DagBag()

    dag = dag_bag.get_dag(
        "advanced_production_pipeline"
    )

    assert dag is not None


def test_task_count():

    dag_bag = DagBag()

    dag = dag_bag.get_dag(
        "advanced_production_pipeline"
    )

    assert len(dag.tasks) > 0