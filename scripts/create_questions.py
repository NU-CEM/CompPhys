from github import Github
from dotenv import load_dotenv
import os
import re

course_repo = "nu-cem/CompPhys"
issue_template_path = '.github/ISSUE_TEMPLATE/python-basics-checklist.md'
issue_template_label = "python_checklist"   # should test for this before running the action....
output_file_path = "../_posts/Issue_{}.png".format()  # format with the issue number here

load_dotenv()
GH_TOKEN = os.getenv("GH_TOKEN")  # this is needed to interact with the Github API

g = Github(GH_TOKEN)
repo = g.get_repo(course_repo)

issue_template_content = repo.get_contents(issue_template_path).decoded_content.decode()
tasks = re.findall(r'\[ ] (.*)\n', issue_template_content)

#issue =       # get the issue
#tick_numbers =    # get the LO numbers that are ticked

# each question will list the objective(s) it requires
# only select the questions when all objectives are ticked

# question_files = 
# create markdown file (with header section?)

# for file in question_files:
#   question_requires = # list the objective numbers required
#    if set(question_requires) <= set(tick_numbers):   # see if all objectives met
#         find question content  
        # append question content to markdown file






