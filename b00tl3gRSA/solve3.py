from pwn import *
import functools
import gmpy2
import re
from functools import reduce

class FactorizationWrapper(object):

    def __init__(self, verbose = False):
        self.verbose = verbose
        self.factor_functions = []

    def _print(self, msg):
        if self.verbose:
            print(msg)

    @classmethod
    def _factordb_factor_list(cls, num):
        from factordb.factordb import FactorDB

        f = FactorDB(num)
        if f.connect().status_code != 200:
            raise Exception("Can't connect")
        status = f.get_status()
        if status == 'C':
            raise Exception("Composite, no factors known")
        elif status == 'P' or status == 'Prp':
            raise Exception("Prime or probably prime")
        elif status == 'CF':
            raise Exception("Composite, factors known")
        elif status == 'FF':
            # Composite, fully factored
            result = f.get_factor_list()
            return result
        else:
            raise Exception("Unexpected status: '{}'".format(status))

    @classmethod
    def _yafu_factor_list(cls, num):
        import subprocess
        try:
            with open('/dev/null') as devnull:
                output = subprocess.check_output(
                    ["yafu", "factor({})".format(num)], stderr=devnull)

                result = []
                
                if "***factors found***" not in output:
                    raise Exception("Factors not found")

                for line in output.splitlines():
                    match = re.search(r'^P[\d]+\s=\s([\d]+)$', line)
                    if match:
                        result.append(int(match.group(1)))
                    elif re.match(r'^C[\d]+\s=\s([\d]+)$', line):
                        raise Exception("Composite number found")
                return result
        except:
            raise

    def get_factor_list(self, num):
        
        functions = {"FactorDB": self._factordb_factor_list, "YAFU": self._yafu_factor_list}
        for engine, function in functions.items():
            try:
                res = function(num)
                self._print("{} found {} factors".format(engine, len(res)))
                assert(num == reduce(lambda x, y: x * y, res))
                return res
            except:
                self._print("{} failed, error = {}".format(engine, str(e)))    

        raise Exception("Can't find factor list")


args = {}
r = remote("jupiter.challenges.picoctf.org", 3726)
output = r.recvall()
for line in output.split("\n"):
    line = line.rstrip()
    if line != "":
        var_name, var_value = line.split(": ")
        args[var_name] = int(var_value)
        log.info("{}: {}".format(var_name, var_value))

assert('c' in args)
assert('n' in args)
assert('e' in args)

factors = FactorizationWrapper().get_factor_list(args['n'])
log.info("factors: {}".format(factors))

phi_n = 1
for i in range(len(factors)):
    phi_n *= (factors[i] - 1)
log.info("phi_n: {}".format(phi_n))

d = gmpy2.invert(args['e'], phi_n)
log.info("d: {}".format(d))

plaintext = pow(args['c'], d, args['n'])
log.info("plaintext: {}".format(str(plaintext)))

plaintext_decoded = (format(plaintext, 'x')).decode("hex")

log.success("Flag: {}".format(plaintext_decoded))