import subprocess, ast


async def get_proxy():
    # Execute the 'getproxy.py' script, and save its output
    proxy_output = subprocess.check_output(
        ["/usr/bin/python3", "./valid_reverses/getproxy.py"]
    )
    proxy_string = proxy_output.decode(
        "utf-8"
    ).strip()  # This is a string like '["https://34.75.225.169:8080/", "https://178.54.21.203:8081/", ...]'

    # Convert string to list
    proxy_list = ast.literal_eval(proxy_string)
    return proxy_list
