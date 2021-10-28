

def escape_by(plan):
    if plan == "jumping over":
        print("\nWe cannot escape that way! The boulder is too big!\n")
    elif plan == "running around":
        print("\nWe cannot escape that way! The boulder is moving too fast!\n")
    elif plan == "going deeper":
        print("\nThat might just work! Let's go deeper!\n")
    else:
        print("\nMaybe we need a different plan!\n")

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
