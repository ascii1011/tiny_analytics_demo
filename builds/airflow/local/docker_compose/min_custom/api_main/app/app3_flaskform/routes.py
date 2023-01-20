from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    url_for,
    session
)

from datetime import timedelta
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from werkzeug.routing import BuildError


from flask_bcrypt import Bcrypt,generate_password_hash, check_password_hash

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

from app import create_app,db,login_manager,bcrypt
from models import User
from forms import login_form,register_form, airflow_request_form

from lib.ai import *


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app = create_app()

@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.html",title="Home")


@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("auth.html",
        form=form,
        text="Login",
        title="Login",
        btn_action="Login"
        )



# Register route
@app.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()
    if form.validate_on_submit():
        try:
            email = form.email.data
            pwd = form.pwd.data
            username = form.username.data
            
            newuser = User(
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )
    
            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("login"))

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"User already exists!.", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured !", "danger")
    return render_template("auth.html",
        form=form,
        text="Create account",
        title="Register",
        btn_action="Register account"
        )

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route("/airflow_request", methods=("GET", "POST"), strict_slashes=False)
@login_required
def airflow_request():
    """use a dag_id from the form to trigger an airflow DAG"""
    form = airflow_request_form()
    print('\nairflow_request:')
    example_dag_id = "example_02_custom"
    example_url = f"http://localhost:8251/api/v1/dags/{example_dag_id}/dagRuns"

    if form.validate_on_submit():
        try:
            response = trigger_dag_v2(form.dag_id.data)
            print(f"{response=}({type(response)})")
            return redirect(url_for("airflow_request", result=response))
        except Exception as e:
            flash(e, "danger")


    return render_template("airflow_request.html",
        form=form,
        text="Airflow Request text",
        title="Airflow Request title",
        btn_action="Trigger DAG",
        result=result
        )


        
    
    if request.method == "POST":
        print('\tpost!')
        dag_id = request.form["dag_id"]
        print(f"{dag_id=}")
        response = trigger_dag_v2(dag_id)

        print(f"{response=}({type(response)})")

        return redirect(url_for("airflow_request", result=response))

    result = request.args.get("result")
    return render_template("airflow_request.html", example_url=example_url, example_dag_id=example_dag_id, result=result)

if __name__ == "__main__":
    app.run(debug=True)
