from math import sqrt


def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2) # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values)%2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result

def mean(list_of_values):
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)


def covariance(first_list_of_values, second_list_of_values):
    """
     this func returns the covariance of 2 lists
     :param first_list_of_values: list one
     :param second_list_of_values: list two
     :return: float: the covariance
       """
    averagex = mean(first_list_of_values)
    averagey = mean(second_list_of_values)
    sum = 0
    for i in range(len(first_list_of_values)):
        sum = sum + (((first_list_of_values[i]) - averagex) * ((second_list_of_values[i]) - averagey))
    result = sum / (len(first_list_of_values) - 1)
    return result


def correlation(first_list_of_values, second_list_of_values):
    """
    this func gives correlation of 2 lists
    :param first_list_of_values: list one
    :param second_list_of_values: list two
    :return: float: the correlation
    """
    sqrt_variance1 = sqrt(variance(first_list_of_values))
    sqrt_variance2 = sqrt(variance(second_list_of_values))
    result = (covariance(first_list_of_values, second_list_of_values)) / (sqrt_variance1 * sqrt_variance2)
    return result

