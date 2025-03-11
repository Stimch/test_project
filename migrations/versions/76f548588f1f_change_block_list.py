"""change block list

Revision ID: 76f548588f1f
Revises: f009163819c9
Create Date: 2025-03-11 13:33:49.564892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76f548588f1f'
down_revision = 'f009163819c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tokens_black_list', schema=None) as batch_op:
        batch_op.drop_constraint('tokens_black_list_user_id_key', type_='unique')
        batch_op.create_unique_constraint(None, ['token_id'])
        batch_op.create_unique_constraint(None, ['jti'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tokens_black_list', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('tokens_black_list_user_id_key', ['user_id'])

    # ### end Alembic commands ###
