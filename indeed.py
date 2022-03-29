import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT} '

def extract_indeed_pages() :
  result = requests.get(URL)
  soup = BeautifulSoup(result.text,"html.parser")
  pagination = soup.find("div",{"class":"pagination"})
  pages = pagination.find_all("a")
  spans = []
  for page in pages[:-1]:
    spans.append(int(page.string))
  max_page = spans[-1]
  return max_page

def extract_job(html):
  if html.select_one("div.companyLocation").string is None:
        location_string = "-"
  else:
        location_string = html.select_one("div.companyLocation").string
  job_span = html.find("h2",{"class":"jobTitle"}).find_all("span")
  for span in job_span:
        if span.string != "new":
          job_string = span.string
  company_string = html.find("span",{"class":"companyName"}).string
  job_id = html["data-jk"]
  return {"company" : company_string, "job" : job_string , "location" : location_string, "link" :  f'https://www.indeed.com/viewjob?jk={job_id}'}

def extract_indeed_jobs(last_page):
  jobs = []
  job_count = 0
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("a", {"class":"tapItem"})
    for jobcard in results:
      jobs.append(extract_job(jobcard))
      job_count = job_count+1
  print(f"Total JOB COUNT ... {job_count}")
  return jobs

