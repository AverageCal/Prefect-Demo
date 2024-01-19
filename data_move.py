from prefect import flow, task

@task
def write_data(from_file='update.csv',to_file='data_updates.csv'):
    open_file = open(from_file,'r')
    data_update = open_file.read()
    open_main = open(to_file,'a')
    open_main.write(data_update)
    open_main.close()
    open_file.close()

@flow(retries=3,retry_delay_seconds=5,log_prints=True)
def get_append_data():
    write_data()


if __name__ == '__main__':
    get_append_data()