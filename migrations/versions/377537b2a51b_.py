"""empty message

Revision ID: 377537b2a51b
Revises: f7099c61ea0d
Create Date: 2022-03-27 11:04:55.688059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '377537b2a51b'
down_revision = 'f7099c61ea0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alergiasUsuario',
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('alergia_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['alergia_id'], ['alergias.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('usuario_id', 'alergia_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alergiasUsuario')
    # ### end Alembic commands ###