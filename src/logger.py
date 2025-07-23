import logging

logging.basicConfig(
    filename = "app.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def log_message(user_id, intake_ml):
    # your logging logic
    print(f"User {user_id} logged {intake_ml} ml of water.")


def log_error(error):
    logging.error(error)

