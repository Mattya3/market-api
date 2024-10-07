"""Add foreign key

Revision ID: fbce9736935a
Revises: cd99ba9b32f1
Create Date: 2024-09-23 16:12:37.799487

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbce9736935a'
down_revision: Union[str, None] = 'cd99ba9b32f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'items', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.drop_column('items', 'user_id')
    # ### end Alembic commands ###