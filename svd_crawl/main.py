from curl_cffi import requests

r = requests.get("https://mvnrepository.com/artifact/io.dropwizard/dropwizard-jersey/4.0.0-beta.4", impersonate="chrome101")

print(r.text)
