""" "
This file is the main entry point for the system monitoring application.
"""

import time
import helpers
import metrics


def mount_csv_report(system_info):
    """Mounts the system information into a CSV report format."""
    print(system_info)
    return {
        "CPU": f"{system_info['cpu_usage']}%",
        "Memory RAM": f"{system_info['memory_usage']}%",
        "Disk Usage": f"{system_info['disk_usage']}%",
        "Bytes Sent": system_info["network_usage"]["bytes_sent"],
        "Bytes Received": system_info["network_usage"]["bytes_recv"],
        "Swap": f"{system_info['swap_memory']}",
    }


def monitoring_system_watch(time_in_seconds=5):
    """Monitors the system's performance and refresh by time_in_seconds duration."""

    while True:
        helpers.clear_console()
        print(f"Monitoring system performance each {time_in_seconds} seconds...")
        try:
            system_info = metrics.get_system_info()
            helpers.save_report_in_csv(mount_csv_report(system_info))

            print(f"CPU Usage: {system_info['cpu_usage']}%")
            print(f"Memory Usage: {system_info['memory_usage']}%")
            print(f"Disk Usage: {system_info['disk_usage']}%")
            print(f"Bytes Sent: {system_info['network_usage']['bytes_sent']}")
            print(f"Bytes Received: {system_info['network_usage']['bytes_recv']}")
            print("----------------------WARNING----------------------")
            print(metrics.alert_on_high_cpu())
            time.sleep(time_in_seconds)
        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
            helpers.delete_report_csv()
            break


if __name__ == "__main__":
    monitoring_system_watch(5)
