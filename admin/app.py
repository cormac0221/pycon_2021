from flask import Flask
from flask_admin import Admin, AdminIndexView

from db import current_session
from db.individ import Individual, TaxableIncome


def create_app() -> Flask:
    app = Flask(__name__)

    app.config['FLASK_ADMIN_SWATCH'] = 'Cosmo'
    app.secret_key = 'kek'

    admin = Admin(app, name='2 НДФЛ', index_view=AdminIndexView(name='📃', url='/'), template_mode='bootstrap4')

    from admin.views.income import IncomeView
    from admin.views.individual import IndividualView
    admin.add_view(IndividualView(Individual, current_session, name='Физлицо'))
    admin.add_view(IncomeView(TaxableIncome, current_session, name='Облагаемый доход'))

    return admin.app


if __name__ == '__main__':
    from db import DBSettings
    DBSettings().setup_db()

    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
