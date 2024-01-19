from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/AverageCal/cal-prefect.git",
        entrypoint="data_move.py:get_append_data",
    ).deploy(
        name="calvin-second-deployment",
        work_pool_name="data-writing",
        cron="0 10 * * *"
    )