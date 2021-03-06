"""creating BalcaoCooktop model

Revision ID: 75a5da1f2676
Revises: e68770cd2bb2
Create Date: 2016-08-24 07:58:59.244462

"""

# revision identifiers, used by Alembic.
revision = '75a5da1f2676'
down_revision = 'e68770cd2bb2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('balcoes_cooktop',
    sa.Column('cor', sa.String(), nullable=True),
    sa.Column('preco_parcelado', sa.Float(), nullable=True),
    sa.Column('preco_a_vista', sa.Float(), nullable=True),
    sa.Column('marca', sa.String(), nullable=True),
    sa.Column('modelo', sa.String(), nullable=True),
    sa.Column('altura', sa.Float(), nullable=True),
    sa.Column('largura', sa.Float(), nullable=True),
    sa.Column('comprimento', sa.Float(), nullable=True),
    sa.Column('link_loja', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loja_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['loja_id'], ['lojas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('balcoes_cooktop')
    ### end Alembic commands ###
