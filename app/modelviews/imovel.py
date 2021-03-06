from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField
from .formatters import (
    money_formatter, square_meters_formatter, link_formatter, phone_formatter
)


class ImovelModelView(ModelView):

    can_view_details = True

    column_default_sort = ('nota', True)
    column_sortable_list = ('valor_total', 'tamanho')

    column_exclude_list = (
        'visitado', 'aprovado', 'tem_garagem', 'andar', 'sol', 'nivel_barulho',
        'endereco', 'nota', 'chuveiro', 'tem_portaria', 'tem_elevador',
        'tem_salao_festas', 'parada_onibus', 'linha_onibus',
        'numero_dormitorios', 'mercado', 'shopping', 'farmacia', 'comentarios',
        'posto_gasolina', 'valor_aluguel', 'valor_condominio', 'valor_iptu'
    )

    column_formatters = dict(
        link=lambda c, v, m, p: link_formatter(m.link, 'Ver no site'),
        tamanho=lambda c, v, m, p: square_meters_formatter(m.tamanho),
        valor_total=lambda c, v, m, p: money_formatter(m.valor_total),
        telefone=lambda c, v, m, p: phone_formatter(m.telefone)
    )

    column_filters = (
        'visitado', 'aprovado', 'valor_total', 'bairro.nome',
        'imobiliaria.nome', 'codigo_imovel'
    )

    form_args = dict(
        sol=dict(
            choices=[
                ('N/A', 'Não Informado'), ('Leste', 'Leste (Melhor)'),
                ('Norte', 'Norte (2ª Melhor)'),
                ('Oeste', 'Oeste (Mais quente)'), ('Sul', 'Sul (Mais fria)')
            ]
        ),
        nota=dict(
            choices=[(x, str(x)) for x in range(0, 6)],
            coerce=int
        ),
        nivel_barulho=dict(
            choices=[(x, str(x)) for x in range(0, 6)],
            coerce=int
        ),
        chuveiro=dict(
            choices=[
                ('N/A', 'Não Informado'), ('Gás', 'Gás'),
                ('Elétrico', 'Elétrico')
            ]
        )
    )

    form_overrides = dict(
        sol=SelectField,
        nota=SelectField,
        nivel_barulho=SelectField,
        chuveiro=SelectField
    )

    def get_column_names(self, only_columns, excluded_columns):

        columns = super().get_column_names(only_columns, excluded_columns)
        columns.insert(1, ('valor_total', 'Valor Total'))

        return columns
