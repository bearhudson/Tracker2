from rich import print as pprint
from SQLClass import SQLClass
from src.environs import *
from rich import box
from rich.console import Console
from rich.live import Live
from rich.table import Table


sql_object = SQLClass.SQLClass(mysql_db=mysql_db,
                               mysql_host=mysql_host,
                               mysql_username=mysql_username,
                               mysql_password=mysql_password)

