from libnmap.parser import NmapParser
import logging

def writetbl(log,files):
    with open(log, 'w') as outfile:
        for xml in snakemake.input:
            logging.info("Parsing {x}".format(x=xml))
            infile = NmapParser.parse_fromfile(xml)
            for host in infile.hosts:
                logging.info("{h}: {s}".format(h=host, s=host.services))
                outfile.write("{h}: {s}\n".format(h=host, s=host.services))


if __name__ == '__main__':
    writetbl("data/nmap.tbl", snakemake.input)
