from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from ProductsApp.views import Uploading_csv
from circles import settings


def start():

    scheduler = BackgroundScheduler()
    scheduler.add_job(Uploading_csv, 'date', args=[], id='id1')
    scheduler.start()
    print("Scheduler started")