from model.project import Project
import random
import string


def random_projectname(perfix, maxlen):
    symbols = string.ascii_letters
    return perfix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project_name = random_projectname("project_", 10)
    old_project = len(app.soap.get_projects("administrator", "root"))
    app.soap.add_projects("administrator", "root", Project(name=project_name, description="Описание2555"))
    new_project = len(app.soap.get_projects("administrator", "root"))
    assert old_project + 1 == new_project

