soil_to_crop = {
    "alluvial": "Rice, Wheat, Sugarcane",
    "black": "Cotton, Soybean, Groundnut",
    "red": "Millets, Pulses, Groundnut",
    "clayey": "Paddy, Wheat, Barley",
    "laterite": "Cashew, Tea, Coffee",
    "sandy": "Coconut, Melons, Peanuts"
}

crop_to_fertilizer = {
    "Rice": ["Compost", "Vermicompost", "Biofertilizers"],
    "Wheat": ["Organic Manure", "Bio-fertilizer"],
    "Sugarcane": ["Neem Cake", "Green Manure"],
    "Cotton": ["Cow Dung Manure", "Compost"],
    "Soybean": ["Rhizobium Biofertilizer"],
    "Groundnut": ["Phosphate-solubilizing Bacteria"],
    "Millets": ["Farmyard Manure"],
    "Pulses": ["Phosphorus-enriched Compost"],
    "Paddy": ["Organic Compost"],
    "Barley": ["Vermicompost"],
    "Cashew": ["Seaweed-based Fertilizer"],
    "Tea": ["Compost Tea"],
    "Coffee": ["Organic Mulch"],
    "Coconut": ["Organic Potash"],
    "Melons": ["Bio-fertilizer"],
    "Peanuts": ["Compost"]
}

def get_recommendations(soil_type):
    crops = soil_to_crop.get(soil_type, "Unknown Soil Type")
    fertilizers = {crop: crop_to_fertilizer.get(crop, ["Unknown Fertilizers"]) for crop in crops.split(", ")}
    return crops, fertilizers
