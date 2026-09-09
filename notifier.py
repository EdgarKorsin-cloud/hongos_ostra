import sqlite3
import smtplib
from datetime import date, timedelta
import os

DB_PATH='siembra.db'
SENDER_EMAIL = os.environ.get('my_email')
EMAIL_PASSWORD = os.environ.get('my_password')
RECIPIENT_EMAIL = os.environ.get('recipient_email')

def upcoming_date():
    target_date = (date.today() + timedelta(days=2)).strftime("%Y-%m-%d")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query="""
    SELECT id, product_name, incubation_start_date, incubation_end_date,fructification_start
    FROM siembra
    WHERE incubation_end_date = ? OR fructification_start = ?
    """
    cursor.execute(query, (target_date, target_date))
    results = cursor.fetchall()
    conn.close()

    return results, target_date

def main():
    upcoming_batches, target_date = upcoming_date()

    if not upcoming_batches:
        print("No upcoming batches to send")
        return
    print(f"Sending {len(upcoming_batches)} emails...")
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=EMAIL_PASSWORD)

        for batch in upcoming_batches:
            batch_name = batch['product_name']

            if batch['incubation_end_date'] == target_date:
                milestone = "Incubation Phase ends"


            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECIPIENT_EMAIL,
                msg=f"Subject: Incubation Phase ends for {batch_name}\n\n"
                    f"Take your substrate where it gets oxygen. "
                    f"Fructification will begin in {batch['fructification_start']}"
            )
if __name__ == "__main__":
    main()