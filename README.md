Processing-Experiments
======================

Experiments with combining [processingjs](http://processingjs.org), [webpy](http://webpy.org) and the [prototype js framework](http://prototypejs.org)

My motivation behind all of these is to create some fun visualizations that can interact with real web applications - webpy gives me a very lightweight and fast way to mock out a backend while concentrating on the meat of the visualization portion.

To Run
======
(in an os x terminal)
python center.py
open http://127.0.0.1:8080/static/map.html

More than one client can connect, although there are concurrency issues in the backend (all the state is global, as I didn't really want to bother with anything more complex; this will be fixed before I host this on my site)
