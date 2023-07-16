import yaml
import os
from urllib import request

URL = 'https://raw.githubusercontent.com/cncf/landscape/master/processed_landscape.yml'
LOCAL_FILENAME = 'processed_landscape.yml'
POST_NAME = '2023-07-16-cncf-projects-by-language.md'


FRONT_MATTER = """
---
title: CNCF Projects by Language
summary: "The projects within the CNCF Landscape listed by their primary programming language"
---
"""

STYLE = """
<style>
ul {
    list-style-type: circle;
}
</style>
"""

INTRO = """
Ever wanted to see a list of CNCF (Cloud-Native Computing Foundation) projects, grouped by their 
primary programming language? No? Just me?

Well, here's the list anyway. The projects are also grouped by their category, ordered by stars and
the languages are ordered by number of projects.

The data comes from the
[CNCF Landscape GitHub](https://github.com/cncf/landscape/blob/master/processed_landscape.yml) and
was massaged into a blog post using
[this Python script](
https://github.com/jrhenderson1988/jrhenderson1988.github.io/tree/master/scripts/cncf.py).
"""


class Data:
    def __init__(self):
        self.languages = []

    def find_or_create_language(self, name, color):
        for language in self.languages:
            if language.name == name:
                return language
        language = Language(name, color)
        self.languages.append(language)
        return language

    def sort(self):
        for language in self.languages:
            for category in language.categories:
                category.projects = sorted(
                    category.projects, key=lambda p: p.stars, reverse=True)
        self.languages = sorted(
            self.languages, key=lambda l: l.total_projects(), reverse=True)


class Language:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def find_or_create_category(self, name, sub_name):
        for category in self.categories:
            if category.category_name == name and category.subcategory_name == sub_name:
                return category
        category = Category(name, sub_name)
        self.categories.append(category)
        return category

    def generate_bullet(self, char):
        color = self.color if self.color is not None else 'inherit'
        return ('<span style="color:%s;">%s</span>' % (color, char))

    def total_projects(self):
        total = 0
        for category in self.categories:
            total += len(category.projects)
        return total


class Category:
    def __init__(self, category_name, subcategory_name):
        self.category_name = category_name
        self.subcategory_name = subcategory_name
        self.projects = []

    def create_project(self, name, repo_url, homepage_url, stars):
        project = Project(name, repo_url, homepage_url, stars)
        self.projects.append(project)
        return project

    def breadcrumb(self):
        names = [self.category_name, self.subcategory_name]
        return ' / '.join(filter(lambda n: n is not None, names))


class Project:
    def __init__(self, name, repo_url, homepage_url, stars):
        self.name = name
        self.repo_url = repo_url
        self.homepage_url = homepage_url
        self.stars = stars


def get_primary_language(github_data):
    languages = github_data['languages'] if 'languages' in github_data else []
    if len(languages) == 0:
        return None, None

    primary_language = max(languages, key=lambda l: l['value'])
    name = primary_language['name']
    color = primary_language['color'] if 'color' in primary_language else None
    return name, color


def parse_projects_by_language(path):
    data = Data()
    with open(path, 'r') as stream:
        try:
            obj = yaml.safe_load(stream)
            for category in obj['landscape']:
                cat_name = category['name'] if 'name' in category else None
                for subcategory in category['subcategories']:
                    sub_name = subcategory['name'] if 'name' in subcategory else None
                    for item in subcategory['items']:
                        github_data = item['github_data'] if 'github_data' in item else {
                        }
                        proj_name = item['name']
                        proj_repo_url = item['repo_url'] if 'repo_url' in item else None
                        proj_homepage_url = item['homepage_url'] if 'homepage_url' in item else None
                        proj_stars = github_data['stars'] if 'stars' in github_data else None

                        language_name, language_color = get_primary_language(
                            github_data)
                        if language_name is not None:
                            language = data.find_or_create_language(
                                language_name, language_color)
                            category = language.find_or_create_category(
                                cat_name, sub_name)
                            category.create_project(
                                proj_name, proj_repo_url, proj_homepage_url, proj_stars)
        except yaml.YAMLError as exc:
            print(exc)
    return data


def generate_post(filename, data):
    with open('_posts/%s' % filename, 'w') as file:
        file.write('%s%s\n%s\n\n' %
                   (FRONT_MATTER.strip(), STYLE, INTRO.strip()))

        for language in data.languages:
            total_projects = language.total_projects()
            projects = 'project' if total_projects == 1 else 'projects'
            lang_line = '%s %s <small>(%d %s)</small>' % (language.generate_bullet('&#9679;'),
                                                          language.name, total_projects, projects)
            file.write('\n\n## ' + lang_line)
            for category in language.categories:
                file.write('\n\n### %s' % category.breadcrumb())
                for project in category.projects:
                    meta = []
                    if project.stars is not None:
                        stars = '{:,}'.format(project.stars)
                        meta.append('&#9733; %s' % stars)
                    if project.repo_url is not None:
                        meta.append('[Repository](%s)' % project.repo_url)
                    if project.homepage_url is not None:
                        meta.append('[Homepage](%s)' % project.homepage_url)

                    meta_data = ' / '.join(meta)
                    meta_line = ' <small> (%s)</small>' % meta_data if meta_data != '' else ''
                    line = ('\n- %s' % project.name) + meta_line
                    file.write(line)

if __name__ == '__main__':
    if not os.path.isfile(LOCAL_FILENAME):
        request.urlretrieve(URL, LOCAL_FILENAME)

    data = parse_projects_by_language(LOCAL_FILENAME)
    data.sort()

    generate_post(POST_NAME, data)
