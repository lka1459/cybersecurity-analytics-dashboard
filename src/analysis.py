import pandas as pd
import sqlalchemy as sqla
import os
import sys

from datetime import datetime
from pathlib import Path
from sqlalchemy import create_engine, text

from dotenv import load_dotenv
from typing import Dict, Optional
from database_setup import get_connection

load_dotenv()

user: str = os.getenv("DB_USER")
password: str = os.getenv("DB_PASSWORD")
host: str = os.getenv("DB_HOST")
port: str = os.getenv("PORT")
database: str = os.getenv("DB_NAME")

engine = get_connection()

def query_database(query: str, para_bindings: Optional[Dict[str, str | int]] = None) -> pd.DataFrame:
    """
    Queries the database based on user input (easier during testing).
    """
    with engine.connect() as connection:
        query: sqla.Text = text(query)

        result: sqla.CursorResult = connection.execute(query, para_bindings)
        df: pd.DataFrame = pd.DataFrame(result)
        
        return df
    
def read_sql(filepath: str) -> pd.DataFrame:
    """
    Reads the SQL query within a SQL file and returns a Pandas DataFrame.
    """
    with engine.connect() as conn:
        with open(Path(filepath), "r") as file:
            query: str = file.read()
            df: pd.DataFrame = pd.read_sql(query, conn)

            return df

def print_df(df):
    while True:
        print(f"Would you like to print the dataframe? ")
        answer: str = input("[1] Yes \n[2] No \n[3] Exit \n")
        if answer == "1":
            print(df)
            return
        elif answer == "2":
            return
        elif answer == "3":
            sys.exit()
        else:
            print("Error please try again")
    
def main():
    total_attacks: pd.DataFrame = read_sql(r"sql\exploration\total_attacks.sql")
    print_df(total_attacks)
    exist_protocols: pd.DataFrame = read_sql(r"sql\exploration\existing_protocols.sql")
    print_df(exist_protocols)


if __name__ == "__main__":
    main()