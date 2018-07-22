def test_signup_new_account(app):
    username = "usertest"
    password = "test"
    app.james.ensure_user_exists(username, password)