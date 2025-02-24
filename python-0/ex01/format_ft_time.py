import time

epoch = time.time()
print(f'Seconds since January 1, 1970: {epoch:,} ', end='')
print(f'or {epoch:.2e} in scientific notation')
print(time.strftime('%b %d %Y'))
