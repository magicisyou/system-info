import platform
import psutil
from datetime import datetime
import flet as ft

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

sys_info_tab=ft.Tab(
    text='System Information',
    icon=ft.icons.COMPUTER,
    content=ft.Container(
        padding=20,
        content=ft.Column(
            controls = [
                ft.Row(controls = [
                    ft.Text("System", width=150),
                    ft.Text(uname.system, color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Node Name", width=150),
                    ft.Text(uname.node, color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Release", width=150),
                    ft.Text(uname.release, color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Version", width=150),
                    ft.Text(uname.version, color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Machine", width=150),
                    ft.Text(uname.machine, color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Processor", width=150),
                    ft.Text(uname.processor, color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Boot Time", width=150),
                    ft.Text(bt, color = ft.colors.TEAL),
                    ]),
                ],
            ),
        ),
    )

cpu_info_tab=ft.Tab(
    text='Processor Information',
    icon=ft.icons.STORAGE,
    content=ft.Container(
        padding=20,
        content=ft.Column(
            controls = [
                ft.Row(controls = [
                    ft.Text("Physical cores", width=150),
                    ft.Text(psutil.cpu_count(logical=False), color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Total cores", width=150),
                    ft.Text(psutil.cpu_count(logical=True), color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("CPU usage", width=150),
                    ft.Text(f"{psutil.cpu_percent()}%", color=ft.colors.TEAL),
                    ]),
                ],
            ),
        ),
    )

mem_info_tab=ft.Tab(
    text='Memory Information',
    icon=ft.icons.MEMORY,
    content=ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row(controls = [
                    ft.Text("Total", width=150),
                    ft.Text(get_size(svmem.total), color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Available", width=150),
                    ft.Text(get_size(svmem.available), color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Used", width=150),
                    ft.Text(get_size(svmem.used), color=ft.colors.TEAL),
                    ]),
                ft.Row(controls = [
                    ft.Text("Percentage", width=150),
                    ft.Text(f"{svmem.percent}%", color=ft.colors.TEAL),
                    ]),
                ],
            ),
        ),
    )


tabs = ft.Tabs(
    selected_index=0,
    animation_duration=200,
    tabs=[
        sys_info_tab,
        cpu_info_tab,
        mem_info_tab,
        ],
    expand=1,
    )


def main(page: ft.Page):
    page.title = "System Information"
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.TEAL)
    page.add(tabs)

ft.app(target = main)
