"""Changed on delete cascade

Revision ID: 364a9318ef10
Revises: b37952c1e22c
Create Date: 2023-04-09 00:06:39.724429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '364a9318ef10'
down_revision = 'b37952c1e22c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('know_skills_resume_fkey', 'know_skills', type_='foreignkey')
    op.create_foreign_key(None, 'know_skills', 'resume', ['resume'], ['resume_id'], ondelete='CASCADE')
    op.drop_constraint('resume_user_id_fkey', 'resume', type_='foreignkey')
    op.create_foreign_key(None, 'resume', 'users', ['user_id'], ['user_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'resume', type_='foreignkey')
    op.create_foreign_key('resume_user_id_fkey', 'resume', 'users', ['user_id'], ['user_id'])
    op.drop_constraint(None, 'know_skills', type_='foreignkey')
    op.create_foreign_key('know_skills_resume_fkey', 'know_skills', 'resume', ['resume'], ['resume_id'])
    # ### end Alembic commands ###
