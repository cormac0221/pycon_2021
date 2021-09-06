from flask_admin.contrib.sqla import ModelView

from admin.views.income import IncomeInlineAdmin
from db.individ import TaxableIncome


class IndividualView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ['name', 'family_name', 'forname', 'birth_date', 'inn']

    column_sortable_list = ['created_at']

    edit_template = 'individual_edit.html'

    inline_models = (IncomeInlineAdmin(TaxableIncome),)
