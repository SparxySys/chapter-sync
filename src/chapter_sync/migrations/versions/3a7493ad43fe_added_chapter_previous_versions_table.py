"""Added chapter_previous_versions table.

Revision ID: 3a7493ad43fe
Revises: 63139caea00e
Create Date: 2024-03-20 00:47:11.344684

"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3a7493ad43fe"
down_revision: str | None = "63139caea00e"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "chapter_previous_versions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("series_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("url", sa.Text(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("ebook", sa.LargeBinary(), nullable=True),
        sa.Column("sent_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["series_id", "number"],
            ["chapter.series_id", "chapter.number"],
            name=op.f("chapter_previous_versions_series_id_number_fkey"),
        ),
        sa.ForeignKeyConstraint(
            ["series_id"],
            ["series.id"],
            name=op.f("chapter_previous_versions_series_id_fkey"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("chapter_previous_versions_pkey")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("chapter_previous_versions")
    # ### end Alembic commands ###
