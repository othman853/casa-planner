"""Adding field ciclo to ItemDespensa

Revision ID: e5c8fab2b858
Revises: 7bcd5c765b72
Create Date: 2016-08-24 13:33:10.107923

"""

# revision identifiers, used by Alembic.
revision = 'e5c8fab2b858'
down_revision = '7bcd5c765b72'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE TYPE ciclos_despensa AS ENUM ('Sem ciclo', 'Semanal', 'Mensal')")
    op.add_column('itens_despensa', sa.Column(
        'ciclo',
        sa.Enum(
            'Sem ciclo', 'Semanal', 'Mensal', name='ciclos_despensa'
        ),
        nullable=True
    ))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('itens_despensa', 'ciclo')
    ### end Alembic commands ###
