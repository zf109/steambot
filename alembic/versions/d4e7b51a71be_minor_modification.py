"""minor modification

Revision ID: d4e7b51a71be
Revises: 388aa87531a1
Create Date: 2017-05-30 00:18:47.355165

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd4e7b51a71be'
down_revision = '388aa87531a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('price_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('app_db_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('discount', sa.Float(), nullable=True),
    sa.Column('price_original', sa.Float(), nullable=True),
    sa.Column('currency', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['app_db_id'], ['app_info.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.drop_table('price')
    op.drop_table('app')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('price',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('app_db_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('discount', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('price_original', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('currency', sa.VARCHAR(length=5), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['app_db_id'], ['app.id'], name='price_app_db_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='price_pkey')
    )
    op.create_table('app',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('app_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=250), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='app_pkey')
    )
    op.drop_table('price_info')
    op.drop_table('app_info')
    # ### end Alembic commands ###
