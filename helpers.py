"""
This module provides utility functions for saving reports in CSV format,
clearing the console, and converting byte sizes to a human-readable format.
"""

import os
import csv
from datetime import datetime


def save_report_in_csv(metrics, file_path="report.csv"):
    """
    Saves the given metrics as a new line in a CSV file, with the current date as the first column.

    Args:
        metrics (dict): A dictionary containing the report data.
        file_path (str): The path to the CSV file. Defaults to 'report.csv'.
    """
    file_exists = os.path.isfile(file_path)

    # Add the current date to the metrics dictionary
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metrics_with_date = {"date": current_date, **metrics}

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=metrics_with_date.keys())

        # Write the header only if the file does not exist
        if not file_exists:
            writer.writeheader()

        writer.writerow(metrics_with_date)


def delete_report_csv(file_path="report.csv"):
    """
    Deletes the specified CSV report file.

    Args:
        file_path (str): The path to the CSV file to be deleted. Defaults to 'report.csv'.
    """
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted the file: {file_path}")
    else:
        print(f"The file {file_path} does not exist.")


def clear_console():
    """
    Clears the console screen based on the operating system.
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def convert_bytes_to_mb(size_in_bytes):
    """Converts bytes to a MB format."""
    return (
        f"{size_in_bytes / (1024 ** 2):.2f} MB"
        if size_in_bytes >= 1024**2
        else f"{size_in_bytes / 1024:.2f} KB"
    )
