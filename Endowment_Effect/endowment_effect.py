GRAPEFRUIT_COST = 10

def dim_returns(k, inverse_scale_factor):
    """
    A simple utility calculation method.

    Given k items in posession return the benefit of a K + 1th item given some
    inverse scale factor.

    The formula used is utility = 100% if no items are in posession or

    utility = 1 / inverse_scale_factor * (k + 1)
    """
    if k == 0:
        return 1;

    return (1 / (inverse_scale_factor * (k + 1)))

def endowment_effect(mkt_val, ref_val, time_held, scale_factor):
    """
    A simple endowment effect calculation method.

    Given an item with a market value, reference value (i.e, value item was
    purchased at), the amount of time it has been held, and a scale factor,
    return the price accounting for a simple endowment effect.

    endowment_effect =
    (mkt_val > ref_val ? mkt_val : ref_val) + time_held * scale_factor
    """

    endowment_effect = mkt_val if mkt_val > ref_val else ref_val
    endowment_effect += time_held * scale_factor
    return endowment_effect

def model_endowment():
    value        = 100
    ref_val      = 90
    time_held    = 20
    scale_factor = 1.02
    print("This script models a simple case of an endowment effect.\n")
    print("Given a market value of a good at {},".format(value))
    print("we can assume a simple endowment effect that scales over time held\n")
    print("Market Value: {}, Endowment Effect: {}"
            .format(value, endowment_effect(value, ref_val, time_held, scale_factor)))

if __name__ == "__main__":
    model_endowment()