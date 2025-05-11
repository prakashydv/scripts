import csv

def csvToJson(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for review in csv_reader:
            review_data = {}
            for i, column in enumerate(header):
                review_data[column] = review[i]
            data.append(review_data)
    return data
