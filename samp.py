import datascience
t = Table().with_columns(
    'letters' , make_array('a,','b','b','d') , 
    'count' , make_array(9,8,3,3),
    'points' , make_array(1,2,2,10)
)
t