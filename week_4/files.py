import csv

my_result_dict = {}
with open ("Artworks.csv",'r') as art_file:
    art_csv = csv.DictReader(art_file)
    for art in art_csv:
        nats =art['Nationality'].split(" ")
        for nat in nats:
            my_result_dict [nat]= my_result_dict.setdefault(nat,0) +1

#print(my_result_dict)
for bla in my_result_dict:
    print(f'{bla}:{my_result_dict[bla]}')