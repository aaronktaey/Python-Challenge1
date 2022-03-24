import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'

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
  location = html.select_one("div.companyLocation").string
  print(location)
  job_span = html.find("h2",{"class":"jobTitle"}).find_all("span")
  for span in job_span:
        if span.string != "new":
          job_string = span.string
  company_string = html.find("span",{"class":"companyName"}).string
  # return {"company" : company_string, "job" : job_string }    

def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text,"html.parser")
  results = soup.find_all("table", {"class":"jobCard_mainContent"})
  for jobcard in results:
    jobs.append(extract_job(jobcard))
  return jobs

