import statistics as stats

def reconvert_results_ig(score):
    results = []
    for data in score:
        for element in data:
            if element == []:
                data.remove(element)
            else:
                results.append(element)

    return results

def calculateStats(results):
    mean=stats.mean(results)
    median=stats.median(results)
    mode=stats.mode(results)
    variance=stats.pvariance(results, mu=None)
    typical_deviation=stats.pstdev(results, mu=None)

    return mean, median, mode, variance, typical_deviation




