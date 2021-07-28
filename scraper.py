from tkinter.constants import END
import requests
from bs4 import BeautifulSoup

ENDPOINT_FOR_SCRAPING = "https://www.freelancer.com/jobs/php_html_css_javascript_python_django_mongodb_mysql_postgresql_full-stack-development_java_nodejs_expressjs_react-js_react-native_flutter_angular_typescript_google-firebase_api/?languages=en&fixed=true"


def scrape_freelancer(text):
    html = requests.get(ENDPOINT_FOR_SCRAPING).text

    scraper = BeautifulSoup(html, 'lxml')
    project_list = scraper.find("div", id="project-list")

    projects = project_list.find_all("div", class_="JobSearchCard-item")

    for project in projects:
        project_bids = project.find(
            "div", class_="JobSearchCard-secondary-entry").text.strip()

        # expression for checking if bids are lesser than 18
        if int(project_bids.split(" ")[0]) < 18:
            project_heading = project.find(
                "div", class_="JobSearchCard-primary-heading").a.text.strip()
            project_desc = project.find(
                "p", class_="JobSearchCard-primary-description").text.strip()
            project_link = project.find(
                "a", class_="JobSearchCard-primary-heading-link")['href']

            text.insert(END,
                        f"\nProject: \n {project_heading} \n Description: \n {project_desc} \n Bids: \n {project_bids} \n Link: \n https://www.freelancer.com/{project_link}\n\n")
