import platform
import psutil
from datetime import datetime
import flet as ft

# Converts bytes to KB, MB, GB, TB, PB
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

uname = platform.uname()
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
svmem = psutil.virtual_memory()

def main(page: ft.Page):
    page.title = "System Information"
    page.add(
            ft.Column(controls = [
                ft.Text("General", color="blue"),
                ft.Row(controls = [
                    ft.Text("System", width=150),
                    ft.Text(uname.system, color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Node Name", width=150),
                    ft.Text(uname.node, color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Release", width=150),
                    ft.Text(uname.release, color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Version", width=150),
                    ft.Text(uname.version, color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Machine", width=150),
                    ft.Text(uname.machine, color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Processor", width=150),
                    ft.Text(uname.processor, color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Boot Time", width=150),
                    ft.Text(bt, color = "green"),
                    ]),
                ft.Text("CPU Information", color="blue"),
                ft.Row(controls = [
                    ft.Text("Physical cores", width=150),
                    ft.Text(psutil.cpu_count(logical=False), color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Total cores", width=150),
                    ft.Text(psutil.cpu_count(logical=True), color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("CPU usage", width=150),
                    ft.Text(f"{psutil.cpu_percent()}%", color="green"),
                    ]),
                ft.Text("Memory Information", color="blue"),
                ft.Row(controls = [
                    ft.Text("Total", width=150),
                    ft.Text(get_size(svmem.total), color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Available", width=150),
                    ft.Text(get_size(svmem.available), color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Used", width=150),
                    ft.Text(get_size(svmem.used), color="green"),
                    ]),
                ft.Row(controls = [
                    ft.Text("Percentage", width=150),
                    ft.Text(f"{svmem.percent}%", color="green"),
                    ]),
            ])
    )

ft.app(target = main)
