from typing import Any, cast
from markupsafe import Markup

from flask_admin.contrib.sqla import ModelView
from flask_admin.model.form import InlineFormAdmin


def individ_formatter(view: 'IncomeView', context: Any, model: 'TaxableIncome', name: str) -> Markup:
    return cast(
        Markup, f'{model.individual.name} {model.individual.family_name} {model.individual.forname}'
    )


class IncomeView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    form_columns = ['individual', 'month', 'sum']

    column_sortable_list = ['created_at', 'month']

    column_formatters = {
       'individual': individ_formatter
    }


class IncomeInlineAdmin(InlineFormAdmin):
    form_excluded_columns = ['individual', 'individual_id', 'created_at']
