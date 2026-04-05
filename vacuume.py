def reflex_vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"


# Example usage
print(reflex_vacuum_agent("A", "Dirty"))   # Output: Suck
print(reflex_vacuum_agent("A", "Clean"))   # Output: Right
print(reflex_vacuum_agent("B", "Clean"))   # Output: Left