import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding='UTF-8')
    writer = csv.writer(file)
    writer.writerow(["company", "title", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values())[:-1])
    return