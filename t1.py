def format_itineraries(itineraries):
    result = []
    for i, itinerary in enumerate(itineraries):
        
        result.append(f"Itinerary {i + 1}: {traveler_name} - From {origin} to {destination}")
    return '\n'.join(result)

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_string = format_itineraries(itineraries)
print(formatted_string)
