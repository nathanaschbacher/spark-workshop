import sys
import csv
import StringIO

from pyspark import SparkContext

if __name__ == "__main__":
    fields = ['dna_seq',
               'sex',
               'name',
               'address',
               'city',
               'state',
               'zip',
               'phone',
               'birthdate',
               'ssn',
               'occupation',
               'blood',
               'weight',
               'height',
               'lat',
               'lng',
               'symptomatic']

    def sample_to_dict(rdd_item):
        item = StringIO.StringIO(rdd_item)
        return csv.DictReader(item, fieldnames=fields, doublequote=True, quotechar='"', quoting=csv.QUOTE_ALL).next()

    def weight_stats(weights_rdd):
        return (weights_rdd.min(), weights_rdd.max(), weights_rdd.mean(), weights_rdd.stdev(), weights_rdd.variance())

    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: PATH_TO_SPARK/bin/spark-submit main.py <csv_file>"
        exit(-1)
    
    sc = SparkContext(appName="AcuteZombilepsyAnalysis")

    samples_rdd = sc.textFile(sys.argv[1])

    vectors_rdd = samples_rdd.map(sample_to_dict)
    
    healthy_rdd = vectors_rdd.filter(lambda s: s['symptomatic'] == 'n')
    zombies_rdd = vectors_rdd.filter(lambda s: s['symptomatic'] == 'y')
    
    healthy_stats = weight_stats(healthy_rdd.map(lambda x: float(x['weight'])))
    zombie_stats = weight_stats(zombies_rdd.map(lambda x: float(x['weight'])))

    print "Healthy Population Stats: "+str(healthy_stats)
    print "Zombie  Population Stats: "+str(zombie_stats)
        
    sc.stop()
