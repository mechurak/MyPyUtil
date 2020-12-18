import pprint

from indeed import get_jobs as get_indeed_jobs

indeed_jobs = get_indeed_jobs()
pprint.pprint(indeed_jobs)
