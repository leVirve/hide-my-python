from hidemypython.proxy_parser import generate_proxy
from hidemypython.utils import Dict


if __name__ == '__main__':

    params = Dict(
        number_of_proxies=20,
        countries_list=['Taiwan', 'Japan'],
        ports=[80, 8080],
        protocols=['http', 'https', 'socks'],
        keep_alive=True,  # Treu/False
        anonymity=3,  # 0, 1, 2, 3
        speed=2,  # 0, 1, 2
        connection_time=2,  # 0, 1, 2
        verbose=False
    )

    proxies = generate_proxy(params)
    for proxy in proxies:
        print(proxy)
