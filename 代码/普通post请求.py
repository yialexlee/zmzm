import requests

url = 'https://www.jisilu.cn/data/new_stock/]'
cookies = "Cookie: kbz_newcookie=1; kbzw__Session=j8kn0mmptr1ticqko30pon42a3; " \
          "Hm_lvt_164fe01b1433a19b507595a43bf58262=1611582342,1611674785,1611675044; kbzw_r_uname=saa1028; " \
          "kbzw__user_login" \
          "=7Obd08_P1ebax9aX6sPXkqepq5mcndHV7Ojg6N7bwNOM2KejrsTSktjc15yrpKjGqcfaqNislqGV1amrzLKjrpmXnKTs3Ny_zYytr" \
          "6maqZ6YnaO2uNXQo67f293l4cqooaWSlonO4OHc0OfUlMfJiaqcpZKxgc7g4a6Vq4Hsr6mSma3n0uLGztzVw8rkkKmsrJesopeKwanLx" \
          "L-kgdzK396VsN7P4tGfgbrf5efO1ZCsrKOZp6CokqmPqKipmLTRx9Xr3piun66QqZeXvNffkKiUoqmjnbCkpZes; Hm_lpv" \
          "t_164fe01b1433a19b507595a43bf58262=1611675492 "
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56 '
}
data = {
    'rp': 22,
    'page': '3',
    'pageSize': '100',
    'market[]': 'shmb',
    'market[]': 'shkc',
    'market[]': 'szmb',
    'market[]': 'szzx',
    'market[]': 'szcy',
    'market[]': 'sbjx'
}
response = requests.post(url, data=data, headers=headers)
print(response.content.decode("utf-8"))
