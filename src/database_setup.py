import pandas as pd
import sqlalchemy as sqla
import re
import os

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv

load_dotenv()

user: str = os.getenv("DB_USER")
password: str = os.getenv("DB_PASSWORD")
host: str = os.getenv("DB_HOST")
port: str = os.getenv("PORT")
database: str = os.getenv("DB_NAME")

def get_connection() -> sqla.Engine:
    """
    Uses SQLAlchemy to create and connect to the cyber dashboard database.
    """
    db_url: str =  f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine: sqla.Engine = sqla.create_engine(db_url)
    
    if not database_exists(engine.url):
        create_database(engine.url)
        print("Database created successfully.")
    else:
        print("Database already exists.")

    return engine

def ingest_data() -> None:
    """
    Populates the Cyber Databoard database with the CSV files data.
    """
    engine: sqla.Engine = get_connection()
    parent: str = (Path.cwd())
    path: Path = Path(f"{parent}/data/")
    day_regex: str = r"[\w\-.]+(?=-[Ww]orkingHours)"
    type_regex: str = r"(?<=-[Ww]orkingHours-)[\w\-.]+(?=.pcap)"

    for file_name in path.iterdir():
        datafile: pd.DataFrame = pd.read_csv(file_name, low_memory=False, encoding="latin1")
        day_match: re.Match = re.search(day_regex, str(file_name.name))
        type_match: re.Match = re.search(type_regex, str(file_name))
        if day_match:
            day_match: str = day_match.group().replace("_", " ")
        if type_match:
            type_match: str = type_match.group().replace("_", " ")
        else:
            type_match: str = "Working_Hours"

        replacements = str.maketrans({" ": "_", "-": "_"})
        table_name: str = f"{day_match}_{type_match}".translate(replacements)
        
        try:
            datafile.to_sql(
            f"{table_name}",
            engine, 
            if_exists="replace",
            index=False
                            )
            print(f"{table_name} has been added to the Database.")
        except Exception as e:
            print(f"Error inserting {table_name}: {e}")
            engine.rollback()
            continue