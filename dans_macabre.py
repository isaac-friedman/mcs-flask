import csv
from app import db
from app.models import Deceased
from datetime import datetime

def enter_the_dead():
    with open('./new_yahrtzeits.csv') as file_in:
        reader = csv.DictReader(file_in)
        to_db = [i for i in reader]
    print(to_db)
    for i in to_db:
        if i.get('secular_death_date') in ['?', 'X', '']:
            continue
        dd = datetime.strptime(i.get('secular_death_date'), '%m/%d/%Y')
        dead=Deceased(full_name=i.get('full_name'), secular_death_date=dd, jewish_death_date=i.get('jewish_death_date'), tablet_column=i.get('tablet_column'), bio=i.get('bio'), order=i.get('order'))
        db.session.add(dead)
    db.session.commit()

def split_names():
    names = Deceased.query.all()
    for name in names:
        tokenized_name = name.full_name.split()
        name.last_name=tokenized_name[0]
        name.first_name= (' ').join(tokenized_name[1:])
        db.session.add(name)
    db.session.commit()
