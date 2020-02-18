import dns.resolver
import logging
import time

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8']
print('nameservers: {}'.format(resolver.nameservers))

# input files
domains_file = open(snakemake.input[0])
scope_ips_file = open(snakemake.input[1])
scope_ips = scope_ips_file.read()

# logging file
logging.basicConfig(filename=snakemake.log[0], level=logging.DEBUG,
        format='[%(asctime)s] - %(levelname)s: %(message)s')
logging.info('Starting dns filtering script at {}'.format(time.asctime()))

# output files
inscope = open(snakemake.output[0], 'w')
outscope = open(snakemake.output[1], 'w')
did_not_resolve = open(snakemake.output[2], 'w')

for domain in domains_file:
    domain = domain.strip()
    logging.info('domain: {}'.format(domain))
    try:
        answer = resolver.query(domain, 'A')
    except dns.resolver.NXDOMAIN:
        # add the domain to did_not_resolve
        logging.warning('domain did not resolve')
        did_not_resolve.write('{}\n'.format(domain))
        continue
    is_inscope = False
    for a in answer:
        logging.info('answer: {}'.format(a))
        # check if the domain is in scope
        a = a.to_text()
        if a in scope_ips:
            logging.debug('{} is in scope'.format(a))
            is_inscope = True
            
    if is_inscope:
        logging.info('{} is in scope'.format(domain))
        inscope.write('{}\n'.format(domain))
    else:
        logging.info('{} is out of scope'.format(domain))
        outscope.write('{}\n'.format(domain))

domains_file.close()
scope_ips_file.close()
inscope.close()
outscope.close()
did_not_resolve.close()
