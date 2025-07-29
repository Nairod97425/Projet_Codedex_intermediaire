friend1_location = (37.7749, -122.4194)    # San Francisco
friend2_location = (40.7128, -74.0060)     # New York
friend3_location = (4.624335, -74.063644)  # Bogota

my_location = (48.8566, 2.3522)            # Paris

def calculer_distance(loc1, loc2):
    """Calcule la distance entre deux emplacements."""
    from math import sqrt

    lat1, lon1 = loc1
    lat2, lon2 = loc2
    return sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

def trouver_ami_le_plus_eloigne(ma_position, positions_amis):
    """Trouve l'ami le plus éloigné de la position de l'utilisateur."""
    ami_le_plus_eloigne = None
    distance_max = 0

    for position_ami in positions_amis:
        distance = calculer_distance(ma_position, position_ami)
        if distance > distance_max:
            distance_max = distance
            ami_le_plus_eloigne = position_ami

    return ami_le_plus_eloigne, distance_max

def main():
    positions_amis = [friend1_location, friend2_location, friend3_location]
    ami_le_plus_eloigne, distance = trouver_ami_le_plus_eloigne(my_location, positions_amis)

    print(f"L'ami le plus éloigné se trouve à l'emplacement : {ami_le_plus_eloigne}")
    print(f"Distance depuis ma position : {distance:.2f} unités")

if __name__ == "__main__":
    main()

# Ce code calcule la distance entre la position de l'utilisateur et celle de trois amis, puis identifie l'ami le plus éloigné.
# Il utilise une formule simple de distance euclidienne pour le calcul.
