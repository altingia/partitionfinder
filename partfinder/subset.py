import logging
log = logging.getLogger("subset")
import os

from fasta import write_fasta

class SubsetError(Exception):
    pass

class SubsetResult(object):
    def __init__(self):
        pass

    def __str__(self):
        return "SubsetResult!"

class Subset(object):
    """A Subset of Partitions
    """
    _results_cache = {}

    def __init__(self, *parts):

        partset = set()
        for p in parts:
            if p.partition_set is None:
                log.error("You cannot add a Partition to a Subset until \
                          the Partition belongs to a PartitionSet")
                raise SubsetError

            if p in partset:
                log.error("%s is duplicated in a Subset", p)
                raise SubsetError

            partset.add(p)

        self.partitions = frozenset(partset)
        
        # Append all of the columns in the partition
        self.columns = []
        self.columnset = set()
        for p in parts:
            self.columns += p.columns
            self.columnset |= p.columnset
        self.columns.sort()

        log.debug("Created %s", self)

    def __str__(self):
        return "Subset(%s)" % ", ".join([str(p) for p in self.partitions])

    def make_filename(self):
        s = sorted([p.name for p in self.partitions])
        return '-'.join(s) + ".fasta"

    def analyse(self):
        # Check first to see if we've got the results
        if self.partitions in self._results_cache:
            log.debug("Returning cached result for %s", self)
            return self._results_cache[self.partitions]

        log.debug("Calculating result for %s", self)
        result = self._really_analyse()
        self._results_cache[self.partitions] = result
        return result

    def _really_analyse(self):
        # self.write_alignment()
        result = SubsetResult()


        return result

    def write_alignment(self):
        """create an alignment for this subset"""
        align = {}
        self.fname = self.make_filename()
        align_path = os.path.join(config.settings.output_path, self.fname)
        if os.path.exists(align_path):
            log.debug(
                "Fasta file '%s' already exists, not rewriting",
                os.path.basename(align_path))
            return 

        # Pull out the columns we need
        for species, old_seq in config.sequence.iteritems():
            new_seq = ''.join([old_seq[i] for i in self.columns])
            align[species] = new_seq

        write_fasta(align_path, align)
        self.align_path = align_path

    def __iter__(self):
        return iter(self.partitions)

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    import config
    from partition import Partition
    config.initialise("~/tmp", True)

    pa = Partition('a', (1, 10, 3))
    pb = Partition('b', (2, 10, 3))
    pc = Partition('c', (3, 10, 3))

    s1 = Subset(pa, pb)
    s2 = Subset(pa, pb)
    s3 = Subset(pc)


    s1.analyse()
    s2.analyse()
    s3.analyse()

