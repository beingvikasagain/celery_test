import time

from celery import Task, shared_task, states


class CeleryTask(Task):
    name="main.tasks.task_check"

@shared_task(bind=True, name="main.tasks.task_check")
def task_check(self,myname):
    # self.update_state(state=states.RECEIVED, meta={"key":"value"})
    time.sleep(50)
    for i in range(10):
        print(i)
    print("Done")
    return "Tested Okay"