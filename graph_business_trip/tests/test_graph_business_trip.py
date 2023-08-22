from graph_business_trip.graph_business_trip import Graph, business_trip

route_map = Graph()

pandora = route_map.add_vertex("Pandora")
arendelle = route_map.add_vertex("Arendelle")
metroville = route_map.add_vertex("Metroville")
monstropolis = route_map.add_vertex("Monstropolis")
naboo = route_map.add_vertex("Naboo")
narnia = route_map.add_vertex("Narnia")

route_map.add_edge(pandora, arendelle, 150)
route_map.add_edge(arendelle, metroville, 99)
route_map.add_edge(metroville, monstropolis, 105)
route_map.add_edge(monstropolis, arendelle, 42) 
route_map.add_edge(metroville, pandora, 82)
route_map.add_edge(metroville, monstropolis, 105)
route_map.add_edge(metroville, naboo, 26)
route_map.add_edge(metroville, narnia, 37)
route_map.add_edge(monstropolis, naboo, 73)
route_map.add_edge(naboo, metroville, 26)
route_map.add_edge(naboo, narnia, 250)
route_map.add_edge(narnia, metroville, 37)
route_map.add_edge(narnia, naboo, 250)


def test_scenario_one():
    result = business_trip(route_map, ["Metroville", "Pandora"])
    assert result == 82

def test_scenario_two():
    result = business_trip(route_map, ["Arendelle", "Monstropolis", "Naboo"])
    assert result == 115

def test_scenario_three():
    result = business_trip(route_map, ["Naboo", "Pandora"])
    assert result == "null"

def test_scenario_four():
    result = business_trip(route_map, ["Narnia", "Arendelle", "Naboo"])
    assert result == "null"