from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


def read_data():
    return pd.read_csv("../datas/movielens-1m/users.dat",
                       sep="::",
                       engine="python",
                       header=None,
                       names="UserID::Gender::Age::Occupation::Zip-code".split("::")
                       )


@app.route('/get_user_info')
def get_user_info():
    df = read_data()
    df_male = df[df["Gender"] == "M"].head()
    df_female = df[df["Gender"] == "F"].head()

    return render_template(
        "user_info.html",
        male_data=df_male.to_html(classes="male", index=False),
        female_data=df_female.to_html(classes="female", index=False)
    )


if __name__ == '__main__':
    app.run(
        debug=True
    )
