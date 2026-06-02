import logging
from dotenv import load_dotenv

import dagshub

load_dotenv()

dagshub.init(repo_owner='Jeisianyf', repo_name='mlops-project-breast-cancer', mlflow=True)

# Configure the logging strategy
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler()
    ]
)
