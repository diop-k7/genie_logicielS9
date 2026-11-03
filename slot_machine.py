def slot_machine(bet, result):
    """
    Simulates a slot machine game.

    Parameters:
    bet (int): The amount of money the player bets.
    result (list): A list of three strings representing the symbols on the slot machine.

    Returns:
    int: The amount of money won or lost.
    """
    # Define the payout rules
    payouts = {
        ("cherry", "cherry", "cherry"): 10,
        ("lemon", "lemon", "lemon"): 5,
        ("orange", "orange", "orange"): 3,
        ("cherry", "cherry", "lemon"): 2,
        ("cherry", "lemon", "lemon"): 1,
        ("lemon", "lemon", "cherry"): 1,
        ("orange", "orange", "cherry"): 1,
        ("orange", "cherry", "cherry"): 1,
    }

    # Check if the result is in the payouts dictionary
    payout = payouts.get(tuple(result), 0)

    # Calculate the total win or loss
    total = payout * bet

    return total