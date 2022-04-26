import scipy
import scipy.stats

def fit(y):
    dist_names = ['norm','lognorm','expon','pareto']

    dist_results = []
    params = {}
    for dist_name in dist_names:
        dist = getattr(scipy.stats, dist_name)
        param = dist.fit(y)
        
        params[dist_name] = param
        #Applying the Kolmogorov-Smirnov test
        D, p = scipy.stats.kstest(y, dist_name, args=param)
        dist_results.append((dist_name,p))

    #select the best fitted distribution
    sel_dist,p = (max(dist_results,key=lambda item:item[1]))
    #store the name of the best fit and its p value
    DistributionName = sel_dist
    PValue = p

    return [DistributionName,PValue]
