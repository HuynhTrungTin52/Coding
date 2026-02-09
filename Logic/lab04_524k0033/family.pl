parent(john, mary).
parent(mary, susan).
parent(john, peter).
parent(peter, james).
ancestor(X, Y) :-parent(X, Y).
ancestor(X, Y) :-parent(X, Z), ancestor(Z, Y).