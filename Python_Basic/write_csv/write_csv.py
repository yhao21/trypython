
'''
You can manually write data to a csv without using pandas.
This can save your memory useage (but run slower) when you have a lot of rows to write.

    csv_file = open('hi.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['title', 'date', 'content'])
    csv_writer.writerow(['Binance Exec Says', 'Dec. 1, 2022', data])
    csv_file.close()
'''
