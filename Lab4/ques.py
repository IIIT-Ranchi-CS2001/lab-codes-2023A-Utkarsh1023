set_s = {'King','Talha Anjum','M-Zee Bella','Badshaah','Emiway'}
set_d = {'King','Raghav Juyal','Puneet','Badshaah','Sakti Mohan'}

artists = set_s.union(set_d)
print(f"All Artists are : {artists}")

allrounders = set_s.intersection(set_d)
print(f"All Rounders are: {allrounders}")

danc_not_sing = set_d.difference(set_s)
print(f"Dancers but not Singers are: {danc_not_sing}")

sing_not_dance = set_s.difference(set_d)
print(f"Singers but not Dancers are: {sing_not_dance}")

sing_not_dance_and_dance_not_sing = set_s.symmetric_difference(set_d)
print(f"Dancers but not Singers cum Singers but not Dancers are: {sing_not_dance_and_dance_not_sing}")