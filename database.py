import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from models import Base, ContactMessage

load_dotenv()


class DatabaseNotConfiguredError(RuntimeError):
	pass


class DatabaseUnavailableError(RuntimeError):
	pass


def _database_url() -> str | None:
	url = os.getenv("DATABASE_URL")

	if not url:
		return None

	if url.startswith("postgres://"):
		return url.replace("postgres://", "postgresql+psycopg://", 1)

	if url.startswith("postgresql://"):
		return url.replace("postgresql://", "postgresql+psycopg://", 1)

	return url


DATABASE_URL = _database_url()
engine = create_engine(DATABASE_URL, pool_pre_ping=True) if DATABASE_URL else None
SessionLocal = sessionmaker(
	bind=engine,
	autoflush=False,
	autocommit=False,
	expire_on_commit=False,
)


def initialize_database() -> bool:
	if engine is None:
		return False

	try:
		Base.metadata.create_all(bind=engine)
	except SQLAlchemyError:
		return False

	return True


def save_contact_message(name: str, email: str, message: str) -> None:
	if engine is None:
		raise DatabaseNotConfiguredError

	session: Session = SessionLocal()

	try:
		session.add(
			ContactMessage(
				name=name,
				email=email,
				message=message,
			)
		)
		session.commit()
	except SQLAlchemyError as error:
		session.rollback()
		raise DatabaseUnavailableError from error
	finally:
		session.close()
