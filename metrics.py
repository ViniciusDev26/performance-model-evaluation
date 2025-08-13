"""
This module provides functions to collect and return various system metrics
such as CPU usage, memory usage, disk usage, network statistics, and swap memory.
"""

import psutil
import helpers


def get_cpu_usage():
    """Returns the CPU usage percentage."""
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """Returns the memory usage percentage."""
    memory_info = psutil.virtual_memory()
    return memory_info.percent


def get_disk_usage():
    """Returns the disk usage percentage."""
    disk_info = psutil.disk_usage("/")
    return disk_info.percent


def get_network_usage():
    """Returns the network usage statistics."""
    net_info = psutil.net_io_counters()
    return {"bytes_sent": net_info.bytes_sent, "bytes_recv": net_info.bytes_recv}


def get_swap_memory():
    """Returns the swap memory usage statistics."""
    swap_info = psutil.swap_memory()
    return {
        "total": helpers.convert_bytes_to_mb(swap_info.total),
        "used": helpers.convert_bytes_to_mb(swap_info.used),
        "free": helpers.convert_bytes_to_mb(swap_info.free),
        "percent": swap_info.percent,
    }


def pretty_network_usage():
    """Returns the pretty network usage statistics."""
    net_info = psutil.net_io_counters()
    return {
        "bytes_sent": helpers.convert_bytes_to_mb(net_info.bytes_sent),
        "bytes_recv": helpers.convert_bytes_to_mb(net_info.bytes_recv),
    }


def alert_on_high_cpu(warning_threshold=70, critical_threshold=85):
    """Alerts if CPU usage exceeds warning or critical thresholds."""
    cpu_usage = get_cpu_usage()
    if cpu_usage >= critical_threshold:
        return f"CRITICAL: CPU usage is at {cpu_usage}%"
    elif cpu_usage >= warning_threshold:
        return f"WARNING: CPU usage is at {cpu_usage}%"
    else:
        return f"CPU usage is at {cpu_usage}%, within normal limits."


def get_system_info():
    """Returns a dictionary containing system information."""
    return {
        "cpu_usage": get_cpu_usage(),
        "memory_usage": get_memory_usage(),
        "disk_usage": get_disk_usage(),
        "network_usage": pretty_network_usage(),
        "swap_memory": get_swap_memory(),
    }
