import numpy as np 
def descriptive_statistics(data):
	percentiles = np.percentile(data, [25, 50, 75])
	iqr =  float(percentiles[2]) - float(percentiles[0])
	stats_dict = {
        "mean": float(np.mean(data)),
        "median": float(np.median(data)),
        "mode": int(np.argmax(np.bincount(data))),
        "variance": float(np.round(np.var(data),4)),
        "standard_deviation": float(np.round(np.std(data),4)),
        "25th_percentile": float(percentiles[0]),
        "50th_percentile": float(percentiles[1]),
        "75th_percentile": float(percentiles[2]),
        "interquartile_range": iqr
    }
	return stats_dict

print(descriptive_statistics([10, 20, 30, 40, 50]))


# {
# 	'mean': 30.0,
# 	'median': 30.0,
# 	'mode': 10,
# 	'variance': 200.0,
# 	'standard_deviation': 14.142135623730951,
# 	'25th_percentile': 20.0, 
# 	'50th_percentile': 30.0,
# 	'75th_percentile': 40.0,
# 	'interquartile_range': 20.0
# }