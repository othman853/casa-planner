"""adding more fields to imovel

Revision ID: 404a39e8d0a6
Revises: 5dd905265cfb
Create Date: 2016-08-23 18:29:19.311941

"""

# revision identifiers, used by Alembic.
revision = '404a39e8d0a6'
down_revision = '5dd905265cfb'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('imoveis', sa.Column('aprovado', sa.Boolean(), nullable=True))
    op.add_column('imoveis', sa.Column('visitado', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('imoveis', 'visitado')
    op.drop_column('imoveis', 'aprovado')
    ### end Alembic commands ###
