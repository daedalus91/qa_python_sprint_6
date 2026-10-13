from datetime import date, timedelta


def generate_delivery_date(days_ahead):
    return (date.today() + timedelta(days=days_ahead)).strftime("%d.%m.%Y")