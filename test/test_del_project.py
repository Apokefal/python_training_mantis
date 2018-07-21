from random import randrange
from model.project import Project

def test_del_project(app):
    if app.project.project_count() == 0:
        app.project.create_project(Project(name="del"))
    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    app.project.del_project_by_index(index)
    new_projects = app.project.get_project_list()
    assert len(old_projects) == len(new_projects)

