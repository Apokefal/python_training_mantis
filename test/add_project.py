from model.project import Project


def test_add_project(app):
    app.project.open_project_page()
    old_project = app.project.project_count()
    app.project.create_project(Project(name="test", description="test"))
    app.project.open_project_page()
    new_project = app.project.project_count()
    assert old_project == new_project
