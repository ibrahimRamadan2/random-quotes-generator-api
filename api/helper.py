import datetime
import datetime
import csv
import api.models


def create_report():
    now = datetime.datetime.now()
    str = now.strftime("%Y_%m_%d_%H_%M_%S")
    with open(f"report/quotes_api_report_{str}.csv", 'w+') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Quote ID", "Count"])
        quote_list = api.models.Quote.objects.all().values("id", "count")
        quote_list = [[quote["id"], quote["count"]] for quote in quote_list]
        csv_writer.writerows(quote_list)


def check_counter():
    with open("api/counter.txt", "r+") as file:
        try:
            text = file.read()
            cnt = int(text) + 1
        except:  # the file is empty = ''
            file.write('0')
            cnt = 0
    with open("api/counter.txt", "w") as file:
        file.write(str(cnt))
    if (cnt % 100 == 0):
        create_report()